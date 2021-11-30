import datetime
from json import JSONEncoder
import json
from collections import defaultdict
from abc import ABC, abstractmethod


class Assignment:
    def __init__(self, assignment_id: int, name: str, description: str, points: int, due_date: datetime.datetime):
        self.AssignmentID = assignment_id
        self.Name = name
        self.Points = points
        self.DueDate = due_date
        self.Description = description

    def readable_due_date(self):
        return self.DueDate.strftime("%B %d, %I:%M %p")


class Course:
    def __init__(self, deptAbbrev: str, courseNo: int, courseName: str):
        self.deptAbbrev = deptAbbrev
        self.courseNo = courseNo
        self.courseName = courseName


class Section:
    def __init__(self, deptAbbrev: str, courseNo: int, sectNo: int, meetingAddress=None):
        self.sectNo = sectNo
        self.courseNo = courseNo
        self.deptAbbrev = deptAbbrev
        self.meetingAddress = meetingAddress

    def add_to_db(self, conn) -> bool:
        cur = conn.cursor()
        sql = 'INSERT INTO studygroupdatabase.section (sectionNum, courseNum, deptAbbrev, meetingAddress) ' \
              'VALUES (%s, %s, %s, %s);'
        values = (self.sectNo, self.courseNo, self.deptAbbrev, self.meetingAddress)
        try:
            cur.execute(sql, values)
            conn.commit()
            return True
        except Exception as e:
            print(e)
            conn.rollback()
            return False
        finally:
            cur.close()

    def exists_in_db(self, conn):
        cur = conn.cursor()
        section_exists_sql = f"SELECT sectionNum, courseNum, deptAbbrev " \
                             f"FROM studygroupdatabase.section " \
                             f"WHERE sectionNum=%s AND courseNum=%s AND deptAbbrev=%s;"
        section_exists_values = (self.sectNo, self.courseNo, self.deptAbbrev)
        cur.execute(section_exists_sql, section_exists_values)
        return bool(cur.fetchall())

    @staticmethod
    def fromCourseAndSectionNumber(course: Course, sectionNumber: int):
        return Section(course.deptAbbrev, course.courseNo, sectionNumber)

    def __hash__(self):
        return hash((self.sectNo, self.courseNo, self.deptAbbrev))

    def __eq__(self, other):
        return self.sectNo == other.sectNo and \
               self.courseNo == other.courseNo and \
               self.deptAbbrev == other.deptAbbrev


class StudyGroupInvite:
    def __init__(self, senderVNumber: str, receiverVNumber: str, studyGroupID: int):
        self.senderVNumber = senderVNumber
        self.receiverVNumber = receiverVNumber
        self.studyGroupID = studyGroupID


class StudyGroup:
    def __init__(self, groupNickname: str, prefMethodOfComm: str, studyGroupID: int):
        self.groupNickname = groupNickname
        self.prefMethodOfComm = prefMethodOfComm
        self.studyGroupID = studyGroupID


class FullName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class StudyTools:
    def __init__(self, address: str, study_tools: list):
        self.address = address
        self.study_tools = study_tools

    @staticmethod
    def get_all_locations_study_tools_from_database(conn):
        cur = conn.cursor()
        section_exists_sql = "SELECT meetingLocationAddress, studyTool " \
                             "FROM studygroupdatabase.studytools;"
        cur.execute(section_exists_sql)
        results = cur.fetchall()
        cur.close()
        address_to_study_tools = defaultdict(set)
        all_tools = set()
        for row in results:
            address = row[0]
            study_tool = row[1]
            address_to_study_tools[address].add(study_tool)
            all_tools.add(study_tool)

        study_tools = [StudyTools(address, list(tools)) for address, tools in address_to_study_tools.items()]
        return study_tools, all_tools


class Meeting(ABC):
    def __init__(self, group_name: str, start_time: datetime.datetime, end_time: datetime.datetime):
        if start_time > end_time:
            raise ValueError("start time cannot be after end time")
        self.group_name = group_name
        self.start_time = start_time
        self.end_time = end_time

    def duration_to_str(self) -> str:
        return f"{self.start_time.strftime(f'%A, %b {self.start_time.day} from %I:%M')}" \
               f"{self.start_time.strftime('%p').lower()} to " \
               f"{self.end_time.strftime('%I:%M')}{self.end_time.strftime('%p').lower()}"

    @abstractmethod
    def get_meeting_location(self):
        raise NotImplementedError("Cannot get meeting location of abstract class Meeting")

    @abstractmethod
    def get_meeting_type(self):
        raise NotImplementedError("Cannot get meeting type of abstract class Meeting")


class OnlineMeeting(Meeting):
    def __init__(self, group_name: str, start_time: datetime.datetime, end_time: datetime.datetime, meeting_url: str):
        super().__init__(group_name, start_time, end_time)
        self.meeting_url = meeting_url

    def get_meeting_location(self):
        return self.meeting_url

    def get_meeting_type(self) -> str:
        return "Online"


class InPersonMeeting(Meeting):
    def __init__(self, group_name: str, start_time: datetime.datetime, end_time: datetime.datetime,
                 meeting_address: str):
        super().__init__(group_name, start_time, end_time)
        self.meeting_address = meeting_address

    def get_meeting_location(self):
        return self.meeting_address

    def get_meeting_type(self) -> str:
        return "In-Person"


class DefaultJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


if __name__ == '__main__':
    group = StudyGroup("Group name", "Discord", 100)
    jsonobj = json.dumps([group], cls=DefaultJSONEncoder)
    print(type(jsonobj))
    print(jsonobj)


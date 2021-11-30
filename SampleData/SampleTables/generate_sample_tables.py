
import random
import re
from collections import OrderedDict
import sys
import datetime
sys.path.append("../StudentData/")
import randomPhoneNumber
import randomSalt
import randomVNumber
import emailFromFullName
import discordFromFullName
sys.path.append("../MeetingData/")
import randomMeetingLink

# Files for sample student data
passwords_file         = "../StudentData/passwords.txt"
first_names_file       = "../StudentData/first-names.txt"
last_names_file        = "../StudentData/last-names.txt"
housing_addresses_file = "../StudentData/housing_addresses.txt"

# Files for sample meeting data
study_tools_file = "../MeetingData/StudyTools.txt"

# Files for sample course data
courses_file = "../CourseData/courses.txt"
classroom_file = "../CourseData/classrooms.txt"

# Files for sample study group data
group_names_file     = "../StudyGroupData/group-nicknames.txt"
methods_of_comm_file = "../StudyGroupData/methods-of-comm.txt"


def read_lines_into_list_elements(filename):
    return list(open(filename, 'r', encoding='ISO-8859-1').read().splitlines())


def read_passwords_file():
    global passwords_file
    return read_lines_into_list_elements(passwords_file)


def read_first_names_file():
    global first_names_file
    return read_lines_into_list_elements(first_names_file)


def to_title_case(s):
    return s[0].upper() + s[1:].lower()


def read_last_names_file():
    global last_names_file
    return list(map(to_title_case, read_lines_into_list_elements(last_names_file)))


def read_housing_addresses_file():
    global housing_addresses_file
    return read_lines_into_list_elements(housing_addresses_file)[1::2]


def read_classroom_addresses_file():
    global classroom_file
    return read_lines_into_list_elements(classroom_file)[1::2]


def read_study_tools_file():
    global study_tools_file
    return read_lines_into_list_elements(study_tools_file)


def read_courses_file():
    global courses_file
    course_data = read_lines_into_list_elements(courses_file)
    _department_abbrevs = []
    _course_numbers = []
    _course_names = []
    for s in course_data:
        match = re.match(r"^(\w{4}) (\d{3})\. (.*?)\..*\.$", s)
        if match:
            _department_abbrevs += [match.group(1)]
            _course_numbers += [match.group(2)]
            _course_names += [match.group(3)]
    return _department_abbrevs, _course_numbers, _course_names


def read_group_nicknames_file():
    global group_names_file
    return read_lines_into_list_elements(group_names_file)


def read_methods_of_communication_file():
    global methods_of_comm_file
    return read_lines_into_list_elements(methods_of_comm_file)


def save_dict_to_markdown(columns: OrderedDict, markdown_filename: str):
    if not markdown_filename.lower().endswith(".md"):
        markdown_filename += ".md"

    with open(markdown_filename, 'w+') as f:
        f.write(" | ".join(columns.keys()) + "\n")
        f.write(" | ".join(["---" for _ in range(len(columns))]))
        rows = list(zip(*list(zip(*columns.items()))[1]))
        for row in rows:
            f.write("\n" + " | ".join(str(data) for data in row))


def make_username_from_full_name(first_name, last_name):
    return first_name[:random.randint(1, 2)] + to_title_case(last_name[:random.randint(3, 4)]) + str(random.randint(0, 999))


def random_birthdate_between_ages(min_age_year, max_age_year):
    start_date = datetime.date.today() - datetime.timedelta(days=max_age_year * 365)
    end_date = datetime.date.today() - datetime.timedelta(days=min_age_year * 365)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


def random_weekly_schedule():
    # for the WEEKDAY() SQL function, it returns the weekday number for a given date.
    # Note: 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday.
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    num_meetings = random.choice([2, 3, 5])
    days_to_meet = random.sample(weekdays, num_meetings)
    meeting_length_hours = random.randint(1, 2)
    start_hour = random.randint(8, 18)  # classes start between 8am and 6pm
    end_hour = start_hour + meeting_length_hours
    start_times = []
    end_times = []
    for _ in range(num_meetings):
        start_day_time = str(start_hour) + ':00'
        end_day_time = str(end_hour) + ':00'
        start_times += [start_day_time]
        end_times += [end_day_time]

    return days_to_meet, start_times, end_times


def random_meeting_time():
    num_days_until_meeting = random.randint(3, 30)
    meeting_date = datetime.datetime.today() + datetime.timedelta(days=num_days_until_meeting)
    start_datetime = meeting_date.replace(hour=random.randint(8, 18), minute=random.randint(0, 3) * 15)
    end_datetime = start_datetime + datetime.timedelta(hours=random.choice([0.5, 1, 1.5, 2]))
    return start_datetime.strftime("%Y-%m-%d %H:%M"), end_datetime.strftime("%Y-%m-%d %H:%M")


def random_due_date(min_num_days_until_due, max_num_days_until_due):
    due_date = datetime.date.today() + datetime.timedelta(days=random.randint(min_num_days_until_due, max_num_days_until_due))
    return due_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    NUM_ROWS_PER_TABLE = 10
    random.seed(0)
    print("Reading files . . .")
    phone_numbers = [randomPhoneNumber.random_US_phone_number() for _ in range(NUM_ROWS_PER_TABLE)]
    V_numbers = set()
    while len(V_numbers) < NUM_ROWS_PER_TABLE:  # must be unique
        V_numbers.add(randomVNumber.random_VNumber())
    methods_of_comm = read_methods_of_communication_file()
    group_nicknames = read_group_nicknames_file()
    department_abbrevs, course_numbers, course_names = read_courses_file()
    classroom_addresses = read_classroom_addresses_file()
    study_tools = read_study_tools_file()
    housing_addresses = read_housing_addresses_file()
    first_names = read_first_names_file()
    last_names = read_last_names_file()
    passwords = read_passwords_file()

    # Student(VNumber, firstName, lastName, address, dateOfBirth, email, discordName, phoneNumber, username, passwordHash, salt)
    print("Generating Student Table . . .")
    student_table = OrderedDict()
    student_table["VNumber"] = list(V_numbers)
    student_table["firstName"] = random.sample(first_names, NUM_ROWS_PER_TABLE)
    student_table["lastName"] = random.sample(last_names, NUM_ROWS_PER_TABLE)
    student_table["username"] = [make_username_from_full_name(first, last) for first, last in zip(student_table["firstName"], student_table["lastName"])]
    student_table["email"] = [emailFromFullName.make_email_from_full_name(first, last) for first, last in zip(student_table["firstName"], student_table["lastName"])]
    student_table["discordUName"] = [discordFromFullName.make_discord_uname_from_full_name(first, last) for first, last in zip(student_table["firstName"], student_table["lastName"])]
    student_table["phoneNumber"] = phone_numbers
    student_table["dateOfBirth"] = [random_birthdate_between_ages(18, 23) for _ in range(NUM_ROWS_PER_TABLE)]
    student_table["address"] = random.sample(housing_addresses, NUM_ROWS_PER_TABLE)
    salts = []
    saltedPasswords = []
    for pwd in random.sample(passwords, NUM_ROWS_PER_TABLE):
        salt = randomSalt.random_salt()
        salts += [salt.hex()]
        saltedPasswords += [randomSalt.hash_password_and_salt(pwd.encode(), salt)]
    student_table["saltedPassword"] = saltedPasswords
    student_table["salt"] = salts
    save_dict_to_markdown(student_table, "StudentTable.md")

    dept_abbrev_sample, course_nums_sample, course_names_sample = zip(*random.sample(list(zip(department_abbrevs, course_numbers, course_names)), NUM_ROWS_PER_TABLE))

    # Section(CourseNum, DeptAbbrev, SectionNumber, MeetingAddress)
    print("Generating Section Table . . .")
    section_table = OrderedDict()
    section_table["deptAbbrev"] = dept_abbrev_sample
    section_table["courseNum"] = course_nums_sample
    section_table["sectionNum"] = [random.randint(1, 999) for _ in range(NUM_ROWS_PER_TABLE)]
    section_table["meetingAddress"] = random.sample(classroom_addresses, NUM_ROWS_PER_TABLE)
    save_dict_to_markdown(section_table, "SectionTable.md")

    # SectionMeetingTimes(CourseNum, DeptAbbrev, SectionNumber, MeetingStartTime, MeetingEndTime)
    print("Generating Section Meeting Times Table . . .")
    section_meeting_table = OrderedDict()
    section_meeting_table["deptAbbrev"] = []
    section_meeting_table["courseNum"] = []
    section_meeting_table["sectionNum"] = []
    section_meeting_table["meetingDay"] = []
    section_meeting_table["meetingStartTime"] = []
    section_meeting_table["meetingEndTime"] = []
    for dept_abbrev, course_num, section_num in zip(dept_abbrev_sample, course_nums_sample, section_table["sectionNum"]):
        for meeting_day, meeting_start, meeting_end in zip(*random_weekly_schedule()):
            section_meeting_table["deptAbbrev"] += [dept_abbrev]
            section_meeting_table["courseNum"] += [course_num]
            section_meeting_table["sectionNum"] += [section_num]
            section_meeting_table["meetingDay"] += [meeting_day]
            section_meeting_table["meetingStartTime"] += [meeting_start]
            section_meeting_table["meetingEndTime"] += [meeting_end]

    save_dict_to_markdown(section_meeting_table, "SectionMeetingTimesTable.md")

    # Course(CourseNum, DeptAbbrev, CourseName)
    print("Generating Course Table . . .")
    course_table = OrderedDict()
    course_table["deptAbbrev"] = dept_abbrev_sample
    course_table["courseNum"] = course_nums_sample
    course_table["courseName"] = course_names_sample
    save_dict_to_markdown(course_table, "CourseTable.md")

    # StudyGroup(studyGroupID, prefMethodOfComm, groupNickname)
    print("Generating Study Group Table . . .")
    study_group_table = OrderedDict()
    study_group_table["studyGroupID"] = list(range(1, NUM_ROWS_PER_TABLE+1))
    study_group_table["prefMethodOfComm"] = random.sample(methods_of_comm, NUM_ROWS_PER_TABLE)
    study_group_table["groupNickname"] = random.sample(group_nicknames, NUM_ROWS_PER_TABLE)
    save_dict_to_markdown(study_group_table, "StudyGroupTable.md")

    # Meeting(MeetingID, startTime, endTime)
    print("Generating Meeting Table . . .")
    meeting_table = OrderedDict()
    meeting_table["MeetingID"] = list(range(1, NUM_ROWS_PER_TABLE+1))
    meeting_table["startTime"] = []
    meeting_table["endTime"] = []
    for _ in range(NUM_ROWS_PER_TABLE):
        start_time, end_time = random_meeting_time()
        meeting_table["startTime"] += [start_time]
        meeting_table["endTime"] += [end_time]
    save_dict_to_markdown(meeting_table, "MeetingTable.md")

    # OnlineMeeting(MeetingID, meetingURL)
    print("Generating OnlineMeeting Table . . .")
    online_meeting_table = OrderedDict()
    online_meeting_table["MeetingID"] = list(range(1, NUM_ROWS_PER_TABLE//2 + 1))
    online_meeting_table["meetingURl"] = [randomMeetingLink.random_meeting_link() for _ in range(len(online_meeting_table["MeetingID"]))]
    save_dict_to_markdown(online_meeting_table, "OnlineMeetingTable.md")

    # InPersonMeeting(MeetingID, meetingLocationAddress)
    print("Generating InPersonMeeting Table . . .")
    in_person_meeting_table = OrderedDict()
    in_person_meeting_table["MeetingID"] = list(range(NUM_ROWS_PER_TABLE//2, NUM_ROWS_PER_TABLE))
    in_person_meeting_table["meetingLocationAddress"] = random.sample(classroom_addresses, len(in_person_meeting_table["MeetingID"]))
    save_dict_to_markdown(in_person_meeting_table, "InPersonMeetingTable.md")

    # InPersonMeetingStudyTools(meetingLocationAddress, studyTool)
    print("Generating InPersonMeetingStudyTools Table . . .")
    study_tools_table = OrderedDict()
    study_tools_table["meetingLocationAddress"] = []
    study_tools_table["studyTool"] = []
    for address in classroom_addresses:
        for study_tool in random.sample(study_tools, random.randint(1, 4)):
            study_tools_table["meetingLocationAddress"] += [address]
            study_tools_table["studyTool"] += [study_tool]
    save_dict_to_markdown(study_tools_table, "InPersonMeetingStudyToolsTable.md")

    # Assignment(AssignmentID, AssignmentName, Description, Points, DueDate)
    print("Generating Assignment Table . . .")
    assignment_table = OrderedDict()
    assignment_table["AssignmentID"] = list(range(1, NUM_ROWS_PER_TABLE + 1))
    assignment_table["AssignmentName"] = ["Assignment #" + str(i) for i in range(1, NUM_ROWS_PER_TABLE+1)]
    assignment_table["Description"] = ["This is a sample assignment description"] * NUM_ROWS_PER_TABLE
    assignment_table["Points"] = [random.randint(3, 10) * 10 for _ in range(NUM_ROWS_PER_TABLE)]
    assignment_table["DueDate"] = [random_due_date(5, 30) for _ in range(NUM_ROWS_PER_TABLE)]
    save_dict_to_markdown(assignment_table, "AssignmentTable.md")


    print("Generating WantsToWorkOn Table . . .")
    wants_to_work_on_table = OrderedDict()
    wants_to_work_on_table["VNumber"] = []
    wants_to_work_on_table["AssignmentID"] = []
    for v_number in student_table["VNumber"]:
        num_wants_to_work = random.randint(2, 4)
        for _ in range(num_wants_to_work):
            random_assignment_index = random.randint(0, len(assignment_table["AssignmentID"])-1)
            wants_to_work_on_table["VNumber"] += [v_number]
            wants_to_work_on_table["AssignmentID"] += [assignment_table["AssignmentID"][random_assignment_index]]
    save_dict_to_markdown(wants_to_work_on_table, "WantsToWorkOnTable.md")

    # Assigns(courseNum, deptAbbrev, sectionNum, AssignmentID)
    print("Generating Assigns Table . . .")
    assigns_table = OrderedDict()
    assigns_table["courseNum"] = []
    assigns_table["deptAbbrev"] = []
    assigns_table["sectionNum"] = []
    assigns_table["AssignmentID"] = []
    for i in range(len(section_table["courseNum"])):
        dept_abbrev = section_table["deptAbbrev"][i]
        course_num = section_table["courseNum"][i]
        section_num = section_table["sectionNum"][i]
        ran_assign_num = random.randint(1, 4)
        for _ in range(ran_assign_num):
            assigns_table["AssignmentID"] += [random.choice(assignment_table['AssignmentID'])]
            assigns_table["deptAbbrev"] += [dept_abbrev]
            assigns_table["courseNum"] += [course_num]
            assigns_table["sectionNum"] += [section_num]
    save_dict_to_markdown(assigns_table, "AssignsTable.md")


    # Takes(VNumber, SectionNumber, CourseNum, DeptAbbrev)
    print("Generating Takes Table . . .")
    takes_table = OrderedDict()
    takes_table["VNumber"] = []
    takes_table["deptAbbrev"] = []
    takes_table["courseNum"] = []
    takes_table["sectionNum"] = []
    for v_number in student_table["VNumber"]:
        num_classes_taken = random.randint(3, 6)
        for _ in range(num_classes_taken):
            rand_course_index = random.randint(0, len(section_table["deptAbbrev"]) - 1)
            takes_table["VNumber"] += [v_number]
            takes_table["deptAbbrev"] += [section_table["deptAbbrev"][rand_course_index]]
            takes_table["courseNum"] += [section_table["courseNum"][rand_course_index]]
            takes_table["sectionNum"] += [section_table["sectionNum"][rand_course_index]]
    save_dict_to_markdown(takes_table, "TakesTable.md")

    # Comprises(VNumber, studyGroupID)
    print("Generating Comprises Table . . .")
    comprises_table = OrderedDict()
    comprises_table["VNumber"] = []
    comprises_table["studyGroupID"] = []
    for study_group_id in study_group_table["studyGroupID"]:
        num_students_in_study_group = random.randint(3, 5)
        random_V_Numbers = random.sample(student_table["VNumber"], num_students_in_study_group)
        for v_num in random_V_Numbers:
            comprises_table["studyGroupID"] += [study_group_id]
            comprises_table["VNumber"] += [v_num]
    save_dict_to_markdown(comprises_table, "ComprisesTable.md")

    print("Generating Assignment Table . . .")
    WorksOn = OrderedDict()
    WorksOn["MeetingID"] = meeting_table["MeetingID"]
    WorksOn["AssignmentID"] = [random.choice(assignment_table["AssignmentID"]) for _ in range(NUM_ROWS_PER_TABLE)]
    save_dict_to_markdown(WorksOn,
                          "../SampleTables/WorksOn.md")

    print("Generating Meets Table . . .")
    Meets = OrderedDict()
    Meets["MeetingID"] = meeting_table["MeetingID"]
    Meets["StudyGroupID"] = [random.choice(study_group_table["studyGroupID"]) for _ in range(NUM_ROWS_PER_TABLE)]
    save_dict_to_markdown(Meets,
                          "../SampleTables/Meets.md")

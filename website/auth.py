from flask import Blueprint, render_template, flash, request, session
import flask
from flask import Blueprint, render_template, flash, request, url_for
import pymysql
import os
import re
import hashlib
import requests
import urllib.parse
from . import db_entities
import datetime
from datetime import timedelta
from .coursescheduling import WeeklyTimeDelta
from .colors import generate_color_palette
import json

from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

auth = Blueprint('auth', __name__)

conn = pymysql.connect(
    host='sgfinder.cp1qgzw0m4tm.us-east-1.rds.amazonaws.com',
    port=3306,
    user='team8',
    password='2[1GV-g[M-4a<[',
    db='studygroupdatabase',
)


def create_online_meeting(study_group_id, start_datetime, end_datetime, meeting_link):
    cur = conn.cursor()
    create_meeting_sql = "INSERT INTO meeting (startTime, endTime) VALUES (%s, %s);"
    create_meeting_values = (start_datetime, end_datetime)
    add_online_meeting_sql = "INSERT INTO onlinemeeting (meetingID, meetingURL) VALUES (%s, %s);"
    add_meets_sql = "INSERT INTO meets (meetingID, studyGroupID) VALUES (%s, %s);"

    try:
        cur.execute(create_meeting_sql, create_meeting_values)
        cur.execute('SELECT LAST_INSERT_ID();')
        results = cur.fetchall()
        meeting_id = int(results[0][0])
        add_online_meeting_values = (meeting_id, meeting_link)
        cur.execute(add_online_meeting_sql, add_online_meeting_values)
        add_meets_values = (meeting_id, study_group_id)
        cur.execute(add_meets_sql, add_meets_values)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    finally:
        cur.close()


def create_in_person_meeting(study_group_id, start_datetime, end_datetime, meeting_address):
    cur = conn.cursor()
    create_meeting_sql = "INSERT INTO meeting (startTime, endTime) VALUES (%s, %s);"
    create_meeting_values = (start_datetime, end_datetime)
    add_in_person_meeting_sql = "INSERT INTO inpersonmeeting (meetingID, meetingLocationAddress) VALUES (%s, %s);"
    add_meets_sql = "INSERT INTO meets (meetingID, studyGroupID) VALUES (%s, %s);"

    try:
        cur.execute(create_meeting_sql, create_meeting_values)
        cur.execute('SELECT LAST_INSERT_ID();')
        results = cur.fetchall()
        meeting_id = int(results[0][0])
        add_online_meeting_values = (meeting_id, meeting_address)
        cur.execute(add_in_person_meeting_sql, add_online_meeting_values)
        add_meets_values = (meeting_id, study_group_id)
        cur.execute(add_meets_sql, add_meets_values)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    finally:
        cur.close()


def get_section_meeting_times_for_all_members_in_group(groupID: int):
    sql = "select VNumber, firstName, lastName, deptAbbrev, courseNum, sectionNum, weekday, startTime, endTime " \
          "from (select VNumber from groupmembership where studyGroupID = %s) as groupMemberVNumbers " \
          "NATURAL JOIN student " \
          "NATURAL JOIN takes " \
          "NATURAL JOIN section " \
          "NATURAL JOIN sectionmeetingtime; " \

    values = (groupID,)

    cur = conn.cursor()
    cur.execute(sql, values)
    results = cur.fetchall()
    cur.close()
    vnumbers = []
    names = []
    sections = []
    section_meeting_times = []
    for row in results:
        vnumber = row[0]
        name = db_entities.FullName(row[1], row[2])
        section = db_entities.Section(row[3], int(row[4]), int(row[5]))
        section_meeting_time = WeeklyTimeDelta(row[6], row[7], row[8])

        vnumbers += [vnumber]
        names += [name]
        sections += [section]
        section_meeting_times += [section_meeting_time]

    return vnumbers, names, sections, section_meeting_times


def is_valid_time_str(time_str):
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def time_string_is_before_time_string(time_str1, time_str2):
    t1 = datetime.datetime.strptime(time_str1, "%H:%M")
    delta1 = timedelta(hours=t1.hour, minutes=t1.minute)

    t2 = datetime.datetime.strptime(time_str2, "%H:%M")
    delta2 = timedelta(hours=t2.hour, minutes=t2.minute)

    return delta2.total_seconds() - delta1.total_seconds() > 0


def course_exists(courseNum, deptAbbrev):
    course_exists_sql = f"SELECT courseNum, deptAbbrev " \
                        f"FROM studygroupdatabase.course " \
                        f"WHERE courseNum=%s AND deptAbbrev=%s;"
    course_exists_values = (courseNum, deptAbbrev)
    cur = conn.cursor()
    cur.execute(course_exists_sql, course_exists_values)
    results = cur.fetchall()
    cur.close()
    return bool(results)


def is_valid_vnumber_format(vnumber: str):
    vnumber_regex = "^V\d{8}$"
    return bool(re.search(vnumber_regex, vnumber)) and ('\n' not in vnumber)


def vnumber_exists(vnumber: str):
    cur = conn.cursor()
    vnumber_exists_sql = f"SELECT VNumber " \
                        f"FROM studygroupdatabase.student " \
                        f"WHERE VNumber=%s;"
    vnumber_exists_values = (vnumber, )
    cur.execute(vnumber_exists_sql, vnumber_exists_values)
    results = cur.fetchall()
    cur.close()
    return bool(results)


def address_to_lat_lon(address: str) -> tuple:
    # https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
    response = requests.get(url).json()
    if not bool(response):
        return None, None
    else:
        lat = float(response[0]["lat"])
        lon = float(response[0]["lon"])
        return lat, lon


def is_valid_address(address: str) -> bool:
    try:
        return address_to_lat_lon(address) != (None, None)
    except Exception:
        return False


def is_valid_weekday(weekday: str):
    return weekday in {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}


def delete_invite_to_study_group_for_vnumber(studyGroupID, vnumber):
    delete_invite_sql = "DELETE FROM pendingStudyGroupInvites " \
                        "WHERE ReceiverVNumber=%s and studyGroupID=%s"
    delete_invite_values = (vnumber, studyGroupID)
    cur = conn.cursor()
    try:
        cur.execute(delete_invite_sql, delete_invite_values)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def add_vnumber_to_studygroup(v_number, study_group_id):
    join_study_group_sql = "INSERT INTO groupmembership (VNumber, studyGroupID)" \
                           "VALUES (%s, %s)"

    join_study_group_values = (v_number, study_group_id)
    cur = conn.cursor()
    try:
        cur.execute(join_study_group_sql, join_study_group_values)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def random_salt():
    return os.urandom(64)


def hash_password_and_salt(password: bytes, salt: bytes):
    return hashlib.pbkdf2_hmac('sha512', password, salt, 100_000).hex()


def get_sections_taken_by_students_with_vnumber(vnumber):
    get_sections_sql = "SELECT deptAbbrev, courseNum, sectionNum, meetingAddress " \
                       "FROM (SELECT * FROM takes WHERE VNumber = %s) as temp " \
                       "NATURAL JOIN section;"
    get_sections_values = (vnumber,)
    cur = conn.cursor()
    cur.execute(get_sections_sql, get_sections_values)
    sections_data = cur.fetchall()
    conn.commit()
    cur.close()
    sections = []
    for row in sections_data:
        s = db_entities.Section(row[0], int(row[1]), int(row[2]), row[3])
        sections.append(s)
    return sections


def get_study_groups_that_vnumber_is_invited_to(v_number: str):
    get_study_group_sql = "SELECT groupNickname, prefMethodOfComm, studyGroupID " \
                          "FROM (SELECT studyGroupID FROM pendingStudyGroupInvites WHERE ReceiverVNumber = %s) as temp " \
                          "NATURAL JOIN studygroup;"
    cur = conn.cursor()
    cur.execute(get_study_group_sql, (v_number,))
    results = cur.fetchall()
    study_groups = []
    for row in results:
        study_group = db_entities.StudyGroup(row[0], row[1], int(row[2]))
        study_groups.append(study_group)
    return study_groups


def get_study_groups_that_vnumber_is_part_of(v_number: str):
    get_study_groups_sql = "SELECT groupNickname, prefMethodOfComm, studyGroupID " \
                           "FROM (SELECT studyGroupID FROM groupmembership WHERE VNumber = %s) as temp " \
                           "NATURAL JOIN studygroup;"
    get_study_groups_values = (v_number,)
    cur = conn.cursor()
    cur.execute(get_study_groups_sql, get_study_groups_values)
    results = cur.fetchall()
    study_groups = []
    for row in results:
        study_group = db_entities.StudyGroup(row[0], row[1], int(row[2]))
        study_groups.append(study_group)
    return study_groups


def get_upcoming_meetings_for_vnumber(vnumber: str):
    upcoming_meetings_sql = \
        '''
        SELECT groupNickname, startTime, endTime, meetingType, location
        FROM (SELECT * FROM groupmembership WHERE VNumber = %s) AS temp1
        NATURAL JOIN studygroup
        NATURAL JOIN meets
        NATURAL JOIN meeting
        NATURAL JOIN
        (select meetingID, "Online" as meetingType, meetingURL as "location" 
        from onlinemeeting 
        UNION ALL 
        select meetingID, "In-Person" as meetingType, meetingLocationAddress as "location" 
        from inpersonmeeting) as temp2
        WHERE startTime > sysdate();
        '''

    upcoming_meetings_values = (vnumber, )

    cur = conn.cursor()
    cur.execute(upcoming_meetings_sql, upcoming_meetings_values)
    results = cur.fetchall()
    meetings = []
    for row in results:
        meetingType = row[3]
        if meetingType == 'Online':
            meeting = db_entities.OnlineMeeting(row[0], row[1], row[2], row[4])
        elif meetingType == 'In-Person':
            meeting = db_entities.InPersonMeeting(row[0], row[1], row[2], row[4])
        else:
            raise ValueError(f"Invalid meetingType '{meetingType}'")
        meetings.append(meeting)

    return meetings


def flag_meetings_with_conflicting_schedules(meetings: list[db_entities.Meeting]):
    is_conflicting_list = [False] * len(meetings)


def student_wants_to_work_on_assignment(vnumber: str, assignment_id: int, commit=False) -> bool:
    get_wants_to_work_on_sql = "SELECT * " \
                               "FROM wantstoworkon " \
                               "WHERE VNumber=%s and AssignmentID=%s;"
    get_wants_to_work_on_values = (vnumber, assignment_id)
    cur = conn.cursor()
    cur.execute(get_wants_to_work_on_sql, get_wants_to_work_on_values)
    response = cur.fetchall()
    if commit:
        conn.commit()
    cur.close()
    return bool(response)


def delete_assignments_to_work_on_for_vnumber(vnumber: str, assignment_ids, commit=True):
    delete_wants_to_work_sql = "DELETE FROM wantstoworkon " \
                               "WHERE VNumber=%s and AssignmentID=%s;"

    cur = conn.cursor()
    try:
        for assignment_id in assignment_ids:
            delete_wants_to_work_values = (vnumber, assignment_id)
            cur.execute(delete_wants_to_work_sql, delete_wants_to_work_values)
        if commit:
            conn.commit()
    except Exception:
        conn.rollback()
    finally:
        cur.close()


def add_assignments_to_work_on_for_vnumber(vnumber, assignment_ids_to_insert, commit=True):
    insert_wants_to_work_sql = "INSERT INTO wantstoworkon (VNumber, AssignmentID) " \
                               "VALUES (%s, %s);"
    cur = conn.cursor()
    try:
        for assignment_id in assignment_ids_to_insert:
            insert_wants_to_work_values = (vnumber, assignment_id)
            cur.execute(insert_wants_to_work_sql, insert_wants_to_work_values)
        if commit:
            conn.commit()
    except Exception:
        conn.rollback()
    finally:
        cur.close()


def assignment_ids_of_what_vnumber_wants_to_work_on(vnumber: str):
    get_assignment_ids_sql = "SELECT AssignmentID " \
                             "FROM wantstoworkon " \
                             "WHERE VNumber=%s"
    get_assignment_ids_values = (vnumber,)
    cur = conn.cursor()
    cur.execute(get_assignment_ids_sql, get_assignment_ids_values)
    response = cur.fetchall()
    conn.commit()
    cur.close()
    return {int(row[0]) for row in response}


def vnumber_is_taking_course(vnumber, course: db_entities.Course):
    already_added_course_sql = f"SELECT * " \
                               f"FROM studygroupdatabase.takes " \
                               f"WHERE VNumber = %s AND courseNum=%s AND deptAbbrev=%s;"
    already_added_course_values = (vnumber, course.courseNo, course.deptAbbrev)

    cur = conn.cursor()
    cur.execute(already_added_course_sql, already_added_course_values)
    result = cur.fetchall()
    cur.close()
    return bool(result)


def insert_vnumber_takes_section(vnumber: str, section: db_entities.Section) -> bool:
    takes_insert_sql = f"INSERT INTO studygroupdatabase.takes (VNumber, sectionNum, courseNum, deptAbbrev) " \
                       f"VALUES (%s, %s, %s, %s);"
    takes_insert_values = (vnumber, section.sectNo, section.courseNo, section.deptAbbrev)
    cur = conn.cursor()
    try:
        cur.execute(takes_insert_sql, takes_insert_values)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    finally:
        cur.close()


def add_meeting_times_to_section(meetingWeekdays: list[str], startTimes: list[str], endTimes: list[str],
                                 section: db_entities.Section):
    cur = conn.cursor()
    sql = "INSERT INTO sectionmeetingtime (deptAbbrev, courseNum, sectionNum, weekday, startTime, endTime) " \
          "VALUES (%s, %s, %s, %s, %s, %s);"
    try:
        for weekday, start, end in zip(meetingWeekdays, startTimes, endTimes):
            values = (section.deptAbbrev, section.courseNo, section.sectNo, weekday, start, end)
            cur.execute(sql, values)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    finally:
        cur.close()


@auth.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template("home.html")


@auth.route('/create_study_Group', methods=['GET', 'POST'])
def create_study_group():
    return render_template("request_sumbitted.html")


@auth.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        address = request.form.get('address')
        vnumber = request.form.get('VNumber')
        username = request.form.get('username')
        password = request.form.get('password')
        phonenumber = request.form.get('phoneNumber')
        dob = request.form.get('dateOfBirth')
        discord = request.form.get('discordUName')
        space = " "
        atSign = "@"

        passwordforsalty = password
        salt = random_salt()
        salted_hash = hash_password_and_salt(passwordforsalty.encode(), salt)
        latitude, longitude = address_to_lat_lon(address)

        if not is_valid_vnumber_format(vnumber):
            flash('Please enter a valid V-number (V########)', category='error')
        elif vnumber_exists(vnumber):
            flash('You already have an account', category='error')
        elif len(firstName) == 0 or space in firstName:
            flash('first Name cannot be empty or contain spaces', category='error')
        elif len(lastName) == 0 or space in lastName:
            flash('last Name cannot be empty or contain spaces', category='error')
        elif len(email) == 0 or space in email or atSign not in email:
            flash('check email', category='error')
        elif len(password) < 10:
            flash('password length must be 10', category='error')
        elif (latitude, longitude) == (None, None):
            flash('Address could not be found!')
        else:
            cur = conn.cursor()
            try:
                cur.execute(
                "INSERT INTO student (VNumber, firstName, lastName, username, email, discordUName, phoneNumber, dateOfBirth, address, saltedPassword, salt) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (vnumber, firstName, lastName, username, email, discord, phonenumber, dob, address, f"{salted_hash}",
                 f"{salt.hex()}"))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
            finally:
                cur.close()
            flash('Your account has been created', category='success')

    return render_template("createAccount.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    after_login_go_to = flask.url_for('auth.add_section_for_user')

    if 'VNumber' in session:
        # if the user is already logged in, just push them through to the next page
        return flask.redirect(after_login_go_to)

    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sql = f"SELECT VNumber, saltedPassword, salt from studygroupdatabase.student WHERE username='{username}';"
        cur = conn.cursor()
        cur.execute(sql)
        myResult = cur.fetchall()
        conn.commit()
        cur.close()

        if len(myResult) != 1:
            flash('Authentication failed! Check credentials.', category='error')
        else:
            VNumber, actual_salted_password, salt_hex = myResult[0]
            salt = bytes.fromhex(salt_hex)
            entered_salted_password = hash_password_and_salt(password.encode(), salt)
            if actual_salted_password == entered_salted_password:
                session['VNumber'] = VNumber
                flash("Success! You're logged in.", category='success')
                return flask.redirect(after_login_go_to)
            else:
                flash('Authentication failed! Check credentials.', category='error')

        return render_template('login.html')


@auth.route('/sections', methods=['GET', 'POST'])
def add_section_for_user():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    if request.method == 'GET':
        return render_template("sections.html", form_values=dict())

    if request.method == 'POST':
        v_number = session['VNumber']  # request.cookies.get('VNumber')
        try:
            sectionNum = int(request.form.get('sectionNum'))
            assert sectionNum >= 0
        except (ValueError, AssertionError):
            flash("Invalid Section Number.", category='error')
            return render_template("sections.html", form_values=request.form)
        try:
            courseNum = int(request.form.get('courseNum'))
            assert courseNum >= 0
        except (ValueError, AssertionError):
            flash("Invalid Course Number.", category='error')
            return render_template("sections.html", form_values=request.form)

        try:
            deptAbbrev = request.form.get('deptAbbrev').strip()
            assert len(deptAbbrev) == 4 and bool(re.search('^[A-Z]{4}$', deptAbbrev))
        except AssertionError:
            flash("Invalid Department Abbreviation (4 characters, all caps).", category='error')
            return render_template("sections.html", form_values=request.form)

        course_already_exists = course_exists(courseNum, deptAbbrev)

        if not course_already_exists:  # if this course hasn't been added to the database yet
            session['sectionNumber'] = sectionNum
            session['courseNumber'] = courseNum
            session['deptAbbrev'] = deptAbbrev
            return flask.redirect(url_for('auth.add_course'))

        section = db_entities.Section(deptAbbrev, courseNum, sectionNum, '?')

        if not section.exists_in_db(conn):  # if this section hasn't been added to the database yet
            # then add this tuple to the database
            session['sectionNumber'] = sectionNum
            session['courseNumber'] = courseNum
            session['deptAbbrev'] = deptAbbrev
            return flask.redirect(url_for('auth.add_section'))

        course = db_entities.Course(deptAbbrev, courseNum, '')
        already_taking_course = vnumber_is_taking_course(v_number, course)
        if already_taking_course:
            flash("You've already added this course to your schedule", category='error')
            return render_template("sections.html", form_values=request.form)

        section = db_entities.Section.fromCourseAndSectionNumber(course, sectionNum)
        successfully_added_section = insert_vnumber_takes_section(v_number, section)

        if successfully_added_section:
            flash("Successfully added course to your schedule!", category='success')
        else:
            flash("Error adding section", category='error')

        return render_template('sections.html', form_values=dict())


@auth.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    if not {'sectionNumber', 'courseNumber', 'deptAbbrev'}.issubset(session):
        return flask.redirect(flask.url_for('auth.add_section_for_user'))

    courseNum = session['courseNumber']
    deptAbbrev = session['deptAbbrev']

    course_already_exists = course_exists(courseNum, deptAbbrev)
    if course_already_exists:
        return flask.redirect(flask.url_for('auth.add_section_for_user'))

    if request.method == 'GET':
        return render_template("add_course.html")

    if request.method == 'POST':
        courseName = request.form.get('courseName').strip()
        if len(courseName) == 0:
            flash("Must provide a course name", category="error")
            return render_template("add_course.html")

        insert_course_sql = "INSERT INTO studygroupdatabase.course (courseNum, deptAbbrev, courseName) " \
                            "VALUES (%s, %s, %s)"
        course_insert_values = (courseNum, deptAbbrev, courseName)

        cur = conn.cursor()
        try:
            cur.execute(insert_course_sql, course_insert_values)
            conn.commit()
            print("Successfully committed")
            return flask.redirect(flask.url_for('auth.add_section'))
        except Exception as e:
            print(e)
            conn.rollback()
            flash("Error adding course to database", category="error")
            return render_template("add_course.html")
        finally:
            cur.close()


@auth.route('/new_section', methods=['GET', 'POST'])
def add_section():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    if not {'sectionNumber', 'courseNumber', 'deptAbbrev'}.issubset(session):
        return flask.redirect(flask.url_for('auth.add_section_for_user'))

    sectionNum = session['sectionNumber']
    courseNum = session['courseNumber']
    deptAbbrev = session['deptAbbrev']
    vnumber = session['VNumber']

    section = db_entities.Section(deptAbbrev, courseNum, sectionNum)
    section_already_exists = section.exists_in_db(conn)
    if section_already_exists:
        return flask.redirect(flask.url_for('auth.add_section_for_user'))

    if request.method == 'GET':
        return render_template("new_section.html")

    if request.method == 'POST':
        meetingAddress = request.form.get('meetingAddress').strip()
        meetingWeekdays = request.form.getlist('meetingDaySelector')
        startTimes = request.form.getlist('startTimeInput')
        endTimes = request.form.getlist('endTimeInput')
        print(f'{meetingAddress=!r}')
        print(f'{meetingWeekdays=!r}')
        print(f'{startTimes=!r}')
        print(f'{endTimes=!r}')

        if not meetingAddress:
            flash("Please enter a valid address", category="error")
            return render_template("new_section.html")

        if not all([meetingWeekdays, startTimes, endTimes]):
            flash("Please enter meeting times", category="error")
            return render_template("new_section.html")

        if not (len(meetingWeekdays) == len(startTimes) and len(startTimes) == len(endTimes)):
            flash("Please enter an equal number of weekdays, start times, and end times", category="error")
            return render_template("new_section.html")

        if not is_valid_address(meetingAddress):
            flash("Please enter a valid address", category="error")
            return render_template("new_section.html")

        if not all(is_valid_weekday(day) for day in meetingWeekdays):
            flash("Please enter a valid weekday, Monday through Friday", category="error")
            return render_template("new_section.html")

        if not all(is_valid_time_str(time_str) for time_str in startTimes + endTimes):
            flash("Please enter valid meeting times", category="error")
            return render_template("new_section.html")

        if not all(is_valid_time_str(time_str) for time_str in startTimes + endTimes):
            flash("Please enter valid meeting times", category="error")
            return render_template("new_section.html")

        if not all(time_string_is_before_time_string(start, end) for start, end in zip(startTimes, endTimes)):
            flash("Please enter start times before end times", category="error")
            return render_template("new_section.html")

        section.meetingAddress = meetingAddress
        successfully_created_section = section.add_to_db(conn)
        if not successfully_created_section:
            flash("Error while creating section", category='error')
            return render_template("new_section.html")

        successfully_added_section_meeting_times = add_meeting_times_to_section(meetingWeekdays, startTimes, endTimes,
                                                                                section)
        if not successfully_added_section_meeting_times:
            flash("Error while adding meeting times to section.", category='error')
            return render_template("new_section.html")

        successfully_added_takes_section = insert_vnumber_takes_section(vnumber, section)
        if not successfully_added_takes_section:
            flash("Error while adding section to your schedule", category='error')
            return render_template("new_section.html")

        flash('Successfully created section and added it to your course!', category='Success')
        session.pop('sectionNumber', None)
        session.pop('courseNumber', None)
        session.pop('deptAbbrev', None)
        return flask.redirect(flask.url_for('auth.add_section_for_user'))


@auth.route('/assignments', methods=['GET', 'POST'])
def view_assignments():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    v_number = session['VNumber']

    get_all_assignments_sql = "SELECT deptAbbrev, courseNum, sectionNum, meetingAddress, AssignmentID, AssignmentName, AssignmentDescription, Points, DueDate " \
                              "FROM (SELECT * FROM takes WHERE VNumber = %s) as temp " \
                              "NATURAL JOIN section " \
                              "NATURAL JOIN assigns " \
                              "NATURAL JOIN assignment;"
    get_all_assignments_values = (v_number,)

    cur = conn.cursor()
    cur.execute(get_all_assignments_sql, get_all_assignments_values)
    all_assignments = cur.fetchall()
    conn.commit()
    cur.close()
    sections, assignments = [], []
    for row in all_assignments:
        section = db_entities.Section(row[0], int(row[1]), int(row[2]), row[3])
        assignment = db_entities.Assignment(int(row[4]), row[5], row[6], int(row[7]), row[8])
        sections.append(section)
        assignments.append(assignment)

    all_assignment_ids = {a.AssignmentID for a in assignments}
    wants_to_work_on_assignment_ids = assignment_ids_of_what_vnumber_wants_to_work_on(v_number)
    does_not_want_to_work_on_assignment_ids = all_assignment_ids - wants_to_work_on_assignment_ids

    if request.method == 'GET':
        return render_template('assignments.html', sections=sections, assignments=assignments,
                               checked_assignment_ids=wants_to_work_on_assignment_ids)

    if request.method == 'POST':
        print(request.form)
        if 'SavePreferences' in request.form:
            selected_assignment_ids = {int(selected_assignment_id) for selected_assignment_id in
                                       request.form.getlist('WorkingOnCheckBox')}
            unselected_assignment_ids = all_assignment_ids - selected_assignment_ids

            assignment_ids_to_insert = selected_assignment_ids - wants_to_work_on_assignment_ids
            assignment_ids_to_delete = unselected_assignment_ids - does_not_want_to_work_on_assignment_ids

            delete_assignments_to_work_on_for_vnumber(v_number, assignment_ids_to_delete)

            add_assignments_to_work_on_for_vnumber(v_number, assignment_ids_to_insert)

            flash("Successfully updated preferences!", category='success')
            return flask.redirect(flask.url_for('auth.view_assignments'))

        if 'AddAssignmentsButton' in request.form:
            return flask.redirect(flask.url_for('auth.add_assignments'))


@auth.route('/add_assignments', methods=['GET', 'POST'])
def add_assignments():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    sections = get_sections_taken_by_students_with_vnumber(session['VNumber'])
    if request.method == 'GET':
        return render_template('add_assignments.html', sections=sections, form_values=dict())

    if request.method == 'POST':
        if "AddCourseButton" in request.form:
            return flask.redirect(flask.url_for('auth.add_section_for_user'))

        if "CreateAssignmentButton" in request.form:
            section_str = request.form.get('SectionSelector')
            assignment_name = request.form.get('AssignmentName').strip()
            assignment_description = request.form.get('AssignmentDescription').strip()
            assignment_points_str = request.form.get('AssignmentPoints')
            assignment_due_date_str = request.form.get('DueDateInput')

            try:
                section_tokens = section_str.split('|')
                dept_name = section_tokens[0]
                courseNumber = int(section_tokens[1])
                sectionNumber = int(section_tokens[2])
                section = db_entities.Section(dept_name, courseNumber, sectionNumber)
                assert section.exists_in_db(conn)
            except (ValueError, IndexError, AssertionError):
                flash("Invalid Section Input", category='error')
                return render_template('add_assignments.html', sections=sections, form_values=request.form)
            try:
                print(f'{assignment_due_date_str=!r}')
                due_date_datetime = datetime.datetime.strptime(assignment_due_date_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                flash("Please enter a valid due date", category='error')
                return render_template('add_assignments.html', sections=sections, form_values=request.form)

            try:
                assignment_points = int(assignment_points_str)
                assert assignment_points >= 0
            except (ValueError, AssertionError):
                flash("Please enter a valid number of points", category='error')
                return render_template('add_assignments.html', sections=sections, form_values=request.form)

            if not (0 < len(assignment_name) < 100):
                flash("Please enter the name of the assignment", category='error')
                return render_template('add_assignments.html', sections=sections, form_values=request.form)

            if not (0 < len(assignment_description) < 500):
                flash("Please enter a short description of the assignment", category='error')
                return render_template('add_assignments.html', sections=sections, form_values=request.form)

            # insert assignment into assignment table and then link Section and Assignment with the Assigns table
            insert_assignment_sql = "INSERT INTO assignment (AssignmentName, AssignmentDescription, Points, DueDate) VALUES (%s, %s, %s, %s);"
            insert_assignment_values = (assignment_name, assignment_description, assignment_points, due_date_datetime)
            cur = conn.cursor()
            try:
                cur.execute(insert_assignment_sql, insert_assignment_values)
                cur.execute("SELECT LAST_INSERT_ID();")
                results = cur.fetchall()
                new_assignment_id = int(results[0][0])
            except Exception as e:
                print(e)
                conn.rollback()
                flash("Error while adding to database.", category='error')
                return render_template('add_assignments.html', sections=sections, form_values=request.form)

            insert_into_assigns_sql = "INSERT INTO assigns (AssignmentID, deptAbbrev, courseNum, sectionNum) " \
                                      "VALUES (%s, %s, %s, %s);"
            insert_into_assigns_values = (new_assignment_id, dept_name, courseNumber, sectionNumber)
            cur.execute(insert_into_assigns_sql, insert_into_assigns_values)
            conn.commit()
            cur.close()
            flash(f"Successfully added assignment to {dept_name} {courseNumber}, {sectionNumber}", category='success')

        return flask.redirect(flask.url_for('auth.add_assignments'))


'''
section_str = (<class 'str'>) CMSC|508|1
assignment_name = (<class 'str'>) Homework 6
assignment_description = (<class 'str'>) naegwjlglnbfknlfgknlbfklndf
assignment_points = (<class 'str'>) 100
assignment_due_date = (<class 'str'>) 2021-12-17T20:30
'''


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop("VNumber", None)
    return render_template('logout.html')


@auth.route('/study_group_invites', methods=['GET', 'POST'])
def study_group_invites():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    v_number = session['VNumber']
    study_groups = get_study_groups_that_vnumber_is_invited_to(v_number)
    if request.method == 'GET':
        return render_template('study_group_invites.html', study_groups=study_groups)

    if request.method == 'POST':
        if 'SendInviteButton' in request.form:
            return flask.redirect(flask.url_for('auth.send_invite'))
        button_name = request.form.get("name")
        user_accepted_invite = (button_name == "AcceptButton")

        try:
            study_group_id = int(request.form.get('value'))
            assert study_group_id in {study_group.studyGroupID for study_group in study_groups}
        except (AssertionError, ValueError):
            flash('Invalid study group ID', category='error')
            return render_template("study_group_invites.html")

        if user_accepted_invite:
            add_vnumber_to_studygroup(v_number, study_group_id)

        delete_invite_to_study_group_for_vnumber(study_group_id, v_number)

        return render_template("study_group_invites.html")


@auth.route('/create_meeting', methods=['GET', 'POST'])
def create_meeting():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    v_number = session['VNumber']

    addresses_study_tools, all_study_tools = db_entities.StudyTools.get_all_locations_study_tools_from_database(conn)

    study_groups = get_study_groups_that_vnumber_is_part_of(v_number)
    study_groups_meeting_times = dict()  # studyGroupID -> {"vnumbers": v_numbers, 'names': names, 'sections': sections, 'section_meeting_times': section_meeting_times, 'colors': v_number_to_color} for that given study group
    for study_group in study_groups:
        v_numbers, names, sections, section_meeting_times = get_section_meeting_times_for_all_members_in_group(
            study_group.studyGroupID)
        members_unique_v_numbers = sorted(list(set(v_numbers)))
        color_palette = generate_color_palette(len(members_unique_v_numbers), study_group.studyGroupID, 0.5, 0.8)
        for i in range(len(color_palette)):
            color_palette[i] += '77'  # add some transparency to it

        v_number_to_color = dict(zip(members_unique_v_numbers, color_palette))
        study_groups_meeting_times[study_group.studyGroupID] = {"vnumbers": v_numbers, "names": names, "sections": sections,
                                                                "section_meeting_times": section_meeting_times,
                                                                "colors": v_number_to_color}

    json_study_groups = json.dumps(study_groups, cls=db_entities.DefaultJSONEncoder)
    json_groups_meeting_times = json.dumps(study_groups_meeting_times, cls=db_entities.DefaultJSONEncoder)
    json_study_tools = json.dumps(addresses_study_tools, cls=db_entities.DefaultJSONEncoder)

    render_create_meeting_template = lambda: render_template('create_meeting.html',
                                                             study_groups=json.loads(json_study_groups),
                                                             study_groups_meeting_times=json.loads(json_groups_meeting_times),
                                                             study_tools=json.loads(json_study_tools),
                                                             all_study_tools=all_study_tools)

    if request.method == 'GET':
        return render_create_meeting_template()

    if request.method == 'POST':
        selector_study_group_id_str = request.form.get("StudyGroupSelect")
        meeting_start_str = request.form.get('startTimeInput')
        meeting_end_str = request.form.get('endTimeInput')
        meeting_date_str = request.form.get('dateInput')
        meeting_type = request.form.get("MeetingTypeSelect")


        try:
            selector_study_group_id = int(selector_study_group_id_str)
            assert any(study_group.studyGroupID == selector_study_group_id for study_group in study_groups)
        except (ValueError, AssertionError) as e:
            print(e)
            flash("Invalid study group ID", category='error')
            return render_create_meeting_template()

        try:
            meeting_date = datetime.datetime.strptime(meeting_date_str, '%Y-%m-%d')
            t = datetime.datetime.strptime(meeting_start_str, "%H:%M")
            start_delta = datetime.timedelta(hours=t.hour, minutes=t.minute)
            t = datetime.datetime.strptime(meeting_end_str, "%H:%M")
            end_delta = datetime.timedelta(hours=t.hour, minutes=t.minute)
            start_datetime = meeting_date + start_delta
            end_datetime = meeting_date + end_delta
            assert start_datetime < end_datetime
        except (ValueError, AssertionError) as e:
            print(e)
            flash("Please enter a valid meeting time.", category='error')
            return render_create_meeting_template()

        if meeting_type == "Online":
            meeting_link = request.form.get("LinkInputTextBox")
            successfully_created_group = create_online_meeting(selector_study_group_id, start_datetime,
                                                               end_datetime, meeting_link)

        elif meeting_type == "In-Person":
            meeting_address = request.form.get("AddressInputTextBox")
            if not is_valid_address(meeting_address):
                flash("Please enter a valid address", category='error')
                return render_create_meeting_template()

            successfully_created_group = create_in_person_meeting(selector_study_group_id, start_datetime,
                                                                 end_datetime, meeting_address)
        else:
            flash("Please enter a valid meeting type.", category='error')
            return render_create_meeting_template()

        if successfully_created_group:
            flash("Successfully created meeting", category='success')
            return render_create_meeting_template()
        else:
            flash("An error occurred while creating meeting", category='error')
            return render_create_meeting_template()


@auth.route('/my_groups', methods=['GET', 'POST'])
def my_groups():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    v_number = session['VNumber']

    show_study_group_sql = "SELECT groupNickname, prefMethodOfComm, studyGroupID " \
                           "FROM studygroup NATURAL JOIN groupmembership WHERE VNumber = %s;"

    get_all_studygroups_values = v_number
    cur = conn.cursor()
    cur.execute(show_study_group_sql, get_all_studygroups_values)
    all_study_groups = cur.fetchall()
    conn.commit()
    cur.close()

    Group_List = []
    for row in all_study_groups:
        sgroup = db_entities.StudyGroup(row[0], row[1], int(row[2]))
        Group_List.append(sgroup)

    if request.method == 'GET':
        return render_template('mygroups.html', Group_List=Group_List)

    if request.method == 'POST':
        if 'CreateGroupButton' in request.form:
            return flask.redirect(flask.url_for('auth.create_group'))


@auth.route('/create_group', methods=['GET', 'POST'])
def create_group():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    v_number = session['VNumber']

    if request.method == 'GET':
        return render_template('Create_Study_Group.html')

    if request.method == 'POST':
        if "CreateTheGroupButton" in request.form:
            group_name = request.form.get("StudyGroupName")
            communication_meth = request.form.get("MethodOfCommunication")

            if (len(group_name) == 0 or len(group_name) > 20):
                flash("Please enter a group name less than 20 characters", category='error')
                return render_template('Create_Study_Group.html')
            if (communication_meth == None):
                flash("Please select a preferred method of communication", category='error')
                return render_template('Create_Study_Group.html')
            else:
                insert_create_group_sql = "INSERT INTO studygroupdatabase.studygroup (prefMethodOfComm, groupNickname)" \
                                          "VALUES (%s,%s);"
                insert_create_group_sql_values = (communication_meth, group_name)
                insert_groupmembership_sql = "INSERT INTO studygroupdatabase.groupmembership (VNumber, studyGroupId)" \
                                             "VALUES (%s,(SELECT LAST_INSERT_ID()));"
                insert_groupmembership_sql_values = (v_number,)
                cur = conn.cursor()
                cur.execute(insert_create_group_sql, insert_create_group_sql_values)
                cur.execute(insert_groupmembership_sql, insert_groupmembership_sql_values)
                conn.commit()
                cur.close()
                flash("Successfully created group" + group_name, category='success')
        return render_template('Create_Study_Group.html')


@auth.route('/send_invite', methods=['GET', 'POST'])
def send_invite():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    v_number = session['VNumber']

    # filling in the select options with groups user is in

    show_study_group_sql = "SELECT groupNickname, prefMethodOfComm, studyGroupID " \
                           "FROM studygroup NATURAL JOIN groupmembership WHERE VNumber = %s;"

    get_all_studygroups_values = v_number
    cur = conn.cursor()
    cur.execute(show_study_group_sql, get_all_studygroups_values)
    all_study_groups = cur.fetchall()
    conn.commit()
    cur.close()

    Group_List = []
    for row in all_study_groups:
        sgroup = db_entities.StudyGroup(row[0], row[1], int(row[2]))
        Group_List.append(sgroup)

    # getting people who want to work on same assignments as user for filliing in options in datalist

    get_people_for_dropdown_sql = "SELECT CONCAT(VNumber,' ', firstName) " \
                                  " FROM wantstoworkon NATURAL JOIN student " \
                                  "WHERE assignmentID IN " \
                                  "(SELECT assignmentID FROM wantstoworkon WHERE VNumber = %s) AND VNumber != %s;"
    get_people_for_dropdown_sql_value = (v_number, v_number)
    cur = conn.cursor()
    cur.execute(get_people_for_dropdown_sql, get_people_for_dropdown_sql_value)
    people_for_dropdown = cur.fetchall()
    conn.commit()
    cur.close()

    list_of_people = [row[0] for row in people_for_dropdown]

    if request.method == 'GET':
        return render_template('Send_Invites.html', Group_List=Group_List, list_of_people=list_of_people)

    if request.method == 'POST':
        if 'SendTheInviteButton' in request.form:
            invite_receiver = request.form.get('VNumberOfReceiver')
            study_group_id = int(request.form.get("GroupThatsInviting"))

            if invite_receiver == None:
                flash("Please select the person you want to invite", category='error')
                return render_template('Send_Invites.html')
            if study_group_id == None:
                flash("Please select the group you want to invite the person to", category='error')
                return render_template('Send_Invites.html')
            else:
                # getting the selected study group's ID
                receiver_v_number = invite_receiver.split()[0]

                # now sending the invite
                sending_the_invite_sql = "INSERT INTO pendingStudyGroupInvites (SenderVNumber, ReceiverVNumber, studyGroupID)" \
                                         "VALUES (%s, %s, %s);"
                sending_the_invite_sql_values = (v_number, receiver_v_number, study_group_id)
                cur = conn.cursor()
                cur.execute(sending_the_invite_sql, sending_the_invite_sql_values)
                conn.commit()
                cur.close()
                flash("Successfully sent invite to " + invite_receiver, category='success')
        return render_template('Send_Invites.html')


@auth.route('/meetings', methods=['GET', 'POST'])
def view_meetings():
    if 'VNumber' not in session:
        # redirect to login page if the user isn't signed in
        return flask.redirect(flask.url_for('auth.login'))

    v_number = session['VNumber']

    upcoming_meetings = get_upcoming_meetings_for_vnumber(v_number)

    if request.method == 'GET':
        return render_template('meetings.html', meetings=upcoming_meetings)

    if request.method == 'POST':
        return flask.redirect(flask.url_for('auth.create_meeting'))


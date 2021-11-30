import random
import re
from collections import OrderedDict
import sys
import datetime
import os


def python_type_to_sql_literal(row_element, elem_type):
    if elem_type is int:
        return str(row_element)
    elif elem_type is str:
        return f"'{row_element}'"
    elif elem_type is datetime.datetime:
        return f"'{row_element}'"


def join_all_files(filenames, out_filename):
    with open(out_filename, "w+") as f_out:
        for file in filenames:
            with open(file, 'r') as f_in:
                f_out.write(f_in.read())
                f_out.write("\n\n")


def save_table_to_sql_procedure(markdown_file, column_types, table_name: str, sql_filename: str, no_repeats=True):
    if not sql_filename.lower().endswith(".sql"):
        sql_filename += ".sql"

    sql_insert_command = f'INSERT INTO {table_name} VALUES ('

    procedure_name = f"populate_{table_name}_procedure"
    seen_rows = set()
    with open(markdown_file, 'r') as f_in:
        with open(sql_filename, 'w+') as f_out:
            f_out.write(f"DROP PROCEDURE IF EXISTS {procedure_name};\n")
            f_out.write("delimiter //\n")
            f_out.write(f"CREATE PROCEDURE {procedure_name}()\n")
            f_out.write("BEGIN\n")
            lines = f_in.readlines()
            for i in range(2, len(lines)):
                line = lines[i].strip()
                if not line:  # ignore blank / whitespace lines
                    continue
                row_elements = tuple(line.split(' | '))
                if no_repeats and row_elements in seen_rows:
                    continue
                seen_rows.add(row_elements)
                sql_insert_command = f'\tINSERT INTO {table_name} VALUES ('
                sql_insert_command += ', '.join(python_type_to_sql_literal(row_element, elem_type)
                                                for row_element, elem_type in zip(row_elements, column_types))
                sql_insert_command += ');\n'

                f_out.write(sql_insert_command)

            f_out.write("END //\n")
            f_out.write("delimiter ;\n")
            print(f"CALL {procedure_name}();")

    return os.path.abspath(sql_filename)


if __name__ == "__main__":
    all_files = []

    all_files.append(save_table_to_sql_procedure('AssignmentTable.md', [int, str, str, int, datetime.datetime],
                                 'assignment', '../../src/Database/CreateDBScripts/create_assignments.sql'))

    all_files.append(save_table_to_sql_procedure('AssignsTable.md', [int, str, int, int],
                                 'assigns', '../../src/Database/CreateDBScripts/create_assigns.sql'))

    all_files.append(save_table_to_sql_procedure('ComprisesTable.md', [str, int],
                                 'groupmembership', '../../src/Database/CreateDBScripts/create_group_membership.sql'))

    all_files.append(save_table_to_sql_procedure('CourseTable.md', [str, int, str],
                                 'course', '../../src/Database/CreateDBScripts/create_course.sql'))

    all_files.append(save_table_to_sql_procedure('InPersonMeetingStudyToolsTable.md', [str, str],
                                 'studytools', '../../src/Database/CreateDBScripts/create_study_tools.sql'))

    all_files.append(save_table_to_sql_procedure('InPersonMeetingTable.md', [int, str],
                                 'inpersonmeeting', '../../src/Database/CreateDBScripts/create_inperson_meeting.sql'))

    all_files.append(save_table_to_sql_procedure('MeetingTable.md', [int, datetime.datetime, datetime.datetime],
                                 'meeting', '../../src/Database/CreateDBScripts/create_meeting.sql'))

    all_files.append(save_table_to_sql_procedure('Meets.md', [int, int],
                                 'meets', '../../src/Database/CreateDBScripts/create_meets.sql'))

    all_files.append(save_table_to_sql_procedure('OnlineMeetingTable.md', [int, str],
                                 'onlinemeeting', '../../src/Database/CreateDBScripts/create_online_meeting.sql'))

    all_files.append(save_table_to_sql_procedure('SectionMeetingTimesTable.md', [str, int, int, str, datetime.datetime, datetime.datetime],
                                 'sectionmeetingtime', '../../src/Database/CreateDBScripts/create_sectionmeetingtimes.sql'))

    all_files.append(save_table_to_sql_procedure('SectionTable.md', [str, int, int, str],
                                 'section', '../../src/Database/CreateDBScripts/create_section.sql'))

    all_files.append(save_table_to_sql_procedure('StudentTable.md', [str, str, str, str, str, str, str, datetime.datetime, str, str, str],
                                 'student', '../../src/Database/CreateDBScripts/create_student.sql'))

    all_files.append(save_table_to_sql_procedure('StudyGroupTable.md', [int, str, str],
                                 'studygroup', '../../src/Database/CreateDBScripts/create_studygroup.sql'))

    all_files.append(save_table_to_sql_procedure('TakesTable.md', [str, str, int, int],
                                 'takes', '../../src/Database/CreateDBScripts/create_takes.sql'))
    
    all_files.append(save_table_to_sql_procedure('WantsToWorkOnTable.md', [str, int],
                                 'wantstoworkon', '../../src/Database/CreateDBScripts/create_wantstoworkon.sql'))

    all_files.append(save_table_to_sql_procedure('WorksOn.md', [int, int],
                                 'workson', '../../src/Database/CreateDBScripts/create_workson.sql'))

    join_all_files(all_files, "../../src/Database/CreateDBScripts/all_populate_procedures.sql")
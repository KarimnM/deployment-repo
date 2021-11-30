**Entities**

Student(<ins>VNumber</ins>, firstName, lastName, address, dateOfBirth, email, discordName, phoneNumber, username, passwordHash, salt)

Section(<ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, *SectionNumber*, MeetingStartTime, MeetingEndTime, MeetingAddress)

Course(<ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, CourseName)

StudyGroup(<ins>studyGroupID</ins>, prefMethodOfComm, groupNickname)

Meeting(<ins>MeetingID</ins>, startTime, endTime)

OnlineMeeting(<ins>MeetingID</ins>, meetingURL)

InPersonMeeting(<ins>MeetingID</ins>, meetingLocationAddress, studyTools)

Assignment(<ins>AssignmentID</ins>, AssignmentName, Description, Points, DueDate)

**Relationships**

Takes(<ins>VNumber</ins>, <ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, <ins>SectionNumber</ins>)

Comprises(<ins>VNumber</ins>, <ins>studyGroupID</ins>)

WantsToWorkOn(<ins>VNumber</ins>, <ins>AssignmentID</ins>)

Assigns(<ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, <ins>SectionNumber</ins>, <ins>AssignmentID</ins>)

WorksOn(<ins>MeetingID</ins>, <ins>AssignmentID</ins>)

Meets(<ins>studyGroupID</ins>, <ins>MeetingID</ins>)

**Types, Domains, and Constraints**

VNumber: varchar with length 9 of the form 'Vdddddddd', not nullable

firstName: varchar with max length 50, not nullable

lastName: varchar with max length 50, not nullable

address: varchar with max length 50, not nullable 

dateOfBirth: date with format (YYYY-MM-DD), not nullable

email: varchar with max length 50, valid email address as defined by RFC 5322, not nullable

discordName: varchar with max length 50 of the form \w+#\d{4} , nullable

phoneNumber: varchar of length 12 with form ddd-ddd-dddd, nullable

username: var char with max length 50 using only word characters, not nullable

passwordHash: var char of length 128 using only hexadecimal charcters, not nullable

salt: var char of length 128 using only hexadecimal characters, not nullable

CourseNum: positive integer, not nullable

DeptAbbrev: varchar of length 4 consisting of only uppercase letters, not nullable

SectionNumber: positive integer, not nullable

MeetingStartTime: DateTime of the form (YYYY-MM-DD HH-MM), not nullable

MeetingEndTime:  DateTime of the form (YYYY-MM-DD HH-MM), must be after its associated MeetingStartTime, not nullable

MeetingAddress: varchar with max length 50, not nullable 

CourseName: var char of max length(50), not nullable

studyGroupID: non-negative integer, not nullable

prefMethodOfComm: var char of max length 50, not nullable

groupNickname: var char of max length 50, not nullable

MeetingID: non-negative integer, not nullable

startTime: DateTime of the form (YYYY-MM-DD HH-MM), not nullable

endTime:  DateTime of the form (YYYY-MM-DD HH-MM), must be chronologically less than startTime, not nullable

meetingURL: var char of length 2040, not nullable

meetingLocationAddress: var char of max length 50, not nullable

studyTools: varchar of length 50, not nullable

AssignmentID: integer > 0, not nullable

AssignmentName: varchar of max length 100, not nullable

Description: varchar of max length 500, not nullable

Points: non-negative integer, not nullable

DueDate: DateTime of the form (YYYY-MM-DD HH-MM) (military time), not nullable

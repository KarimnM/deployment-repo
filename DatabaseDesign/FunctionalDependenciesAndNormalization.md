# Function Dependencies in Study Group Database

## Original Relational Schema

Refer to [RelationalSchema.md](https://github.com/cmsc-vcu/semester_project-team_8/blob/master/DatabaseDesign/RelationalScheme.md)

## Normalized Relational Schema

Student(<ins>VNumber</ins>, firstName, lastName, address, dateOfBirth, email, discordName, phoneNumber, username, passwordHash, salt)

Section(<ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, *SectionNumber*, MeetingAddress)

SectionMeetingTimes(<ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, <ins>SectionNumber</ins>, MeetingStartTime, MeetingEndTime)

Course(<ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, CourseName)

StudyGroup(<ins>studyGroupID</ins>, prefMethodOfComm, groupNickname)

Meeting(<ins>MeetingID</ins>, startTime, endTime)

OnlineMeeting(<ins>MeetingID</ins>, meetingURL)

InPersonMeeting(<ins>MeetingID</ins>, meetingLocationAddress)

InPersonMeetingStudyTools(<ins>meetingLocationAddress</ins>, studyTool)

Assignment(<ins>AssignmentID</ins>, AssignmentName, Description, Points, DueDate)

Takes(<ins>VNumber</ins>, <ins>SectionNumber</ins>, <ins>CourseNum</ins>, <ins>DeptAbbrev</ins>)

Comprises(<ins>VNumber</ins>, <ins>studyGroupID</ins>)

WantsToWorkOn(<ins>VNumber</ins>, <ins>AssignmentID</ins>)

Assigns(<ins>CourseNum</ins>, <ins>DeptAbbrev</ins>, <ins>SectionNumber</ins>, <ins>AssignmentID</ins>)

WorksOn(<ins>MeetingID</ins>, <ins>AssignmentID</ins>)

Meets(<ins>studyGroupID</ins>, <ins>MeetingID</ins>)

## Functional Dependencies for the above schema

VNumber &rarr; firstName,lastName, address, dateOfBirth, email, discordUName, phoneNumber, username, passwordHash, salt

SectionNumber, DeptAbbrev, CourseNum &rarr; MeetingAddress

SectionNumber, DeptAbbrev, CourseNum &rarr;&rarr; MeetingStartTime, MeetingEndTime

DeptAbbrev, CourseNum &rarr; CourseName

studyGroupID &rarr; groupNickname, prefMethodOfComm

MeetingID &rarr; startTime, endTime, meetingLocationAddress, meetingURL

meetingLocationAddress &rarr;&rarr; studyTools

AssignmentID &rarr; Description, Points, AssignmentName, DueDate

## Normalization Process


For the Student relation, all attributes are functionally determined by the single primary key "VNumber" (with no partial, transitive, or non-prime-to-prime dependecies), and there are no multivalued dependencies. This meets the defintion of 4NF, so no further normalization was necessary.


The same is true for the Assignment and StudyGroup relations; all attributes are functionally determined by a single primary key, and there are no partial, transitive, or non-prime-to-prime dependecies. Neither of these relations have multivalued attributes either, so they are also in 4NF.


The Section relation did have to be decomposed from its original schema in order to put it in 4NF. The original schema had the multivalued attributes MeetingStartTimes and MeetingEndTimes. These were pulled out and put into their own table (SectionMeetingTimes) to prevent redundant information. Because meetingStartTime and meetingEndTime are effectively a composite attribute, they can be treated as a single multi-valued attribute, so it meets the 4NF requirement.


After removing these attributes, the only non-prime attribute left in the Section relation was MeetingAddress, which is functionally dependant on the 3 primary keys (the only other attributes in the table left). MeetingAddress is not a key attribute for any functional dependency. This is also in 4NF.


The OnlineMeeting and InPersonMeeting relations are specializations of the Meeting relation. The original InPersonMeeting relation has a multivalued attribute "studyTools", which was pulled out and put into its own table InPersonMeetingStudyTools with the primary key "meetingLocationAddress". meetingLocationAddress functionally determines studyTools, and studyTools does not functional determine anything, so this new table is in 4NF. The new InPersonMeetingRelation now only contains the attributes MeetingID and meetingLocationAddress. MeetingID functionally determines meetingLocationAddress, and meetingLocationAddress doesn't determine anything, so this is also in 4NF. The same reasoning can be applied to both OnlineMeeting and Meeting and their attributes (MeetingID, meetingURL) and (MeetingID, startTime, endTime); they are also in 4NF.




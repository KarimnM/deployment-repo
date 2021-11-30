use studygroupdatabase;
show tables;
select * from student;
select * from pendingStudyGroupInvites;
select * from groupmembership;
select * from takes;
select * from assignment;
select * from course;
select * from section;
select * from groupmembership;
select * from meeting;
select * from sectionmeetingtime;
select * from student;
select * from wantstoworkon;

select * from assigns;

select firstName, saltedPassword, salt
from student
where firstName like 'User%';

select studyGroupID, prefMethodOfComm, groupNickname from
(select studyGroupID from groupmembership where VNumber = 'V00954912') as temp
natural join studygroup;

SELECT groupNickname, prefMethodOfComm, studyGroupID 
                           FROM (SELECT studyGroupID FROM groupmembership WHERE VNumber = 'V00954912') as temp
                           NATURAL JOIN studygroup;

select * from groupmembership where studyGroupID = 1;
select * from (select * from groupmembership where studyGroupID = 1) as temp natural join student;

select firstName, lastName, sectionNum, courseNum, deptAbbrev, weekday, startTime, endTime from
(select VNumber from groupmembership where studyGroupID = 1) as groupMemberVNumbers
NATURAL JOIN student
NATURAL JOIN takes
NATURAL JOIN section
NATURAL JOIN sectionmeetingtime;

delete from student where VNumber = 'V00954912';

/*
insert into pendingStudyGroupInvites (SenderVNumber, ReceiverVNumber, studyGroupID)
VALUES ("V23024342", "V00954912", 1);


insert into pendingStudyGroupInvites (SenderVNumber, ReceiverVNumber, studyGroupID)
VALUES ("V00954912", "V23024342", 25);


delete from sectionmeetingtime 
where deptAbbrev = 'CMSC' and courseNum='355';

commit;

delete from groupmembership where VNumber="V00954912" and studyGroupID=25;
*/

select groupNickname, startTime, endTime from groupmembership where studyGroupID = 25;

select * from meets;
select * from meeting;



SELECT groupNickname, startTime, endTime, meetingType, location
FROM (SELECT * FROM groupmembership WHERE VNumber = "V00954912") AS temp
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

select * from onlinemeeting;
select * from inpersonmeeting;

select * from groupmembership where VNumber = "V00954912"

SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS studygroupdatabase;
use studygroupdatabase;
show tables;

DROP TABLE IF EXISTS takes;
DROP TABLE IF EXISTS groupmembership;
DROP TABLE IF EXISTS wantstoworkon;
DROP TABLE IF EXISTS assigns;
DROP TABLE IF EXISTS workson;
DROP TABLE IF EXISTS meets;
DROP TABLE IF EXISTS pendingStudyGroupInvites;
DROP TABLE IF EXISTS sectionmeetingtime;
DROP TABLE IF EXISTS studytools;
DROP TABLE IF EXISTS assignment;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS studygroup;
DROP TABLE IF EXISTS section;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS onlinemeeting;
DROP TABLE IF EXISTS inpersonmeeting;
DROP TABLE IF EXISTS meeting;

DROP TRIGGER IF EXISTS cantInviteSelfInsertTrigger;




CREATE TABLE assignment
(
	AssignmentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	AssignmentName VARCHAR(100) NOT NULL,
    AssignmentDescription  VARCHAR(500) NOT NULL,
    Points INT NOT NULL,
    DueDate DATETIME NOT NULL
);


CREATE TABLE student
(
	VNumber	VARCHAR(9) NOT NULL PRIMARY KEY CONSTRAINT valid_v_number_contraint check(VNumber RLIKE'^V[[:digit:]]{8}$'),
	firstName VARCHAR(50) NOT NULL,
	lastName VARCHAR(50) NOT NULL,
	username VARCHAR(50) NOT NULL CONSTRAINT valid_username_contraint check(username RLIKE'^[[:alnum:]_]+$'),
	email VARCHAR(320) NOT NULL, -- have the backend check RFC 5322 compliance, too complicated for SQL
	discordUName VARCHAR(50) CONSTRAINT valid_discarduname_contraint check(discordUName RLIKE'^.+#[[:digit:]]{4}$'),
	phoneNumber	VARCHAR(12) CONSTRAINT valid_phonenumber_contraint check(phoneNumber RLIKE'^[[:digit:]]{3}-[[:digit:]]{3}-[[:digit:]]{4}$'),
	dateOfBirth	date NOT NULL,
	address	VARCHAR(50) NOT NULL,
	saltedPassword VARCHAR(128) NOT NULL CONSTRAINT valid_saltedpwd_contraint check(saltedPassword RLIKE'^[[:xdigit:]]{128}$'),
	salt VARCHAR(128) NOT NULL CONSTRAINT valid_salt_contraint check(salt RLIKE'^[[:xdigit:]]{128}$')
);


CREATE TABLE studygroup
(
	studyGroupID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	prefMethodOfComm VARCHAR(50) NOT NULL,
	groupNickname VARCHAR(50) NOT NULL
);


CREATE TABLE meeting
(
	MeetingID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	startTime DATETIME NOT NULL, 
	endTime DATETIME NOT NULL
);


CREATE TABLE course
(
	deptAbbrev VARCHAR(4) NOT NULL,
	courseNum INT NOT NULL CHECK (courseNum > 0),
	courseName VARCHAR(50) NOT NULL,
	primary key (deptAbbrev, courseNum)
);


CREATE TABLE section
(
	deptAbbrev VARCHAR(4), 
	courseNum INT, 
	sectionNum INT NOT NULL check(sectionNum > 0), 
	meetingAddress VARCHAR(50) NOT NULL,
    
    FOREIGN KEY (deptAbbrev, courseNum)
        REFERENCES course(deptAbbrev, courseNum)
        ON DELETE CASCADE ON UPDATE CASCADE,
	
    PRIMARY KEY(courseNum, deptAbbrev, sectionNum)
);


CREATE TABLE onlinemeeting
(
	MeetingID INT,
    meetingURL VARCHAR(2040) NOT NULL,
    
    FOREIGN KEY (MeetingID)
        REFERENCES meeting(MeetingID)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE inpersonmeeting
(
	MeetingID INT,
    meetingLocationAddress VARCHAR(50) NOT NULL,
    
    FOREIGN KEY (MeetingID)
        REFERENCES meeting(MeetingID)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE studytools
(
	meetingLocationAddress VARCHAR(50) NOT NULL,
    studyTool VARCHAR(50) NOT NULL,
    PRIMARY KEY(meetingLocationAddress, studyTool)
);


CREATE TABLE takes 
(
	VNumber	VARCHAR(9),
	deptAbbrev VARCHAR(4),
    courseNum INT,
    sectionNum INT,
    
    FOREIGN KEY (VNumber)
        REFERENCES student(VNumber)
        ON DELETE CASCADE ON UPDATE CASCADE,
        
	FOREIGN KEY (deptAbbrev, courseNum, sectionNum)
        REFERENCES section(deptAbbrev, courseNum, sectionNum)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    PRIMARY KEY(VNumber, courseNum, deptAbbrev, sectionNum)
);


CREATE TABLE groupmembership
(
	VNumber VARCHAR(9),
	studyGroupID INT,
    
    FOREIGN KEY (VNumber)
        REFERENCES student(VNumber)
        ON DELETE CASCADE ON UPDATE CASCADE,
        
	FOREIGN KEY (studyGroupID)
        REFERENCES studygroup(studyGroupID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    PRIMARY KEY(VNumber, studyGroupID)
);


CREATE TABLE wantstoworkon
(
	VNumber VARCHAR(9),
    AssignmentID INT,
    
    FOREIGN KEY (VNumber)
        REFERENCES student(VNumber)
        ON DELETE CASCADE ON UPDATE CASCADE,
        
	FOREIGN KEY (AssignmentID)
        REFERENCES assignment(AssignmentID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    PRIMARY KEY(VNumber, AssignmentID)
);



CREATE TABLE assigns
(
	courseNum INT,
	deptAbbrev VARCHAR(4),
	sectionNum INT,
	AssignmentID INT,
        
	FOREIGN KEY (deptAbbrev, courseNum, sectionNum)
        REFERENCES section(deptAbbrev, courseNum, sectionNum)
        ON DELETE CASCADE ON UPDATE CASCADE,
        
	FOREIGN KEY (AssignmentID)
        REFERENCES assignment(AssignmentID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    PRIMARY KEY(courseNum, deptAbbrev, sectionNum, AssignmentID)
);


CREATE TABLE workson 
(
	MeetingID INT,
    AssignmentID INT,
    
    FOREIGN KEY (MeetingID)
        REFERENCES meeting(MeetingID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    FOREIGN KEY (AssignmentID)
        REFERENCES assignment(AssignmentID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    PRIMARY KEY(MeetingID, AssignmentID)
);


CREATE TABLE meets
(
	MeetingID INT,
    studyGroupID INT,
    
    FOREIGN KEY (MeetingID)
        REFERENCES meeting(MeetingID)
        ON DELETE CASCADE ON UPDATE CASCADE,
        
	FOREIGN KEY (studyGroupID)
        REFERENCES studygroup(studyGroupID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
	PRIMARY KEY(MeetingID, studyGroupID)
);

CREATE TABLE pendingStudyGroupInvites
(
	SenderVNumber	VARCHAR(9),
    ReceiverVNumber	VARCHAR(9),
    studyGroupID INT, 
        
	FOREIGN KEY (ReceiverVNumber)
        REFERENCES student(VNumber)
        ON DELETE CASCADE ON UPDATE CASCADE,
        
	FOREIGN KEY (SenderVNumber, studyGroupID)
        REFERENCES groupmembership(VNumber, studyGroupID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    -- CONSTRAINT cantInviteSelfContraint check(SenderVNumber != ReceiverVNumber),
    PRIMARY KEY(SenderVNumber, ReceiverVNumber, studyGroupID)
);


CREATE TABLE sectionmeetingtime
(
	deptAbbrev VARCHAR(4),
    courseNum INT,
    sectionNum INT,
    weekday ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'),
    startTime TIME NOT NULL,
    endTime TIME NOT NULL,
    
    FOREIGN KEY (deptAbbrev, courseNum, sectionNum)
        REFERENCES section(deptAbbrev, courseNum, sectionNum)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    CONSTRAINT start_before_end_constraint check(startTime < endTime),
    PRIMARY KEY(courseNum, deptAbbrev, sectionNum, weekday, startTime, endTime)
);


delimiter //
CREATE TRIGGER cantInviteSelfInsertTrigger 
BEFORE INSERT ON pendingStudyGroupInvites
FOR EACH ROW
BEGIN
	IF NEW.SenderVNumber = NEW.ReceiverVNumber then
		set NEW.SenderVNumber = NULL;
        set NEW.ReceiverVNumber = NULL;
        -- hopefully this should cause an error and prevent it from being inserted
    END IF;
END //


CALL populate_student_procedure();
CALL populate_assignment_procedure();
CALL populate_studytools_procedure();
CALL populate_course_procedure();
CALL populate_section_procedure();
CALL populate_studygroup_procedure();
CALL populate_meeting_procedure();
CALL populate_onlinemeeting_procedure();
CALL populate_inpersonmeeting_procedure();

CALL populate_meets_procedure();
CALL populate_sectionmeetingtime_procedure();
CALL populate_takes_procedure();
CALL populate_wantstoworkon_procedure();
CALL populate_workson_procedure();
CALL populate_groupmembership_procedure();
CALL populate_assigns_procedure();




SELECT TABLE_NAME, TABLE_ROWS 
	FROM information_schema.tables 
    WHERE table_schema = DATABASE()
    ORDER BY TABLE_ROWS;


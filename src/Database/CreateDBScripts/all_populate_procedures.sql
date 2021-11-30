DROP PROCEDURE IF EXISTS populate_assignment_procedure;
delimiter //
CREATE PROCEDURE populate_assignment_procedure()
BEGIN
	INSERT INTO assignment VALUES (1, 'Assignment #1', 'This is a sample assignment description', 60, '2021-11-27');
	INSERT INTO assignment VALUES (2, 'Assignment #2', 'This is a sample assignment description', 30, '2021-12-06');
	INSERT INTO assignment VALUES (3, 'Assignment #3', 'This is a sample assignment description', 60, '2021-11-25');
	INSERT INTO assignment VALUES (4, 'Assignment #4', 'This is a sample assignment description', 40, '2021-12-07');
	INSERT INTO assignment VALUES (5, 'Assignment #5', 'This is a sample assignment description', 30, '2021-12-03');
	INSERT INTO assignment VALUES (6, 'Assignment #6', 'This is a sample assignment description', 70, '2021-12-14');
	INSERT INTO assignment VALUES (7, 'Assignment #7', 'This is a sample assignment description', 80, '2021-11-30');
	INSERT INTO assignment VALUES (8, 'Assignment #8', 'This is a sample assignment description', 30, '2021-11-26');
	INSERT INTO assignment VALUES (9, 'Assignment #9', 'This is a sample assignment description', 60, '2021-11-22');
	INSERT INTO assignment VALUES (10, 'Assignment #10', 'This is a sample assignment description', 50, '2021-11-28');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_assigns_procedure;
delimiter //
CREATE PROCEDURE populate_assigns_procedure()
BEGIN
	INSERT INTO assigns VALUES (798, 'OCCT', 730, 6);
	INSERT INTO assigns VALUES (798, 'OCCT', 730, 2);
	INSERT INTO assigns VALUES (798, 'OCCT', 730, 4);
	INSERT INTO assigns VALUES (434, 'FREN', 660, 6);
	INSERT INTO assigns VALUES (434, 'FREN', 660, 9);
	INSERT INTO assigns VALUES (434, 'FREN', 660, 1);
	INSERT INTO assigns VALUES (434, 'FREN', 660, 7);
	INSERT INTO assigns VALUES (493, 'HPEX', 925, 1);
	INSERT INTO assigns VALUES (493, 'HPEX', 925, 7);
	INSERT INTO assigns VALUES (493, 'HPEX', 925, 6);
	INSERT INTO assigns VALUES (493, 'HPEX', 925, 8);
	INSERT INTO assigns VALUES (212, 'PAPR', 470, 6);
	INSERT INTO assigns VALUES (212, 'PAPR', 470, 5);
	INSERT INTO assigns VALUES (199, 'APPM', 656, 2);
	INSERT INTO assigns VALUES (199, 'APPM', 656, 3);
	INSERT INTO assigns VALUES (199, 'APPM', 656, 5);
	INSERT INTO assigns VALUES (675, 'SCMA', 446, 9);
	INSERT INTO assigns VALUES (726, 'SLWK', 382, 8);
	INSERT INTO assigns VALUES (726, 'SLWK', 382, 7);
	INSERT INTO assigns VALUES (301, 'PHTO', 893, 7);
	INSERT INTO assigns VALUES (660, 'PSYC', 551, 4);
	INSERT INTO assigns VALUES (660, 'PSYC', 551, 8);
	INSERT INTO assigns VALUES (421, 'EGMN', 183, 9);
	INSERT INTO assigns VALUES (421, 'EGMN', 183, 3);
	INSERT INTO assigns VALUES (421, 'EGMN', 183, 6);
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_groupmembership_procedure;
delimiter //
CREATE PROCEDURE populate_groupmembership_procedure()
BEGIN
	INSERT INTO groupmembership VALUES ('V21730086', 1);
	INSERT INTO groupmembership VALUES ('V86848339', 1);
	INSERT INTO groupmembership VALUES ('V65934232', 1);
	INSERT INTO groupmembership VALUES ('V94775159', 1);
	INSERT INTO groupmembership VALUES ('V98910139', 2);
	INSERT INTO groupmembership VALUES ('V21730086', 2);
	INSERT INTO groupmembership VALUES ('V16151090', 2);
	INSERT INTO groupmembership VALUES ('V94775159', 3);
	INSERT INTO groupmembership VALUES ('V16151090', 3);
	INSERT INTO groupmembership VALUES ('V79533041', 3);
	INSERT INTO groupmembership VALUES ('V86848339', 3);
	INSERT INTO groupmembership VALUES ('V21730086', 3);
	INSERT INTO groupmembership VALUES ('V86848339', 4);
	INSERT INTO groupmembership VALUES ('V16151090', 4);
	INSERT INTO groupmembership VALUES ('V83989471', 4);
	INSERT INTO groupmembership VALUES ('V52560123', 4);
	INSERT INTO groupmembership VALUES ('V94711220', 4);
	INSERT INTO groupmembership VALUES ('V98910139', 5);
	INSERT INTO groupmembership VALUES ('V79533041', 5);
	INSERT INTO groupmembership VALUES ('V86848339', 5);
	INSERT INTO groupmembership VALUES ('V94775159', 5);
	INSERT INTO groupmembership VALUES ('V94775159', 6);
	INSERT INTO groupmembership VALUES ('V52560123', 6);
	INSERT INTO groupmembership VALUES ('V79533041', 6);
	INSERT INTO groupmembership VALUES ('V21730086', 6);
	INSERT INTO groupmembership VALUES ('V65934232', 6);
	INSERT INTO groupmembership VALUES ('V79533041', 7);
	INSERT INTO groupmembership VALUES ('V16151090', 7);
	INSERT INTO groupmembership VALUES ('V52560123', 7);
	INSERT INTO groupmembership VALUES ('V94711220', 8);
	INSERT INTO groupmembership VALUES ('V79533041', 8);
	INSERT INTO groupmembership VALUES ('V94775159', 8);
	INSERT INTO groupmembership VALUES ('V83989471', 8);
	INSERT INTO groupmembership VALUES ('V79533041', 9);
	INSERT INTO groupmembership VALUES ('V94711220', 9);
	INSERT INTO groupmembership VALUES ('V65934232', 9);
	INSERT INTO groupmembership VALUES ('V21730086', 9);
	INSERT INTO groupmembership VALUES ('V86848339', 9);
	INSERT INTO groupmembership VALUES ('V98910139', 10);
	INSERT INTO groupmembership VALUES ('V94711220', 10);
	INSERT INTO groupmembership VALUES ('V83989471', 10);
	INSERT INTO groupmembership VALUES ('V52560123', 10);
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_course_procedure;
delimiter //
CREATE PROCEDURE populate_course_procedure()
BEGIN
	INSERT INTO course VALUES ('OCCT', 798, 'Thesis');
	INSERT INTO course VALUES ('FREN', 434, 'The 19th Century');
	INSERT INTO course VALUES ('HPEX', 493, 'Field Experience III');
	INSERT INTO course VALUES ('PAPR', 212, 'Print Techniques: Etching');
	INSERT INTO course VALUES ('APPM', 199, 'Recital/Convocation Attendance');
	INSERT INTO course VALUES ('SCMA', 675, 'Operations Management');
	INSERT INTO course VALUES ('SLWK', 726, 'Social Work Practice and Health Care');
	INSERT INTO course VALUES ('PHTO', 301, 'Junior Seminar');
	INSERT INTO course VALUES ('PSYC', 660, 'Health Psychology');
	INSERT INTO course VALUES ('EGMN', 421, 'CAE Analysis');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_studytools_procedure;
delimiter //
CREATE PROCEDURE populate_studytools_procedure()
BEGIN
	INSERT INTO studytools VALUES ('1015 Grove Ave., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('1015 Grove Ave., Richmond, VA 23220', 'Coffee');
	INSERT INTO studytools VALUES ('1015 Grove Ave., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('1015 Grove Ave., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('609 Bowe St., Richmond, VA 23220', 'Printer');
	INSERT INTO studytools VALUES ('609 Bowe St., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('1315 Floyd Ave., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('1315 Floyd Ave., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('1315 Floyd Ave., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('10 N. Brunswick St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('10 N. Brunswick St., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('10 N. Brunswick St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('10 N. Brunswick St., Richmond, VA 23220', '3D Printer');
	INSERT INTO studytools VALUES ('1000 W. Broad St., Richmond, VA 23220', 'Printer');
	INSERT INTO studytools VALUES ('801 W. Marshall St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('801 W. Marshall St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('801 W. Marshall St., Richmond, VA 23220', '3D Printer');
	INSERT INTO studytools VALUES ('814 W. Broad St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('814 W. Broad St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('814 W. Broad St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('814 W. Broad St., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('812-814 W. Franklin St., Richmond, VA 23220', 'Printer');
	INSERT INTO studytools VALUES ('812-814 W. Franklin St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('812-814 W. Franklin St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('812-814 W. Franklin St., Richmond, VA 23220', '3D Printer');
	INSERT INTO studytools VALUES ('419 W. Broad St, Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('419 W. Broad St, Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('325 N. Harrison St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('325 N. Harrison St., Richmond, VA 23220', 'Coffee');
	INSERT INTO studytools VALUES ('325 N. Harrison St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('922 Park Ave., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('301 W. Main St., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('301 W. Main St., Richmond, VA 23220', 'Coffee');
	INSERT INTO studytools VALUES ('301 W. Main St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('301 W. Main St., Richmond, VA 23220', '3D Printer');
	INSERT INTO studytools VALUES ('101 N. Harrison St., Richmond, VA 23220', 'Printer');
	INSERT INTO studytools VALUES ('101 N. Harrison St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('101 N. Harrison St., Richmond, VA 23220', 'Coffee');
	INSERT INTO studytools VALUES ('1015 W. Main St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('401 W. Main St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('401 W. Main St., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('401 W. Main St., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('401 W. Main St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('601 W. Main St., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('601 W. Main St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('601 W. Main St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('1015 Floyd Ave., Richmond, VA 23220', '3D Printer');
	INSERT INTO studytools VALUES ('1015 Floyd Ave., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('1015 Floyd Ave., Richmond, VA 23220', 'Coffee');
	INSERT INTO studytools VALUES ('1015 Floyd Ave., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('1015 Floyd Ave., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('900 Park Ave., Richmond, VA 23220', '3D Printer');
	INSERT INTO studytools VALUES ('900 Park Ave., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('900 Park Ave., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('900 Park Ave., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('701 W. Grace St., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('701 W. Grace St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('701 W. Grace St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('701 W. Grace St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('103 S. Jefferson St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('1001 W. Main St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('1001 W. Main St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('901 W. Main St., Richmond, VA 23220', 'Quiet Room');
	INSERT INTO studytools VALUES ('901 W. Main St., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('901 W. Main St., Richmond, VA 23220', 'Copier');
	INSERT INTO studytools VALUES ('901 W. Main St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('1000 W. Cary St., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('1000 W. Cary St., Richmond, VA 23220', 'Coffee');
	INSERT INTO studytools VALUES ('1000 W. Cary St., Richmond, VA 23220', 'Printer');
	INSERT INTO studytools VALUES ('1000 W. Cary St., Richmond, VA 23220', 'White Board');
	INSERT INTO studytools VALUES ('1000 W. Cary St., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('103 S. Jefferson St., Richmond, VA 23220', 'Computer');
	INSERT INTO studytools VALUES ('901 W. Main St., Richmond, VA 23220', 'Printer');
	INSERT INTO studytools VALUES ('901 W. Main St., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('1000 Floyd Ave., Richmond, VA 23220', 'Projector');
	INSERT INTO studytools VALUES ('1000 Floyd Ave., Richmond, VA 23220', '3D Printer');
	INSERT INTO studytools VALUES ('1000 Floyd Ave., Richmond, VA 23220', 'Coffee');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_inpersonmeeting_procedure;
delimiter //
CREATE PROCEDURE populate_inpersonmeeting_procedure()
BEGIN
	INSERT INTO inpersonmeeting VALUES (5, '901 W. Main St., Richmond, VA 23220');
	INSERT INTO inpersonmeeting VALUES (6, '419 W. Broad St, Richmond, VA 23220');
	INSERT INTO inpersonmeeting VALUES (7, '103 S. Jefferson St., Richmond, VA 23220');
	INSERT INTO inpersonmeeting VALUES (8, '325 N. Harrison St., Richmond, VA 23220');
	INSERT INTO inpersonmeeting VALUES (9, '1000 W. Cary St., Richmond, VA 23220');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_meeting_procedure;
delimiter //
CREATE PROCEDURE populate_meeting_procedure()
BEGIN
	INSERT INTO meeting VALUES (1, '2021-12-04 18:15', '2021-12-04 18:45');
	INSERT INTO meeting VALUES (2, '2021-12-05 14:30', '2021-12-05 15:30');
	INSERT INTO meeting VALUES (3, '2021-12-10 08:15', '2021-12-10 09:15');
	INSERT INTO meeting VALUES (4, '2021-11-23 11:45', '2021-11-23 13:45');
	INSERT INTO meeting VALUES (5, '2021-12-01 16:15', '2021-12-01 16:45');
	INSERT INTO meeting VALUES (6, '2021-12-09 15:15', '2021-12-09 17:15');
	INSERT INTO meeting VALUES (7, '2021-12-10 18:45', '2021-12-10 20:45');
	INSERT INTO meeting VALUES (8, '2021-12-11 13:45', '2021-12-11 15:45');
	INSERT INTO meeting VALUES (9, '2021-12-10 18:15', '2021-12-10 19:15');
	INSERT INTO meeting VALUES (10, '2021-11-20 13:30', '2021-11-20 15:00');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_meets_procedure;
delimiter //
CREATE PROCEDURE populate_meets_procedure()
BEGIN
	INSERT INTO meets VALUES (1, 4);
	INSERT INTO meets VALUES (2, 3);
	INSERT INTO meets VALUES (3, 10);
	INSERT INTO meets VALUES (4, 5);
	INSERT INTO meets VALUES (5, 4);
	INSERT INTO meets VALUES (6, 2);
	INSERT INTO meets VALUES (7, 7);
	INSERT INTO meets VALUES (8, 8);
	INSERT INTO meets VALUES (9, 6);
	INSERT INTO meets VALUES (10, 7);
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_onlinemeeting_procedure;
delimiter //
CREATE PROCEDURE populate_onlinemeeting_procedure()
BEGIN
	INSERT INTO onlinemeeting VALUES (1, 'https://zoom.us/j/8249269471');
	INSERT INTO onlinemeeting VALUES (2, 'https://zoom.us/j/8013204075');
	INSERT INTO onlinemeeting VALUES (3, 'https://zoom.us/j/2758688091');
	INSERT INTO onlinemeeting VALUES (4, 'https://zoom.us/j/6348967699');
	INSERT INTO onlinemeeting VALUES (5, 'https://zoom.us/j/0024894517');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_sectionmeetingtime_procedure;
delimiter //
CREATE PROCEDURE populate_sectionmeetingtime_procedure()
BEGIN
	INSERT INTO sectionmeetingtime VALUES ('OCCT', 798, 730, 'Monday', '8:00', '9:00');
	INSERT INTO sectionmeetingtime VALUES ('OCCT', 798, 730, 'Wednesday', '8:00', '9:00');
	INSERT INTO sectionmeetingtime VALUES ('OCCT', 798, 730, 'Thursday', '8:00', '9:00');
	INSERT INTO sectionmeetingtime VALUES ('FREN', 434, 660, 'Tuesday', '13:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('FREN', 434, 660, 'Friday', '13:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('FREN', 434, 660, 'Wednesday', '13:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('HPEX', 493, 925, 'Friday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('HPEX', 493, 925, 'Tuesday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('HPEX', 493, 925, 'Thursday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Tuesday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Monday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Friday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Thursday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Wednesday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('APPM', 199, 656, 'Wednesday', '16:00', '17:00');
	INSERT INTO sectionmeetingtime VALUES ('APPM', 199, 656, 'Thursday', '16:00', '17:00');
	INSERT INTO sectionmeetingtime VALUES ('APPM', 199, 656, 'Monday', '16:00', '17:00');
	INSERT INTO sectionmeetingtime VALUES ('SCMA', 675, 446, 'Thursday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('SCMA', 675, 446, 'Wednesday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('SCMA', 675, 446, 'Tuesday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('SLWK', 726, 382, 'Thursday', '12:00', '13:00');
	INSERT INTO sectionmeetingtime VALUES ('SLWK', 726, 382, 'Friday', '12:00', '13:00');
	INSERT INTO sectionmeetingtime VALUES ('PHTO', 301, 893, 'Tuesday', '18:00', '20:00');
	INSERT INTO sectionmeetingtime VALUES ('PHTO', 301, 893, 'Friday', '18:00', '20:00');
	INSERT INTO sectionmeetingtime VALUES ('PHTO', 301, 893, 'Wednesday', '18:00', '20:00');
	INSERT INTO sectionmeetingtime VALUES ('PSYC', 660, 551, 'Monday', '11:00', '12:00');
	INSERT INTO sectionmeetingtime VALUES ('PSYC', 660, 551, 'Friday', '11:00', '12:00');
	INSERT INTO sectionmeetingtime VALUES ('EGMN', 421, 183, 'Thursday', '14:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('EGMN', 421, 183, 'Monday', '14:00', '15:00');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_section_procedure;
delimiter //
CREATE PROCEDURE populate_section_procedure()
BEGIN
	INSERT INTO section VALUES ('OCCT', 798, 730, '814 W. Broad St., Richmond, VA 23220');
	INSERT INTO section VALUES ('FREN', 434, 660, '101 N. Harrison St., Richmond, VA 23220');
	INSERT INTO section VALUES ('HPEX', 493, 925, '1015 Floyd Ave., Richmond, VA 23220');
	INSERT INTO section VALUES ('PAPR', 212, 470, '325 N. Harrison St., Richmond, VA 23220');
	INSERT INTO section VALUES ('APPM', 199, 656, '1015 Grove Ave., Richmond, VA 23220');
	INSERT INTO section VALUES ('SCMA', 675, 446, '1000 W. Broad St., Richmond, VA 23220');
	INSERT INTO section VALUES ('SLWK', 726, 382, '901 W. Main St., Richmond, VA 23220');
	INSERT INTO section VALUES ('PHTO', 301, 893, '419 W. Broad St, Richmond, VA 23220');
	INSERT INTO section VALUES ('PSYC', 660, 551, '922 Park Ave., Richmond, VA 23220');
	INSERT INTO section VALUES ('EGMN', 421, 183, '701 W. Grace St., Richmond, VA 23220');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_student_procedure;
delimiter //
CREATE PROCEDURE populate_student_procedure()
BEGIN
	INSERT INTO student VALUES ('V94711220', 'Carry', 'Anliker', 'CAnl989', 'CarryA0@hotmail.com', 'CarryA5#2337', '660-555-4876', '2003-10-17', '720 W Franklin St, Richmond, VA 23220', 'b514b504618abd419b2a442d5e78c744dbe59a8df69cfacfb0cf98bd2e5438d9d2ead998e247480f8a729e0f9e37a3f3155f66c65485ebe19d0766cb98672e64', '8c166cd28025d12076d74fd44549e507b8ed83d5df2dd393037186d3940fd4115ebf932f7e6302be8f6af881c2ee3372cf1a926d5e6e892d21ebea99d6a50738');
	INSERT INTO student VALUES ('V83989471', 'Heath', 'Pesner', 'HPes865', 'HeathP4@gmail.com', 'HeathP6#9606', '475-555-9382', '2000-08-03', '1100 W. Broad St, Richmond, VA 23220', '78e40f0c6a1319a485cfce6e3bbad0eb1171a2b5703c59c46fbc389bb2951aa7e71775c1b1fa945f2841ccf21bc4b2c64d6b2e59a30fefea08dd8123d2c0bd89', '10c03e560e4ba8f6509d14feb5b34bda958ba0636d2829b92b9392aecf00d788b4c00c73d9bd386ebbba3a6c48a834be4d61862369086fdae4b95f5a91f28950');
	INSERT INTO student VALUES ('V86848339', 'Betsy', 'Helmick', 'BHelm542', 'BetsyH3@aol.com', 'BetsyH9#6027', '421-555-9489', '2000-06-18', '711 W. Main St, Richmond, Va 23220', 'fd47b3fde4998cac8ad0208ff64014ea1d7712abdc379f8c2541df8fa959af4d5cfb43d36940baf0dd8e52121459241b70801bab49c39052c94e3450bd92bce9', '110a28333d3c5ce041c80e362f9c6c4dcff9f558e46af3abe2bc1597c8319451d88265fa77d29fcb4e78c2cb764d8c04ef394fcf92a97461448865803557e2b3');
	INSERT INTO student VALUES ('V65934232', 'Fifine', 'Siami', 'FiSia611', 'FifineS5@hotmail.com', 'FifineS1#4278', '241-555-1578', '2002-10-03', '301 W. Cary St, Richmond, VA 23220', 'bf07176e8f036f1ee5e8f09fbde985970f18da1fb518a5e808ecb6e55327042b1e61cda7d927a1f39ba848e4100a39f60a9c5248d4c2a00e7c5b0de82b1ed123', '349b1c66b2e0f57eaf981a35899c520a38848ce39a5485540864873ff8f28084c34ccdc23bb2d15f905da986f7a04d9370982cf6a95cbec7efa477d535cbea26');
	INSERT INTO student VALUES ('V94775159', 'Beverlie', 'Lundell', 'BeLun13', 'BeverlieL4@yahoo.com', 'BeverlieL7#8900', '156-555-5938', '1999-12-01', '830 W. Grace St, Richmond, VA 23220', 'f8b5b588be6259848ab6ffc5217b1e671fb777da19da23d6f26cb0b581ce79030f7b70fac6365d5545e36050a26a7a3c1fb01fe23aeac602ad332452a432a343', '1e194f354ffc323ad59ddfcc71e1695f504af2e9750345cd3b09098f87f950ba9198669b46795b215cd4ac2e3106efec002dcd0d9568d494b46d336d993e9477');
	INSERT INTO student VALUES ('V52560123', 'Jodee', 'Houy', 'JoHouy921', 'JodeeH9@hotmail.com', 'JodeeH7#5470', '778-555-4080', '1999-06-16', '732 W. Broad St, Richmond, VA 23220', '84de9bf72edccd07a616b41385ceaad9c1ecab4e4c51062bda7cfb518c5bfa627830d0667db3b2be1f6268cb35ac71754b0db0d1f7436b88b59d76010189d3c4', '2fdb9e5bdcd137fa1c09a2553282bff999706f12d6a83f10e7e906cd1a94611bfc252206dff9307ad88af382522153f1fa8e3ee0bf1a5cffd52c988a819c207f');
	INSERT INTO student VALUES ('V98910139', 'Latisha', 'Rhoda', 'LaRhod397', 'LatishaR2@yahoo.com', 'LatishaR6#3812', '160-555-9753', '2001-07-24', '835 W. Grace St, Richmond, VA 23220', 'e8465fb49ee47d1ca6920832b72f51c93bc6e80698e0f61870dbe257e029cdd657304f2a5af41145cc7ac3c442484e1239803e158586744ac4d019554c4b3675', '6d57525995bae5b845257cb21c68fd5d5773fd4614860951124d179c52efed9a938a91e9ee8262fd17989cc8ea45d478f792bfdb5b37a7efd0ee656eb9b9bb0e');
	INSERT INTO student VALUES ('V79533041', 'Mirabella', 'Carlyon', 'MiCar574', 'MirabellaC6@aol.com', 'MirabellaC0#6650', '513-555-9332', '2003-09-06', '710 W. Franklin St, Richmond, VA 23220', '5702b59c3d70645065a25f7467d41c8246007e24bc9e42741e2fba4e8c7086a4c28d820e7eb2425bb2d7fb2b24c66d32a84e6842b53831432a5c77fcdec43a5f', 'ee453a6101bd3fa926598aaff491406a191da8733c0f180fe0e1e013649a20da6f7f1b3846a15f05cc4c76fd0998d29d8fe0c9a6770ddf84bd158d07a2fec576');
	INSERT INTO student VALUES ('V21730086', 'Dulce', 'Hoque', 'DHoqu759', 'DulceH1@vcu.edu', 'DulceH3#0089', '871-555-1587', '2001-02-12', '801 W. Franklin St, Richmond, VA 23220', '84c649bbcf8b917513d4900b825bf59b0066e9f02a7fdc5c007c7e15561bf80c2a83276c83b99790f8930bfd38c617eec36e40ed997e6980e1a86fc27713869e', 'bbd746b9fca35f62af4e488366f9d6d6bd2d226225a522cb0d778a51bc32a72bfd33888b8608350786f1ee86062113ab9799cdb99f4223d36e6ea867182a35e9');
	INSERT INTO student VALUES ('V16151090', 'Becka', 'Nefzger', 'BNefz756', 'BeckaN9@gmail.com', 'BeckaN1#3193', '148-555-4185', '2002-05-31', '1000 W. Grace St, Richmond, VA 23220', '6a59fdc60bfe1b74381f79ee9e30dd822b15efb6ef46b20e822376c8c744a1171963a23ef1c1f11c9b89d65b68eaccb85abae16993896825b4de319f4172f82b', '9feefa5c464488d77f97c28d4d9e3d0847e4d2fe022a0215e768af59f48d16a0673317b64b49d1c16899e9937f2a37ec720f8ceda8f1eb63ce8b5cdf3fc2f631');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_studygroup_procedure;
delimiter //
CREATE PROCEDURE populate_studygroup_procedure()
BEGIN
	INSERT INTO studygroup VALUES (1, 'Telegraph', 'Jackrabbits');
	INSERT INTO studygroup VALUES (2, 'Yelling Really Loudly', 'Yankees');
	INSERT INTO studygroup VALUES (3, 'Zoom', 'Executioners');
	INSERT INTO studygroup VALUES (4, 'HAM Radio', 'Rock Stars');
	INSERT INTO studygroup VALUES (5, 'USPS', 'Foundation');
	INSERT INTO studygroup VALUES (6, 'Phone Call', 'Panthers');
	INSERT INTO studygroup VALUES (7, 'Clay Tablet', 'Connected');
	INSERT INTO studygroup VALUES (8, 'Email', 'Blue Jackets');
	INSERT INTO studygroup VALUES (9, 'Slack', 'Bad Boys');
	INSERT INTO studygroup VALUES (10, 'Discord', 'Tidal Waves');
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_takes_procedure;
delimiter //
CREATE PROCEDURE populate_takes_procedure()
BEGIN
	INSERT INTO takes VALUES ('V94711220', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V94711220', 'PHTO', 301, 893);
	INSERT INTO takes VALUES ('V94711220', 'PAPR', 212, 470);
	INSERT INTO takes VALUES ('V94711220', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V94711220', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V83989471', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V83989471', 'PAPR', 212, 470);
	INSERT INTO takes VALUES ('V83989471', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V83989471', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V83989471', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V86848339', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V86848339', 'PHTO', 301, 893);
	INSERT INTO takes VALUES ('V86848339', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V65934232', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V65934232', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V65934232', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V65934232', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V94775159', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V94775159', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V52560123', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V52560123', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V52560123', 'EGMN', 421, 183);
	INSERT INTO takes VALUES ('V52560123', 'PHTO', 301, 893);
	INSERT INTO takes VALUES ('V98910139', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V98910139', 'SCMA', 675, 446);
	INSERT INTO takes VALUES ('V79533041', 'EGMN', 421, 183);
	INSERT INTO takes VALUES ('V79533041', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V79533041', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V21730086', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V21730086', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V21730086', 'SCMA', 675, 446);
	INSERT INTO takes VALUES ('V21730086', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V16151090', 'HPEX', 493, 925);
	INSERT INTO takes VALUES ('V16151090', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V16151090', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V16151090', 'APPM', 199, 656);
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_wantstoworkon_procedure;
delimiter //
CREATE PROCEDURE populate_wantstoworkon_procedure()
BEGIN
	INSERT INTO wantstoworkon VALUES ('V94711220', 6);
	INSERT INTO wantstoworkon VALUES ('V94711220', 8);
	INSERT INTO wantstoworkon VALUES ('V94711220', 5);
	INSERT INTO wantstoworkon VALUES ('V83989471', 9);
	INSERT INTO wantstoworkon VALUES ('V83989471', 6);
	INSERT INTO wantstoworkon VALUES ('V83989471', 3);
	INSERT INTO wantstoworkon VALUES ('V86848339', 2);
	INSERT INTO wantstoworkon VALUES ('V86848339', 9);
	INSERT INTO wantstoworkon VALUES ('V86848339', 10);
	INSERT INTO wantstoworkon VALUES ('V65934232', 3);
	INSERT INTO wantstoworkon VALUES ('V65934232', 7);
	INSERT INTO wantstoworkon VALUES ('V94775159', 4);
	INSERT INTO wantstoworkon VALUES ('V94775159', 6);
	INSERT INTO wantstoworkon VALUES ('V52560123', 4);
	INSERT INTO wantstoworkon VALUES ('V52560123', 3);
	INSERT INTO wantstoworkon VALUES ('V52560123', 5);
	INSERT INTO wantstoworkon VALUES ('V98910139', 7);
	INSERT INTO wantstoworkon VALUES ('V98910139', 1);
	INSERT INTO wantstoworkon VALUES ('V98910139', 3);
	INSERT INTO wantstoworkon VALUES ('V79533041', 1);
	INSERT INTO wantstoworkon VALUES ('V79533041', 7);
	INSERT INTO wantstoworkon VALUES ('V79533041', 2);
	INSERT INTO wantstoworkon VALUES ('V21730086', 7);
	INSERT INTO wantstoworkon VALUES ('V21730086', 5);
	INSERT INTO wantstoworkon VALUES ('V16151090', 7);
	INSERT INTO wantstoworkon VALUES ('V16151090', 3);
	INSERT INTO wantstoworkon VALUES ('V16151090', 10);
END //
delimiter ;


DROP PROCEDURE IF EXISTS populate_workson_procedure;
delimiter //
CREATE PROCEDURE populate_workson_procedure()
BEGIN
	INSERT INTO workson VALUES (1, 2);
	INSERT INTO workson VALUES (2, 7);
	INSERT INTO workson VALUES (3, 1);
	INSERT INTO workson VALUES (4, 6);
	INSERT INTO workson VALUES (5, 1);
	INSERT INTO workson VALUES (6, 2);
	INSERT INTO workson VALUES (7, 10);
	INSERT INTO workson VALUES (8, 1);
	INSERT INTO workson VALUES (9, 5);
	INSERT INTO workson VALUES (10, 5);
END //
delimiter ;



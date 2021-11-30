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

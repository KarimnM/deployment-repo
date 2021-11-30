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

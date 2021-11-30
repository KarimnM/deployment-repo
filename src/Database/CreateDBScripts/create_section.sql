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

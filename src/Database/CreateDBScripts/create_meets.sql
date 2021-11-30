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

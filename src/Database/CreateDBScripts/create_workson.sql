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

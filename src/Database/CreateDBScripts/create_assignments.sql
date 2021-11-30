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

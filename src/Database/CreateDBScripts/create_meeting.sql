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

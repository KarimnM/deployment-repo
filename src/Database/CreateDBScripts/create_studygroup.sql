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

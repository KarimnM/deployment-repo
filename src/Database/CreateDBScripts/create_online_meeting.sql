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

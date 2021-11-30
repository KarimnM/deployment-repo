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

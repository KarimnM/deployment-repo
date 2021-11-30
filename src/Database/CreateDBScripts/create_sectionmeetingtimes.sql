DROP PROCEDURE IF EXISTS populate_sectionmeetingtime_procedure;
delimiter //
CREATE PROCEDURE populate_sectionmeetingtime_procedure()
BEGIN
	INSERT INTO sectionmeetingtime VALUES ('OCCT', 798, 730, 'Monday', '8:00', '9:00');
	INSERT INTO sectionmeetingtime VALUES ('OCCT', 798, 730, 'Wednesday', '8:00', '9:00');
	INSERT INTO sectionmeetingtime VALUES ('OCCT', 798, 730, 'Thursday', '8:00', '9:00');
	INSERT INTO sectionmeetingtime VALUES ('FREN', 434, 660, 'Tuesday', '13:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('FREN', 434, 660, 'Friday', '13:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('FREN', 434, 660, 'Wednesday', '13:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('HPEX', 493, 925, 'Friday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('HPEX', 493, 925, 'Tuesday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('HPEX', 493, 925, 'Thursday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Tuesday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Monday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Friday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Thursday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('PAPR', 212, 470, 'Wednesday', '14:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('APPM', 199, 656, 'Wednesday', '16:00', '17:00');
	INSERT INTO sectionmeetingtime VALUES ('APPM', 199, 656, 'Thursday', '16:00', '17:00');
	INSERT INTO sectionmeetingtime VALUES ('APPM', 199, 656, 'Monday', '16:00', '17:00');
	INSERT INTO sectionmeetingtime VALUES ('SCMA', 675, 446, 'Thursday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('SCMA', 675, 446, 'Wednesday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('SCMA', 675, 446, 'Tuesday', '15:00', '16:00');
	INSERT INTO sectionmeetingtime VALUES ('SLWK', 726, 382, 'Thursday', '12:00', '13:00');
	INSERT INTO sectionmeetingtime VALUES ('SLWK', 726, 382, 'Friday', '12:00', '13:00');
	INSERT INTO sectionmeetingtime VALUES ('PHTO', 301, 893, 'Tuesday', '18:00', '20:00');
	INSERT INTO sectionmeetingtime VALUES ('PHTO', 301, 893, 'Friday', '18:00', '20:00');
	INSERT INTO sectionmeetingtime VALUES ('PHTO', 301, 893, 'Wednesday', '18:00', '20:00');
	INSERT INTO sectionmeetingtime VALUES ('PSYC', 660, 551, 'Monday', '11:00', '12:00');
	INSERT INTO sectionmeetingtime VALUES ('PSYC', 660, 551, 'Friday', '11:00', '12:00');
	INSERT INTO sectionmeetingtime VALUES ('EGMN', 421, 183, 'Thursday', '14:00', '15:00');
	INSERT INTO sectionmeetingtime VALUES ('EGMN', 421, 183, 'Monday', '14:00', '15:00');
END //
delimiter ;

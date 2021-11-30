DROP PROCEDURE IF EXISTS populate_takes_procedure;
delimiter //
CREATE PROCEDURE populate_takes_procedure()
BEGIN
	INSERT INTO takes VALUES ('V94711220', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V94711220', 'PHTO', 301, 893);
	INSERT INTO takes VALUES ('V94711220', 'PAPR', 212, 470);
	INSERT INTO takes VALUES ('V94711220', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V94711220', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V83989471', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V83989471', 'PAPR', 212, 470);
	INSERT INTO takes VALUES ('V83989471', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V83989471', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V83989471', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V86848339', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V86848339', 'PHTO', 301, 893);
	INSERT INTO takes VALUES ('V86848339', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V65934232', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V65934232', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V65934232', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V65934232', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V94775159', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V94775159', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V52560123', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V52560123', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V52560123', 'EGMN', 421, 183);
	INSERT INTO takes VALUES ('V52560123', 'PHTO', 301, 893);
	INSERT INTO takes VALUES ('V98910139', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V98910139', 'SCMA', 675, 446);
	INSERT INTO takes VALUES ('V79533041', 'EGMN', 421, 183);
	INSERT INTO takes VALUES ('V79533041', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V79533041', 'OCCT', 798, 730);
	INSERT INTO takes VALUES ('V21730086', 'APPM', 199, 656);
	INSERT INTO takes VALUES ('V21730086', 'PSYC', 660, 551);
	INSERT INTO takes VALUES ('V21730086', 'SCMA', 675, 446);
	INSERT INTO takes VALUES ('V21730086', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V16151090', 'HPEX', 493, 925);
	INSERT INTO takes VALUES ('V16151090', 'FREN', 434, 660);
	INSERT INTO takes VALUES ('V16151090', 'SLWK', 726, 382);
	INSERT INTO takes VALUES ('V16151090', 'APPM', 199, 656);
END //
delimiter ;

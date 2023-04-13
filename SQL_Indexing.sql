SELECT * FROM Github_DB.GITHUB;

-- quick look-ups of "login", "location", and "hireable". 
Use Github_DB;

CREATE INDEX idx_login ON GITHUB (login(50));
CREATE INDEX idx_location ON GITHUB (location(50));
CREATE INDEX idx_hireable ON GITHUB (hireable(50));

SELECT * FROM Github_DB.GITHUB WHERE location is not null;
SELECT * FROM GITHUB WHERE login is not null;
SELECT * FROM GITHUB WHERE hireable is not null;

DROP INDEX idx_login ON GITHUB;
DROP INDEX idx_location ON GITHUB;
DROP INDEX idx_hireable ON GITHUB;
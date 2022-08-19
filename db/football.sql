DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS trainings;
DROP TABLE IF EXISTS players_trainings;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    position VARCHAR(255),
    fatigue INT
);

CREATE TABLE trainings (
    id SERIAL PRIMARY KEY,
    time VARCHAR(255),
    duration INT
);

CREATE TABLE players_trainings (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    training_id INT NOT NULL REFERENCES trainings(id) ON DELETE CASCADE,
    comments TEXT
);
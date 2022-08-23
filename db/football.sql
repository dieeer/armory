DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS trainings;
DROP TABLE IF EXISTS players_trainings;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    shirt_no INT,
    position VARCHAR(255),
    fatigue INT
);

CREATE TABLE trainings (
    id SERIAL PRIMARY KEY,
    training_name VARCHAR(255),
    time VARCHAR(255),
    duration INT,
    intensity VARCHAR(255)
);

CREATE TABLE players_trainings (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    training_id INT NOT NULL REFERENCES trainings(id) ON DELETE CASCADE,
    comments TEXT
);

CREATE TABLE current_squad (
    id SERIAL PRIMARY KEY,
    gk_id INT REFERENCES players(id),
    lb_id INT REFERENCES players(id),
    cb1_id INT REFERENCES players(id),
    cb2_id INT REFERENCES players(id),
    rb_id INT REFERENCES players(id),
    lm_id INT REFERENCES players(id),
    cm1_id INT REFERENCES players(id),
    cm2_id INT REFERENCES players(id),
    rm_id INT REFERENCES players(id),
    cam_id INT REFERENCES players(id),
    st_id INT REFERENCES players(id),
    sub1_id INT REFERENCES players(id),
    sub2_id INT REFERENCES players(id),
    sub3_id INT REFERENCES players(id),
    sub4_id INT REFERENCES players(id),
    sub5_id INT REFERENCES players(id),
    sub6_id INT REFERENCES players(id)
);
use ipl_project;

CREATE TABLE matches (
    team1s1 VARCHAR(10),
    team2s2 VARCHAR(10),
    id INT PRIMARY KEY,
    season INT,
    city VARCHAR(50),
    date DATE,
    team1 VARCHAR(10),
    team2 VARCHAR(10),
    toss_winner VARCHAR(10),
    toss_decision VARCHAR(10),
    result VARCHAR(20),
    winner VARCHAR(10),
    win_by_runs INT,
    win_by_wickets INT,
    player_of_match VARCHAR(50),
    venue VARCHAR(100),
    umpire1 VARCHAR(50),
    umpire2 VARCHAR(50)
);

CREATE TABLE squads (
    sid INT,
    team VARCHAR(10),
    player VARCHAR(50),
    role VARCHAR(30),
    nationality VARCHAR(30),
    type_of_player VARCHAR(20),
    head_coach VARCHAR(50),
    bowling_coach VARCHAR(50),
    batting_coach VARCHAR(50),
    owner VARCHAR(100),
    home_ground VARCHAR(100)
);

CREATE TABLE deliveries (
    match_id INT NOT NULL,
    inning INT NOT NULL,
    batting_team VARCHAR(10) NOT NULL,
    bowling_team VARCHAR(10) NOT NULL,
    m_over INT NOT NULL,
    ball INT NOT NULL,
    batsman VARCHAR(50) NOT NULL,
    non_striker VARCHAR(50) NOT NULL,
    bowler VARCHAR(50) NOT NULL,
    is_super_over INT NOT NULL,
    wide_runs INT NOT NULL DEFAULT 0,
    legbye_runs INT NOT NULL DEFAULT 0,
    noball_runs INT NOT NULL DEFAULT 0,
    penalty_runs INT NOT NULL DEFAULT 0,
    batsman_runs INT NOT NULL DEFAULT 0,
    extra_runs INT NOT NULL DEFAULT 0,
    total_runs INT NOT NULL DEFAULT 0,
    player_dismissed VARCHAR(50),
    dismissal_kind VARCHAR(20),
    fielder VARCHAR(50),
    PRIMARY KEY (match_id, inning, m_over, ball)
);

select * from matches;
select * from deliveries;
select * from squads;



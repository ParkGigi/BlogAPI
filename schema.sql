CREATE TABLE IF NOT EXISTS Users (
       id         INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       username   blob NOT NULL,
       password   blob NOT NULL,
       nickname   blob NOT NULL,
       picture    blob,
       user_level blob NOT NULL,
       deleted    boolean DEFAULT False,
       created    timestamp DEFAULT CURRENT_TIMESTAMP,       
       updated    timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Posts (
       id         INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       author_id  INT NOT NULL, 
       title      blob NOT NULL,
       content    blob NOT NULL,
       deleted    boolean DEFAULT False,
       created    timestamp DEFAULT CURRENT_TIMESTAMP,       
       updated    timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
       FOREIGN KEY (author_id) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS Comments (
       id            INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       post_id       INT NOT NULL,
       commentor_id  INT NOT NULL,
       content       blob NOT NULL,
       deleted       boolean DEFAULT False,   
       created       timestamp DEFAULT CURRENT_TIMESTAMP,       
       updated       timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
       FOREIGN KEY (post_id) REFERENCES Posts(id),
       FOREIGN KEY (commentor_id) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS Sessions (
       id       INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       user_id  INT NOT NULL,
       created  timestamp DEFAULT CURRENT_TIMESTAMP,
       expires  timestamp DEFAULT CURRENT_TIMESTAMP,
       expired  boolean DEFAULT False,
       FOREIGN KEY (user_id) REFERENCES Users(id)
);

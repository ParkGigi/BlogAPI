CREATE TABLE User (
       id       INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       username blob NOT NULL,
       password blob NOT NULL,
       nickname blob NOT NULL,
       picture  blob,
       created  timestamp DEFAULT CURRENT_TIMESTAMP,       
       updated  timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Post (
       id         INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       author_id  INT NOT NULL, 
       title      blob NOT NULL,
       content    blob NOT NULL,
       created    timestamp DEFAULT CURRENT_TIMESTAMP,       
       updated    timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
       FOREIGN KEY (author_id) REFERENCES User(id)
);

CREATE TABLE Comment (
       id            INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       post_id       INT NOT NULL,
       commentor_id  INT NOT NULL,
       content       blob NOT NULL,
       created       timestamp DEFAULT CURRENT_TIMESTAMP,       
       updated       timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
       FOREIGN KEY (post_id) REFERENCES Post(id),
       FOREIGN KEY (commentor_id) REFERENCES User(id)
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id)
);


"""CREATE DATABASE college;
USE college;

CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year ENUM('1st', '2nd') NOT NULL,
    stream ENUM('Arts', 'Commerce', 'Science') NOT NULL,
    subject_name VARCHAR(255) NOT NULL
);

INSERT INTO subjects (year, stream, subject_name) VALUES
('1st', 'Arts', 'History'),
('1st', 'Arts', 'Political Science'),
('1st', 'Commerce', 'Accounting'),
('1st', 'Commerce', 'Business Studies'),
('1st', 'Science', 'Physics'),
('1st', 'Science', 'Chemistry'),
('2nd', 'Arts', 'Sociology'),
('2nd', 'Arts', 'Philosophy'),
('2nd', 'Commerce', 'Economics'),
('2nd', 'Commerce', 'Finance'),
('2nd', 'Science', 'Biology'),
('2nd', 'Science', 'Mathematics');

CREATE TABLE cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id)
);
"""
INSERT INTO tbl_users(id, name, roles) VALUES (10, 'Jan Nowak', 'user');
INSERT INTO tbl_users(id, name, roles) VALUES (20, 'Grażyna Kowalska', 'user,admin');
INSERT INTO tbl_users(id, name, roles) VALUES (30, 'Tomasz Wójcik', 'user');

INSERT INTO tbl_books(id, title, author, quantity) VALUES (1, 'Praktyczna inżynieria wsteczna. Metody, techniki i narzędzia', 'Gynvael Coldwind', 2);
INSERT INTO tbl_books(id, title, author, quantity) VALUES (2, 'Zrozumieć programowanie', 'Gynvael Coldwind', 3);
INSERT INTO tbl_books(id, title, author, quantity) VALUES (3, 'Python - Wprowadzenie', 'Mark Lutz', 4);
INSERT INTO tbl_books(id, title, author, quantity) VALUES (4, 'Python. Leksykon kieszonkowy', 'Mark Lutz', 5);
INSERT INTO tbl_books(id, title, author, quantity) VALUES (5, 'Python. Zadania z programowania. Przykładowe imperatywne rozwiązania', 'Mirosław J. Kubiak', 7);

INSERT INTO tbl_rentals(id, user_id, book_id, rental_date, return_date) VALUES (1001, 10, 5, '2021-10-01', '2021-10-14');
INSERT INTO tbl_rentals(id, user_id, book_id, rental_date, return_date) VALUES (1002, 10, 3, '2021-11-01', NULL);
INSERT INTO tbl_rentals(id, user_id, book_id, rental_date, return_date) VALUES (1003, 10, 1, '2021-10-15', NULL);
INSERT INTO tbl_rentals(id, user_id, book_id, rental_date, return_date) VALUES (1004, 20, 1, '2021-10-16', NULL);
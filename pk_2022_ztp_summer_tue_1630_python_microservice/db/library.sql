DROP TABLE IF EXISTS tbl_books;
DROP TABLE IF EXISTS tbl_rentals;

CREATE TABLE IF NOT EXISTS "tbl_books" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" VARCHAR(255) NOT NULL,
    "author" VARCHAR(255) NOT NULL,
    "quantity" INT NOT NULL
   );

CREATE TABLE IF NOT EXISTS "tbl_rentals" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" INT NOT NULL,
    "book_id" INT NOT NULL,
    "rental_date" DATE NOT NULL,
    "return_date" DATE
    );
    
INSERT INTO "tbl_books"("title", "author", "quantity") VALUES ('Praktyczna inżynieria wsteczna. Metody, techniki i narzędzia', 'Gynvael Coldwind', 2);
INSERT INTO "tbl_books"("title", "author", "quantity") VALUES ('Zrozumieć programowanie', 'Gynvael Coldwind', 2);
INSERT INTO "tbl_books"("title", "author", "quantity") VALUES ('Python - Wprowadzenie', 'Mark Lutz', 2);
INSERT INTO "tbl_books"("title", "author", "quantity") VALUES ('Python. Leksykon kieszonkowy', 'Mark Lutz', 2);
INSERT INTO "tbl_books"("title", "author", "quantity") VALUES ('Python. Zadania z programowania. Przykładowe imperatywne rozwiązania', 'Mirosław J. Kubiak', 2);



DROP TABLE IF EXISTS tbl_users;

CREATE TABLE IF NOT EXISTS "tbl_users" (
    "uuid" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" varchar(255) NOT NULL,
    "library" Boolean NOT NULL DEFAULT 0
    );
    
   
INSERT INTO "tbl_users"("username", "library") VALUES ('Anna Pietruszka',1);
INSERT INTO "tbl_users"("username", "library") VALUES ('Witold Baran',1);
INSERT INTO "tbl_users"("username", "library") VALUES ('Grzegorz Kamil',0);
INSERT INTO "tbl_users"("username", "library") VALUES ('Tomasz Seweryn',0);

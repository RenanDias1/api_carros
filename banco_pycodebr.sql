USE Pycodebr;

CREATE TABLE Carros(
	id integer not null auto_increment,
    marca varchar(100),
    modelo varchar(100),
    ano integer,
    Primary key (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO carros (marca, modelo, ano) values ('Fiat', 'Marea', 1999);
INSERT INTO carros (marca, modelo, ano) values ('Fiat', 'Uno', 1992);
INSERT INTO carros (marca, modelo, ano) values ('Ford', 'Escort', 1985);

SELECT * FROM CARROS
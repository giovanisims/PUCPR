DROP DATABASE LAB_05;
CREATE DATABASE LAB_05;
USE LAB_05;

-- 5.1

DROP FUNCTION IF EXISTS Diagonal;

DELIMITER $$
-- function: não usa IN / OUT nos parâmetros da função
CREATE FUNCTION Diagonal (ladoA FLOAT, ladoB FLOAT)
RETURNS FLOAT
DETERMINISTIC -- define que a função é determinística
BEGIN
DECLARE DIAG FLOAT DEFAULT -1;
SET DIAG = SQRT(POWER(ladoA, 2) + POWER(ladoB, 2));
RETURN DIAG;
END; $$
DELIMITER ;
SELECT Diagonal(3, 4) AS 'Diagonal do retângulo 3m x 4m';

DELIMITER $$

-- 5.2

CREATE FUNCTION CalcSalario (valor_inicial INT)
RETURNS INT
DETERMINISTIC
BEGIN
DECLARE salario INT DEFAULT 0;
WHILE salario <= 3000 DO
SET salario = salario + valor_inicial;
END WHILE;
RETURN salario;
END; $$
DELIMITER ;
SELECT CalcSalario(500) AS 'Salário Final';

-- 5.3

DROP TABLE IF EXISTS Tab_Teste;
CREATE TABLE Tab_Teste (
col1 INT NOT NULL PRIMARY KEY,
col2 INT NOT NULL);
SELECT * FROM Tab_Teste;

START TRANSACTION ;
INSERT Tab_Teste VALUES (1,111) ;
INSERT Tab_Teste VALUES (2,222) ;
COMMIT;
SELECT * FROM Tab_Teste;

START TRANSACTION ;
INSERT Tab_Teste VALUES (3,333) ;
INSERT Tab_Teste VALUES (4,444) ;
ROLLBACK;
SELECT * FROM Tab_Teste;

-- 5.4

DROP TABLE IF EXISTS Tab_Teste;
CREATE TABLE Tab_Teste (
col1 INT NOT NULL PRIMARY KEY,
col2 INT NOT NULL);
SELECT * FROM Tab_Teste;

DROP PROCEDURE IF EXISTS nãoTratErroTransact;
DELIMITER $$
CREATE PROCEDURE nãoTratErroTransact()
BEGIN
START TRANSACTION;
INSERT Tab_Teste VALUES (1,111) ;
INSERT Tab_Teste VALUES (2,222) ;
INSERT Tab_Teste VALUES (3,333) ;
INSERT Tab_Teste VALUES (1,101) ;
COMMIT; -- esse commando executa?
END $$
DELIMITER ;
CALL nãoTratErroTransact();
SELECT * FROM Tab_Teste;

-- 5.5

DROP TABLE IF EXISTS Tab_Teste;
CREATE TABLE Tab_Teste (
col1 INT NOT NULL PRIMARY KEY,
col2 INT NOT NULL);
SELECT * FROM Tab_Teste;

DROP PROCEDURE IF EXISTS tratErroTransact;
DELIMITER $$
CREATE PROCEDURE tratErroTransact()
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
ROLLBACK;
RESIGNAL;
END;
START TRANSACTION;
INSERT Tab_Teste VALUES (1,111) ;
INSERT Tab_Teste VALUES (2,222) ;
INSERT Tab_Teste VALUES (3,'um') ;
INSERT Tab_Teste VALUES (3,333) ;
COMMIT; -- esse commando executa?
END $$
DELIMITER ;
CALL tratErroTransact();
SELECT * FROM Tab_Teste;

-- 5.6 & 5.7

DROP TABLE IF EXISTS EstoqueProduto;
-- Cria Tabela EstoqueProduto
CREATE TABLE EstoqueProduto (
ID_Prod INT PRIMARY KEY,
Nome_Prod VARCHAR(20) NOT NULL UNIQUE,
Estoque INT NOT NULL
);
INSERT INTO EstoqueProduto (ID_Prod, Nome_prod, Estoque) VALUES (123, 'Caderno', 100);
INSERT INTO EstoqueProduto (ID_Prod, Nome_prod, Estoque) VALUES (456, 'Bloco A4', 50);
INSERT INTO EstoqueProduto (ID_Prod, Nome_prod, Estoque) VALUES (789, 'Caneta', 200);
SELECT * FROM EstoqueProduto;

DROP TABLE IF EXISTS ItensVenda;
-- Cria Tabela ItensVenda
CREATE TABLE ItensVenda (
ID_Venda INT AUTO_INCREMENT PRIMARY KEY,
fk_ID_Pedido INT, -- Tab Pedido não criada nesta demonstração
fk_ID_Prod INT NOT NULL REFERENCES EstoqueProduto(ID_Prod), -- FK
Quantidade INT NOT NULL,
UNIQUE (fk_ID_Pedido, fk_ID_Prod)
);
SELECT * FROM ItensVenda;

DROP TRIGGER IF EXISTS Tgr_ItensVenda_Insert;
-- Cria Trigger Tgr_ItensVenda_Insert
DELIMITER $$
CREATE TRIGGER Tgr_ItensVenda_Insert
AFTER INSERT -- A Trigger dispara após o INSERT
ON ItensVenda
FOR EACH ROW
BEGIN
UPDATE EstoqueProduto
SET Estoque = Estoque - NEW.Quantidade
WHERE ID_Prod = NEW.fk_ID_Prod;
END $$
DELIMITER ;

DROP TRIGGER IF EXISTS Tgr_ItensVenda_Delete;
-- Cria Trigger Tgr_ItensVenda_Insert
DELIMITER $$
CREATE TRIGGER Tgr_ItensVenda_Delete
AFTER DELETE -- A Trigger dispara após o DELETE
ON ItensVenda
FOR EACH ROW
BEGIN
UPDATE EstoqueProduto
SET Estoque = Estoque + OLD.Quantidade
WHERE ID_Prod = OLD.fk_ID_Prod;
END $$
DELIMITER ;

-- 5.8

INSERT INTO ItensVenda (fk_ID_Pedido, fk_ID_Prod, Quantidade) VALUES (1, 123, 30);
INSERT INTO ItensVenda (fk_ID_Pedido, fk_ID_Prod, Quantidade) VALUES (1, 456, 10);
INSERT INTO ItensVenda (fk_ID_Pedido, fk_ID_Prod, Quantidade) VALUES (1, 789, 25);
SELECT * FROM ItensVenda;
SELECT * FROM EstoqueProduto;

DELETE FROM ItensVenda WHERE fk_ID_Pedido = 1 AND fk_ID_Prod = 123;
DELETE FROM ItensVenda WHERE fk_ID_Pedido = 1 AND fk_ID_Prod = 789;
SELECT * FROM ItensVenda;
SELECT * FROM EstoqueProduto;

-- 5.9

CREATE TABLE Editora
(
ID_edit INT AUTO_INCREMENT PRIMARY KEY, -- Tabela PAI
Nome_Edit VARCHAR(60) NOT NULL,
Cidade VARCHAR(60) NOT NULL,
Estado CHAR(2) NOT NULL,
Pais VARCHAR(50) NOT NULL
);
INSERT Editora (Nome_Edit, Cidade, Estado, Pais) VALUES ('Editora AAA', 'São Paulo', 'SP', 'Brasil');
INSERT Editora (Nome_Edit, Cidade, Estado, Pais) VALUES ('Editora Sul', 'Porto Alegre', 'RS', 'Brasil');
INSERT Editora (Nome_Edit, Cidade, Estado, Pais) VALUES ('LTC', 'São Paulo', 'SP', 'Brasil');
INSERT Editora (Nome_Edit, Cidade, Estado, Pais) VALUES ('CENGAGE', 'Rio de Janeiro', 'RJ', 'Brasil');
INSERT Editora (Nome_Edit, Cidade, Estado, Pais) VALUES ('Três Estrelas', 'Alagoas', 'CE', 'Brasil');
SELECT * FROM Editora;

-- 5.10

DROP TABLE IF EXISTS Autor;
CREATE TABLE Autor
(
ID_Autor INT AUTO_INCREMENT PRIMARY KEY, -- Tabela FILHO
Nome_Autor VARCHAR(60) NOT NULL,
Dt_Nasc DATE NOT NULL,
fk_ID_Edit INT NULL
);
ALTER TABLE Autor ADD CONSTRAINT FK_Autor_Editora FOREIGN KEY(fk_ID_edit)
REFERENCES Editora (ID_edit);
ALTER TABLE Autor AUTO_INCREMENT = 100; -- Seed = 100 (início do AUTO_INCREMENT)
INSERT Autor (Nome_Autor, Dt_Nasc, fk_ID_Edit) VALUES ('José', '1956-09-08', 1);
INSERT Autor (Nome_Autor, Dt_Nasc, fk_ID_Edit) VALUES ('Maria', '1975-04-18', 2);
INSERT Autor (Nome_Autor, Dt_Nasc, fk_ID_Edit) VALUES ('Antônia', '1954-12-10', 3);
INSERT Autor (Nome_Autor, Dt_Nasc, fk_ID_Edit) VALUES ('Armínio', '1976-07-28', 5);
INSERT Autor (Nome_Autor, Dt_Nasc, fk_ID_Edit) VALUES ('Luiza', '1945-11-09', 5);
SELECT * FROM Autor;

-- 5.11

DROP TABLE IF EXISTS AutorLog;
-- Tabela de LOG (rastreamento) referente à Tabela Autor
CREATE TABLE AutorLog (
ID_log INT AUTO_INCREMENT PRIMARY KEY,
Operation CHAR(6) NOT NULL, -- Operação realizada
ChangeDate DATETIME NOT NULL, -- Data da realização da operação
UserName VARCHAR(20) NOT NULL, -- Usuário de BD que realizou a operção
OldID_Autor INT NULL, -- Valor antigo para ID_Autor
NewID_autor INT NULL, -- Valor novo para ID_Autor
OldAutor VARCHAR(50) NULL, -- Valor antigo para Nome de Autor
NewAutor VARCHAR(50) NULL, -- Valor novo para Nome de Autor
OldDtNasc DATE NULL, -- Valor antigo para Data de Nascimento do Autor
NewDtNasc DATE NULL, -- Valor novo para Data de Nascimento do Autor
OldID_Edit INT NULL, -- Valor antigo para ID do Editor do Autor
NewID_Edit INT NULL -- Valor novo para ID do Editor do Autor
);
SELECT * FROM AutorLog;

-- 5.12

DROP TRIGGER IF EXISTS AutorLogInsert;
-- Cria Trigger Tgr_ItensVenda_Insert
DELIMITER $$
CREATE TRIGGER AutorLogInsert
AFTER INSERT -- A Trigger dispara após o INSERT
ON Autor
FOR EACH ROW
BEGIN
INSERT INTO -- Insere registro na tabela AutorLog
AutorLog (Operation, ChangeDate, UserName, NewID_Autor, NewAutor, NewDtNasc, NewID_Edit)
SELECT 'Insert', NOW(), CURRENT_USER(), NEW.ID_autor, NEW.nome_autor, NEW.dt_nasc, NEW.fk_ID_edit;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER AutorLogDelete
AFTER DELETE -- A Trigger dispara após o DELETE
ON Autor
FOR EACH ROW
BEGIN
INSERT INTO -- Insere registro na tabela AutorLog
AutorLog (Operation, ChangeDate, UserName, OldID_Autor, OldAutor, OldDtNasc, OldID_Edit)
SELECT 'Delete', NOW(), CURRENT_USER(), OLD.ID_autor, OLD.nome_autor, OLD.dt_nasc, OLD.fk_ID_edit;
END $$
DELIMITER ;

-- 5.13

DROP TRIGGER IF EXISTS AutorLogUpdate;
-- Cria Trigger Tgr_ItensVenda_Update
DELIMITER $$
CREATE TRIGGER AutorLogUpdate
AFTER UPDATE -- A Trigger dispara após o UPDATE
ON Autor
FOR EACH ROW
BEGIN
INSERT INTO -- Insere registro na tabela AutorLog
AutorLog (Operation, ChangeDate, UserName, OldID_Autor, NewID_Autor, OldAutor, NewAutor,OldDtNasc,NewDtNasc, OldID_Edit, NewID_Edit)
SELECT 'Update', NOW(), CURRENT_USER(), OLD.ID_autor, NEW.ID_autor, OLD.nome_autor, NEW.nome_autor, OLD.dt_nasc, NEW.dt_nasc, OLD.fk_ID_edit, NEW.fk_ID_edit;
END $$
DELIMITER ;

-- 5.14

-- Comandos 1) Teste de UPDATE ----
UPDATE Autor SET nome_autor = 'José da Silva'
WHERE ID_autor = 100;
SELECT * FROM Autor;
SELECT * FROM AutorLog;
-- Comandos 2) Teste de INSERT ----
INSERT Autor (nome_autor, dt_nasc, fk_ID_Edit)
VALUES
('Karolina', '1976-06-18', 3),
('Cláudio', '1982-10-28', 4),
('Ricardo', '1990-02-13', 3);
SELECT * FROM Autor;
SELECT * FROM AutorLog;
-- Comandos 3) Teste de DELETE ---
DELETE FROM Autor
WHERE ID_autor = 102 OR ID_autor = 103;
SELECT * FROM Autor;
SELECT * FROM AutorLog;
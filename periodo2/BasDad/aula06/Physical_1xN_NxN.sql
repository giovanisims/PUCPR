DROP DATABASE testebsi;
CREATE DATABASE TESTEBSI;
USE TESTEBSI;

/* Lógico_1: */

CREATE TABLE Colaborador (
    Matricula INT PRIMARY KEY,
    Nome VARCHAR(50),
    CPF VARCHAR(20),
    Dt_Nasc DATE
);

CREATE TABLE Dependente (
    ID_Dependente INT PRIMARY KEY,
    Nome VARCHAR(50),
    Dt_Nasc DATE,
    Parentesco VARCHAR(20),
    fk_Colaborador_Matricula INT
);
 
ALTER TABLE Dependente ADD CONSTRAINT FK_Dependente_2
    FOREIGN KEY (fk_Colaborador_Matricula)
    REFERENCES Colaborador (Matricula)
    ON DELETE CASCADE;
    
    
INSERT INTO Colaborador (Matricula, Nome, CPF, Dt_Nasc)
	VALUES 				(123, 'Maria', '12345', '1990-10-12'),
						(124, 'Pedro', '45678', '1992-05-19'),
						(125, 'João', '78904', '1995-03-01');
                        
SELECT Matricula, CPF, Nome, Dt_Nasc, 
		TIMESTAMPDIFF(YEAR, Dt_Nasc, NOW() ) AS Idade
FROM Colaborador;

INSERT INTO Dependente (ID_Dependente, Nome, Dt_Nasc, Parentesco, fk_Colaborador_Matricula)
	VALUES 				(200, 'Huguinho', '2020-10-12', 'Filho',123),
						(300, 'Zezinho', '2022-05-19', 'Filho',123),
						(400, 'Luizinho', '2021-03-01', 'Enteado',125);
                        
SELECT ID_Dependente, Nome, Dt_Nasc, Parentesco,
		TIMESTAMPDIFF(YEAR, Dt_Nasc, NOW() ) AS 'Idade Criança',
        fk_Colaborador_Matricula AS 'Mat. Colaborador'
FROM Dependente;

CREATE TABLE Projeto (
    ID_Proj INT PRIMARY KEY,
    Nome_Proj VARCHAR(50)
);

CREATE TABLE Trabalha (
    ID_Trab INT PRIMARY KEY,
    Dt_Inicio DATE,
    Dt_Fim DATE NOT NULL,
    fk_Colaborador_Matricula INT NOT NULL,
    fk_Projeto_ID_Proj INT NOT NULL
);

ALTER TABLE Trabalha ADD CONSTRAINT FK_Trabalha_2
    FOREIGN KEY (fk_Colaborador_Matricula)
    REFERENCES Colaborador (Matricula)
    ON DELETE RESTRICT;
 
ALTER TABLE Trabalha ADD CONSTRAINT FK_Trabalha_3
    FOREIGN KEY (fk_Projeto_ID_Proj)
    REFERENCES Projeto (ID_Proj);
    
SELECT Matricula, C.Nome AS Colaborador, 
	TIMESTAMPDIFF(YEAR, C.Dt_Nasc, NOW()) AS 'Idade Colaborador',
	TIMESTAMPDIFF(YEAR, D.Dt_Nasc, NOW()) AS 'Idade Dependente',
	D.Parentesco
FROM Colaborador AS C, Dependente AS D
WHERE C.Matricula = D.fk_Colaborador_Matricula;
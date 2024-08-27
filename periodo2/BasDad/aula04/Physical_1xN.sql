DROP DATABASE testebsi;
CREATE DATABASE TESTEBSI;
USE TESTEBSI;


CREATE TABLE Colaborador (
    Matricula INT PRIMARY KEY,
    Nome VARCHAR(50),
    CPF VARCHAR(20),
    Dt_Nasc DATE
);

CREATE TABLE Telefone (
	Telefone VARCHAR(20),
    fk_Colaborador_Matricula INT,
    FOREIGN KEY (fk_Colaborador_Matricula)  REFERENCES Colaborador (Matricula),
    PRIMARY KEY (Telefone, fk_Colaborador_Matricula)
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
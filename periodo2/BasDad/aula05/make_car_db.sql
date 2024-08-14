DROP TABLE CARRO;

CREATE TABLE Carro (
CodCarro INT PRIMARY KEY,
Marca VARCHAR(20),
Modelo VARCHAR(20),
AnoFabricacao INT,
Kilometragem FLOAT,
Cor VARCHAR(20));


INSERT INTO Carro (CodCarro, Marca, Modelo, AnoFabricacao, Kilometragem, Cor)
VALUES
	(1, 'MarcaTeste', 'ModeloTeste', 0, 0.1, 'CorTeste'),
	(2, 'MarcaTeste', 'ModeloTeste', 0, 0.1, 'CorTeste'),
    (3, 'MarcaTeste', 'ModeloTeste', 0, 0.1, 'CorTeste'),
    (4, 'MarcaTeste', 'ModeloTeste', 0, 0.1, 'CorTeste'),
    (5, 'MarcaTeste', 'ModeloTeste', 0, 0.1, 'CorTeste');



SELECT * FROM Carro;

UPDATE Carro
SET Cor = 'CorTeste2'
WHERE CodCarro = 1;

UPDATE Carro
SET AnoFabricacao = 1
WHERE CodCarro = 2;

SELECT * FROM Carro;

DELETE FROM Carro
WHERE CodCarro = 5;

SELECT * FROM Carro;

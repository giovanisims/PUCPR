CREATE DATABASE IF NOT EXISTS LAB_03;

-- 3.1

USE LAB_03;
SELECT
nome, -- campo / coluna da tabela
dt_nascimento, -- campo / coluna da tabela
DATE_FORMAT(dt_nascimento, '%d/%d/%Y') AS 'Aniversário', -- formata data em dia/mês/ano com 4 dígitos
(
YEAR(NOW()) - YEAR(dt_nascimento) - -- vai SUBTRAIR de 0 ou 1, dependendo se já fez aniversário ou não
CASE
WHEN (MONTH(NOW()) * 100 + DAY(NOW())) > (MONTH(dt_nascimento) * 100 + DAY(dt_nascimento))
THEN 0 -- Valor de retorno para ser subtraído = 0
ELSE 1 -- Valor de retorno para ser subtraído = 1
END
) AS Idade -- AS é a indicação de apelido de exibição para a coluna recém calculada
FROM Empregado;

-- 3.2

SELECT *
FROM Empregado AS E, Departamento AS D -- PRODUTO CARTESIANO
WHERE E.ID_depto = D.ID_depto -- Condição para retorno
ORDER BY E.nome;
SELECT *
FROM Empregado AS E INNER JOIN Departamento AS D -- JOIN ou INNER JOIN
ON (E.ID_depto = D.ID_depto) -- Condição para retorno
ORDER BY E.nome;

-- 3.3

SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E, EmpSkill AS ES, Skill AS S -- PRODUTO CARTESIANO
WHERE E.ID_emp = ES.ID_emp AND -- Condição para retorno
S.ID_skill = ES.ID_skill
ORDER BY S.nome, E.nome;
SELECT E.nome AS Empregado, ES.nivel, S.nome -- JOIN
FROM
( -- Primeiro, faz JOIN entre as tabelas Empregado e EmpSkill
Empregado AS E INNER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
-- Depois, associa o resultado anterior com a tabela Skill
) INNER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
ORDER BY S.nome, E.nome;

-- 3.4

SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM
( -- Primeiro, associa (LEFT OUTER JOIN) Empregado e EmpSkill
Empregado AS E LEFT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
-- Depois, associa (LEFT OUTER JOIN) o resultado com Skill
) LEFT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
ORDER BY S.nome, E.nome;

-- 3.5

SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM
( -- Primeiro, associa (RIGHT OUTER JOIN) Empregado e EmpSkill
Empregado AS E RIGHT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
-- Depois, associa (RIGHT OUTER JOIN) o resultado com Skill
)RIGHT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
ORDER BY S.nome, E.nome;

-- 3.6

(
SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM
( -- Primeiro, associa (LEFT OUTER JOIN) Empregado e EmpSkill
Empregado AS E LEFT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
-- Depois, associa (LEFT OUTER JOIN) o resultado com Skill
) LEFT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
)
UNION
(
SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM
( -- Primeiro, associa (RIGHT OUTER JOIN) Empregado e EmpSkill
Empregado AS E RIGHT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
-- Depois, associa (RIGHT OUTER JOIN) o resultado com Skill
)RIGHT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
)
ORDER BY nivel;

-- 3.7

SELECT E.ID_emp, E.nome
FROM Empregado AS E JOIN Departamento AS D
ON (E.ID_depto = D.ID_depto)
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
ORDER BY E.nome;

SELECT E.ID_emp, E.nome
FROM Empregado AS E
WHERE E.ID_depto IN
(
SELECT D.ID_depto
FROM Departamento AS D
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
)
ORDER BY E.nome;

-- 3.8

SELECT E.ID_depto, E.ID_emp, E.nome
FROM Empregado AS E
WHERE E.ID_depto NOT IN
(
SELECT D.ID_depto
FROM Departamento AS D
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
)
ORDER BY E.nome;

SELECT E.ID_depto, E.ID_emp, E.nome
FROM Empregado AS E
WHERE E.ID_depto <> ALL
(
SELECT D.ID_depto
FROM Departamento AS D
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
)
ORDER BY E.nome;

-- 3.9

SELECT E.ID_depto, E.ID_emp, E.nome, E.dt_nascimento
FROM Empregado AS E
WHERE YEAR(E.dt_nascimento) >= 1998 AND
E.ID_depto IN
(
SELECT D.ID_depto
FROM Departamento AS D, Empregado AS E1
WHERE D.ID_depto = E1.ID_depto AND
(D.sigla = 'CTB' OR D.sigla ='VND')
)
ORDER BY E.nome;

-- 3.10

-- Apaga a VIEW se ela já existir
DROP VIEW IF EXISTS CompetenciasEmpregados;
CREATE VIEW CompetenciasEmpregados AS
(
SELECT D.sigla AS Depto, S.nome AS Competencia, ES.nivel AS Nivel, E.nome AS Empregado
FROM
((
Empregado AS E INNER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
) INNER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
) INNER JOIN Departamento AS D ON (D.ID_depto = E.ID_depto)
);

SELECT * FROM competenciasempregados;

-- 3.11

SELECT *
FROM CompetenciasEmpregados
ORDER BY Depto, Competencia, Empregado;

-- 3.12

SELECT
COUNT(*) AS 'Número de Empregados',
AVG(salario) AS 'Salário Médio',
MIN(salario) AS 'Menor Salário' ,
MAX(salario) AS 'Maior Salário' ,
SUM(salario) AS 'Total Salários'
FROM Empregado;
SELECT
COUNT(*) AS 'Número de Empregados',
CONVERT(AVG(salario), DECIMAL(8,2)) AS 'Salário Médio',
MIN(salario) AS 'Menor Salário' ,
MAX(salario) AS 'Maior Salário' ,
SUM(salario) AS 'Total Salários'
FROM Empregado;
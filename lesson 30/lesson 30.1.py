CREATE TABLE Test_Task(
    ColumnID int,
    Colum1 varchar,
    Colum2 varchar,
    Colum3 varchar
);

SELECT * FROM Test_Task

ALTER TABLE Test_Task
ADD Colum4 varchar;

INSERT INTO Test_Task (Colum1, Colum2, Colum3, Colum4)
VALUES ('columtest1','columtest2','columtest3','columtest4');

INSERT INTO Test_Task (Colum1, Colum2, Colum3, Colum4)
VALUES ('columtest1.2','columtest2.2','columtest3.2','columtest4.2');

UPDATE Test_Task
SET ColumnID=2
WHERE Colum1='columtest2';

UPDATE Test_Task
SET ColumnID=2
WHERE Colum1='columtest1.2';

UPDATE Test_Task
SET ColumnID=1
WHERE Colum1='columtest1';

DELETE FROM Test_Task WHERE Colum4='columtest4.2'
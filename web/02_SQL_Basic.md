# OverView

##### 1. 데이터베이스 생성

```sql
DROP DATABASE IF EXISTS sqlDB;
CREATE DATABASE sqlDB;

USE sqlDB;
```

<br/>

<br/>

##### 2. 테이블 생성

```sql
CREATE TABLE userTbl(
	userID		CHAR(8) 	NOT NULL PRIMARY KEY,
    name		VARCHAR(10)	NOT NULL,
    birthYear	INT			NOT NULL,
    addr		CHAR(3)		NOT NULL,
    mobile1		CHAR(3),
    mobile2		CHAR(8),
    height		SMALLINT,
    mDate		DATE
);

CREATE TABLE buyTbl(
	num			INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userID		CHAR(8)		NOT NULL,
    prodName	CHAR(6)		NOT NULL,
    groupName	CHAR(4),
    price		INT			NOT NULL,
    amount		SMALLINT	NOT NULL,
    FOREIGN KEY (userID) REFERENCES userTbl(userID)
);

DESC userTbl;
DESC buyTbl;
```

<br/>

<br/>

##### 3. 데이터 추가

```sql
INSERT INTO userTbl VALUES('LSG', '이승기', 1987, '서울', '011', '11111111', 182, '2008-8-8');
INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '22222222', 173, '2012-4-4');
INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '33333333', 177, '2007-7-7');
INSERT INTO userTbl VALUES('JYP', '조용필', 1950, '경기', '011', '44444444', 166, '2009-4-4');
INSERT INTO userTbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO userTbl VALUES('LJB', '임재범', 1963, '서울', '016', '66666666', 182, '2009-9-9');
INSERT INTO userTbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO userTbl VALUES('EJW', '은지원', 1972, '경북', '011', '88888888', 174, '2014-3-3');
INSERT INTO userTbl VALUES('JKW', '조관우', 1965, '경기', '018', '99999999', 172, '2010-10-10');
INSERT INTO userTbl VALUES('BBK', '바비킴', 1973, '서울', '010', '00000000', 176, '2013-5-5');
INSERT INTO buyTbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buyTbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
```

<br/>

<br/>

##### 4. 데이터 조회, 수정, 삭제

```sql
SELECT * FROM userTbl;
SELECT * FROM buyTbl;
```

<br/>

<br/>

<br/>

# SELECT FROM

* 테이블에서 **데이터 조회**

> **SELECT** <컬럼명>
>
> ​	**FROM** <테이블명>
>
> ​	**WHERE** <조건>

```sql
select * from userTbl;
select * from buyTbl;

select * from userTbl where name = '임재범';
select * from buyTbl where groupname = '전자';

select userID, prodName, price, amount from buyTbl where groupName = '전자';

select userID as '아이디' from buyTbl;
```

<br/>

<br/>

- 조건 연산자 : `OR` , `AND` , `BETWEEN` , `IN` , `LIKE`

```sql
select * from userTbl where birthYear >= 1970 and height <= 180;

select * from userTbl where height between 170 and 180;

select * from userTbl where addr in ('서울', '전남');

select * from userTbl where name like '김%';
```

<br/>

<br/>

- 서브 쿼리 : `ANY`, `ALL`

```sql
select * from userTbl where userID = any(
	select userID from buyTbl where prodName = '운동화'
);
```

<br/>

<br/>

- `ORDER BY`

```sql
select * from buyTbl where amount > 1 order by price;
select * from buyTbl where amount > 1 order by price desc;
```

<br/>

<br/>

- `DISTINCT`

```sql
select distinct addr from userTbl;
select distinct prodName, groupName from buyTbl;
```

<br/>

<br/>

- `LIMIT`

```sql
select * from buyTbl order by price desc limit 10;
```

<br/>

<br/>

- 테이블 복사
  - PK, FK 등 제약 조건은 복사되지 않음

```sql
create table copyTbl (select userID, prodName from buyTbl);

desc copyTbl;
desc buyTbl;
```

<br/>

<br/>

<br/>

# GROUP BY ~ HAVING

>SELECT <컬럼명>
>
>​	FROM <테이블명>
>
>​	WHERE <조건>
>
>​	**GROUP BY** <컬럼명>
>
>​	**HAVING** <조건>
>
>​	ORDER BY <컬럼명>

```sql
select userID, sum(price*amount) as '총 구매액' from buyTbl group by userID;
```

<br/>

<br/>

- 집계 함수(Aggregate Function)

| 함수 명         | 설명                         |
| :-------------- | ---------------------------- |
| AVG()           | 평균                         |
| MIN()           | 최소값                       |
| MAX()           | 최대값                       |
| COUNT()         | 행의 개수                    |
| COUNT(DISTINCT) | 행의 개수(중복은 1개만 인정) |
| STDEV()         | 표준편차                     |
| VAR_SAMP()      | 분산                         |

```sql
-- 가장 큰 키와 작은 키의 회원의 이름과 키를 출력
select name, height from userTbl
	where height = (select max(height) from userTbl)
		or height = (select min(height) from userTbl);

-- 휴대폰이 있는 사용자의 수
select count(mobile1) as '휴대폰 있는 사용자' from userTbl;


```

<br/>

<br/>

- `HAVING`
  - 집계 함수를 조건으로 사용할 때 사용
  - 집계 함수는 `WHERE` 절에 나타낼 수 없음
  - 반드시 `GROUP BY` 절 다음에 위치

```sql
select userID, sum(price*amount) as '총 구매액'
	from buyTbl
	group by userID
	having sum(price*amount) > 1000
	order by sum(price*amount);
```

<br/>

<br/>

- `WITH ROLLUP` : 총합 또는 중간 합계

```sql
select groupName, avg(price*amount) as '비용'
	from buyTbl
	group by groupName
	with rollup;
```

<br/>

<br/>

<br/>

# INSERT

- 테이블에 **데이터 삽입**

> **INSERT INTO** <테이블명> **VALUES** (값1, 값2, ...)

````sql
insert into userTbl values ('JYP', '조용필', 1950, '경기', '011', '44444444', 166, '2009-4-4');
````

<br/>

<br/>

# UPDATE

- 테이블에서 **데이터 수정**

> **UPDATE** <테이블명>
>
> ​	**SET** 열1 = 값1, 열2 = 값2, ...
>
> ​	**WHERE** <조건>;

```sql
update userTbl set mobile2 = '12345678', height = 180 where userID = 'EJW';
```

<br/>

<br/>

<br/>

# DELETE

- 테이블에서 **데이터 삭제**

> **DELETE FROM** <테이블명>
>
> ​	**WHERE** <조건>

```sql
DELETE FROM testTBL4 WHERE Fname = 'Aamer';
DELETE FROM testTBL4 WHERE Fname = 'Mary' LIMIT 5;
```

<br/>

<br/>

| `DELETE`                                        | `DROP`        | `TRUNCATE`                                        |
| :---------------------------------------------- | :------------ | :------------------------------------------------ |
| - 데이터 삭제<br />- 로그 기록<br />- 속도 느림 | - 테이블 삭제 | - 데이터 삭제<br />- 로그 기록 x<br />- 속도 빠름 |

```sql
CREATE TABLE bigTBL1 (SELECT * FROM employees.employees);
CREATE TABLE bigTBL2 (SELECT * FROM employees.employees);
CREATE TABLE bigTBL3 (SELECT * FROM employees.employees);

DELETE FROM bigTBL1;
DROP TABLE bigTBL2;
TRUNCATE TABLE bigTBL3;

SHOW TABLES;
```

<br/>

<br/>

<br/>

# 변수

- **`@변수이름 = 값`**

```sql
SET @myVar1 = 5 ;
SET @myVar2 = 3 ;
SET @myVar3 = 4.25 ;
SET @myVar4 = '가수 이름==> ' ;

SELECT @myVar1 ;
SELECT @myVar2 + @myVar3 ;
SELECT @myVar4 , Name FROM userTBL WHERE height > 180 ;
```

<br/>

<br/>

- **`EXECUTE 쿼리문 USING @변수이름`**

```sql
SET @myVar1 = 3 ;
PREPARE myQuery 
    FROM 'SELECT Name, height FROM userTBL ORDER BY height LIMIT ?';
EXECUTE myQuery USING @myVar1 ;
```

<br/>

<br/>

<br/>

# INNER JOIN

> SELECT (컬럼이름) FROM (테이블이름)
>
> ​	**INNER JOIN** (테이블이름)
>
> ​		**ON** (기준)
>
> ​	WHERE (조건);

- `buyTBL`에 `userTBL`을 `join`

```sql
SELECT * FROM buyTBL
	INNER JOIN userTBL
		ON buyTBL.userID = userTBL.userID;
	--WHERE buyTBL.userID = 'JYP';
```

<br/>

<br/>

- `userTBL`에 `buyTBL`을 `join`

```sql
SELECT * FROM userTBL
	INNER JOIN buyTBL
		ON userTBL.userID = buyTBL.userID;
```

<br/>

<br/>

- `buyTBL`을 `B`로, `userTBL`을 `U`로 사용

```sql
SELECT addr, NAME, birthyear, CONCAT(mobile1, mobile2), B.userID
	FROM buyTBL B
		INNER JOIN userTBL U
			ON B.userID = U.userID
	WHERE B.userID = 'JYP';
```

<br/>

<br/>

<br/>

# OUTER JOIN

>SELECT (컬럼이름) FROM (테이블이름)
>
>​	**\<LEFT | RIGHT | FULL> OUTER JOIN** (테이블이름)
>
>​		**ON** (기준)
>
>WHERE (조건);

<br/>

- `RIGHT OUTER JOIN` : 구매이력이 없는 user까지 출력

```sql
--SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2)  AS '연락처'
SELECT *
   FROM buyTBL B 
      RIGHT OUTER JOIN userTBL U
         ON U.userID = B.userID 
   ORDER BY U.userID;
```

<br/>

- `LEFT OUTER JOIN`

```sql
SELECT *
   FROM buyTBL B 
      LEFT OUTER JOIN userTBL U
         ON U.userID = B.userID 
   ORDER BY U.userID;
```

<br/>

<br/>

<br/>

# SELF JOIN

- 자기 자신과 `JOIN`
- 주로 조직도에서 사용

```sql
SELECT * FROM empTBL A
	INNER JOIN empTBL B
		ON A.manager = B.emp
	WHERE A.emp = '우대리';
```

<br/>

<br/>

<br/>

# PROCEDURE

```sql
DELIMITER $$
CREATE PROCEDURE ifProc()
BEGIN
  DECLARE var1 INT;  -- var1 변수선언
  SET var1 = 100;  -- 변수에 값 대입

  IF var1 = 100 THEN  -- 만약 @var1이 100이라면,
	SELECT '100입니다.';
  ELSE
    SELECT '100이 아닙니다.';
  END IF;
END $$
DELIMITER ;
CALL ifProc();
```

<br/>

```sql
DROP PROCEDURE IF EXISTS ifProc3; 
DELIMITER $$
CREATE PROCEDURE ifProc3()
BEGIN
    DECLARE point INT ;
    DECLARE credit CHAR(1);
    SET point = 77 ;
    
    IF point >= 90 THEN
		SET credit = 'A';
    ELSEIF point >= 80 THEN
		SET credit = 'B';
    ELSEIF point >= 70 THEN
		SET credit = 'C';
    ELSEIF point >= 60 THEN
		SET credit = 'D';
    ELSE
		SET credit = 'F';
    END IF;
    SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;
CALL ifProc3();
```

<br/>

```sql
DROP PROCEDURE IF EXISTS caseProc; 
DELIMITER $$
CREATE PROCEDURE caseProc()
BEGIN
    DECLARE point INT ;
    DECLARE credit CHAR(1);
    SET point = 77 ;
    
    CASE 
		WHEN point >= 90 THEN
			SET credit = 'A';
		WHEN point >= 80 THEN
			SET credit = 'B';
		WHEN point >= 70 THEN
			SET credit = 'C';
		WHEN point >= 60 THEN
			SET credit = 'D';
		ELSE
			SET credit = 'F';
    END CASE;
    SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;
CALL caseProc();
```

<br/>

```sql
DROP PROCEDURE IF EXISTS whileProc2; 
DELIMITER $$
CREATE PROCEDURE whileProc2()
BEGIN
    DECLARE i INT; -- 1에서 100까지 증가할 변수
    DECLARE hap INT; -- 더한 값을 누적할 변수
    SET i = 1;
    SET hap = 0;

    myWhile: WHILE (i <= 100) DO  -- While문에 label을 지정
	IF (i%7 = 0) THEN
		SET i = i + 1;     
		ITERATE myWhile; -- 지정한 label문으로 가서 계속 진행
	END IF;
        
        SET hap = hap + i; 
        IF (hap > 1000) THEN 
		LEAVE myWhile; -- 지정한 label문을 떠남. 즉, While 종료.
	END IF;
        SET i = i + 1;
    END WHILE;

    SELECT hap;   
END $$
DELIMITER ;
CALL whileProc2();
```

<br/>

```sql
DROP TABLE IF EXISTS myTable;
CREATE TABLE myTable (id INT AUTO_INCREMENT PRIMARY KEY, mDate DATETIME);

SET @curDATE = CURRENT_TIMESTAMP(); -- 현재 날짜와 시간

PREPARE myQuery FROM 'INSERT INTO myTable VALUES(NULL, ?)';
EXECUTE myQuery USING @curDATE;
DEALLOCATE PREPARE myQuery;

SELECT * FROM myTable;
```












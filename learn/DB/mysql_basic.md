# mysql 학습

## DB 정의하기

어떤 DB가 있는지 확인

```sql
SHOW DATABASES; -- 목록 출력
```

데이터 베이스 `company` 구축 → 활성화 X

```sql
CREATE DATABASE company; -- Query OK, 1 row affected
```

데이터 베이스 활성화

```sql
SELECT database(); -- 활성화된 DB확인. NULL 이면, 선택된 데이터 베이스가 없다.
USE company; -- company 활성화(사용하는 DB)
SELECT database(); -- company 출력된다.
```

참고) DATABASE vs SCHMA

- MySQL에서는 DATABASE와 SCHEMA 가 동일
  
  ```sql
  CREATE DATABASE company;
  CREATE SCHEMA company; -- 똑같이 작동
  ```

- i.g. PostgreSQL 에서는 SCHEMA가 DATABASE의 namespace 를 의미

## IT 회사 RDB 만들기(table 정의)

# create table

### DEPARTMENT table 생성

```sql
create table DEPARTMENT(
    id INT PRIMAY KEY,
    name varchar(20) NOT NULL UNIQUE,
    leader_id INT
);
```

> 이름, 데이터 타입, 옵션(키, nul 유무…)

### EMPLOYEE table 생성

```sql
create table EMPLOYEE(
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    birth_date DATE,
    sex CHAR(1) CHECK(sex in ('M', 'f')),
    position VARCHAR(10),
    salary INT DEFAULT 5000000,
    dept_id INT,
    FOREIGN KEY (dept_id) references DEPARTMENT(id)
        on delete SET NULL on update CASCADE,
    CHECCK (salary >= 5000000)
);
```

### PROJECT table 생성

```sql
create table PROJECT(
    id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL, UNIQUE,
    leader_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY(leader_id) references EMPLOYEE(id)
        on delete SET NULL
        on update CASCADE,
    CHECK(start_date < end_date)
);
```

### WORKS_ON table 생성

```sql
create table WORKS_ON(
    empl_id INT,
    proj_id INT
    PRIMARY KEY(empl_id, proj_id),
    FOREIGN KEY(empl_id) references EMPLOYEE(id)
        on delete SET CASCATE
        on update CASCADE,
    FOREIGN KEY(proj_id) references PROJECT(id)
        on delete SET CASCATE
        on update CASCADE,
);
```

# ALTER TABLE

> table의 schema를 변경하고 싶을 때 사용

### DEPARTMENT table에 leader_id FK 지정

```sql
ALTER TABLE department ADD FOREIGN KEY (leader_id)
-> REFERENCES employee(id)
-> on update CASCATE
-> on delete SET NULL;
```

- 이미 서비스 중인 table의 schema를 변경하는 것이라면 변경 작업 때문에 서비스의 백엔드에 영향이 없을지 검토한 후에 변경하는 것이 중요

## 데이터 타입

숫자

- PostgreSQL에서는 `TINYINT` `MEDIUMINT` 가 없다.

- 돈 처럼 소수점이 정확해 때는 고정 소수점 방식을 사용

- 고정 소수점의 경우 `precision` (전체 자리 수)과 `scale` (소수 점 이하)을 작성해야한다.

- DECIMAL vs NUMERIC
  
  원래 공식 SQL 스택은 NUMERIC 은 염격하게 자리수를 초과하면 저장하지 않지만, DECIMAL 은 유연하게 값이 넘어도 저장하는 타입이다.
  
  MySQL 에서 DECIMAL, NUMERIC 는 차이가 없이 `precision` 넘으면 저장하지 않는다.



문자열

- VARCHAR VS CHAR
  
  RDBMS의 구현에 따라 성능이 다
  
  PostgreSQL 에서는 VARCHAR를 권장
  
  MySQL에서는 VARCHAR 사용 시 스토리지 적인 이점이 있지만, 시간적인 성능이 CHAR 보다 나쁘다.

- MySQL에서는 VARCHAR 보다 큰 데이터는 MEDIUMTEXT나 LONGTEXT를 쓴다.
  
  - TINYTEXT, TEXT는 VARCHAR보다 데이터 크기 작거나 같다.

- PostgreSQL은 TINYTEXT, MEDIUMTEXT, LONGTEXT 이 없이 TEXT만 있다.



날짜와 시간

- DATETIME VS TIMESTAMP
  
  TIMESTAMP `UTC` 다. 즉, TIMEZONE에 영향을 받는다.



byte-string

byte-string : 보안과 관련해서 암호화 하고자 할 때, 사용된다.



## 제약 조건 (constraints)

### constraint PRIMARY KEY

- primary key : table의 tuple 을 식별하기 위해 사용, 하나 이상의 attribue(s) 로 구성
- primary key 는 중복된 값을 가질 수 없으며, NULL 도 값으로 가질 수 없다.

### constraint UNIQUE

- UNIQUE로 지정된 attribue(s)는 중복된 값을 가질 수 없다.
- 단, NULL 은 중복을 허용할 수도 있다. (RDBMS 마다 다름)

### constraint NOT NULL

- attribute가 NOT NULL로 지정되면 해당 attribute는 NULL을 값으로 가질 수 없다.
- UNIQUE와 자주 사용

### constraint DEFAULT

- attribute의 default 값을 정의할 때 사용
- 새로운 tuple을 저장할 때 해당 attribute에 대한 값이 없다면 default 값으로 저장

### constraint CHECK

- attribute의 값을 제한하고 싶을 때 사용

## constraint FOREIGN KEY

- attribute(s)가 다른 table의 primary key 나 unique key 를 참조할 때 사용

## 추가) constraint 이름 명시하기

- 이름을 붙이면 어떤 constraint을 위반했는지 쉽게 파악할 수 있다.
- constraint를 삭제하고 싶을 때 해당 이름으로 삭제 가능

```sql
crate table TEST(
    age INT CONSTRAINT age_over_20 CHECK(age > 20)
);
```

- 만약 age에 15라는 값을 넣으면( 에러 )
- “CONSTRAINT age_over_20” 라고 이름을 붙였을 때
  - Check constraint ‘age_over_20’ is violated.
- 아무런 이름을 안 넣었을 때,
  - Check constraint ‘test_chk_1’ is violated.

```sql
show create table TEST; -- 에러난 페이지 확
```

# SQL 조회

# 기본 SELECT

```sql
-- id 가 9인 직원 이름, 직책 조회
SELECT name, position FROM employee WHERE id = 9;
```

```sql
-- project 2002 를 리딩하고 임직원의 ID와 이름과 직군을 조회( 테이블 2개)
SELECT employee.id, employee.name, position
FROM project, employee
WHERE project.id =2002 
and project.leader_id = employee.id; -- join conddition
```

> table 이름이 겹치면 안 되니까. table 명을 명시해주자.

## SELECT 실행순서

> 명세적인 순서, RDBMS 따라 다름

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. ORDER BY
6. SELECT

### AS 키워드

```sql
SELECT E.id, E.name, position
FROM project AS P, employee AS E -- AS 는 생략 가능
WHERE P.id =2002 and P.leader_id = E.id;
```

> 테이블 명 별칭으로 간략하게 작성 가능

```sql
SELECT E.id AS leader_id, E.name AS leader_name, position -- AS 는 생략 가능
FROM project AS P, employee AS E
WHERE P.id =2002 and P.leader_id = E.id;
```

> 컬럼 명도 바꿀 수 있음

### DISTINCT 키워드 → 중복된 튜플 제거

```sql
SELECT DISTINCT P.id, P.name -- 중복 제거
FROM employee AS E, works_on AS W, project AS P
WHERE E.position = 'DSGN' and
    E.id = W.empl_id and W.proj_id = P.id;
```

### LIKE 키워드

```sql
SELECT name FROM employee -- N 으로 시작하거나 끝나는 임직원 이름
WHERE name LIKE 'N%' or name LIKE '%N';

SELECT name FROM employee -- 이름에 NG가 들어가는 임직원 이름
WHERE name LIKE '%NG%';

SELECT name FROM employee -- J로 시작하는 4글자인 사람 
WHERE name LIKE 'J___';
```

- `%` 0 개 이상의 임의의 개수를 가지는 문자를 의미
- `_` 하나의 문자를 의미
- `\\` escape 로 `\\%%` 식으로 사용된다.
- `*` asterisk 로 모든 값을 출력

# SUBQUERY

- ID 가 14인 임직원보다 생일이 빠른 임직원의 ID, 이름, 생일을 알고 싶다.

```sql
SELECT birth_date FROM employee WHERE id=14; -- 결과 1992-08-04
SELECT id, name, birth_date FROM employee WHERE birth_date < '1992-08-04';
-- 이걸  한 문장으로 합치면,
SELECT id, name, birth_date FROM employee WHERE birth_date < (
    SELECT birth_date FROM employee WHERE id=14; -- subquery
); -- outer query
```

- subquery : select, insert, update, delete에 포함된 query
- outer query : subquery를 포함하는 query
- subquery 는 `()` 안에 기술 된다.

### IN : 조건이 여러가지 값에 포함되는지 확인

```sql
SELECT DISTINCT empl_id FROM works_on
WHERE empl_id != 5 AND proj_id IN (
    SELECT proj_id FROM works_on WHERE empl_id = 5
); -- 직원 id 5인 직원과 같이 프로젝트에 참여한 직원들의 id 조회
```

### EXISTS : 조건 최소 1개라도 존재하면 True

```sql
SELECT P.id, P.name
FROM project p
WHERE EXISTS (
    SELECT *
    FROM works_on W
    WHERE W.proj_id = P.id AND W.empl_id IN (7, 12)
); -- id 가 7 혹은 12 인 임직원이 참여한 프로젝트의 id와 이름을 조회 
```

### ANY : 단 하나라도 조건에 부합하면

```sql
SELECT E.id, E.name, E.salary
FROM department D, employee E
WHERE D.leader_id = E.id AND E.salary < ANY (
    SELECT salary
    FROM employee
    WHERE id <> D.leader_id AND dept_id = E.dept_id
); -- 리더보다 높은 연봉을 받는 부서원을 가진 리더의 ID와 이름, 연봉을 조회.

-- select 절에도 subquery 가능
SELECT E.id, E.name, E.salary,
    ( 
        SELECT max(salary)
        FROM employee
        WHERE dept_id = E.dept_id
    ) AS dept_max_salary  -- 부서별 최고 연봉
FROM department D, employee E
WHERE D.leader_id = E.id AND E.salary < ANY (
    SELECT salary
    FROM employee
    WHERE id <> D.leader_id AND dept_id = E.dept_id
);
```

### ALL :

```sql
SELECT DISTINCT E.id, E.name, E.position
FROM employee E, works_on W
WHERE E.id = W.empl_id AND W.proj_id <> ALL (
    SELECT proj_id
    FROM works_on
    WHERE empl_id =  13
); -- id가 13인 임직원가 한 번도 같은 프로젝트에 참여하지 못한 직원 정
```

# NULL

> 여러가지 의미를 가지고 있지만, 퉁쳐서 null 이라고 한다.

## null 의 의미

- unknown : 모른다.
- unavailable or withheld : 제공 되지 않았다.
- not applicable : 해당 사항이 아니다.

참고 : null 값 비교할 때 `=` 말고 `is` 로 해야 한다.

```sql
SELECT id FROM employee WHERE birth_date = NULL; -- 올바르지 않다.
SELECT id FROM employee WHERE birth_date IS NULL; -- 제대로 조회됨
```

## three-value logic

- SQL 에서 NULL과 비교 연산을 하게 되면 그 결과는 UNKNOWN이다.
- UNKNOWN 은 `TRUE 일수도 있고 FALSE 일 수도 있다`라는 의미이다.
- three-value logic : 비교 / 논리 연산의 결과로 TRUE, FALSE UNKNOWN을 가진다.

## 

## 집계 함수 (Aggregate Functions)

### COUNT

- 튜플의 수를 센다.
- null이 아닌 값을 센다.

```sql
SELECT COUNT(*) FROM employee; 
-- 모든 튜플의 수를 센다. SELECT COUNT(name) FROM employee; 
-- name이 null이 아닌 값을 센다.
```

### SUM

- 특정 attribute의 합을 구한다.
- null은 계산에서 제외된다.

```sql
SELECT SUM(salary) FROM employee; -- salary의 합을 구한다
```

### AVG

- 특정 attribute의 평균을 구한다.
- null은 계산에서 제외된다.

```sql
SELECT AVG(salary) FROM employee; -- salary의 평균을 구한다.
```

### MAX

- 특정 attribute의 최대값을 구한다.
- null은 계산에서 제외된다.

```sql
SELECT MAX(salary) FROM employee; -- salary의 최대값을 구한다.
```

### MIN

- 특정 attribute의 최소값을 구한다.
- null은 계산에서 제외된다.

```sql
SELECT MIN(salary) FROM employee; -- salary의 최소값을 구한다.
```

## GROUP BY

- 특정 attribute를 기준으로 튜플을 그룹화 한다.
- 집계 함수를 사용하여 각 그룹에 대한 통계를 구할 수 있다.

```sql
SELECT dept_id, COUNT(*) as num_employees FROM employee GROUP BY dept_id; -- 각 부서별 직원 수를 센다.
```

## HAVING

- GROUP BY 절로 그룹화한 결과에 조건을 걸 때 사용한다.
- WHERE 절과 비슷하지만, HAVING 절은 그룹화된 데이터에 조건을 적용한다.

```sql
SELECT dept_id, AVG(salary) as avg_salary 
FROM employee 
GROUP BY dept_id 
HAVING AVG(salary) > 6000000; 
-- 평균 연봉이 6000000 이상인 부서만 조회
```

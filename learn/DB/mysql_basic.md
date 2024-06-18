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
CREATE SCHEMA company; -- 동일하게 작동
```

- i.g. PostgreSQL 에서는 SCHEMA가 DATABASE의 namespace 를 의미

## IT 회사 RDB 만들기(table 정의)

# create table

### DEPARTMENT table 생성

```sql
CREATE TABLE DEPARTMENT(
    id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    leader_id INT
);
```

> 이름, 데이터 타입, 옵션(키, nul 유무…)

### EMPLOYEE table 생성

```sql
CREATE TABLE EMPLOYEE(
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    birth_date DATE,
    sex CHAR(1) CHECK (sex IN ('M', 'F')),
    position VARCHAR(10),
    salary INT DEFAULT 5000000,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CHECK (salary >= 5000000)
);
```

### PROJECT table 생성

```sql
CREATE TABLE PROJECT(
    id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    leader_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (leader_id) REFERENCES EMPLOYEE(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CHECK (start_date < end_date)
);
```

### WORKS_ON table 생성

```sql
CREATE TABLE WORKS_ON(
    empl_id INT,
    proj_id INT,
    PRIMARY KEY (empl_id, proj_id),
    FOREIGN KEY (empl_id) REFERENCES EMPLOYEE(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (proj_id) REFERENCES PROJECT(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

# ALTER TABLE

> table의 schema를 변경하고 싶을 때 사용

### DEPARTMENT table에 leader_id FK 지정

```sql
ALTER TABLE DEPARTMENT ADD FOREIGN KEY (leader_id)
    REFERENCES EMPLOYEE(id)
    ON UPDATE CASCADE
    ON DELETE SET NULL;
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
CREATE TABLE TEST(
    age INT CONSTRAINT age_over_20 CHECK (age > 20)
);
```

- 만약 age에 15라는 값을 넣으면( 에러 )
- “CONSTRAINT age_over_20” 라고 이름을 붙였을 때
  - Check constraint ‘age_over_20’ is violated.
- 아무런 이름을 안 넣었을 때,
  - Check constraint ‘test_chk_1’ is violated.

```sql
SHOW CREATE TABLE TEST; -- 에러난 페이지 확인
```




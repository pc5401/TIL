# 고급 SQL 기능 및 트랜잭션

## JOIN

### INNER JOIN

- 두 테이블에서 조건에 맞는 데이터만 조회한다.

```sql
SELECT e.id, e.name, d.name as department_name 
FROM employee e INNER JOIN department d 
ON e.dept_id = d.id;
```

### LEFT JOIN (LEFT OUTER JOIN)

- 왼쪽 테이블의 모든 데이터를 조회하고, 오른쪽 테이블에서 조건에 맞는 데이터만 조회한다.
- 오른쪽 테이블에 조건에 맞는 데이터가 없는 경우, null로 표시된다.

```sql
SELECT e.id, e.name, d.name as department_name 
FROM employee e LEFT JOIN department d 
ON e.dept_id = d.id;
```

### RIGHT JOIN (RIGHT OUTER JOIN)

- 오른쪽 테이블의 모든 데이터를 조회하고, 왼쪽 테이블에서 조건에 맞는 데이터만 조회한다.
- 왼쪽 테이블에 조건에 맞는 데이터가 없는 경우, null로 표시된다.

```sql
SELECT e.id, e.name, d.name as department_name 
FROM employee e RIGHT JOIN department d 
ON e.dept_id = d.id;
```

### FULL JOIN (FULL OUTER JOIN)

- 두 테이블의 모든 데이터를 조회하고, 조건에 맞는 데이터만 서로 매칭한다.
- 조건에 맞는 데이터가 없는 경우, null로 표시된다.
- MySQL에서는 FULL OUTER JOIN을 지원하지 않는다. 대신 LEFT JOIN과 RIGHT JOIN을 조합하여 사용한다.

```sql
SELECT e.id, e.name, d.name as department_name 
FROM employee e LEFT JOIN department d 
ON e.dept_id = d.id 
UNION SELECT e.id, e.name, d.name as department_name 
FROM employee e RIGHT JOIN department d 
ON e.dept_id = d.id;
```

## 윈도우 함수 (Window Functions)

### 기본 개념

- 집계 함수와 달리, 윈도우 함수는 각 튜플에 대해 결과를 반환한다.
- 윈도우 함수는 OVER 절을 사용하여 윈도우를 정의한다.

### ROW_NUMBER()

- 각 그룹 내에서 행 번호를 매긴다.

```sql
SELECT name, salary, ROW_NUMBER() 
OVER (PARTITION BY dept_id ORDER BY salary DESC) as row_num 
FROM employee;
```

### RANK()

- 각 그룹 내에서 순위를 매긴다. 동점자가 있을 경우, 같은 순위를 부여하고 다음 순위는 건너뛴다.

```sql
SELECT name, salary, RANK() 
OVER (PARTITION BY dept_id ORDER BY salary DESC) as rank 
FROM employee;
```

### DENSE_RANK()

- 각 그룹 내에서 순위를 매긴다. 동점자가 있을 경우, 같은 순위를 부여하지만 다음 순위를 건너뛰지 않는다.

```sql
SELECT name, salary, DENSE_RANK() 
OVER (PARTITION BY dept_id ORDER BY salary DESC) as dense_rank 
FROM employee;
```

### NTILE(n)

- 각 그룹을 n개의 버킷으로 나눈다.

```sql
SELECT name, salary, NTILE(4) 
OVER (PARTITION BY dept_id ORDER BY salary DESC) as quartile 
FROM employee;
```

### LAG()와 LEAD()

- LAG()는 이전 행의 값을 가져온다.
- LEAD()는 다음 행의 값을 가져온다.

```sql
SELECT name, salary, LAG(salary, 1) 
OVER (PARTITION BY dept_id ORDER BY salary) as prev_salary, LEAD(salary, 1) 
OVER (PARTITION BY dept_id ORDER BY salary) as next_salary 
FROM employee;
```

### CUME_DIST()와 PERCENT_RANK()

- CUME_DIST()는 누적 분포를 계산한다.
- PERCENT_RANK()는 백분위 순위를 계산한다.

```sql
SELECT name, salary, CUME_DIST() 
OVER (PARTITION BY dept_id ORDER BY salary) as cume_dist, 
PERCENT_RANK() OVER (PARTITION BY dept_id ORDER BY salary) as percent_rank 
FROM employee;
```

## 트랜잭션 (Transactions)

### 기본 개념

- 트랜잭션은 데이터베이스에서의 일련의 작업들을 하나의 논리적인 단위로 묶은 것이다.
- 트랜잭션은 ACID 특성을 가져야 한다.
  - Atomicity (원자성)
  - Consistency (일관성)
  - Isolation (고립성)
  - Durability (지속성)

### 트랜잭션 제어 구문

#### 시작

```sql
START TRANSACTION;
```

#### 커밋 (Commit)

- 트랜잭션 내의 모든 작업을 영구적으로 반영한다.

```sql
COMMIT;
```

#### 롤백 (Rollback)

- 트랜잭션 내의 모든 작업을 취소한다.

```sql
ROLLBACK;
```

#### 저장점 (Savepoint)

- 트랜잭션 내에서 특정 시점으로 롤백할 수 있도록 저장점을 설정한다.

```sql
SAVEPOINT savepoint_name;
```

#### 저장점으로 롤백

```sql
ROLLBACK TO savepoint_name;
```

#### 저장점 해제

```sql
RELEASE SAVEPOINT savepoint_name;
```

### 트랜잭션 격리 수준 (Transaction Isolation Levels)

- 트랜잭션 격리 수준은 동시에 여러 트랜잭션이 실행될 때 일관성 있는 결과를 유지하기 위한 메커니즘이다.

#### READ UNCOMMITTED

- 커밋되지 않은 데이터를 읽을 수 있다.

```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
```

#### READ COMMITTED

- 커밋된 데이터만 읽을 수 있다.

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

#### REPEATABLE READ

- 트랜잭션이 시작된 후, 동일한 데이터를 읽을 때 항상 같은 값을 반환한다.

```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

#### SERIALIZABLE

- 가장 높은 격리 수준으로, 트랜잭션이 순차적으로 실행되는 것처럼 동작한다.

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

## 인덱스 (Indexes)

### 기본 개념

- 인덱스는 테이블에서 특정 컬럼의 값을 빠르게 찾을 수 있도록 도와준다.
- 인덱스를 사용하면 조회 속도가 빨라지지만, 삽입, 삭제, 갱신 시 성능이 저하될 수 있다.

#### 인덱스 생성

```sql
CREATE INDEX idx_name ON table_name(column_name);
```

#### 유니크 인덱스 생성

```sql
CREATE UNIQUE INDEX idx_name ON table_name(column_name);
```

#### 인덱스 삭제

```sql
DROP INDEX idx_name ON table_name;
```

#### 인덱스 조회

```sql
SHOW INDEXES FROM table_name;
```

## 뷰 (Views)

### 기본 개념

- 뷰는 하나 이상의 테이블에서 유도된 가상 테이블이다.
- 뷰를 사용하면 복잡한 쿼리를 단순화하고, 데이터 보안을 강화할 수 있다.

### 뷰 생성

```sql
CREATE VIEW view_name AS 
SELECT column1, column2 
FROM table_name 
WHERE condition;
```

### 뷰 조회

```sql
SELECT * FROM view_name;
```

### 뷰 삭제

```sql
DROP VIEW view_name;
```

## 스토어드 프로시저 (Stored Procedures)

### 기본 개념

- 스토어드 프로시저는 미리 컴파일된 SQL 쿼리 집합으로, 데이터베이스 내에서 실행된다.
- 프로시저를 사용하면 복잡한 작업을 수행할 수 있으며, 코드의 재사용성을 높일 수 있다.

### 프로시저 생성

```sql
CREATE PROCEDURE procedure_name(IN param1 datatype, OUT param2 datatype) 
BEGIN 
    -- SQL 구문 
    SELECT column1 INTO param2 
    FROM table_name 
    WHERE column2 = param1; 
END;
```

### 프로시저 호출

```sql
CALL procedure_name(param1, @param2); 
SELECT @param2;
```

### 프로시저 삭제

```sql
DROP PROCEDURE procedure_name;
```

## 트리거 (Triggers)

### 기본 개념

- 트리거는 특정 이벤트가 발생할 때 자동으로 실행되는 저장된 프로시저이다.
- 트리거는 데이터 무결성을 유지하는 데 유용하다.

### 트리거 생성

```sql
CREATE TRIGGER trigger_name BEFORE 
INSERT ON table_name 
FOR EACH ROW BEGIN 
-- SQL 구문 END;
```

### 트리거 삭제

```sql
DROP TRIGGER trigger_name;
```

### 트리거 예제

```sql
CREATE TRIGGER before_employee_insert 
BEFORE INSERT ON employee 
FOR EACH ROW 
BEGIN 
    IF NEW.salary < 5000000 THEN 
        SET NEW.salary = 5000000; 
    END IF; 
END;
```
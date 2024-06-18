# MySQL 조회 및 집계 함수

## 기본 SELECT

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
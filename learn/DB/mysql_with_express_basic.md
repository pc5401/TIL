# Express와 MySQL

## 기본 설정

#### 1. MySQL 클라이언트 선택

Express에서 MySQL을 사용하려면 MySQL 클라이언트 패키지가 필요하다. 두 가지 주요 패키지가 있는데, **`mysql`**과 **`mysql2`**이다. (당연히 2가 더 좋다)

##### 1.1 `mysql`과 `mysql2`의 차이점

- `mysql2`는 성능 면에서 더 최적화되어 있고, **Promise**를 기본적으로 지원한다. 특히 비동기 처리를 더 깔끔하게 할 수 있다. `mysql`은 기본적으로 콜백 기반이기 때문에, `async/await`을 쓰고 싶다면 `mysql2`가 더 나은 선택이다.
- 두 패키지 모두 MySQL 쿼리 실행에 큰 차이는 없지만, 향후 유지보수와 성능 측면에서 `mysql2`가 유리하다. 그래서 `mysql2`를 사용하는 것이 좋다.

##### 1.2 설치 방법

```bash
npm install mysql2
```

#### 2. MySQL과의 연결 설정

Express에서 MySQL과 연결하는 방법에는 **단일 연결**과 **Connection Pool** 두 가지 방법이 있다. Connection Pool을 설정하는 게 여러 요청을 처리할 때 더 효율적이니, 기본적으로 이 방식을 사용하자.

##### 2.1 단일 연결 설정

단일 연결 방식은 간단하지만, 여러 요청을 동시에 처리하기에는 적합하지 않다. 작은 프로젝트나 테스트용으로는 괜찮다.

```javascript
const mysql = require('mysql2');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'test_db'
});

connection.connect((err) => {
  if (err) {
    console.error('MySQL 연결 실패:', err);
    return;
  }
  console.log('MySQL 연결 성공');
});
```

##### 2.2 Connection Pool 설정

Connection Pool을 사용하면 여러 개의 연결을 미리 만들어 놓고, 요청마다 연결을 재사용할 수 있다. 성능이 중요한 애플리케이션에서는 이 방식을 쓰는 게 좋다.

```javascript
const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'test_db'
});

// 연결 요청 및 쿼리 실행
pool.getConnection((err, connection) => {
  if (err) throw err;
  connection.query('SELECT 1 + 1 AS solution', (error, results) => {
    connection.release();  // 사용 후 연결 해제
    if (error) throw error;
    console.log('쿼리 결과:', results[0].solution);
  });
});
```

#### 3. Express에서 MySQL과 연결

Express와 MySQL을 통합하려면, 먼저 MySQL과 연결을 설정한 후에 쿼리를 실행할 수 있다. 아래는 간단한 Express 앱에서 MySQL과 연결해 데이터를 가져오는 방법이다.

##### 연결 예제

```javascript
const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'test_db'
});

// 연결 요청 및 쿼리 실행
pool.getConnection((err, connection) => {
  if (err) throw err;
  connection.query('SELECT 1 + 1 AS solution', (error, results) => {
    connection.release();  // 사용 후 연결 해제
    if (error) throw error;
    console.log('쿼리 결과:', results[0].solution);
  });
});
```

#### 3. Express에서 MySQL과 연결

Express와 MySQL을 통합하려면, 먼저 MySQL과 연결을 설정한 후에 쿼리를 실행할 수 있다. 아래는 간단한 Express 앱에서 MySQL과 연결해 데이터를 가져오는 방법이다.

##### 연결 예제

```javascript
const express = require('express');
const mysql = require('mysql2');
const app = express();

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'test_db'
});

connection.connect();

app.get('/', (req, res) => {
  connection.query('SELECT * FROM users', (error, results) => {
    if (error) throw error;
    res.json(results);
  });
});

app.listen(3000, () => {
  console.log('서버가 3000번 포트에서 실행 중입니다.');
});
```



이 코드를 실행하면, `/` 경로로 GET 요청을 보내 MySQL의 `users` 테이블 데이터를 조회할 수 있다.

#### 4. MySQL 쿼리 처리

##### 4.1 콜백 기반 쿼리 실행

`db.query`를 통해 SQL 쿼리를 실행한다. 콜백 기반으로 결과를 처리하며, 에러가 발생하면 에러 핸들링을 해주는 것이 중요하다.

```javascript
const sql = 'SELECT * FROM users';
connection.query(sql, (error, results) => {
  if (error) {
    console.error('쿼리 실행 중 오류 발생:', error);
    return;
  }
  console.log('결과:', results);
});
```

##### 4.2 에러 처리 패턴

쿼리 실행 중 에러가 발생할 수 있다. 에러 발생 시 로그를 남기고, 적절하게 클라이언트에게 에러를 반환해야 한다.

```javascript
const sql = 'SELECT * FROM users';
connection.query(sql, (error, results) => {
  if (error) {
    console.error('쿼리 실행 중 오류 발생:', error);
    return;
  }
  console.log('결과:', results);
});
```

##### 4.3 SQL 인젝션 예방을 위한 Prepared Statements

사용자 입력을 SQL에 직접 삽입하면 위험할 수 있다. 이럴 때 Prepared Statements를 사용해서 SQL 인젝션을 방지한다. 플레이스홀더(`?`)를 사용해 값을 바인딩하면 안전하다.

```javascript
const userId = 1;
const sql = 'SELECT * FROM users WHERE id = ?';
connection.query(sql, [userId], (error, results) => {
  if (error) throw error;
  console.log(results);
});
```

Prepared Statements를 사용하면 SQL 인젝션을 걱정할 필요가 없으니, 사용자 입력이 포함된 쿼리에서는 반드시 이 방식을 사용해야 한다.

---

### 마무리

이렇게 하면 Express와 MySQL을 기본적으로 연동하고, 데이터를 조회하고, 쿼리 실행 시 발생할 수 있다. 끝!



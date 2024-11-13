# 로그인 방법에 대한 이야기

웹 개발을 하다 보면 **사용자 인증**은 빼놓을 수 없는 중요한 부분이다. 오늘은 예전에 정리했던 **세션 기반 인증**과 **JWT 기반 인증**에 대해 좀 더 자연스럽게 이야기해보려고 한다. 또한 알아두면 좋을 추가적인 예시들도 함께 살펴보겠다.

## 목차

- [세션 기반 인증](#세션-기반-인증)
- [JWT 기반 인증](#jwt-json-web-token-기반-인증)
- [세션과 JWT의 비교](#세션과-jwt의-비교)
- [어떤 방식을 선택해야 할까?](#어떤-방식을-선택해야-할까)
- [마무리하며](#마무리하며)

---

## 세션 기반 인증

**세션 기반 인증**은 웹 애플리케이션에서 사용자의 로그인 상태를 유지하는 전통적인 방법이다. 사용자가 로그인하면 서버는 고유한 세션을 생성하고, 이후의 요청을 이 세션을 통해 인증한다. 세션 정보는 서버 측에 저장되고, 클라이언트는 브라우저의 쿠키를 통해 세션 ID를 보관한다.

### 기본 작동 원리

1. **로그인 요청**: 사용자가 아이디와 비밀번호를 입력하고 로그인하면, 서버는 이를 검증한 후 고유한 세션을 생성한다. 이 세션은 서버의 메모리나 데이터베이스에 저장된다.
2. **세션 ID 전달**: 서버는 생성된 세션 ID를 클라이언트에게 **쿠키**로 전달한다. 이때 쿠키는 `HttpOnly` 속성이 적용되어 있어 자바스크립트로 접근할 수 없도록 보호된다.
3. **요청 시 세션 확인**: 사용자가 이후 요청을 보낼 때마다 브라우저는 쿠키에 저장된 세션 ID를 서버에 전송한다.
4. **인증 상태 확인**: 서버는 세션 ID를 기반으로 세션 데이터를 조회해 사용자의 로그인 상태를 확인하고 요청을 처리한다.

### CS 원리와 보안 고려사항

- **세션 하이재킹 방지**: 세션 ID가 탈취되면 공격자가 사용자로 가장할 수 있으므로, HTTPS를 사용해 통신을 암호화해야 한다.
- **세션 고정 공격 방지**: 로그인할 때마다 새로운 세션 ID를 발급하여 이전 세션 ID를 무효화해야 한다.
- **세션 만료 설정**: 세션의 유효 기간을 설정해 일정 시간 동안 활동이 없으면 자동으로 로그아웃되도록 한다.

### Express.js에서의 세션 기반 인증

Express.js에서는 `express-session` 미들웨어를 사용해 세션을 관리할 수 있다.

### 설치 및 기본 설정

```bash
npm install express-session
```

```jsx
const express = require('express');
const session = require('express-session');
const app = express();

app.use(session({
  secret: 'your_secret_key', // 세션 암호화에 사용되는 비밀 키
  resave: false,             // 세션이 수정되지 않아도 다시 저장할지 여부
  saveUninitialized: false,  // 초기화되지 않은 세션을 저장할지 여부
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 // 쿠키 유효 기간 (1일)
  }
}));
```

### 로그인 처리 예시

```jsx
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // 실제로는 데이터베이스에서 사용자 인증 처리
  if (username === 'user' && password === 'pass') {
    req.session.user = { username };
    res.send('로그인 성공');
  } else {
    res.send('로그인 실패');
  }
});
```

### 인증된 사용자만 접근 가능한 라우트

```jsx
app.get('/dashboard', (req, res) => {
  if (req.session.user) {
    res.send(`환영합니다, ${req.session.user.username}님!`);
  } else {
    res.send('로그인이 필요합니다.');
  }
});
```

### 로그아웃 처리

```jsx
app.post('/logout', (req, res) => {
  req.session.destroy(err => {
    if (err) {
      res.send('로그아웃 실패');
    } else {
      res.clearCookie('connect.sid'); // 세션 쿠키 삭제
      res.send('로그아웃 성공');
    }
  });
});
```

### 세션 관리에 대한 추가 팁

- **세션 저장소 선택**: 기본적으로 세션은 서버의 메모리에 저장되지만, 사용자 수가 많아지면 메모리 사용량이 증가한다. 이때는 **Redis**나 **MongoDB** 같은 외부 저장소를 세션 스토어로 사용하는 것이 좋다.

### Redis를 이용한 세션 저장

```bash
npm install connect-redis redis
```

```jsx
const RedisStore = require('connect-redis')(session);
const redis = require('redis');
const redisClient = redis.createClient();

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: 'your_secret_key',
  resave: false,
  saveUninitialized: false,
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 // 1일
  }
}));
```

- **보안 강화**: 세션 하이재킹을 방지하기 위해 **HTTPS**를 사용하고, 세션 ID를 자주 변경하는 것도 좋다.

```jsx
req.session.regenerate(err => {
  if (err) {
    res.send('세션 재생성 실패');
  } else {
    req.session.user = { username };
    res.send('로그인 성공');
  }
});
```

### 장점과 단점

### 장점

- **간단한 구현**: 서버가 상태를 관리하므로 클라이언트에서 복잡한 처리가 필요 없다.
- **보안성**: 서버에서 세션을 관리하므로 로그아웃 시 즉시 세션을 무효화할 수 있다.
- **세밀한 제어**: 세션 데이터를 서버에서 직접 관리하므로 사용자 상태를 세밀하게 제어할 수 있다.

### 단점

- **서버 부하**: 많은 사용자가 접속하면 서버 메모리나 저장소에 부담이 된다.
- **확장성 문제**: 여러 대의 서버를 사용할 경우 세션 공유가 필요하다.
- **쿠키 의존성**: 클라이언트에서 쿠키를 차단하면 세션 관리가 어려워진다.

---

## JWT (JSON Web Token) 기반 인증

**JWT**는 서버가 상태를 유지하지 않는 **무상태(stateless)** 인증 방법이다. 사용자가 로그인하면 서버는 JWT를 생성해 클라이언트에게 전달하고, 클라이언트는 이 토큰을 저장해 두었다가 이후의 요청 시마다 토큰을 전송한다.

### 기본 작동 원리

1. **로그인 요청**: 사용자가 아이디와 비밀번호로 로그인하면, 서버는 이를 검증한 후 JWT를 생성한다.
2. **토큰 저장**: 클라이언트는 이 JWT를 **로컬 스토리지**나 **쿠키**에 저장한다.
3. **요청 시 토큰 전송**: 클라이언트는 이후 요청 시마다 이 토큰을 HTTP 헤더에 포함해 서버에 전송한다.
4. **토큰 검증**: 서버는 받은 토큰의 유효성을 검증하고, 필요한 경우 요청을 처리한다.

### JWT의 구성 요소

JWT는 마침표(`.`)로 구분된 세 부분으로 이루어져 있다.

1. **Header**: 토큰의 타입과 해싱 알고리즘 정보
2. **Payload**: 토큰에 담길 데이터(클레임)
3. **Signature**: 토큰의 무결성을 검증하기 위한 서명

예시:

```css
header.payload.signature
```

### CS 원리와 보안 고려사항

- **무상태성**: 서버가 상태를 유지하지 않으므로 확장성이 높다.
- **토큰 변조 방지**: 서명(Signature)을 통해 토큰의 무결성을 검증한다.
- **토큰 탈취 위험**: 토큰이 탈취되면 유효 기간 동안 악용될 수 있으므로, 토큰의 유효 기간을 짧게 설정하고 HTTPS를 사용해야 한다.

### Express.js에서의 JWT 기반 인증

### 설치 및 기본 설정

```bash
npm install jsonwebtoken
```

```jsx
const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();

const secretKey = 'your_secret_key';
```

### 로그인 처리 및 토큰 발급

```jsx
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // 실제로는 데이터베이스에서 사용자 인증 처리
  if (username === 'user' && password === 'pass') {
    const token = jwt.sign({ username }, secretKey, { expiresIn: '1h' });
    res.json({ token });
  } else {
    res.send('로그인 실패');
  }
});
```

### 토큰 검증 미들웨어

```jsx
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // Bearer 토큰일 경우

  if (!token) return res.sendStatus(401);

  jwt.verify(token, secretKey, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}
```

### 인증된 사용자만 접근 가능한 라우트

```jsx
app.get('/dashboard', authenticateToken, (req, res) => {
  res.send(`환영합니다, ${req.user.username}님!`);
});
```

### 리프레시 토큰과 액세스 토큰

액세스 토큰의 유효 기간을 짧게 설정하고, **리프레시 토큰**을 사용해 새로운 액세스 토큰을 발급받을 수 있다.

### 리프레시 토큰 발급

```jsx
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (username === 'user' && password === 'pass') {
    const accessToken = jwt.sign({ username }, secretKey, { expiresIn: '15m' });
    const refreshToken = jwt.sign({ username }, secretKey, { expiresIn: '7d' });
    res.json({ accessToken, refreshToken });
  } else {
    res.send('로그인 실패');
  }
});
```

### 액세스 토큰 재발급

```jsx
app.post('/token', (req, res) => {
  const { refreshToken } = req.body;

  if (!refreshToken) return res.sendStatus(401);

  jwt.verify(refreshToken, secretKey, (err, user) => {
    if (err) return res.sendStatus(403);
    const accessToken = jwt.sign({ username: user.username }, secretKey, { expiresIn: '15m' });
    res.json({ accessToken });
  });
});
```

### JWT 사용 시 고려사항

- **토큰 저장 위치**: 토큰을 로컬 스토리지에 저장하면 XSS 공격에 취약하다. 따라서 **HttpOnly 쿠키**에 저장하는 것이 더 안전하다.
- **보안 강화**: **HTTPS**를 사용해 토큰 전송 시 암호화하고, 토큰 탈취에 대비해 토큰의 유효 기간을 짧게 설정한다.
- **CSRF 방지**: 토큰을 쿠키에 저장할 경우 CSRF 공격에 노출될 수 있으므로 추가적인 방어 기법이 필요하다.

### 장점과 단점

### 장점

- **무상태성**: 서버가 상태를 유지하지 않아 확장성이 높다.
- **유연성**: 여러 도메인이나 모바일 앱에서 동일한 토큰을 사용할 수 있다.
- **보안성**: 토큰의 변조를 방지할 수 있다.

### 단점

- **토큰 탈취 위험**: 토큰이 탈취되면 만료될 때까지 악용될 수 있다.
- **로그아웃 처리 어려움**: 서버에서 토큰을 즉시 무효화하기 어렵다.
- **토큰 크기**: 토큰의 크기가 커질 수 있어 네트워크 비용이 증가한다.

---

## 세션과 JWT의 비교

| 특징 | 세션 기반 인증 | JWT 기반 인증 |
| --- | --- | --- |
| **상태 관리** | 서버가 상태를 유지 | 서버는 무상태 |
| **확장성** | 서버 간 세션 공유 필요 | 확장성이 높음 |
| **보안** | 세션 ID 탈취 시 위험 | 토큰 변조 방지 가능 |
| **저장 위치** | 세션 ID는 쿠키에 저장 | 토큰은 클라이언트에 저장 |
| **로그아웃 처리** | 즉시 세션 무효화 가능 | 토큰 만료 시까지 유효 |
| **서버 부하** | 서버 메모리 사용 | 서버 부하 적음 |

---

## 어떤 방식을 선택해야 할까?

- **세션 기반 인증**은 서버가 사용자 상태를 관리하기 때문에 로그아웃 처리나 세션 만료 등이 용이하다. 하지만 서버 자원을 사용하고, 여러 대의 서버를 운영할 때 세션 공유 문제가 발생할 수 있다.
- **JWT 기반 인증**은 서버가 상태를 유지하지 않아도 되어 확장성이 뛰어나다. 하지만 토큰이 탈취되면 유효 기간 동안 악용될 수 있어 보안에 신경 써야 한다.

### 선택 팁

- **작은 규모의 애플리케이션**: 세션 기반 인증이 관리하기 쉽다.
- **마이크로서비스나 모바일 앱**: JWT 기반 인증이 적합하다.
- **보안이 최우선일 때**: 세션 기반 인증이 더 안전할 수 있다.
- **API 서버**: JWT를 사용하면 클라이언트 간에 인증 상태를 쉽게 공유할 수 있다.

---

## 마무리하며

인증 방식은 애플리케이션의 특성과 요구 사항에 따라 선택해야 한다. 두 방식 모두 장단점이 있으니, 프로젝트에 가장 알맞은 방법을 선택하는 것이 중요하다. 앞으로 실제로 적용해 보면서 더 깊이 있는 이해를 쌓아가면 좋을 것 같다.
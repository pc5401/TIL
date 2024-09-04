# 로그인 방법

## 세션 기반 인증

**세션 기반 인증**은 웹 애플리케이션에서 사용자의 로그인 상태를 유지하는 전통적이면서도 널리 사용되는 방식이다. 이 방식은 사용자가 로그인하면 서버가 고유한 세션을 생성하고, 이후 요청들을 인증하는 방식으로 작동한다. 세션은 서버 측에 저장되고, 클라이언트는 브라우저의 쿠키를 통해 세션 ID를 저장하며, 이를 통해 서버와 통신한다.

### **기본 작동 원리**

1. 사용자가 로그인 폼에 아이디와 비밀번호를 입력하면, 서버는 이를 검증한 후 고유한 세션을 생성한다. 이 세션은 보통 서버의 메모리나 데이터베이스에 저장된다.
2. 서버는 생성된 세션 ID를 클라이언트에 **쿠키**로 전달한다. 이때 쿠키는 `HttpOnly` 속성이 적용되어 있어 자바스크립트를 통해 접근할 수 없도록 보호된다.
3. 사용자가 이후 요청을 보낼 때, 브라우저는 세션 ID를 쿠키에 담아 서버에 전송한다.
4. 서버는 세션 ID를 기반으로 세션 데이터를 조회해 사용자의 로그인 상태를 확인하고 요청을 처리한다.

### **Express.js에서 세션 기반 인증의 작동 원리**

Express.js에서 세션 기반 인증을 구현하려면 `express-session` 미들웨어를 사용하여 세션을 관리할 수 있다. 일반적인 흐름은 다음과 같다:

1. 사용자가 로그인 요청을 보내면 서버는 사용자의 자격 증명을 확인하고, 자격 증명이 유효하면 세션을 생성한다.
2. 서버는 생성된 세션 ID를 클라이언트에게 **쿠키**로 전달한다. 클라이언트는 이 쿠키를 브라우저에 저장한다.
3. 사용자가 다음 요청을 보낼 때, 브라우저는 세션 ID를 포함한 쿠키를 서버로 전송한다.
4. 서버는 세션 ID를 확인하여 사용자의 인증 상태를 확인하고 요청을 처리한다.

### **세션의 관리**

세션은 서버가 관리하는 데이터로, 사용자가 로그인하면 서버에 세션이 생성되고 사용자가 로그아웃하거나 세션이 만료될 때 삭제된다. 일반적으로 세션은 일정 시간 동안 유효하며, 이 시간을 **세션 타임아웃**이라 한다. 타임아웃이 지나면 사용자는 자동으로 로그아웃되고, 다시 로그인을 시도해야 한다.

서버는 세션을 메모리, 파일 시스템, 또는 데이터베이스에 저장할 수 있다. 또한 분산 서버 환경에서 세션 데이터를 여러 서버 간에 공유해야 하는 경우가 많아, **Redis**와 같은 외부 저장소를 사용하여 중앙에서 세션을 관리하는 방식이 유용하다.

### **Express.js에서의 세션 설정**

Express.js에서 세션을 사용하려면 `express-session` 모듈을 설치하고 설정해야 한다.

```bash
npm install express-session
```

### 기본 세션 설정 코드

```jsx
const express = require('express');
const session = require('express-session');
const app = express();

// 세션 미들웨어 설정
app.use(session({
  secret: 'your_secret_key',   // 세션 암호화에 사용되는 비밀 키
  resave: false,               // 세션을 항상 저장할지 여부 (변경되지 않아도 저장)
  saveUninitialized: true,     // 초기화되지 않은 세션도 저장할지 여부
  cookie: {
    maxAge: 60000              // 쿠키의 유효 시간 (밀리초 단위)
  }
}));

// 로그인 요청 처리
app.post('/login', (req, res) => {
  // 사용자 인증 로직 (예: DB 조회 등)
  const username = req.body.username;
  const password = req.body.password;

  if (username === 'user' && password === 'pass') {
    // 세션에 사용자 정보 저장
    req.session.user = { username: 'user' };
    res.send('로그인 성공');
  } else {
    res.send('로그인 실패');
  }
});

// 인증된 사용자만 접근 가능
app.get('/dashboard', (req, res) => {
  if (req.session.user) {
    res.send(`환영합니다, ${req.session.user.username}님!`);
  } else {
    res.send('로그인이 필요합니다.');
  }
});

// 로그아웃 처리
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.send('로그아웃 실패');
    }
    res.clearCookie('connect.sid');  // 세션 쿠키 삭제
    res.send('로그아웃 성공');
  });
});

app.listen(3000, () => {
  console.log('서버가 3000번 포트에서 실행 중입니다.');
});
```

### **쿠키와 세션 ID의 관계**

- Express.js에서 `express-session` 미들웨어를 사용하면 서버는 `Set-Cookie` 헤더를 통해 세션 ID를 클라이언트에 전달한다. 이 쿠키는 브라우저에 저장되며, 사용자가 서버에 요청을 보낼 때마다 자동으로 세션 ID를 포함하여 전송된다.
- 기본적으로 Express.js는 `connect.sid`라는 이름으로 세션 쿠키를 설정한다.

### `Set-Cookie` 예시

로그인 성공 후, 서버가 클라이언트에 응답할 때 HTTP 헤더에 `Set-Cookie`를 포함하여 세션 ID를 전달한다.

```
Set-Cookie: connect.sid=s%3AAbCdEfGh1234567890; Path=/; Expires=Sun, 25 Oct 2020 07:28:00 GMT; HttpOnly
```

- `connect.sid`: Express.js에서 생성된 세션 ID.
- `Path`: 쿠키가 적용되는 경로.
- `Expires`: 쿠키의 만료 시간.
- `HttpOnly`: 자바스크립트로 쿠키에 접근할 수 없도록 설정.

### **세션 데이터 관리**

- 세션 데이터는 서버에 저장되며, 서버는 세션 ID를 통해 데이터를 조회한다. 기본적으로 `express-session`은 서버 메모리에 세션을 저장하지만, 이 방식은 확장성 문제를 일으킬 수 있다. 따라서 외부 세션 스토어를 사용하는 것이 권장된다.

### 세션 스토어 사용 예시 (Redis)

```bash
npm install connect-redis redis
```

```jsx
javascript코드 복사
const RedisStore = require('connect-redis')(session);
const redis = require('redis');
const redisClient = redis.createClient();

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: 'your_secret_key',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 60000 }
}));
```

이 방식은 Redis와 같은 외부 스토리지를 사용해 세션 데이터를 관리할 수 있어, 대규모 애플리케이션에서도 확장성을 제공한다.

### **보안 고려 사항**

세션 기반 인증을 구현할 때 보안을 강화하는 몇 가지 방법이 있다:

- **HTTPS 사용**: 세션 ID가 HTTP를 통해 암호화되지 않은 채로 전송되면 공격자가 이를 쉽게 가로챌 수 있으므로, 반드시 HTTPS를 사용해 통신을 암호화해야 한다.
- **세션 고정 공격 방지**: 사용자가 로그인할 때마다 새로운 세션 ID를 발급해야 한다. 이를 통해 공격자가 기존 세션 ID를 알고 있어도 새로운 로그인 시 새로운 세션 ID가 부여되어 보안이 유지된다.

```jsx
req.session.regenerate((err) => {
  if (err) {
    return res.send('세션 재생성 실패');
  }
  // 새로운 세션이 만들어짐
  req.session.user = { username: 'user' };
  res.send('로그인 성공');
});
```

- **세션 타임아웃**: 세션이 너무 오래 유지되면 보안 위험이 증가할 수 있으므로, 적절한 만료 시간을 설정하는 것이 중요하다. 예를 들어, 사용자가 일정 시간 동안 활동하지 않으면 세션을 만료시키는 방식이다.

```jsx
app.use(session({
  secret: 'your_secret_key',
  resave: false,
  saveUninitialized: true,
  cookie: {
    maxAge: 300000,  // 5분 동안 활동이 없으면 세션 만료
    secure: true     // HTTPS에서만 쿠키 전송
  }
}));
```

### **장점**

- **간단함**: 서버가 사용자의 인증 상태를 관리하기 때문에 구현이 간단하고 클라이언트에서 복잡한 처리가 필요 없다.
- **보안성**: 서버에서 상태를 관리하므로, 로그아웃 시 서버에서 즉시 세션을 제거해 명확하게 인증을 해제할 수 있다.
- **확장성**: 외부 세션 스토어를 사용하면 대규모 서비스에서도 확장성을 유지할 수 있다.

### **단점**

- **서버 부하**: 세션을 서버에서 유지하므로 많은 사용자가 접속하는 대규모 시스템에서는 서버의 메모리나 저장소에 부하가 발생할 수 있다.
- **확장성 문제**: 여러 대의 서버가 분산된 환경에서는 세션 데이터가 일관되지 않을 수 있어, 이를 해결하기 위해 세션을 중앙 저장소에서 관리하거나 로드 밸런싱 설정을 세밀하게 해야 한다.
- **쿠키 의존성**: 세션 ID는 클라이언트 측 쿠키에 저장되므로, 쿠키 사용이 제한된 환경에서는 인증이 불가능할 수 있다.

### **사용 사례**

세션 기반 인증은 사용자 수가 적고 서버 리소스를 효율적으로 관리할 수 있는 중소형 웹 애플리케이션에 적합하다. 예를 들어 관리자 페이지, 쇼핑몰 등에서 사용자의 로그인 상태를 확실히 관리해야 하는 환경에서 유용하다.

### **결론**

세션 기반 인증은 Express.js에서 쉽게 구현할 수 있으며, 간단한 웹 애플리케이션에서 매우 유용하다. 확장성을 고려해 Redis와 같은 외부 세션 스토어를 사용하면 대규모 시스템에서도 안정적으로 동작할 수 있다.
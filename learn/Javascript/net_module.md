
# Node.js net 모듈 사용법과 서버, client 구현

## net 모듈 개요

Node.js의 `net` 모듈은 네트워크 관련 기능을 제공하며, 주로 TCP 및 IPC 소켓을 구현하는 데 사용된다. 이 모듈을 사용하여 네트워크 애플리케이션을 작성할 수 있다.

## TCP 클라이언트 예제

다음은 TCP 클라이언트를 구현한 코드 예제이다.

```javascript
// client.js

const net = require('net');

// 서버에 연결하는 클라이언트 소켓을 생성한다.
const client = net.connect({ port: 8107, host: 'localhost' }, () => {
    console.log('Client connected');
    // 서버로 메시지를 보낸다.
    client.write('Hello, Server');
});

// 서버로부터 데이터를 수신할 때마다 호출되는 이벤트 핸들러
client.on('data', (data) => {
    console.log('from 서버: ' + data.toString());
    // 서버로부터 데이터를 수신한 후 연결을 종료한다.
    client.end();
});

// 클라이언트 연결이 종료되었을 때 호출되는 이벤트 핸들러
client.on('end', () => {
    console.log('Client disconnected');
});

// 소켓 오류가 발생했을 때 호출되는 이벤트 핸들러
client.on('error', (err) => {
    console.log('Socket error: ' + err.message);
});
```

## TCP 서버 예제

다음은 TCP 서버를 구현한 코드 예제이다.

```javascript
// server.js

const net = require('net');

// 서버 객체를 생성한다.
const server = net.createServer((client) => {
    console.log('Client connected');

    // 클라이언트로부터 데이터를 수신할 때마다 호출되는 이벤트 핸들러
    client.on('data', (data) => {
        console.log('Received data from client: ' + data.toString());
        // 클라이언트로 응답을 보낸다.
        client.write('Hello, client!');
    });

    // 클라이언트 연결이 종료되었을 때 호출되는 이벤트 핸들러
    client.on('end', () => {
        console.log('Client disconnected');
    });

    // 소켓 오류가 발생했을 때 호출되는 이벤트 핸들러
    client.on('error', (err) => {
        console.log('Socket error: ' + err.message);
    });
});

// 서버를 특정 포트(8107)에서 수신하도록 설정한다.
server.listen(8107, () => {
    console.log('Server listening on port 8107');
});
```

## 코드 설명

### 클라이언트 코드 (client.js)

1. `net` 모듈을 불러온다.
2. `net.connect` 메서드를 사용하여 서버에 연결하는 클라이언트 소켓을 생성한다. 연결이 완료되면 "Client connected" 메시지를 출력하고, 서버로 "Hello, Server" 메시지를 보낸다.
3. 서버로부터 데이터를 수신할 때마다 `data` 이벤트가 발생하며, 수신한 데이터를 출력한 후 연결을 종료한다.
4. 클라이언트 연결이 종료되면 `end` 이벤트가 발생하여 "Client disconnected" 메시지를 출력한다.
5. 소켓 오류가 발생하면 `error` 이벤트가 발생하여 오류 메시지를 출력한다.

### 서버 코드 (server.js)

1. `net` 모듈을 불러온다.
2. `net.createServer` 메서드를 사용하여 서버 객체를 생성한다. 클라이언트가 연결되면 "Client connected" 메시지를 출력한다.
3. 클라이언트로부터 데이터를 수신할 때마다 `data` 이벤트가 발생하며, 수신한 데이터를 출력하고 클라이언트로 "Hello, client!" 메시지를 보낸다.
4. 클라이언트 연결이 종료되면 `end` 이벤트가 발생하여 "Client disconnected" 메시지를 출력한다.
5. 소켓 오류가 발생하면 `error` 이벤트가 발생하여 오류 메시지를 출력한다.
6. 서버를 8107 포트에서 수신하도록 설정하며, "Server listening on port 8107" 메시지를 출력한다.

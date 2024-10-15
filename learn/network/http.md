# HTTP 정리
> http를 쭉 정리를 해보기로 다짐함.

## 1. HTTP 소개

### 1.1 HTTP란?

- *HTTP (HyperText Transfer Protocol)**는 월드 와이드 웹(WWW)에서 클라이언트와 서버 간에 정보를 주고받기 위한 프로토콜이다. HTTP는 요청-응답(Request-Response) 모델을 기반으로 하며, 웹 브라우저(클라이언트)가 서버에 요청을 보내면 서버가 그에 대한 응답을 반환하는 방식으로 작동한다.
- **주요 특징:**
    - **비연결성 (Stateless):** 각 요청은 독립적으로 처리되고, 이전 요청의 상태를 유지하지 않는다.
    - **유연성:** 다양한 데이터 형식을 전송할 수 있으며, 텍스트, 이미지, 비디오 등 다양한 콘텐츠를 지원한다.
    - **확장성:** 헤더와 메서드를 확장하여 새로운 기능을 추가할 수 있다.
- **기본 동작 방식:**
    1. 클라이언트가 서버에 요청을 보낸다.
    2. 서버가 요청을 처리하고 응답을 반환한다.
    3. 연결이 종료되거나 유지됨 (HTTP/1.1부터 기본적으로 연결을 유지).

### 1.2 HTTP의 역사

HTTP는 웹의 발전과 함께 지속적으로 진화해왔다. 주요 버전과 그 특징은 다음과 같다.

### **HTTP/0.9**

- **출시 시기:** 1991년
- **특징:**
    - 단순한 프로토콜로, GET 요청만 지원한다.
    - 텍스트 기반의 단일 문서 전송.
    - 헤더와 상태 코드가 없다.
- **제한 사항:**
    - 기능이 매우 제한적이며, 현대적인 웹 요구사항을 충족하지 못한다.

### **HTTP/1.0**

- **출시 시기:** 1996년 (RFC 1945)
- **특징:**
    - 요청과 응답에 헤더가 추가된다.
    - 다양한 HTTP 메서드 지원 (GET, POST 등).
    - 상태 코드 도입 (200 OK, 404 Not Found 등).
    - 비연결성 유지: 각 요청마다 새로운 연결을 생성한다.
- **개선점:**
    - 콘텐츠 유형과 길이를 명시.
    - 캐싱 메커니즘 도입.

### **HTTP/1.1**

- **출시 시기:** 1997년 (RFC 2068), 1999년 (RFC 2616)
- **특징:**
    - 지속적인 연결 (Persistent Connections): 기본적으로 연결을 유지하여 여러 요청을 처리.
    - 파이프라이닝: 여러 요청을 동시에 보낼 수 있음 (하지만 널리 사용되지는 않음).
    - 추가적인 캐싱 헤더와 개선된 캐싱 메커니즘.
    - 호스트 헤더 도입으로 가상 호스팅 지원.
- **개선점:**
    - 네트워크 효율성 증가.
    - 다양한 최적화 기능 추가.

### **HTTP/2**

- **출시 시기:** 2015년 (RFC 7540)
- **특징:**
    - 이진 프로토콜: 텍스트 기반이 아닌 이진 형식으로 데이터 전송.
    - 다중화 (Multiplexing): 하나의 연결에서 여러 스트림을 동시에 처리.
    - 헤더 압축: 헤더 정보를 효율적으로 압축하여 전송.
    - 서버 푸시: 서버가 클라이언트의 요청 없이 리소스를 미리 전송.
- **개선점:**
    - 성능 향상: 페이지 로딩 속도 개선.
    - 네트워크 자원을 효율적으로 사용.

### **HTTP/3**

- **출시 시기:** 2022년 (RFC 9114)
- **특징:**
    - QUIC 프로토콜 기반: UDP 위에서 동작하여 지연 시간 감소.
    - 연결 설정 속도 향상: 0-RTT 핸드셰이크 지원.
    - 내장된 보안: TLS 1.3이 기본적으로 통합.
    - 패킷 손실에 대한 더 나은 처리.
- **개선점:**
    - 더욱 빠르고 안정적인 데이터 전송.
    - 모바일 및 실시간 애플리케이션에 적합.

### 1.3 클라이언트-서버 모델

HTTP는 **클라이언트-서버(Client-Server)** 아키텍처를 기반으로 동작한다. 이 모델은 네트워크 상에서 역할을 명확히 구분하여 효율적인 통신을 가능하게 한다.

### **클라이언트 (Client)**

- **역할:** 사용자 인터페이스를 제공하고, 서버에 요청을 보낸다.
- **예시:** 웹 브라우저 (Chrome, Firefox), 모바일 애플리케이션.
- **기능:**
    - 사용자 입력 처리.
    - 서버로 HTTP 요청 생성 및 전송.
    - 서버로부터 받은 응답을 사용자에게 표시.

### **서버 (Server)**

- **역할:** 클라이언트의 요청을 처리하고, 적절한 응답을 반환한다.
- **예시:** 웹 서버 (Apache, Nginx), 애플리케이션 서버.
- **기능:**
    - 클라이언트의 요청 수신 및 해석.
    - 요청된 리소스 처리 (정적 파일 제공, 동적 콘텐츠 생성).
    - HTTP 응답 생성 및 전송.

### **요청과 응답의 흐름**

1. **요청(Request):**
    - 클라이언트가 서버에 특정 리소스에 대한 요청을 보낸다.
    - 요청은 메서드 (GET, POST 등), URL, 헤더, 바디로 구성.
    - 예시:
        
        ```
        GET /index.html HTTP/1.1
        Host: www.example.com
        Accept: text/html
        ```
        
2. **응답(Response):**
    - 서버가 요청을 처리한 후, 결과를 클라이언트에 반환한다.
    - 응답은 상태 코드, 헤더, 바디로 구성.
    - 예시:
        
        ```
        HTTP/1.1 200 OK
        Content-Type: text/html
        Content-Length: 1256
        
        <html>
        <head><title>Example</title></head>
        <body>...</body>
        </html>
        ```
        

### **클라이언트-서버 모델의 장점**

- **분산 처리:** 클라이언트와 서버가 별도로 동작하여 작업을 분산 처리할 수 있다.
- **유지보수 용이성:** 서버 측에서 로직을 중앙 관리하여 업데이트 및 유지보수가 용이하다.
- **확장성:** 서버를 추가하거나 확장하여 트래픽 증가에 대응 가능하다.

### **실제 동작 예시**

1. 사용자가 웹 브라우저에 `www.example.com`을 입력한다.
2. 브라우저가 DNS를 통해 도메인 이름을 IP 주소로 변환한다.
3. 브라우저가 서버에 HTTP GET 요청을 전송한다.
4. 서버가 요청을 처리하고 HTML 문서를 포함한 HTTP 응답을 전송한다.
5. 브라우저가 응답을 받아 렌더링하여 사용자에게 웹 페이지를 표시한다.

---

## 2. HTTP 메서드

HTTP 메서드는 클라이언트가 서버에 요청을 보낼 때 요청의 목적을 나타내는 방법(Method)이다. 각 메서드는 특정한 작업을 수행하며, 그에 따라 서버는 적절한 응답을 반환한다. HTTP 메서드는 RESTful API 설계에서도 중요한 역할을 한다.

### 2.1 GET

**GET** 메서드는 서버에서 특정 리소스를 요청할 때 사용된다. 주로 데이터를 조회할 때 사용하며, 서버의 상태를 변경하지 않는다.

- **역할 및 사용 사례:**
    - 웹 페이지나 API에서 데이터를 조회할 때 사용.
    - 검색 쿼리 실행.
    - 이미지, 비디오 등의 정적 리소스 요청.
- **특징:**
    - **안전성 (Safe):** GET 요청은 서버의 상태를 변경하지 않으므로 안전하다고 간주된다.
    - **멱등성 (Idempotent):** 동일한 GET 요청을 여러 번 보내도 결과가 동일하다.
    - **캐싱 가능:** GET 요청은 캐시될 수 있어 네트워크 효율성을 높인다.
    - **데이터 전달:** URL의 쿼리 스트링에 데이터를 포함시킬 수 있다.
- **예제:**
    
    ```
    GET /users/123 HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```
    

### 2.2 POST

**POST** 메서드는 서버에 새로운 리소스를 생성하거나, 데이터를 제출하여 서버의 상태를 변경할 때 사용된다. 주로 폼 제출, 파일 업로드 등에 사용된다.

- **역할 및 사용 사례:**
    - 새 사용자 등록.
    - 블로그 포스트 작성.
    - 파일 업로드.
- **특징:**
    - **비안전성 (Unsafe):** POST 요청은 서버의 상태를 변경할 수 있다.
    - **비멱등성 (Non-idempotent):** 동일한 POST 요청을 여러 번 보내면 여러 리소스가 생성될 수 있다.
    - **데이터 전달:** 요청 본문(body)에 데이터를 포함시킨다.
- **예제:**
    
    ```
    POST /users HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
    

### 2.3 PUT

**PUT** 메서드는 서버에 특정 리소스를 업데이트하거나, 존재하지 않는 경우 새로 생성할 때 사용된다. 전체 리소스를 대체하는 경우가 많다.

- **역할 및 사용 사례:**
    - 사용자 정보 전체 업데이트.
    - 문서 전체 수정.
    - 특정 리소스의 전체 교체.
- **특징:**
    - **안전성:** PUT 요청은 리소스를 업데이트하지만, 요청의 의도에 따라 안전하다고 간주될 수 있다.
    - **멱등성:** 동일한 PUT 요청을 여러 번 보내도 결과가 동일하다.
    - **데이터 전달:** 요청 본문에 전체 리소스 데이터를 포함시킨다.
- **예제:**
    
    ```
    PUT /users/123 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "name": "John Doe",
      "email": "john.newemail@example.com"
    }
    ```
    

### 2.4 DELETE

**DELETE** 메서드는 서버에서 특정 리소스를 삭제할 때 사용된다.

- **역할 및 사용 사례:**
    - 사용자 계정 삭제.
    - 블로그 포스트 삭제.
    - 파일 삭제.
- **특징:**
    - **안전성:** DELETE 요청은 리소스를 삭제하므로 안전하지 않을 수 있다.
    - **멱등성:** 동일한 DELETE 요청을 여러 번 보내도 결과는 동일하다. 리소스가 이미 삭제된 상태이기 때문에 추가 요청은 영향을 미치지 않는다.
- **예제:**
    
    ```
    DELETE /users/123 HTTP/1.1
    Host: api.example.com
    ```
    

### 2.5 PATCH

**PATCH** 메서드는 서버에 특정 리소스의 일부를 수정할 때 사용된다. PUT과 달리 전체 리소스를 대체하지 않고 일부 필드만 업데이트한다.

- **역할 및 사용 사례:**
    - 사용자 정보 일부 업데이트.
    - 게시글 제목 변경.
    - 설정 옵션 수정.
- **특징:**
    - **비안전성 (Unsafe):** 리소스를 수정하므로 안전하지 않다.
    - **비멱등성 (Non-idempotent):** 동일한 PATCH 요청을 여러 번 보내면 결과가 다를 수 있다.
    - **데이터 전달:** 요청 본문에 수정할 데이터만 포함시킨다.
- **예제:**
    
    ```
    PATCH /users/123 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "email": "john.updated@example.com"
    
    ```
    

### 2.6 HEAD

**HEAD** 메서드는 GET 메서드와 동일한 요청을 보내지만, 응답 본문을 포함하지 않는다. 주로 메타데이터나 헤더 정보를 확인할 때 사용된다.

- **역할 및 사용 사례:**
    - 리소스의 존재 여부 확인.
    - 리소스의 메타데이터 조회 (예: Content-Type, Content-Length).
    - 캐싱된 리소스의 유효성 검사.
- **특징:**
    - **안전성 (Safe):** 서버의 상태를 변경하지 않으므로 안전하다.
    - **멱등성 (Idempotent):** 동일한 HEAD 요청을 여러 번 보내도 결과가 동일하다.
    - **캐싱 가능:** GET과 마찬가지로 캐시될 수 있다.
- **예제:**
    
    ```
    HEAD /users/123 HTTP/1.1
    Host: api.example.com
    ```
    

### 2.7 OPTIONS

**OPTIONS** 메서드는 특정 리소스가 지원하는 HTTP 메서드의 목록을 요청할 때 사용된다. 주로 클라이언트가 서버와의 상호작용을 사전에 확인하는 데 사용된다.

- **역할 및 사용 사례:**
    - CORS(Cross-Origin Resource Sharing) 요청 사전 검사.
    - API 지원 메서드 확인.
    - 서버의 기능 및 옵션 파악.
- **특징:**
    - **안전성 (Safe):** 서버의 상태를 변경하지 않으므로 안전하다.
    - **멱등성 (Idempotent):** 동일한 OPTIONS 요청을 여러 번 보내도 결과가 동일하다.
    - **데이터 전달:** Allow 헤더를 통해 지원되는 메서드 목록을 반환한다.
- **예제:**
    
    ```
    OPTIONS /users/123 HTTP/1.1
    Host: api.example.com
    ```
    

### 2.8 CONNECT

**CONNECT** 메서드는 주로 프록시 서버를 통해 터널을 설정할 때 사용된다. SSL/TLS를 통해 HTTPS 요청을 프록시 서버를 통해 전달할 때 사용된다.

- **역할 및 사용 사례:**
    - HTTPS 트래픽을 프록시 서버를 통해 터널링.
    - 네트워크 터널링 설정.
- **특징:**
    - **비안전성 (Unsafe):** 서버의 상태를 변경하지는 않지만, 터널링을 설정하는 데 사용된다.
    - **특수한 사용 사례:** 일반적인 웹 애플리케이션 개발에서는 잘 사용되지 않는다.
- **예제:**
    
    ```
    CONNECT www.example.com:443 HTTP/1.1
    Host: www.example.com:44
    ```
    

### 2.9 TRACE

**TRACE** 메서드는 서버가 클라이언트의 요청을 그대로 반환하도록 요청한다. 주로 디버깅 목적으로 사용된다.

- **역할 및 사용 사례:**
    - 요청이 서버에 도달하기까지의 경로 확인.
    - 디버깅 및 테스트.
- **특징:**
    - **안전성 (Safe):** 서버의 상태를 변경하지 않으므로 안전하다.
    - **멱등성 (Idempotent):** 동일한 TRACE 요청을 여러 번 보내도 결과가 동일하다.
    - **보안 이슈:** 악용될 수 있어 많은 서버에서 비활성화 되어 있다.
- **예제:**
    
    ```
    TRACE / HTTP/1.1
    Host: www.example.com
    ```
    

### 2.10 HTTP 메서드의 특징 및 차이점 분석

각 HTTP 메서드는 특정한 목적과 특성을 가지고 있으며, 이를 이해하는 것은 RESTful API 설계 및 웹 개발에서 중요하다.

- **안전성 (Safety):**
    - **Safe Methods:** GET, HEAD, OPTIONS, TRACE
        - 서버의 상태를 변경하지 않는다.
        - 안전하게 여러 번 호출 가능하다.
    - **Unsafe Methods:** POST, PUT, DELETE, PATCH, CONNECT
        - 서버의 상태를 변경할 수 있다.
- **멱등성 (Idempotency):**
    - **Idempotent Methods:** GET, PUT, DELETE, HEAD, OPTIONS, TRACE, CONNECT
        - 동일한 요청을 여러 번 보내도 결과가 동일하다.
    - **Non-idempotent Methods:** POST, PATCH
        - 동일한 요청을 여러 번 보내면 결과가 달라질 수 있다.
- **캐싱:**
    - **캐싱 가능한 메서드:** GET, HEAD, OPTIONS
    - **캐싱 불가능한 메서드:** POST, PUT, DELETE, PATCH, CONNECT, TRACE
- **데이터 전달 방식:**
    - **URL 쿼리 스트링:** GET, DELETE
    - **요청 본문:** POST, PUT, PATCH
- **사용 용도:**
    - **데이터 조회:** GET
    - **데이터 생성:** POST
    - **데이터 전체 수정 또는 교체:** PUT
    - **데이터 부분 수정:** PATCH
    - **데이터 삭제:** DELETE
    - **메서드 및 옵션 확인:** OPTIONS, HEAD
    - **터널링 설정:** CONNECT
    - **요청 추적:** TRACE

## 3. HTTP 상태 코드

HTTP 상태 코드는 클라이언트의 요청에 대한 서버의 응답 상태를 나타낸다. 상태 코드는 주로 3자리 숫자로 구성되며, 각 숫자는 특정한 의미를 가진다. 상태 코드는 다섯 가지 범주로 분류되며, 각 범주는 클라이언트와 서버 간의 상호작용에서 발생할 수 있는 다양한 상황을 설명한다.

### 3.1 상태 코드의 분류과 각 코드의 의미

HTTP 상태 코드는 첫 번째 숫자에 따라 다섯 가지 범주로 분류된다:

1. **1xx: 정보 응답 (Informational)**
    - 요청을 수신하여 처리 중임을 나타낸다.
    - 주로 프로토콜의 상태를 알리는 데 사용된다.
2. **2xx: 성공 응답 (Successful)**
    - 클라이언트의 요청이 성공적으로 처리되었음을 나타낸다.
3. **3xx: 리다이렉션 (Redirection)**
    - 클라이언트가 추가적인 동작을 수행하여 요청을 완료해야 함을 나타낸다.
4. **4xx: 클라이언트 오류 (Client Error)**
    - 클라이언트의 요청에 오류가 있음을 나타낸다.
5. **5xx: 서버 오류 (Server Error)**
    - 서버가 요청을 처리하는 데 실패했음을 나타낸다.

### 3.2 상태 코드별 예제와 활용 방법

각 범주별로 주요 상태 코드의 의미와 사용 사례를 살펴본다.

### **1xx: 정보 응답**

**100 Continue**

- **의미:** 클라이언트가 요청을 계속 진행해도 됨을 서버가 알려준다.
- **사용 사례:** 클라이언트가 대용량 데이터를 전송하기 전에 서버의 준비 상태를 확인할 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 100 Continue
    ```
    

**101 Switching Protocols**

- **의미:** 클라이언트가 요청한 프로토콜로 전환됨을 나타낸다.
- **사용 사례:** 웹소켓 연결 시 프로토콜 전환을 위해 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 101 Switching Protocols
    Upgrade: websocket
    Connection: Upgrade
    ```
    

### **2xx: 성공 응답**

**200 OK**

- **의미:** 요청이 성공적으로 처리되었음을 나타낸다.
- **사용 사례:** GET, POST, PUT 등 다양한 메서드의 성공적인 응답.
- **예제:**
    
    ```
    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 123
    
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
    

**201 Created**

- **의미:** 요청이 성공적으로 처리되었으며, 새로운 리소스가 생성되었음을 나타낸다.
- **사용 사례:** POST 요청으로 새 리소스를 생성할 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 201 Created
    Location: /users/123
    Content-Type: application/json
    Content-Length: 456
    
    {
      "id": 123,
      "name": "Jane Doe"
    }
    ```
    

**204 No Content**

- **의미:** 요청이 성공적으로 처리되었으나, 반환할 콘텐츠가 없음을 나타낸다.
- **사용 사례:** DELETE 요청 후 응답으로 사용되거나, PUT 요청에서 업데이트만 수행했을 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 204 No Content
    ```
    

### **3xx: 리다이렉션**

**301 Moved Permanently**

- **의미:** 요청한 리소스가 영구적으로 새로운 위치로 이동되었음을 나타낸다.
- **사용 사례:** URL이 영구적으로 변경되었을 때 클라이언트를 새 위치로 안내.
- **예제:**
    
    ```
    HTTP/1.1 301 Moved Permanently
    Location: https://www.newdomain.com/
    ```
    

**302 Found**

- **의미:** 요청한 리소스가 일시적으로 다른 위치에 있음을 나타낸다.
- **사용 사례:** 임시적인 리다이렉션 시 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 302 Found
    Location: https://www.temporary.com/
    ```
    

**304 Not Modified**

- **의미:** 클라이언트가 조건부 요청을 보냈으며, 리소스가 변경되지 않았음을 나타낸다.
- **사용 사례:** 캐시된 리소스를 재사용할 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 304 Not Modified
    ```
    

### **4xx: 클라이언트 오류**

**400 Bad Request**

- **의미:** 클라이언트의 요청이 잘못되었음을 나타낸다.
- **사용 사례:** 잘못된 요청 구문이나 유효하지 않은 요청 데이터.
- **예제:**
    
    ```
    HTTP/1.1 400 Bad Request
    Content-Type: application/json
    Content-Length: 89
    
    {
      "error": "Bad Request",
      "message": "Invalid JSON format."
    }
    ```
    

**401 Unauthorized**

- **의미:** 인증이 필요함을 나타낸다.
- **사용 사례:** 인증이 필요한 리소스에 접근할 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 401 Unauthorized
    WWW-Authenticate: Basic realm="Access to the site"
    ```
    

**403 Forbidden**

- **의미:** 서버가 요청을 이해했으나, 권한이 없어 접근을 거부함을 나타낸다.
- **사용 사례:** 인증된 사용자가 특정 리소스에 접근할 권한이 없을 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 403 Forbidden
    Content-Type: application/json
    Content-Length: 76
    
    {
      "error": "Forbidden",
      "message": "You do not have permission to access this resource."
    }
    ```
    

**404 Not Found**

- **의미:** 요청한 리소스를 서버에서 찾을 수 없음을 나타낸다.
- **사용 사례:** 존재하지 않는 URL에 접근할 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 404 Not Found
    Content-Type: text/html
    Content-Length: 178
    
    <html>
      <head><title>404 Not Found</title></head>
      <body>
        <h1>Not Found</h1>
        <p>The requested URL was not found on this server.</p>
      </body>
    </html>
    ```
    

**405 Method Not Allowed**

- **의미:** 요청한 HTTP 메서드가 지원되지 않음을 나타낸다.
- **사용 사례:** 특정 리소스에서 허용되지 않는 메서드로 요청할 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 405 Method Not Allowed
    Allow: GET, POST
    Content-Type: application/json
    Content-Length: 95
    
    {
      "error": "Method Not Allowed",
      "message": "The PUT method is not allowed for this resource."
    }
    ```
    

**409 Conflict**

- **의미:** 요청이 현재 서버의 상태와 충돌함을 나타낸다.
- **사용 사례:** 중복된 리소스 생성 시도 등.
- **예제:**
    
    ```
    HTTP/1.1 409 Conflict
    Content-Type: application/json
    Content-Length: 102
    
    {
      "error": "Conflict",
      "message": "A user with this email already exists."
    }
    ```
    

### **5xx: 서버 오류**

**500 Internal Server Error**

- **의미:** 서버에서 예기치 못한 오류가 발생했음을 나타낸다.
- **사용 사례:** 서버 측 코드 오류 등.
- **예제:**
    
    ```
    HTTP/1.1 500 Internal Server Error
    Content-Type: text/html
    Content-Length: 150
    
    <html>
      <head><title>500 Internal Server Error</title></head>
      <body>
        <h1>Internal Server Error</h1>
        <p>An unexpected error has occurred.</p>
      </body>
    </html>
    ```
    

**502 Bad Gateway**

- **의미:** 서버가 게이트웨이 또는 프록시로부터 잘못된 응답을 받았음을 나타낸다.
- **사용 사례:** 역방향 프록시 서버가 원 서버로부터 유효하지 않은 응답을 받을 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 502 Bad Gateway
    Content-Type: text/html
    Content-Length: 145
    
    <html>
      <head><title>502 Bad Gateway</title></head>
      <body>
        <h1>Bad Gateway</h1>
        <p>The server received an invalid response from the upstream server.</p>
      </body>
    </html>
    ```
    

**503 Service Unavailable**

- **의미:** 서버가 일시적으로 과부하 상태이거나 유지보수 중임을 나타낸다.
- **사용 사례:** 서버가 일시적으로 요청을 처리할 수 없을 때 사용된다.
- **예제:**
    
    ```
    HTTP/1.1 503 Service Unavailable
    Retry-After: 3600
    Content-Type: text/html
    Content-Length: 160
    
    <html>
      <head><title>503 Service Unavailable</title></head>
      <body>
        <h1>Service Unavailable</h1>
        <p>The server is currently unable to handle the request due to a temporary overloading or maintenance.</p>
      </body>
    </html>
    ```
    

### **3.3 상태 코드 요약표**

| 범주 | 코드 | 의미 | 설명 |
| --- | --- | --- | --- |
| 1xx | 100 | Continue | 요청을 계속 진행해도 됨 |
|  | 101 | Switching Protocols | 프로토콜 전환됨 |
| 2xx | 200 | OK | 요청 성공 |
|  | 201 | Created | 리소스 생성됨 |
|  | 204 | No Content | 콘텐츠 없음 |
| 3xx | 301 | Moved Permanently | 영구적 리다이렉션 |
|  | 302 | Found | 일시적 리다이렉션 |
|  | 304 | Not Modified | 수정되지 않음 |
| 4xx | 400 | Bad Request | 잘못된 요청 |
|  | 401 | Unauthorized | 인증 필요 |
|  | 403 | Forbidden | 접근 금지 |
|  | 404 | Not Found | 리소스 없음 |
|  | 405 | Method Not Allowed | 메서드 허용되지 않음 |
|  | 409 | Conflict | 충돌 발생 |
| 5xx | 500 | Internal Server Error | 내부 서버 오류 |
|  | 502 | Bad Gateway | 잘못된 게이트웨이 |
|  | 503 | Service Unavailable | 서비스 이용 불가 |

### 3.4 상태 코드의 활용 방법

HTTP 상태 코드를 올바르게 이해하고 사용하는 것은 웹 개발 및 API 설계에서 중요하다. 각 상태 코드는 클라이언트와 서버 간의 통신에서 발생하는 다양한 상황을 명확하게 전달하며, 이를 통해 클라이언트는 서버의 응답을 적절히 처리할 수 있다.

- **클라이언트 측 활용:**
    - **에러 처리:** 4xx 및 5xx 상태 코드를 기반으로 사용자에게 적절한 에러 메시지를 표시.
    - **리다이렉션 처리:** 3xx 상태 코드를 통해 클라이언트를 새로운 위치로 안내.
    - **캐싱 관리:** 2xx 및 3xx 상태 코드를 활용하여 응답을 캐시하거나 캐시를 무효화.
- **서버 측 활용:**
    - **정확한 응답 제공:** 클라이언트의 요청에 맞는 상태 코드를 반환하여 클라이언트가 요청 결과를 정확히 이해할 수 있도록 함.
    - **보안 강화:** 401, 403 등의 상태 코드를 통해 인증 및 권한 관리를 효과적으로 수행.
    - **성능 최적화:** 304 상태 코드를 활용하여 불필요한 데이터 전송을 줄이고 네트워크 효율성을 높임.

### 3.5 상태 코드 처리 예제

**예제 1: 사용자 생성 요청**

- **요청:**
    
    ```
    POST /users HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "name": "Alice",
      "email": "alice@example.com"
    }
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 201 Created
    Location: /users/124
    Content-Type: application/json
    Content-Length: 150
    
    {
      "id": 124,
      "name": "Alice",
      "email": "alice@example.com"
    }
    ```
    
- **응답 (이미 존재):**
    
    ```
    HTTP/1.1 409 Conflict
    Content-Type: application/json
    Content-Length: 102
    
    {
      "error": "Conflict",
      "message": "A user with this email already exists."
    }
    ```
    

**예제 2: 리소스 조회 요청**

- **요청:**
    
    ```
    GET /users/124 HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 150
    
    {
      "id": 124,
      "name": "Alice",
      "email": "alice@example.com"
    }
    ```
    
- **응답 (존재하지 않음):**
    
    ```
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    Content-Length: 89
    
    {
      "error": "Not Found",
      "message": "The requested user does not exist."
    }
    ```
    

**예제 3: 리소스 삭제 요청**

- **요청:**
    
    ```
    DELETE /users/124 HTTP/1.1
    Host: api.example.com
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 204 No Content
    ```
    
- **응답 (이미 삭제됨):**
    
    ```
    HTTP/1.1 404 Not Found
    Content-Type: application/json
    Content-Length: 89
    
    {
      "error": "Not Found",
      "message": "The requested user does not exist."
    }
    ```
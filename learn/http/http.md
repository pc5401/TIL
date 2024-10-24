# HTTP 정리
> http를 쭉 정리를 해보기로 다짐함.

## 0. 목차
- [1. HTTP 소개](#1-http-소개)
- [2. HTTP 메서드](#2-http-메서드)
- [3. HTTP 상태 코드](#3-http-상태-코드)
- [4. HTTP 버전](#4-http-버전)
- [5. HTTP 헤더](#5-http-헤더)
- [6. HTTP 상태 코드](#6-https-및-보안)
- [7. HTTP 쿠키](#7-http-쿠키)
- [8. restful API와 http](#8-restful-api와-http)
- [9. http 캐싱](#9-http-캐싱)

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

    ## 4. HTTP 버전

HTTP는 초기 버전부터 현재의 HTTP/3에 이르기까지 지속적으로 발전해왔다. 각 HTTP 버전은 이전 버전의 한계를 극복하고 성능을 향상시키기 위해 다양한 특징과 개선점을 도입하였다. 이 장에서는 각 HTTP 버전의 주요 특징과 개선점, 그리고 버전 간 호환성 및 전환 과정을 살펴본다.

### 4.1 각 HTTP 버전의 특징과 개선점

HTTP는 현재까지 HTTP/0.9, HTTP/1.0, HTTP/1.1, HTTP/2, 그리고 최신 버전인 HTTP/3으로 발전해왔다. 각 버전의 주요 특징과 개선점을 아래와 같이 정리할 수 있다.

### **HTTP/0.9**

- **출시 시기:** 1991년
- **특징:**
    - 매우 단순한 프로토콜로, GET 요청만 지원한다.
    - 텍스트 기반의 단일 문서 전송.
    - 헤더와 상태 코드가 존재하지 않는다.
- **개선점:**
    - 기능이 제한적이어서 현대적인 웹 요구사항을 충족하지 못한다.

### **HTTP/1.0**

- **출시 시기:** 1996년 (RFC 1945)
- **특징:**
    - 요청과 응답에 헤더가 추가된다.
    - 다양한 HTTP 메서드 지원 (GET, POST 등).
    - 상태 코드 도입 (200 OK, 404 Not Found 등).
    - 비연결성 유지: 각 요청마다 새로운 연결을 생성한다.
- **개선점:**
    - 콘텐츠 유형과 길이를 명시할 수 있어 유연성이 향상된다.
    - 캐싱 메커니즘 도입으로 네트워크 효율성이 증가된다.

### **HTTP/1.1**

- **출시 시기:** 1997년 (RFC 2068), 1999년 (RFC 2616)
- **특징:**
    - 지속적인 연결 (Persistent Connections): 기본적으로 연결을 유지하여 여러 요청을 처리한다.
    - 파이프라이닝: 여러 요청을 동시에 보낼 수 있으나, 널리 사용되지는 않는다.
    - 추가적인 캐싱 헤더와 개선된 캐싱 메커니즘.
    - 호스트 헤더 도입으로 가상 호스팅 지원.
- **개선점:**
    - 네트워크 효율성 증가.
    - 다양한 최적화 기능 추가로 성능 향상.

### **HTTP/2**

- **출시 시기:** 2015년 (RFC 7540)
- **특징:**
    - 이진 프로토콜: 텍스트 기반이 아닌 이진 형식으로 데이터 전송.
    - 다중화 (Multiplexing): 하나의 연결에서 여러 스트림을 동시에 처리할 수 있다.
    - 헤더 압축: 헤더 정보를 효율적으로 압축하여 전송.
    - 서버 푸시: 서버가 클라이언트의 요청 없이 리소스를 미리 전송할 수 있다.
- **개선점:**
    - 성능 향상: 페이지 로딩 속도가 개선된다.
    - 네트워크 자원을 효율적으로 사용하여 대역폭 절약.
    - 지연 시간 감소로 사용자 경험 향상.

### **HTTP/3**

- **출시 시기:** 2022년 (RFC 9114)
- **특징:**
    - QUIC 프로토콜 기반: UDP 위에서 동작하여 지연 시간을 감소시킨다.
    - 연결 설정 속도 향상: 0-RTT 핸드셰이크 지원으로 빠른 연결 설정이 가능하다.
    - 내장된 보안: TLS 1.3이 기본적으로 통합되어 보안이 강화된다.
    - 패킷 손실에 대한 더 나은 처리로 안정적인 데이터 전송을 지원한다.
- **개선점:**
    - 더욱 빠르고 안정적인 데이터 전송이 가능해진다.
    - 모바일 및 실시간 애플리케이션에 적합한 성능을 제공한다.
    - 연결 복구 기능이 강화되어 네트워크 변동성에 강하다.

### 4.2 버전 간 호환성 및 전환 과정

HTTP 버전 간의 호환성과 전환 과정은 웹의 발전과 함께 중요한 역할을 해왔다. 각 버전 간의 호환성과 전환 방식을 이해하는 것은 웹 개발과 네트워크 관리에서 필수적이다.

### **호환성**

- **HTTP/1.0과 HTTP/1.1:**
    - HTTP/1.1은 HTTP/1.0의 상위 호환 버전이다.
    - 대부분의 HTTP/1.0 클라이언트와 서버는 HTTP/1.1을 지원하며, 역호환성을 유지한다.
    - HTTP/1.1에서 도입된 기능들은 HTTP/1.0에서 지원되지 않지만, 기본적인 요청과 응답은 호환된다.
- **HTTP/2:**
    - HTTP/2는 HTTP/1.1과 호환되지 않는다. 그러나 대부분의 HTTP/2 구현체는 HTTP/1.1 클라이언트와 서버와의 호환성을 유지하기 위해 프로토콜 협상을 통해 적절한 버전을 선택한다.
    - ALPN(Application-Layer Protocol Negotiation)을 사용하여 클라이언트와 서버가 지원하는 최적의 프로토콜을 협상한다.
- **HTTP/3:**
    - HTTP/3는 QUIC 프로토콜을 기반으로 하여 HTTP/2와는 다른 전송 계층을 사용한다.
    - 기존의 TCP 기반 HTTP/1.1 및 HTTP/2와는 직접적인 호환성이 없지만, ALPN을 통해 클라이언트와 서버가 HTTP/3를 지원하는지 여부를 협상한다.
    - HTTP/3를 지원하지 않는 클라이언트와 서버는 이전 버전인 HTTP/2 또는 HTTP/1.1을 사용하여 통신을 지속한다.

### **전환 과정**

HTTP 버전 간의 전환은 주로 다음과 같은 단계를 거친다:

1. **프로토콜 지원 확인:**
    - 클라이언트와 서버가 지원하는 HTTP 버전을 확인한다.
    - ALPN을 통해 클라이언트와 서버가 협상을 시작한다.
2. **프로토콜 협상:**
    - 클라이언트는 TLS 핸드셰이크 중에 지원하는 프로토콜 목록을 서버에 제공한다.
    - 서버는 클라이언트가 제공한 목록 중에서 자신이 지원하는 최상의 프로토콜을 선택하여 응답한다.
3. **연결 설정:**
    - 선택된 HTTP 버전에 따라 연결이 설정된다.
    - 예를 들어, HTTP/2가 선택되면 이진 프레임을 사용하여 데이터가 전송된다.
4. **연속적인 전환:**
    - 네트워크 환경이나 클라이언트 및 서버의 업데이트에 따라 HTTP 버전이 지속적으로 전환되고 개선된다.
    - 새로운 버전이 도입될 때마다 점진적으로 채택되며, 이전 버전과의 호환성을 유지하면서 전환이 이루어진다.

### **전환 시 고려사항**

- **서버 및 클라이언트 지원:**
    - 서버와 클라이언트가 새로운 HTTP 버전을 지원하는지 확인해야 한다.
    - 소프트웨어 업데이트를 통해 최신 버전을 지원하도록 설정한다.
- **보안:**
    - 새로운 버전에서는 보안 기능이 강화되므로, 보안 정책을 최신화해야 한다.
    - 예를 들어, HTTP/3에서는 TLS 1.3이 기본적으로 통합되므로, 관련 인증서를 업데이트해야 한다.
- **성능 최적화:**
    - 새로운 버전의 프로토콜을 사용하여 성능을 최적화할 수 있다.
    - 예를 들어, HTTP/2의 다중화와 헤더 압축을 활용하여 네트워크 효율성을 높일 수 있다.
- **테스트 및 검증:**
    - 새로운 HTTP 버전으로 전환하기 전에 충분한 테스트를 통해 호환성과 성능을 검증해야 한다.
    - 다양한 환경에서의 동작을 확인하여 예기치 않은 문제가 발생하지 않도록 한다.

### 4.3 HTTP 버전 전환 예제

**예제 1: HTTP/1.1에서 HTTP/2로 전환**

- **단계:**
    1. 서버가 HTTP/2를 지원하도록 설정한다 (예: Nginx 설정 변경).
    2. 클라이언트가 HTTP/2를 지원하는지 확인한다 (대부분의 최신 브라우저는 지원).
    3. 서버와 클라이언트 간의 ALPN 협상을 통해 HTTP/2 연결을 설정한다.
- **설정 예시 (Nginx):**
    
    ```
    server {
        listen 443 ssl http2;
        server_name www.example.com;
    
        ssl_certificate /path/to/cert.pem;
        ssl_certificate_key /path/to/key.pem;
    
        # 기타 SSL 설정
        ...
    }
    ```
    
- **결과:**
    - 클라이언트가 HTTP/2를 지원하면, 서버는 HTTP/2 프로토콜을 사용하여 데이터 전송을 시작한다.
    - 그렇지 않으면, HTTP/1.1로 대체하여 통신을 계속한다.

**예제 2: HTTP/2에서 HTTP/3로 전환**

- **단계:**
    1. 서버가 QUIC 및 HTTP/3를 지원하도록 설정한다 (예: 최신 Nginx 또는 Caddy 서버 사용).
    2. 클라이언트가 HTTP/3를 지원하는지 확인한다 (최신 브라우저 사용).
    3. 서버와 클라이언트 간의 ALPN 협상을 통해 HTTP/3 연결을 설정한다.
- **설정 예시 (Caddy):**
    
    ```
    example.com {
        tls /path/to/cert.pem /path/to/key.pem
        encode gzip
        ...
    }
    ```
    
    - Caddy는 기본적으로 HTTP/3를 지원하며, 별도의 설정 없이 자동으로 활성화된다.
- **결과:**
    - 클라이언트가 HTTP/3를 지원하면, 서버는 HTTP/3 프로토콜을 사용하여 데이터 전송을 시작한다.
    - 그렇지 않으면, HTTP/2 또는 HTTP/1.1로 대체하여 통신을 계속한다.

### 4.4 HTTP 버전 전환의 장단점

각 HTTP 버전으로의 전환에는 장단점이 존재한다. 이를 이해하고 적절히 활용하는 것이 중요하다.

### **장점**

- **성능 향상:**
    - HTTP/2와 HTTP/3는 다중화, 헤더 압축, 서버 푸시 등 다양한 성능 최적화 기능을 제공하여 페이지 로딩 속도를 개선한다.
- **보안 강화:**
    - HTTP/2 이후 버전에서는 보안 기능이 강화되어 데이터 전송의 안전성이 높아진다.
    - HTTP/3에서는 TLS 1.3이 기본적으로 통합되어 보안이 강화된다.
- **네트워크 효율성:**
    - 새로운 버전에서는 네트워크 자원을 보다 효율적으로 사용할 수 있도록 설계되었다.
    - 특히, HTTP/3의 QUIC 프로토콜은 패킷 손실에 대한 회복 능력이 뛰어나 네트워크 안정성이 향상된다.
- **실시간 통신 지원:**
    - HTTP/3는 모바일 및 실시간 애플리케이션에 적합한 성능을 제공하여 다양한 응용 프로그램에 활용할 수 있다.

### **단점**

- **호환성 문제:**
    - 새로운 HTTP 버전은 일부 구형 클라이언트나 서버에서 지원되지 않을 수 있어 호환성 문제가 발생할 수 있다.
- **설정 복잡성:**
    - HTTP/2와 HTTP/3는 이전 버전에 비해 설정이 복잡할 수 있으며, 서버 설정 및 관리에 추가적인 노력이 필요하다.
- **채택 속도:**
    - 새로운 버전의 프로토콜을 채택하는 데 시간이 걸릴 수 있으며, 모든 사용자와 시스템이 동시에 업데이트되지 않는다.
- **학습 곡선:**
    - 새로운 기능과 개념을 이해하고 활용하는 데 추가적인 학습이 필요할 수 있다.

### 4.5 HTTP 버전 전환 시 고려사항

HTTP 버전 간의 전환을 계획할 때는 다음과 같은 사항을 고려해야 한다:

- **현재 인프라 평가:**
    - 현재 사용하는 서버와 클라이언트가 새로운 HTTP 버전을 지원하는지 확인한다.
- **보안 정책 업데이트:**
    - 새로운 HTTP 버전에서는 보안 기능이 강화되므로, 관련 보안 정책과 인증서를 최신화해야 한다.
- **성능 테스트:**
    - 전환 전후의 성능을 비교하여 실제로 성능 향상이 이루어지는지 확인한다.
- **점진적 도입:**
    - 모든 시스템을 한 번에 전환하기보다는, 단계적으로 도입하여 문제를 최소화한다.
- **문서화 및 교육:**
    - 전환 과정과 새로운 프로토콜의 사용 방법을 문서화하고, 팀원들에게 교육하여 원활한 전환을 지원한다.

## 5. HTTP 헤더

HTTP 헤더는 클라이언트와 서버 간의 요청과 응답에 추가적인 정보를 전달하는 데 사용된다. 헤더는 요청 헤더(Request Headers), 응답 헤더(Response Headers), 공통 헤더(Common Headers)로 구분되며, 각 헤더는 특정한 목적과 기능을 가지고 있다. 이 장에서는 각 헤더의 종류와 역할, 사용 사례를 학습한다.

### 5.1 요청 헤더

요청 헤더는 클라이언트가 서버에 요청을 보낼 때 추가적인 정보를 전달하는 데 사용된다. 주요 요청 헤더와 그 역할은 다음과 같다.

### **Accept**

- **역할:** 클라이언트가 처리할 수 있는 미디어 타입을 서버에 알려준다.
- **사용 사례:** 클라이언트가 JSON 데이터를 요청할 때 사용된다.
- **예제:**
    
    ```
    Accept: application/json
    ```
    

### **Authorization**

- **역할:** 클라이언트가 서버에 인증 정보를 제공한다.
- **사용 사례:** API 접근 시 토큰 기반 인증에 사용된다.
- **예제:**
    
    ```
    Authorization: Bearer <token>
    ```
    

### **Content-Type**

- **역할:** 요청 본문에 포함된 데이터의 미디어 타입을 지정한다.
- **사용 사례:** POST나 PUT 요청 시 전송하는 데이터의 형식을 명시할 때 사용된다.
- **예제:**
    
    ```
    Content-Type: application/json
    ```
    

### **User-Agent**

- **역할:** 클라이언트 애플리케이션의 이름, 버전, 호스트 정보 등을 서버에 전달한다.
- **사용 사례:** 서버가 클라이언트의 종류에 따라 다른 응답을 제공할 때 사용된다.
- **예제:**
    
    ```
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36
    ```
    

### **Cookie**

- **역할:** 클라이언트가 서버에 저장된 쿠키 데이터를 전송한다.
- **사용 사례:** 세션 유지나 사용자 추적에 사용된다.
- **예제:**
    
    ```
    Cookie: sessionId=abc123; theme=light
    ```
    

### **Referer**

- **역할:** 현재 요청이 발생한 이전 페이지의 URL을 서버에 전달한다.
- **사용 사례:** 서버가 트래픽 소스를 분석하거나 보안 목적으로 사용된다.
- **예제:**
    
    ```
    Referer: https://www.example.com/page.html
    ```
    

### **Host**

- **역할:** 요청하는 서버의 호스트 이름과 포트를 지정한다.
- **사용 사례:** 가상 호스팅 환경에서 필수적으로 사용된다.
- **예제:**
    
    ```
    Host: www.example.com
    ```
    

### **Accept-Encoding**

- **역할:** 클라이언트가 지원하는 콘텐츠 인코딩 방식을 서버에 알려준다.
- **사용 사례:** 압축된 데이터를 요청할 때 사용된다.
- **예제:**
    
    ```
    Accept-Encoding: gzip, deflate, br
    ```
    

### **Accept-Language**

- **역할:** 클라이언트가 선호하는 언어를 서버에 전달한다.
- **사용 사례:** 다국어 지원 웹사이트에서 사용자에게 적합한 언어로 콘텐츠를 제공할 때 사용된다.
- **예제:**
    
    ```
    Accept-Language: en-US,en;q=0.9,ko;q=0.
    ```
    

### 5.2 응답 헤더

응답 헤더는 서버가 클라이언트의 요청에 응답할 때 추가적인 정보를 전달하는 데 사용된다. 주요 응답 헤더와 그 역할은 다음과 같다.

### **Content-Type**

- **역할:** 응답 본문에 포함된 데이터의 미디어 타입을 지정한다.
- **사용 사례:** 서버가 클라이언트에 전송하는 데이터의 형식을 명시할 때 사용된다.
- **예제:**
    
    ```
    Content-Type: application/json
    ```
    

### **Content-Length**

- **역할:** 응답 본문의 길이를 바이트 단위로 지정한다.
- **사용 사례:** 클라이언트가 응답 데이터를 올바르게 처리하기 위해 필요하다.
- **예제:**
    
    ```
    Content-Length: 3495
    ```
    

### **Set-Cookie**

- **역할:** 서버가 클라이언트에 쿠키를 설정한다.
- **사용 사례:** 세션 관리나 사용자 추적에 사용된다.
- **예제:**
    
    ```
    Set-Cookie: sessionId=abc123; Path=/; HttpOnl
    ```
    

### **Location**

- **역할:** 클라이언트에게 리다이렉션할 URL을 제공한다.
- **사용 사례:** 3xx 상태 코드와 함께 사용되어 클라이언트를 다른 위치로 안내할 때 사용된다.
- **예제:**
    
    ```
    Location: https://www.example.com/newpage.html
    ```
    

### **Cache-Control**

- **역할:** 응답에 대한 캐싱 정책을 지정한다.
- **사용 사례:** 브라우저나 중간 캐시 서버가 응답을 어떻게 캐시할지 결정할 때 사용된다.
- **예제:**
    
    ```
    Cache-Control: no-cache, no-store, must-revalidat
    ```
    

### **ETag**

- **역할:** 응답 리소스의 고유 식별자를 제공하여 캐시된 리소스의 유효성을 검사한다.
- **사용 사례:** 조건부 요청에서 리소스가 변경되었는지 확인할 때 사용된다.
- **예제:**
    
    ```
    ETag: "686897696a7c876b7e"
    ```
    

### **Expires**

- **역할:** 응답이 만료되는 날짜와 시간을 지정하여 캐싱 기간을 설정한다.
- **사용 사례:** 브라우저가 응답을 캐시할 때 유효 기간을 정할 때 사용된다.
- **예제:**
    
    ```
    Expires: Wed, 21 Oct 2025 07:28:00 GMT
    ```
    

### **Server**

- **역할:** 서버 소프트웨어의 정보를 클라이언트에 제공한다.
- **사용 사례:** 서버의 종류나 버전을 클라이언트가 확인할 수 있도록 한다.
- **예제:**
    
    ```
    Server: Apache/2.4.41 (Ubuntu
    ```
    

### **WWW-Authenticate**

- **역할:** 클라이언트에게 인증 방법을 제시한다.
- **사용 사례:** 401 Unauthorized 상태 코드와 함께 사용되어 클라이언트가 인증 정보를 제공하도록 유도할 때 사용된다.
- **예제:**
    
    ```
    WWW-Authenticate: Basic realm="Access to the site"
    ```
    

### 5.3 공통 헤더

공통 헤더는 요청과 응답 모두에서 사용될 수 있는 헤더로, 클라이언트와 서버 간의 공통적인 정보를 전달하는 데 사용된다. 주요 공통 헤더와 그 역할은 다음과 같다.

### **Connection**

- **역할:** 현재 연결의 옵션을 지정하거나 연결을 종료할지 여부를 서버에 알려준다.
- **사용 사례:** 지속적인 연결을 유지하거나, 특정 헤더를 연결에만 적용할 때 사용된다.
- **예제:**
    
    ```
    Connection: keep-alive
    ```
    

### **Date**

- **역할:** 요청이나 응답이 생성된 날짜와 시간을 지정한다.
- **사용 사례:** 응답의 타임스탬프를 제공하여 캐싱이나 로그 분석에 사용된다.
- **예제:**
    
    ```
    Date: Wed, 21 Oct 2020 07:28:00 GMT
    ```
    

### **Via**

- **역할:** 요청이나 응답이 통과한 프록시나 게이트웨이의 정보를 제공한다.
- **사용 사례:** 트래픽 경로 추적이나 네트워크 디버깅에 사용된다.
- **예제:**
    
    ```
    Via: 1.1 vegur
    ```
    

### **Transfer-Encoding**

- **역할:** 응답 본문이 어떤 전송 인코딩 방식을 사용했는지 지정한다.
- **사용 사례:** 청크 전송 인코딩 등으로 데이터를 전송할 때 사용된다.
- **예제:**
    
    ```
    Transfer-Encoding: chunked
    ```
    

### **Trailer**

- **역할:** 청크ed 전송 인코딩에서 본문 이후에 전송될 헤더의 목록을

제공한다.

- **사용 사례:** 본문 전송 후에 추가적인 헤더 정보를 전달할 때 사용된다.
- **예제:**
    
    ```
    Trailer: Expires, Content-MD5
    ```
    

### **Upgrade**

- **역할:** 클라이언트가 서버와의 프로토콜을 업그레이드할 것을 요청한다.
- **사용 사례:** 웹소켓 연결 설정 시 HTTP에서 웹소켓 프로토콜로 전환할 때 사용된다.
- **예제:**
    
    ```
    Upgrade: websocket
    ```
    

### **Pragma**

- **역할:** HTTP/1.0 클라이언트와 서버 간의 캐싱 정책을 지정한다.
- **사용 사례:** 주로 `Pragma: no-cache`를 사용하여 응답이 캐시되지 않도록 할 때 사용된다.
- **예제:**
    
    ```
    Pragma: no-cache
    ```
    

### **Origin**

- **역할:** 요청이 시작된 출처(origin)를 서버에 알려준다.
- **사용 사례:** CORS(Cross-Origin Resource Sharing) 요청 시 사용된다.
- **예제:**
    
    ```
    Origin: https://www.example.com
    ```
    

### 5.4 HTTP 헤더 요약표

| 헤더 종류 | 헤더 이름 | 역할 및 설명 | 사용 사례 |
| --- | --- | --- | --- |
| **요청 헤더** | Accept | 클라이언트가 처리할 수 있는 미디어 타입 지정 | 데이터 조회 시 미디어 타입 명시 |
|  | Authorization | 인증 정보 제공 | API 접근 시 토큰 기반 인증 |
|  | Content-Type | 요청 본문의 데이터 타입 지정 | POST, PUT 요청 시 데이터 형식 명시 |
|  | User-Agent | 클라이언트 애플리케이션 정보 전달 | 서버가 클라이언트 종류에 따라 다른 응답 제공 |
|  | Cookie | 서버에 저장된 쿠키 데이터 전송 | 세션 유지, 사용자 추적 |
|  | Referer | 이전 페이지의 URL 전달 | 트래픽 소스 분석, 보안 목적으로 사용 |
|  | Host | 요청하는 서버의 호스트 이름과 포트 지정 | 가상 호스팅 환경에서 필수적으로 사용 |
|  | Accept-Encoding | 지원하는 콘텐츠 인코딩 방식 전달 | 압축된 데이터 요청 |
|  | Accept-Language | 선호하는 언어 전달 | 다국어 지원 웹사이트에서 사용 |
| **응답 헤더** | Content-Type | 응답 본문의 데이터 타입 지정 | 서버가 클라이언트에 전송하는 데이터 형식 명시 |
|  | Content-Length | 응답 본문의 길이 지정 | 클라이언트가 응답 데이터를 올바르게 처리 |
|  | Set-Cookie | 클라이언트에 쿠키 설정 | 세션 관리, 사용자 추적 |
|  | Location | 리다이렉션할 URL 제공 | 3xx 상태 코드와 함께 사용 |
|  | Cache-Control | 캐싱 정책 지정 | 응답 캐시 설정 |
|  | ETag | 리소스의 고유 식별자 제공 | 조건부 요청에서 리소스 변경 여부 확인 |
|  | Expires | 응답의 만료 날짜와 시간 지정 | 응답의 유효 기간 설정 |
|  | Server | 서버 소프트웨어 정보 제공 | 서버의 종류나 버전 확인 |
|  | WWW-Authenticate | 인증 방법 제시 | 401 Unauthorized 상태 코드와 함께 사용 |
| **공통 헤더** | Connection | 연결의 옵션 지정 또는 연결 유지/종료 여부 전달 | 지속적인 연결 유지, 특정 헤더의 적용 |
|  | Date | 요청 또는 응답 생성 날짜와 시간 지정 | 응답 타임스탬프 제공 |
|  | Via | 요청이나 응답이 통과한 프록시/게이트웨이 정보 제공 | 트래픽 경로 추적, 네트워크 디버깅 |
|  | Transfer-Encoding | 응답 본문의 전송 인코딩 방식 지정 | 청크 전송 인코딩 등 |
|  | Trailer | 청크ed 전송 인코딩에서 본문 이후에 전송될 헤더 목록 제공 | 본문 전송 후 추가 헤더 정보 전달 |
|  | Upgrade | 프로토콜 업그레이드 요청 | 웹소켓 연결 설정 |
|  | Pragma | HTTP/1.0 캐싱 정책 지정 | 응답 캐시 방지 |
|  | Origin | 요청이 시작된 출처(origin) 전달 | CORS 요청 시 사용 |

### 5.5 HTTP 헤더의 활용 방법

HTTP 헤더를 올바르게 이해하고 사용하는 것은 웹 개발과 API 설계에서 중요하다. 각 헤더는 클라이언트와 서버 간의 통신에서 특정한 역할을 수행하며, 이를 통해 보다 효율적이고 안전한 웹 애플리케이션을 구축할 수 있다.

- **클라이언트 측 활용:**
    - **데이터 요청 최적화:** `Accept`, `Accept-Encoding`, `Accept-Language` 헤더를 활용하여 필요한 데이터만 요청함으로써 네트워크 효율성을 높인다.
    - **인증 및 보안 관리:** `Authorization`, `Cookie` 헤더를 사용하여 안전한 인증 과정을 구현한다.
    - **리소스 관리:** `If-None-Match`, `If-Modified-Since` 헤더를 사용하여 캐시된 리소스의 유효성을 검사하고 불필요한 데이터 전송을 줄인다.
- **서버 측 활용:**
    - **응답 최적화:** `Cache-Control`, `ETag`, `Expires` 헤더를 통해 클라이언트가 응답을 효율적으로 캐시할 수 있도록 한다.
    - **보안 강화:** `Set-Cookie`, `WWW-Authenticate` 헤더를 사용하여 안전한 인증과 세션 관리를 구현한다.
    - **콘텐츠 관리:** `Content-Type`, `Content-Length` 헤더를 활용하여 클라이언트에게 올바른 데이터 형식과 크기를 전달한다.
    - **리다이렉션 및 프로토콜 관리:** `Location`, `Upgrade` 헤더를 사용하여 클라이언트를 적절한 리소스나 프로토콜로 안내한다.

### 5.6 HTTP 헤더 처리 예제

**예제 1: 사용자 로그인 요청**

- **요청:**
    
    ```
    POST /login HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    Accept: application/json
    
    {
      "username": "alice",
      "password": "securepassword"
    }
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 200 OK
    Content-Type: application/json
    Set-Cookie: sessionId=abc123; Path=/; HttpOnly
    Content-Length: 89
    
    {
      "message": "Login successful",
      "userId": 124
    }
    ```
    
- **응답 (인증 실패):**
    
    ```
    HTTP/1.1 401 Unauthorized
    WWW-Authenticate: Basic realm="Access to the site"
    Content-Type: application/json
    Content-Length: 76
    
    {
      "error": "Unauthorized",
      "message": "Invalid username or password."
    }
    ```
    

**예제 2: 리소스 업데이트 요청**

- **요청:**
    
    ```
    PUT /users/124 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    Authorization: Bearer <token>
    
    {
      "name": "Alice Smith",
      "email": "alice.smith@example.com"
    }
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 200 OK
    Content-Type: application/json
    ETag: "686897696a7c876b7e"
    Content-Length: 150
    
    {
      "id": 124,
      "name": "Alice Smith",
      "email": "alice.smith@example.com"
    }
    ```
    
- **응답 (리소스 없음):**
    
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
    Authorization: Bearer <token>
    
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

## 6. HTTPS 및 보안

HTTPS는 HTTP의 보안 버전으로, 데이터를 암호화하여 전송함으로써 데이터의 무결성과 기밀성을 보장한다. 이 장에서는 HTTPS의 필요성과 동작 원리, 그리고 SSL/TLS 인증 과정과 보안 강화 방법에 대해 학습한다.

### 6.1 HTTPS의 필요성과 동작 원리

### **HTTPS의 필요성**

인터넷을 통해 전송되는 데이터는 중간에 탈취되거나 변조될 위험이 있다. 특히 로그인 정보, 결제 정보 등 민감한 데이터가 포함된 경우 이러한 보안 위협은 심각하다. HTTPS는 이러한 보안 위협을 방지하기 위해 다음과 같은 이유로 필요하다.

- **데이터 암호화:** 전송되는 데이터를 암호화하여 중간에서 탈취하더라도 내용을 해독할 수 없게 한다.
- **데이터 무결성:** 데이터가 전송 중에 변경되거나 손상되지 않았음을 보장한다.
- **서버 인증:** 클라이언트가 실제로 신뢰할 수 있는 서버와 통신하고 있음을 확인할 수 있게 한다.

### **HTTPS의 동작 원리**

HTTPS는 HTTP에 SSL(Secure Sockets Layer) 또는 TLS(Transport Layer Security) 프로토콜을 결합하여 보안을 제공한다. HTTPS의 기본 동작 원리는 다음과 같다.

1. **클라이언트 요청:** 사용자가 HTTPS URL을 입력하거나, 클라이언트 애플리케이션이 HTTPS 요청을 보낸다.
2. **서버 응답:** 서버는 SSL/TLS 인증서를 클라이언트에게 전송하여 자신의 신원을 증명한다.
3. **인증서 검증:** 클라이언트는 서버의 인증서를 검증하여 신뢰할 수 있는지 확인한다.
4. **암호화 세션 설정:** 클라이언트와 서버는 대칭 키 암호화를 위한 세션 키를 생성하고 교환한다.
5. **데이터 전송:** 세션 키를 사용하여 데이터를 암호화하여 전송한다.

### **HTTPS의 구성 요소**

- **SSL/TLS 프로토콜:** 데이터 암호화 및 무결성 보장을 담당한다.
- **인증서:** 서버의 신원을 확인하고 신뢰성을 제공한다.
- **대칭 키 암호화:** 데이터 전송 시 빠르고 효율적인 암호화를 가능하게 한다.
- **비대칭 키 암호화:** 세션 키 교환을 안전하게 수행하기 위해 사용된다.

### 6.2 SSL/TLS 인증 과정과 보안 강화 방법

### **SSL/TLS 인증 과정**

SSL/TLS는 클라이언트와 서버 간의 안전한 통신을 설정하기 위해 다음과 같은 과정을 거친다.

1. **클라이언트 헬로우 (Client Hello):**
    - 클라이언트가 서버에 연결을 시도하며 지원하는 SSL/TLS 버전, 암호화 알고리즘, 랜덤 데이터를 포함한 헬로우 메시지를 보낸다.
    - 예제:
        
        ```
        Client Hello
        - SSL/TLS 버전: TLS 1.2
        - 암호화 알고리즘: ECDHE-RSA-AES128-GCM-SHA256
        - 랜덤 데이터: [무작위 바이트]
        ```
        
2. **서버 헬로우 (Server Hello):**
    - 서버는 클라이언트의 요청을 수락하고 사용할 SSL/TLS 버전과 암호화 알고리즘을 선택하여 헬로우 메시지를 보낸다.
    - 예제:
        
        ```
        Server Hello
        - SSL/TLS 버전: TLS 1.2
        - 암호화 알고리즘: ECDHE-RSA-AES128-GCM-SHA256
        - 랜덤 데이터: [무작위 바이트]
        ```
        
3. **서버 인증서 전송 (Certificate):**
    - 서버는 신뢰할 수 있는 인증 기관(CA)에서 발급한 SSL/TLS 인증서를 클라이언트에게 보낸다.
    - 인증서에는 서버의 공개 키와 도메인 정보가 포함되어 있다.
    - 예제:
        
        ```
        Certificate
        - 서버 공개 키
        - 인증 기관 서명
        - 도메인 정보
        ```
        
4. **서버 키 교환 (Server Key Exchange):**
    - 서버가 선택한 암호화 알고리즘에 따라 추가 키 교환 정보를 보낸다.
    - 예제:
        
        ```
        Server Key Exchange
        - Diffie-Hellman 매개변수
        ```
        
5. **서버 헬로우 완료 (Server Hello Done):**
    - 서버는 헬로우 메시지 전송을 완료했음을 알린다.
    - 예제:
        
        ```
        Server Hello Done
        ```
        
6. **클라이언트 키 교환 (Client Key Exchange):**
    - 클라이언트는 서버의 공개 키를 사용하여 세션 키를 암호화하여 서버에게 전송한다.
    - 예제:
        
        ```
        Client Key Exchange
        - 암호화된 세션 키
        ```
        
7. **클라이언트 인증 및 핸드셰이크 완료 (Change Cipher Spec & Finished):**
    - 클라이언트는 세션 키를 사용하여 암호화 설정을 변경하고, 핸드셰이크 과정을 완료한다.
    - 예제:
        
        ```
        Change Cipher Spec
        Finished
        ```
        
8. **서버 핸드셰이크 완료 (Change Cipher Spec & Finished):**
    - 서버도 동일한 방식으로 암호화 설정을 변경하고 핸드셰이크를 완료한다.
    - 예제:
        
        ```
        Change Cipher Spec
        Finished
        ```
        
9. **암호화된 데이터 전송 (Encrypted Data Transfer):**
    - 이제 클라이언트와 서버는 설정된 세션 키를 사용하여 암호화된 데이터를 안전하게 주고받을 수 있다.
    - 예제:
        
        ```
        Encrypted HTTP Requests and Responses
        ```
        

### **보안 강화 방법**

HTTPS와 SSL/TLS를 사용하여 웹 애플리케이션의 보안을 강화할 수 있는 여러 가지 방법이 있다. 주요 보안 강화 방법은 다음과 같다.

1. **최신 SSL/TLS 버전 사용:**
    - 가능한 최신 버전인 TLS 1.3을 사용하여 보안 취약점을 최소화한다.
    - 구버전 SSL/TLS는 보안 취약점이 발견되어 사용을 피해야 한다.
2. **강력한 암호화 알고리즘 선택:**
    - 강력한 암호화 알고리즘과 키 교환 방식을 선택하여 데이터 보호를 강화한다.
    - 예: ECDHE-RSA-AES256-GCM-SHA384
3. **HSTS (HTTP Strict Transport Security) 설정:**
    - 클라이언트에게 HTTPS 연결을 강제하도록 지시하여 중간자 공격을 방지한다.
    - 예제:
        
        ```
        Strict-Transport-Security: max-age=31536000; includeSubDomains; preloa
        ```
        
4. **인증서 관리 및 갱신:**
    - SSL/TLS 인증서를 정기적으로 갱신하고, 신뢰할 수 있는 인증 기관에서 발급받는다.
    - 인증서 유출 시 즉시 폐기하고 새로운 인증서를 발급받는다.
5. **완전한 인증서 체인 사용:**
    - 서버에 완전한 인증서 체인을 구성하여 클라이언트가 서버를 신뢰할 수 있도록 한다.
    - 루트 인증서, 중간 인증서, 서버 인증서가 모두 포함되어야 한다.
6. **보안 헤더 추가:**
    - HTTPS와 함께 보안 헤더를 설정하여 추가적인 보안 계층을 제공한다.
    - 예: `Content-Security-Policy`, `X-Content-Type-Options`, `X-Frame-Options`, `X-XSS-Protection`
7. **취약점 스캐닝 및 모니터링:**
    - 정기적으로 SSL/TLS 설정과 인증서를 스캐닝하여 취약점을 발견하고 수정한다.
    - 모니터링 도구를 사용하여 실시간으로 보안 상태를 확인한다.
8. **HTTP/2 및 HTTP/3 사용:**
    - 최신 HTTP 버전을 사용하여 보안과 성능을 동시에 향상시킨다.
    - HTTP/3는 추가적인 보안 기능과 성능 개선을 제공한다.

### 6.3 HTTPS 설정 예제

**예제 1: Nginx 서버에 HTTPS 설정**

1. **SSL 인증서 획득:**
    - Let's Encrypt와 같은 무료 인증 기관을 사용하거나, 유료 인증서를 구매한다.
    - 인증서를 `/etc/ssl/certs/`에 저장하고, 개인 키를 `/etc/ssl/private/`에 저장한다.
2. **Nginx 설정 파일 수정:**
    - 서버 블록에 SSL 설정을 추가한다.
    - 예제:
        
        ```
        server {
            listen 443 ssl http2;
            server_name www.example.com;
        
            ssl_certificate /etc/ssl/certs/example.com.crt;
            ssl_certificate_key /etc/ssl/private/example.com.key;
        
            ssl_protocols TLSv1.2 TLSv1.3;
            ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';
            ssl_prefer_server_ciphers on;
        
            add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
        
            # 기타 설정
            ...
        }
        ```
        
3. **HTTP에서 HTTPS로 리다이렉션 설정:**
    - HTTP 요청을 HTTPS로 리다이렉트하여 모든 트래픽이 안전하게 전송되도록 한다.
    - 예제:
        
        ```
        server {
            listen 80;
            server_name www.example.com;
        
            return 301 https://$host$request_uri;
        }
        ```
        
4. **Nginx 재시작:**
    - 설정 변경을 적용하기 위해 Nginx를 재시작한다.
        
        ```bash
        sudo systemctl restart nginx
        ```
        

**예제 2: Apache 서버에 HTTPS 설정**

1. **SSL 모듈 활성화:**
    - Apache에서 SSL 모듈을 활성화한다.
        
        ```bash
        sudo a2enmod ssl
        sudo a2ensite default-ssl
        ```
        
2. **SSL 인증서 설정:**
    - 인증서 파일과 개인 키 파일을 지정한다.
    - 예제 (`/etc/apache2/sites-available/default-ssl.conf`):
        
        ```
        <VirtualHost _default_:443>
            ServerAdmin webmaster@example.com
            ServerName www.example.com
        
            SSLEngine on
            SSLCertificateFile /etc/ssl/certs/example.com.crt
            SSLCertificateKeyFile /etc/ssl/private/example.com.key
        
            SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
            SSLCipherSuite HIGH:!aNULL:!MD5
            SSLHonorCipherOrder on
        
            Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        
            # 기타 설정
            ...
        </VirtualHost>
        ```
        
3. **HTTP에서 HTTPS로 리다이렉션 설정:**
    - `.htaccess` 파일이나 서버 설정을 통해 HTTP 요청을 HTTPS로 리다이렉트한다.
    - 예제 (`.htaccess`):
        
        ```
        RewriteEngine On
        RewriteCond %{HTTPS} !=on
        RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R=301,L]
        ```
        
4. **Apache 재시작:**
    - 설정 변경을 적용하기 위해 Apache를 재시작한다.
        
        ```bash
        sudo systemctl restart apache2
        ```
        

### 6.4 HTTPS 보안 강화 팁

- **강력한 암호화 설정:** 최신 TLS 버전을 사용하고, 강력한 암호화 알고리즘을 선택하여 보안을 강화한다.
- **인증서 투명성 로그 활용:** 인증서 발급 시 투명성 로그를 사용하여 인증서의 신뢰성을 높인다.
- **중간 인증서 체인 확인:** 중간 인증서가 올바르게 설정되어 있는지 확인하여 인증서 체인의 무결성을 보장한다.
- **정기적인 보안 감사:** SSL/TLS 설정과 인증서를 정기적으로 감사하여 취약점을 발견하고 수정한다.
- **자동화된 인증서 갱신:** Let's Encrypt와 같은 서비스를 사용하여 인증서 갱신을 자동화함으로써 인증서 만료로 인한 서비스 중단을 방지한다.

## 7. HTTP 쿠키

HTTP 쿠키는 클라이언트와 서버 간의 상태 정보를 저장하고 관리하는 데 사용되는 작은 데이터 조각이다. 쿠키는 웹 애플리케이션에서 사용자 세션을 유지하고, 사용자 설정을 저장하며, 추적 목적으로 활용된다. 이 장에서는 쿠키의 정의, 작동 방식, 그리고 보안 고려사항에 대해 학습한다.

### 7.1 쿠키란?

- *쿠키(Cookie)**는 웹 서버가 클라이언트(주로 웹 브라우저)에 저장하는 작은 텍스트 파일이다. 쿠키는 사용자 식별, 세션 관리, 개인화된 설정 저장, 추적 등의 목적으로 사용된다.
- **주요 특징:**
    - **크기 제한:** 하나의 쿠키는 최대 약 4KB의 데이터를 저장할 수 있다.
    - **유효 기간:** 쿠키는 세션 쿠키와 영구 쿠키로 구분된다. 세션 쿠키는 브라우저가 종료되면 삭제되며, 영구 쿠키는 설정된 만료 날짜까지 유지된다.
    - **도메인 및 경로 제한:** 쿠키는 특정 도메인과 경로에만 접근할 수 있어 보안이 강화된다.
    - **보안 속성:** `Secure`, `HttpOnly`, `SameSite` 등의 속성을 설정하여 쿠키의 보안 수준을 높일 수 있다.
- **사용 사례:**
    - **사용자 인증:** 로그인 상태를 유지하기 위해 세션 ID를 쿠키에 저장.
    - **개인화 설정:** 사용자 선호 테마, 언어 설정 등을 쿠키에 저장.
    - **트래킹:** 사용자 행동을 추적하여 웹사이트 개선 및 맞춤형 광고 제공.

### 7.2 쿠키의 작동 방식

쿠키는 클라이언트와 서버 간의 요청과 응답 과정에서 주고받으며, 다음과 같은 방식으로 작동한다.

### **쿠키 설정 과정**

1. **서버에서 쿠키 설정:**
    - 서버는 응답 헤더에 `Set-Cookie` 헤더를 포함하여 클라이언트에게 쿠키를 설정하도록 지시한다.
    - 예제:
        
        ```
        HTTP/1.1 200 OK
        Set-Cookie: sessionId=abc123; Path=/; HttpOnly; Secure; SameSite=Strict
        Content-Type: text/html
        Content-Length: 150
        
        <html>
          <head><title>Welcome</title></head>
          <body>...</body>
        </html>
        ```
        
2. **클라이언트에서 쿠키 저장:**
    - 웹 브라우저는 `Set-Cookie` 헤더의 내용을 해석하여 쿠키를 저장한다.
    - 저장된 쿠키는 지정된 도메인과 경로에 따라 관리된다.
3. **클라이언트에서 쿠키 전송:**
    - 클라이언트는 이후의 요청 시, 해당 도메인과 경로에 일치하는 쿠키를 `Cookie` 헤더에 포함하여 서버로 전송한다.
    - 예제:
        
        ```
        GET /dashboard HTTP/1.1
        Host: www.example.com
        Cookie: sessionId=abc123
        Accept: text/html
        ```
        

### **쿠키의 주요 속성**

- **Name=Value:** 쿠키의 이름과 값.
- **Expires/Max-Age:** 쿠키의 만료 날짜 또는 지속 시간.
- **Domain:** 쿠키가 유효한 도메인.
- **Path:** 쿠키가 유효한 경로.
- **Secure:** HTTPS 연결에서만 쿠키를 전송.
- **HttpOnly:** 클라이언트 측 스크립트에서 쿠키 접근을 제한.
- **SameSite:** 크로스 사이트 요청 시 쿠키 전송 정책 (`Strict`, `Lax`, `None`).

### **쿠키의 작동 흐름 예시**

1. **사용자 로그인:**
    - 사용자가 로그인 폼을 제출하면, 서버는 인증 정보를 확인한 후 `Set-Cookie` 헤더를 통해 세션 ID를 쿠키로 설정한다.
2. **세션 유지:**
    - 클라이언트는 이후의 요청 시마다 쿠키에 저장된 세션 ID를 서버로 전송하여 사용자의 인증 상태를 유지한다.
3. **로그아웃:**
    - 사용자가 로그아웃하면, 서버는 `Set-Cookie` 헤더를 사용하여 쿠키의 만료 날짜를 과거로 설정하거나 삭제 지시를 내려 쿠키를 제거한다.

### 7.3 보안 고려사항

쿠키는 사용자 정보를 저장하고 전송하는 중요한 역할을 하기 때문에 보안에 유의해야 한다. 다음은 쿠키 사용 시 고려해야 할 주요 보안 사항이다.

### **1. HttpOnly 속성 사용**

- **설명:** `HttpOnly` 속성을 설정하면 클라이언트 측 스크립트(예: JavaScript)에서 쿠키에 접근할 수 없게 된다.
- **목적:** XSS(Cross-Site Scripting) 공격으로부터 쿠키를 보호.
- **설정 예시:**
    
    ```
    Set-Cookie: sessionId=abc123; HttpOnly
    ```
    

### **2. Secure 속성 사용**

- **설명:** `Secure` 속성을 설정하면 쿠키가 HTTPS 연결을 통해서만 전송된다.
- **목적:** 쿠키가 평문으로 전송되는 것을 방지하여 중간자 공격(MITM)을 예방.
- **설정 예시:**
    
    ```
    Set-Cookie: sessionId=abc123; Secure
    ```
    

### **3. SameSite 속성 설정**

- **설명:** `SameSite` 속성을 설정하여 크로스 사이트 요청 시 쿠키 전송 여부를 제어.
    - **Strict:** 동일한 사이트 내에서만 쿠키 전송.
    - **Lax:** 일부 크로스 사이트 요청에서도 쿠키 전송(예: GET 요청).
    - **None:** 모든 크로스 사이트 요청에서 쿠키 전송(단, `Secure` 속성 필요).
- **목적:** CSRF(Cross-Site Request Forgery) 공격을 방지.
- **설정 예시:**
    
    ```
    Set-Cookie: sessionId=abc123; SameSite=Strict
    ```
    

### **4. 쿠키 데이터 암호화**

- **설명:** 쿠키에 민감한 데이터를 저장할 경우, 데이터를 암호화하여 저장한다.
- **목적:** 쿠키 데이터가 탈취되더라도 내용을 해독할 수 없도록 보호.
- **방법:** 서버 측에서 데이터를 암호화하여 쿠키에 저장하고, 필요 시 복호화하여 사용한다.

### **5. 쿠키 만료 설정**

- **설명:** 쿠키의 `Expires` 또는 `Max-Age` 속성을 적절히 설정하여 쿠키의 유효 기간을 제한한다.
- **목적:** 오래된 쿠키가 남아있지 않도록 하여 보안 위험을 줄인다.
- **설정 예시:**
    
    ```
    Set-Cookie: sessionId=abc123; Max-Age=360
    ```
    

### **6. 도메인 및 경로 제한**

- **설명:** 쿠키의 `Domain`과 `Path` 속성을 설정하여 쿠키가 유효한 도메인과 경로를 제한한다.
- **목적:** 쿠키가 불필요하게 넓은 범위에서 사용되지 않도록 하여 보안 강화.
- **설정 예시:**
    
    ```
    Set-Cookie: sessionId=abc123; Domain=www.example.com; Path=/secure
    ```
    

### **7. 세션 관리**

- **설명:** 세션 쿠키는 브라우저 세션이 종료되면 삭제되도록 설정한다.
- **목적:** 세션 하이재킹을 방지.
- **설정 예시:**
    
    ```
    Set-Cookie: sessionId=abc123; Expires=Wed, 21 Oct 2025 07:28:00 GMT; Path=/
    ```
    

### 7.4 HTTP 쿠키 요약표

| 헤더 종류 | 헤더 이름 | 역할 및 설명 | 사용 사례 |
| --- | --- | --- | --- |
| **요청 헤더** | Cookie | 서버에 저장된 쿠키 데이터 전송 | 세션 유지, 사용자 추적 |
| **응답 헤더** | Set-Cookie | 클라이언트에 쿠키 설정 | 세션 관리, 사용자 설정 저장 |
| **공통 헤더** | - | 쿠키 관련 공통 속성 설정 | 보안 강화, 데이터 무결성 유지 |

### 7.5 HTTP 쿠키 활용 방법

HTTP 쿠키를 올바르게 이해하고 사용하는 것은 웹 개발과 사용자 경험 개선에 중요하다. 각 쿠키의 역할과 보안 속성을 적절히 활용하여 안전하고 효율적인 웹 애플리케이션을 구축할 수 있다.

- **클라이언트 측 활용:**
    - **세션 유지:** `Cookie` 헤더를 사용하여 세션 ID를 서버로 전송하고, 사용자의 로그인 상태를 유지한다.
    - **개인화 설정 저장:** 사용자의 선호 테마, 언어 설정 등을 쿠키에 저장하여 개인화된 경험을 제공한다.
    - **트래킹 및 분석:** 사용자 행동을 추적하여 웹사이트 개선 및 맞춤형 광고를 제공한다.
- **서버 측 활용:**
    - **세션 관리:** `Set-Cookie` 헤더를 사용하여 세션 ID를 클라이언트에 설정하고, 서버에서 세션 정보를 관리한다.
    - **보안 강화:** `HttpOnly`, `Secure`, `SameSite` 속성을 설정하여 쿠키의 보안 수준을 높인다.
    - **캐싱 최적화:** 쿠키를 활용하여 사용자별로 캐시를 관리하고, 불필요한 데이터 전송을 줄인다.
    - **개인화된 응답 제공:** 쿠키에 저장된 정보를 기반으로 사용자에게 맞춤형 콘텐츠를 제공한다.

### 7.6 HTTP 쿠키 처리 예제

**예제 1: 사용자 로그인 및 세션 관리**

- **요청:**
    
    ```
    POST /login HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    Accept: application/json
    
    {
      "username": "alice",
      "password": "securepassword"
    }
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 200 OK
    Set-Cookie: sessionId=abc123; Path=/; HttpOnly; Secure; SameSite=Strict
    Content-Type: application/json
    Content-Length: 89
    
    {
      "message": "Login successful",
      "userId": 124
    }
    ```
    
- **클라이언트 요청 시 쿠키 전송:**
    
    ```
    GET /dashboard HTTP/1.1
    Host: api.example.com
    Cookie: sessionId=abc123
    Accept: application/json
    ```
    

**예제 2: 사용자 로그아웃 및 쿠키 삭제**

- **요청:**
    
    ```
    POST /logout HTTP/1.1
    Host: api.example.com
    Cookie: sessionId=abc123
    Accept: application/jso
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 200 OK
    Set-Cookie: sessionId=abc123; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT
    Content-Type: application/json
    Content-Length: 78
    
    {
      "message": "Logout successful",
      "userId": 124
    }
    ```
    

**예제 3: 개인화 설정 저장**

- **요청:**
    
    ```
    POST /settings HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    Cookie: sessionId=abc123
    Accept: application/json
    
    {
      "theme": "dark",
      "language": "ko"
    }
    ```
    
- **응답 (성공):**
    
    ```
    HTTP/1.1 200 OK
    Set-Cookie: userSettings=theme=dark;language=ko; Path=/; HttpOnly
    Content-Type: application/json
    Content-Length: 85
    
    {
      "message": "Settings updated successfully",
      "userId": 124
    }
    ```

## 8. RESTful API와 HTTP

RESTful API는 REST(Representational State Transfer) 아키텍처 스타일을 따르는 API로, HTTP 프로토콜의 메서드와 상태 코드를 효과적으로 활용하여 클라이언트와 서버 간의 상호작용을 설계한다. 

### 8.1 REST 아키텍처 스타일과 HTTP의 관계

### **REST 아키텍처 스타일**

REST는 웹 아키텍처의 원칙을 따르는 아키텍처 스타일로, 시스템 간의 통신을 단순화하고 확장성을 높이기 위해 설계되었다. REST의 주요 원칙은 다음과 같다.

- **클라이언트-서버 구조:** 클라이언트와 서버는 명확하게 분리되어 독립적으로 발전할 수 있다.
- **무상태성 (Stateless):** 각 요청은 독립적으로 처리되며, 서버는 이전 요청의 상태를 유지하지 않는다.
- **캐시 가능성 (Cacheable):** 응답은 캐시될 수 있어 클라이언트의 성능을 향상시킨다.
- **일관된 인터페이스 (Uniform Interface):** 일관된 인터페이스를 통해 클라이언트와 서버 간의 상호작용을 단순화한다.
- **계층화된 시스템 (Layered System):** 클라이언트는 중간 계층을 인지하지 못하며, 중간 계층을 통해 요청이 전달될 수 있다.
- **코드 온 디맨드 (Code on Demand) (선택적):** 서버는 클라이언트에게 코드를 전송하여 실행할 수 있다.

### **HTTP와 REST의 관계**

HTTP는 REST 아키텍처 스타일의 기본 통신 프로토콜로 사용된다. REST의 원칙을 효과적으로 구현하기 위해 HTTP의 메서드, 상태 코드, 헤더 등을 적절히 활용한다. 주요 관계는 다음과 같다.

- **자원(Resource):** REST에서는 모든 것을 자원으로 간주하며, 각 자원은 고유한 URI를 가진다. HTTP의 URI를 통해 자원을 식별한다.
- **HTTP 메서드:** REST의 주요 작업(Create, Read, Update, Delete)은 HTTP 메서드(GET, POST, PUT, DELETE 등)를 통해 구현된다.
- **상태 코드:** 서버는 클라이언트의 요청에 대해 적절한 HTTP 상태 코드를 반환하여 요청의 결과를 전달한다.
- **헤더:** HTTP 헤더를 통해 요청과 응답에 추가적인 정보를 전달하여 RESTful한 상호작용을 지원한다.

### 8.2 RESTful API 설계 시 HTTP 메서드 활용 방법

RESTful API를 설계할 때 HTTP 메서드를 효과적으로 활용하는 것은 매우 중요하다. 각 HTTP 메서드는 특정한 목적을 가지며, 이를 올바르게 사용함으로써 API의 직관성과 효율성을 높일 수 있다. 주요 HTTP 메서드와 그 활용 방법은 다음과 같다.

### **GET**

- **목적:** 서버에서 자원을 조회할 때 사용한다.
- **특징:**
    - **안전성 (Safe):** 서버의 상태를 변경하지 않는다.
    - **멱등성 (Idempotent):** 동일한 요청을 여러 번 보내도 결과가 동일하다.
    - **캐싱 가능:** 응답을 캐시할 수 있어 성능 향상에 기여한다.
- **사용 사례:**
    - 특정 사용자의 정보를 조회할 때.
    - 제품 목록을 가져올 때.
- **예제:**
    
    ```
    GET /users/123 HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```
    

### **POST**

- **목적:** 서버에 새로운 자원을 생성할 때 사용한다.
- **특징:**
    - **비안전성 (Unsafe):** 서버의 상태를 변경할 수 있다.
    - **비멱등성 (Non-idempotent):** 동일한 요청을 여러 번 보내면 여러 자원이 생성될 수 있다.
    - **데이터 전달:** 요청 본문(body)에 데이터를 포함시킨다.
- **사용 사례:**
    - 새로운 사용자를 등록할 때.
    - 새로운 게시물을 작성할 때.
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
    

### **PUT**

- **목적:** 서버에 특정 자원을 업데이트하거나, 존재하지 않을 경우 새로 생성할 때 사용한다.
- **특징:**
    - **안전성:** 요청의 의도에 따라 안전할 수 있다.
    - **멱등성 (Idempotent):** 동일한 요청을 여러 번 보내도 결과가 동일하다.
    - **데이터 전달:** 요청 본문에 전체 자원 데이터를 포함시킨다.
- **사용 사례:**
    - 사용자의 전체 정보를 업데이트할 때.
    - 특정 문서를 전체 교체할 때.
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
    

### **PATCH**

- **목적:** 서버에 특정 자원의 일부를 수정할 때 사용한다.
- **특징:**
    - **비안전성 (Unsafe):** 자원을 수정할 수 있다.
    - **비멱등성 (Non-idempotent):** 동일한 요청을 여러 번 보내면 결과가 달라질 수 있다.
    - **데이터 전달:** 요청 본문에 수정할 데이터만 포함시킨다.
- **사용 사례:**
    - 사용자의 이메일 주소만 업데이트할 때.
    - 게시물의 제목만 변경할 때.
- **예제:**
    
    ```
    PATCH /users/123 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "email": "john.updated@example.com"
    }
    ```
    

### **DELETE**

- **목적:** 서버에서 특정 자원을 삭제할 때 사용한다.
- **특징:**
    - **안전성:** 자원을 삭제하므로 안전하지 않을 수 있다.
    - **멱등성 (Idempotent):** 동일한 요청을 여러 번 보내도 결과는 동일하다.
- **사용 사례:**
    - 사용자를 삭제할 때.
    - 게시물을 삭제할 때.
- **예제:**
    
    ```
    DELETE /users/123 HTTP/1.1
    Host: api.example.com
    ```
    

### **HEAD**

- **목적:** GET과 동일한 요청을 보내되, 응답 본문을 포함하지 않는다.
- **특징:**
    - **안전성 (Safe):** 서버의 상태를 변경하지 않는다.
    - **멱등성 (Idempotent):** 동일한 요청을 여러 번 보내도 결과가 동일하다.
    - **캐싱 가능:** GET과 마찬가지로 캐시될 수 있다.
- **사용 사례:**
    - 리소스의 존재 여부를 확인할 때.
    - 리소스의 메타데이터를 조회할 때.
- **예제:**
    
    ```
    HEAD /users/123 HTTP/1.1
    Host: api.example.com
    ```
    

### **OPTIONS**

- **목적:** 특정 자원이 지원하는 HTTP 메서드의 목록을 요청할 때 사용한다.
- **특징:**
    - **안전성 (Safe):** 서버의 상태를 변경하지 않는다.
    - **멱등성 (Idempotent):** 동일한 요청을 여러 번 보내도 결과가 동일하다.
    - **데이터 전달:** `Allow` 헤더를 통해 지원되는 메서드 목록을 반환한다.
- **사용 사례:**
    - CORS 사전 요청 시 사용.
    - API가 지원하는 메서드를 확인할 때.
- **예제:**
    
    ```
    OPTIONS /users/123 HTTP/1.1
    Host: api.example.com
    ```
    

### 8.3 RESTful API 설계 시 HTTP 메서드 활용 방법

RESTful API를 설계할 때 HTTP 메서드를 효과적으로 활용하는 것은 API의 직관성과 효율성을 높이는 데 중요하다. 다음은 RESTful API 설계 시 각 HTTP 메서드를 활용하는 방법이다.

### **자원 기반 URI 설계**

RESTful API는 자원(Resource)을 중심으로 URI를 설계한다. 자원은 고유한 URI를 가지며, HTTP 메서드를 통해 자원에 대한 작업을 수행한다.

- **자원 식별:** `/users`, `/posts`, `/products`와 같은 명사형 URI를 사용하여 자원을 식별한다.
- **자원의 계층 구조:** `/users/123/posts/456`와 같이 자원의 계층 구조를 반영한 URI를 사용한다.

### **HTTP 메서드를 통한 작업 정의**

각 HTTP 메서드는 특정 작업을 정의하며, 이를 일관되게 사용하여 API의 직관성을 높인다.

- **GET:** 자원의 조회. 예를 들어, `GET /users/123`은 사용자 123의 정보를 조회한다.
- **POST:** 새로운 자원의 생성. 예를 들어, `POST /users`는 새로운 사용자를 생성한다.
- **PUT:** 자원의 전체 업데이트 또는 생성. 예를 들어, `PUT /users/123`은 사용자 123의 정보를 전체적으로 업데이트하거나 존재하지 않을 경우 새로 생성한다.
- **PATCH:** 자원의 일부 업데이트. 예를 들어, `PATCH /users/123`은 사용자 123의 일부 정보를 업데이트한다.
- **DELETE:** 자원의 삭제. 예를 들어, `DELETE /users/123`은 사용자 123을 삭제한다.
- **HEAD:** 자원의 메타데이터 조회. 예를 들어, `HEAD /users/123`은 사용자 123의 헤더 정보를 조회한다.
- **OPTIONS:** 자원이 지원하는 메서드 목록 조회. 예를 들어, `OPTIONS /users/123`은 사용자 123이 지원하는 메서드를 조회한다.

### **HTTP 상태 코드 활용**

RESTful API는 HTTP 상태 코드를 적절하게 사용하여 클라이언트에게 요청의 결과를 명확하게 전달한다.

- **200 OK:** 요청이 성공적으로 처리되었음을 나타낸다.
- **201 Created:** 새로운 자원이 성공적으로 생성되었음을 나타낸다.
- **204 No Content:** 요청이 성공적으로 처리되었으나, 반환할 콘텐츠가 없음을 나타낸다.
- **400 Bad Request:** 클라이언트의 요청이 잘못되었음을 나타낸다.
- **401 Unauthorized:** 인증이 필요함을 나타낸다.
- **403 Forbidden:** 권한이 없어 요청을 거부함을 나타낸다.
- **404 Not Found:** 요청한 자원을 찾을 수 없음을 나타낸다.
- **405 Method Not Allowed:** 요청한 메서드가 지원되지 않음을 나타낸다.
- **409 Conflict:** 요청이 현재 서버의 상태와 충돌함을 나타낸다.
- **500 Internal Server Error:** 서버에서 예기치 못한 오류가 발생했음을 나타낸다.

### **URI 설계의 일관성 유지**

API의 URI는 일관성을 유지하여 클라이언트가 쉽게 이해하고 사용할 수 있도록 해야 한다.

- **복수형 사용:** 자원의 URI는 일반적으로 복수형을 사용한다. 예: `/users`, `/posts`.
- **명확한 계층 구조:** 자원의 관계를 명확히 반영한 계층 구조를 사용한다. 예: `/users/123/posts`는 사용자 123의 게시물을 나타낸다.
- **명사 사용:** URI는 동사가 아닌 명사를 사용하여 자원을 식별한다. 예: `/users`, `/orders`.

### **필터링, 정렬, 페이징**

RESTful API는 자원의 조회 시 필터링, 정렬, 페이징 기능을 제공하여 클라이언트가 필요한 데이터를 효율적으로 요청할 수 있도록 한다.

- **필터링:** 쿼리 파라미터를 사용하여 특정 조건에 맞는 자원을 조회한다. 예: `GET /users?role=admin`.
- **정렬:** 쿼리 파라미터를 사용하여 자원의 정렬 순서를 지정한다. 예: `GET /users?sort=name`.
- **페이징:** 쿼리 파라미터를 사용하여 자원의 페이지를 지정한다. 예: `GET /users?page=2&limit=50`.

### **HATEOAS (Hypermedia as the Engine of Application State)**

HATEOAS는 REST의 중요한 원칙 중 하나로, 클라이언트가 응답을 통해 다음 가능한 동작에 대한 링크를 제공받아 API를 탐색할 수 있도록 한다.

- **링크 포함:** 응답에 관련된 자원의 링크를 포함시킨다. 예:
    
    ```json
    {
      "id": 123,
      "name": "John Doe",
      "links": {
        "self": "/users/123",
        "posts": "/users/123/posts"
      }
    }
    ```
    
- **동적 API 탐색:** 클라이언트는 응답에 포함된 링크를 따라가며 API를 동적으로 탐색할 수 있다.

### 8.4 RESTful API 설계 예제

**예제 1: 사용자 관리 API**

- **사용자 목록 조회**
    
    ```
    GET /users HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```
    
- **새 사용자 생성**
    
    ```
    POST /users HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "name": "Alice",
      "email": "alice@example.com"
    }
    ```
    
- **특정 사용자 정보 조회**
    
    ```
    GET /users/123 HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```
    
- **사용자 정보 전체 업데이트**
    
    ```
    PUT /users/123 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "name": "Alice Smith",
      "email": "alice.smith@example.com"
    }
    ```
    
- **사용자 정보 일부 업데이트**
    
    ```
    PATCH /users/123 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "email": "alice.new@example.com"
    }
    ```
    
- **사용자 삭제**
    
    ```
    DELETE /users/123 HTTP/1.1
    Host: api.example.com
    ```
    

**예제 2: 게시물 관리 API**

- **게시물 목록 조회**
    
    ```
    GET /posts HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```
    
- **새 게시물 생성**
    
    ```
    POST /posts HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "title": "New Post",
      "content": "This is the content of the new post."
    }
    ```
    
- **특정 게시물 조회**
    
    ```
    GET /posts/456 HTTP/1.1
    Host: api.example.com
    Accept: application/json
    ```
    
- **게시물 전체 업데이트**
    
    ```
    PUT /posts/456 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "title": "Updated Post",
      "content": "This is the updated content."
    }
    ```
    
- **게시물 일부 업데이트**
    
    ```
    PATCH /posts/456 HTTP/1.1
    Host: api.example.com
    Content-Type: application/json
    
    {
      "title": "Partially Updated Post"
    }
    ```
    
- **게시물 삭제**
    
    ```
    DELETE /posts/456 HTTP/1.1
    Host: api.example.com
    ```
    

### 8.5 RESTful API 설계의 모범 사례

RESTful API를 효과적으로 설계하기 위해 다음과 같은 모범 사례를 따르는 것이 중요하다.

- **일관된 네이밍 컨벤션:** 자원 이름은 일관되고 직관적으로 설정하여 클라이언트가 쉽게 이해할 수 있도록 한다.
- **명확한 자원 식별:** 각 자원은 고유한 URI를 가져야 하며, URI는 명사형으로 설계한다.
- **HTTP 메서드의 올바른 사용:** 각 HTTP 메서드는 그 목적에 맞게 일관되게 사용하여 API의 직관성을 높인다.
- **적절한 상태 코드 사용:** 요청의 결과에 따라 적절한 HTTP 상태 코드를 반환하여 클라이언트가 요청의 결과를 명확하게 이해할 수 있도록 한다.
- **HATEOAS 준수:** 응답에 관련된 자원의 링크를 포함시켜 클라이언트가 API를 동적으로 탐색할 수 있도록 한다.
- **버전 관리:** API의 버전을 명시하여 클라이언트와 서버 간의 호환성을 유지한다. 예: `/v1/users`
- **보안 강화:** HTTPS를 사용하고, 인증 및 권한 부여 메커니즘을 구현하여 API의 보안을 강화한다.
- **문서화:** API의 사용 방법과 각 엔드포인트의 기능을 명확하게 문서화하여 클라이언트 개발자가 쉽게 사용할 수 있도록 한다.

## 9. HTTP 캐싱

HTTP 캐싱은 웹 애플리케이션의 성능을 향상시키고, 서버 부하를 줄이며, 사용자 경험을 개선하는 데 중요한 역할을 한다. 이 장에서는 캐싱의 중요성과 HTTP 캐싱 메커니즘, 그리고 캐시 관련 헤더의 설정과 관리 방법에 대해 학습한다.

### 9.1 캐싱의 중요성과 HTTP 캐싱 메커니즘

### **캐싱의 중요성**

웹 애플리케이션에서 캐싱은 반복되는 요청에 대해 응답 시간을 단축하고, 네트워크 대역폭을 절약하며, 서버의 부하를 줄이는 데 기여한다. 캐싱을 통해 다음과 같은 이점을 얻을 수 있다.

- **성능 향상:** 클라이언트는 캐시된 데이터를 빠르게 로드하여 페이지 로딩 속도를 개선할 수 있다.
- **네트워크 효율성:** 동일한 데이터를 반복적으로 다운로드할 필요가 없어 네트워크 트래픽을 줄일 수 있다.
- **서버 부하 감소:** 서버는 캐시된 데이터를 재사용함으로써 요청 처리에 소요되는 자원을 절약할 수 있다.
- **사용자 경험 개선:** 빠른 응답으로 사용자에게 원활한 인터페이스를 제공할 수 있다.

### **HTTP 캐싱 메커니즘**

HTTP 캐싱은 클라이언트(주로 웹 브라우저)와 중간 캐시 서버(프록시 서버, CDN 등)가 서버로부터 받은 응답을 저장하고 재사용하는 과정을 말한다. HTTP 캐싱 메커니즘은 다음과 같은 요소로 구성된다.

1. **캐시 저장소(Cache Storage):**
    - **클라이언트 캐시:** 사용자의 브라우저에 저장된 캐시.
    - **중간 캐시:** 프록시 서버나 CDN과 같은 중간 서버에 저장된 캐시.
2. **캐시 정책(Cache Policy):**
    - 서버는 응답 헤더를 통해 캐시가 어떻게 동작해야 하는지 지시한다.
    - 클라이언트와 중간 캐시 서버는 이 지침을 따라 캐시를 저장하고 재사용한다.
3. **캐시 유효성 검사(Cache Validation):**
    - 클라이언트는 캐시된 리소스가 최신인지 확인하기 위해 서버에 조건부 요청을 보낸다.
    - 조건부 요청은 `If-Modified-Since` 또는 `If-None-Match` 헤더를 사용한다.
    - 서버는 리소스가 변경되지 않았을 경우 `304 Not Modified` 상태 코드를 반환하여 캐시된 리소스를 재사용하도록 한다.
4. **캐시 무효화(Cache Invalidation):**
    - 리소스가 변경되었을 때, 서버는 새로운 리소스를 제공하거나 캐시를 무효화한다.
    - 이를 통해 클라이언트는 최신 데이터를 받을 수 있다.

### 9.2 캐시 관련 헤더의 설정과 관리

HTTP 캐싱은 다양한 헤더를 통해 제어할 수 있으며, 각 헤더는 캐시 동작에 대한 특정한 지침을 제공한다. 주요 캐시 관련 헤더와 그 설정 방법은 다음과 같다.

### **1. Cache-Control**

- **역할:** 캐시의 동작 방식을 세부적으로 제어한다.
- **사용 사례:** 캐싱 정책을 명확하게 지정하여 클라이언트와 중간 캐시 서버가 이를 준수하도록 한다.
- **설정 예시:**
    
    ```
    Cache-Control: max-age=3600, must-revalidate
    ```
    
    - **max-age=3600:** 리소스가 최대 3600초(1시간) 동안 캐시될 수 있음을 의미.
    - **must-revalidate:** 캐시된 리소스가 만료되면 반드시 서버에 유효성을 검사해야 함을 의미.

### **2. Expires**

- **역할:** 리소스의 만료 날짜와 시간을 지정한다.
- **사용 사례:** 특정 시점까지 리소스가 캐시될 수 있도록 설정.
- **설정 예시:**
    
    ```
    Expires: Wed, 21 Oct 2025 07:28:00 GMT
    ```
    
    - 리소스가 2025년 10월 21일 07:28:00 GMT까지 캐시될 수 있음을 의미.

### **3. ETag**

- **역할:** 리소스의 고유 식별자를 제공하여 캐시된 리소스의 유효성을 검사한다.
- **사용 사례:** 조건부 요청 시 리소스가 변경되었는지 확인.
- **설정 예시:**
    
    ```
    ETag: "686897696a7c876b7e"
    ```
    
    - 리소스의 특정 버전을 식별하는 고유한 태그를 제공.

### **4. Last-Modified**

- **역할:** 리소스가 마지막으로 수정된 날짜와 시간을 지정한다.
- **사용 사례:** 조건부 요청 시 리소스의 변경 여부를 확인.
- **설정 예시:**
    
    ```
    Last-Modified: Wed, 21 Oct 2020 07:28:00 GMT
    ```
    
    - 리소스가 2020년 10월 21일 07:28:00 GMT에 마지막으로 수정되었음을 의미.

### **5. Vary**

- **역할:** 캐시된 리소스를 저장할 때 어떤 요청 헤더를 기준으로 캐시할지 지정한다.
- **사용 사례:** 다양한 요청 헤더에 따라 다른 캐시를 제공.
- **설정 예시:**
    
    ```
    Vary: Accept-Encoding
    ```
    
    - `Accept-Encoding` 헤더의 값에 따라 캐시를 다르게 관리.

### **6. Pragma**

- **역할:** HTTP/1.0에서 캐시 정책을 제어하기 위해 사용되며, 주로 `no-cache` 값을 가진다.
- **사용 사례:** 구형 브라우저와의 호환성을 위해 사용.
- **설정 예시:**
    
    ```
    Pragma: no-cache
    ```
    
    - 클라이언트가 캐시를 사용하지 않고 서버에서 직접 데이터를 가져오도록 지시.

### **7. Age**

- **역할:** 리소스가 캐시에 저장된 후 경과한 시간을 초 단위로 표시한다.
- **사용 사례:** 캐시된 리소스의 최신성을 평가.
- **설정 예시:**
    
    ```
    Age: 120
    ```
    
    - 리소스가 캐시에 저장된 후 120초가 경과했음을 의미.

### 9.3 HTTP 캐싱 설정 예제

**예제 1: 정적 리소스에 대한 캐싱 설정 (Nginx)**

1. **Nginx 설정 파일 수정:**
    - 정적 리소스(이미지, CSS, JavaScript 등)에 대한 캐싱 정책을 설정.
    - 예제:
        
        ```
        server {
            listen 80;
            server_name www.example.com;
        
            location /static/ {
                root /var/www/html;
                expires 30d;
                add_header Cache-Control "public, max-age=2592000";
            }
        
            # 기타 설정
            ...
        }
        ```
        
2. **설정 설명:**
    - `/static/` 경로의 리소스는 30일 동안 캐시될 수 있으며, `Cache-Control` 헤더를 통해 캐시 정책을 명시적으로 설정.

**예제 2: 동적 컨텐츠에 대한 캐싱 제어 (Apache)**

1. **Apache 설정 파일 수정:**
    - 동적 컨텐츠에 대한 캐싱을 제어하기 위해 `mod_headers` 모듈을 사용.
    - 예제 (`.htaccess`):
        
        ```
        <IfModule mod_headers.c>
            Header set Cache-Control "no-cache, no-store, must-revalidate"
            Header set Pragma "no-cache"
            Header set Expires "0"
        </IfModule>
        ```
        
2. **설정 설명:**
    - 동적 컨텐츠는 캐시되지 않도록 설정하여 항상 최신 데이터를 제공.

### 9.4 HTTP 캐싱의 장단점

### **장점**

- **성능 향상:** 클라이언트는 캐시된 리소스를 빠르게 로드할 수 있어 페이지 로딩 속도가 개선된다.
- **네트워크 효율성:** 동일한 데이터를 반복적으로 다운로드할 필요가 없어 네트워크 트래픽이 감소한다.
- **서버 부하 감소:** 서버는 캐시된 데이터를 재사용하여 요청 처리에 소요되는 자원을 절약할 수 있다.
- **사용자 경험 개선:** 빠른 응답으로 사용자에게 원활한 인터페이스를 제공.

### **단점**

- **데이터 최신성 문제:** 캐시된 데이터가 오래될 경우, 사용자에게 최신 정보가 전달되지 않을 수 있다.
- **캐시 무효화 복잡성:** 리소스가 변경되었을 때 캐시를 적절히 무효화하지 않으면 문제가 발생할 수 있다.
- **보안 위험:** 민감한 데이터가 캐시에 저장될 경우, 보안 위협이 될 수 있다.

### 9.5 HTTP 캐싱 모범 사례

- **적절한 캐시 헤더 설정:** 리소스의 특성에 맞는 캐시 헤더를 설정하여 최적의 캐싱 정책을 적용.
- **캐시 무효화 전략:** 리소스가 변경될 때 캐시를 적절히 무효화하여 최신 데이터를 제공.
- **ETag 및 Last-Modified 사용:** 조건부 요청을 활용하여 캐시된 리소스의 최신성을 효율적으로 검사.
- **캐시 가능한 리소스와 비캐시 가능한 리소스 구분:** 정적 리소스는 캐시하고, 민감한 동적 리소스는 캐시하지 않도록 설정.
- **중간 캐시 서버 활용:** CDN과 같은 중간 캐시 서버를 활용하여 글로벌 사용자에게 빠른 응답을 제공.
- **보안 고려:** 민감한 데이터가 캐시에 저장되지 않도록 주의하고, `Cache-Control` 헤더를 적절히 설정.
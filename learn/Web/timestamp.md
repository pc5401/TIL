
# TIL: 타임스탬프(Timestamp) 정리

오늘 웹 개발하면서 시간 관리에 대한 코드를 작성했다. 그러고 보니 타임스탬프들에 대해 한번 정리하면 좋을 거 같아서 사용 예시와 함께 정리한다.

---

## 1. Unix Time (Epoch Time)

**설명**: Unix Time은 1970년 1월 1일 00:00:00 UTC(GMT)부터의 경과 시간을 `초 단위`로 표현한 방식이다.(js 처럼 언어 차원에서는 밀리초를 다루기도 한다.) 참고로 UTC는 협정 세계시를 의미하며, 이는 영국 런던의 그리니치 천문대에서 설정된 기준 시간이다. 한국 시간(KST)은 UTC보다 9시간 빠르다.

**사용처**:
- **상대적 시간 표현**: `1분 전`, `10분 전` 등 상대적인 시간을 표현하는 데 매우 적합했다. 현재 시간을 기준으로 과거 또는 미래의 시간을 쉽게 계산할 수 있다.
- **API 요청 및 응답**: 클라이언트-서버 간의 시간 데이터를 간결하게 주고받기 위해 사용된다.
- **데이터베이스 저장**: 시간 데이터를 간결하게 저장할 때 효율적이다. 예를 들어, MySQL에서는 Unix Time으로 시간을 저장하면 불필요한 포맷팅 없이 빠르게 조회 가능하다.

**예시**:
- `1694344805` (2024년 9월 10일 00:00:05 UTC)

**JavaScript 예시 코드**:
```js
// 현재 시간을 Unix Time으로 출력
const unixTime = Math.floor(Date.now() / 1000);
console.log(unixTime); // 1694344805 (예시 출력)

// 10분 전 시간 계산 (10 * 60초)
const tenMinutesAgo = unixTime - (10 * 60);
console.log(tenMinutesAgo); // 상대적 시간: 10분 전
```

**한국 시간(KST) 변환**:
```js
// 현재 시간을 한국 시간으로 변환
const now = new Date();
const kstTime = new Date(now.getTime() + (9 * 60 * 60 * 1000)); // 9시간 더하기
console.log(kstTime.toISOString()); // ISO 형식으로 한국 시간 출력
```

---

## 2. ISO 8601

**설명**: ISO 8601은 국제 표준 시간 표현 방식으로, 사람이 읽기 좋은 형식이다. 특히, UTC 기준의 시간을 'Z'로 나타낸다. ISO 형식은 시간대와 관련된 정보를 포함하기 때문에 글로벌 시스템에서 널리 사용된다.

**사용처**:
- **RESTful API**: 시간을 주고받을 때 사람이 읽기 쉬운 형식으로 데이터를 전달할 수 있다.
- **로그 파일 기록**: 로그를 남길 때, 특히 글로벌 환경에서 작업할 때 표준 시간대를 명시하기 위해 ISO 8601 형식을 사용한다.
- **JSON 데이터 교환**: 클라이언트와 서버 간의 데이터를 교환할 때 ISO 8601 형식은 시간대를 포함하므로 일관성을 유지하기 쉽다.

**예시**:
- `2024-09-10T12:00:00Z`

**JavaScript 예시 코드**:
```js
// 현재 시간을 ISO 8601 형식으로 출력
const isoTime = new Date().toISOString();
console.log(isoTime); // "2024-09-10T12:00:00.000Z" (예시 출력)

// 한국 시간으로 ISO 8601 형식 출력
const now = new Date();
const kstTime = new Date(now.getTime() + (9 * 60 * 60 * 1000));
console.log(kstTime.toISOString()); // 한국 시간으로 ISO 형식 출력
```

---

## 3. RFC 2822

**설명**: RFC 2822는 주로 이메일 및 HTTP 헤더에서 사용하는 시간 형식이다. 그리니치 천문대(Greenwich Mean Time, GMT)를 기준으로 한 UTC 시간대와 시차 정보를 포함한다. 이 형식은 사람이 읽기 쉽고 서버 간 통신에서 신뢰할 수 있는 시간 형식으로 사용된다.

**사용처**:
- **HTTP 헤더**: HTTP 응답에서 `Date` 필드에 시간을 표현할 때 이 형식을 사용한다.
- **이메일 헤더**: 이메일의 `Date` 필드에서 시간 정보가 RFC 2822 형식으로 기록된다.

**예시**:
- `Tue, 10 Sep 2024 12:00:00 +0000`

**JavaScript 예시 코드**:
```js
// 현재 시간을 RFC 2822 형식으로 출력
const rfcTime = new Date().toUTCString();
console.log(rfcTime); // "Tue, 10 Sep 2024 12:00:00 GMT" (예시 출력)

// 한국 시간으로 변환 후 출력
const kstTime = new Date();
kstTime.setHours(kstTime.getHours() + 9); // 9시간 더하기
console.log(kstTime.toUTCString()); // 한국 시간으로 RFC 형식 출력
```

---

### 결론
- **Unix Time**은 숫자로 처리하기 때문에 상대적 시간 계산에 매우 적합하고, 시스템 간 시간 동기화를 위해 자주 사용된다. 특히, "10분 전", "1시간 후" 등의 상대적 시간 계산이 쉽게 가능했다.
- **ISO 8601**은 글로벌 환경에서 시간대를 고려해 시간을 표현하는 데 유리하다. 특히 REST API와 JSON 데이터 전송 시에 자주 사용된다.
- **RFC 2822**는 이메일 및 HTTP 통신에서 중요한 타임스탬프 형식이다. 클라이언트와 서버 간의 시간 통신에서 신뢰할 수 있는 형식으로 사용된다.(자주 사용은 안 할듯)
- **시차 처리**는 웹 개발필수적이다. 특히 개발자로서 KST(한국 표준시)와 UTC의 차이를 고려해야 한다.에서  한국은 UTC보다 9시간 빠르므로, 시스템에서는 이를 자동으로 변환하는 로직에 대해서 늘 생각하자.
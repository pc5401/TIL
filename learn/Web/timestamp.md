# TIL: 타임스탬프(Timestamp) 정리 ⏱️  

> **Unix Time · ISO 8601 · RFC 2822**  
> 프로젝트마다 요구 형식이 달라 헷갈려서 핵심만 정리.

---

### 1. Unix Time (Epoch)  
- 1970-01-01 00:00:00 **UTC** 기준, _초_ 단위 정수.  
- JS 같은 런타임은 내부에서 **밀리초** 다룸(`Date.now()`).  
- 상대 시간 계산이 편해 “**10 분 전**” 같은 UI에 최적.

```js
// 현재
const now = Math.floor(Date.now() / 1000);

// 10분 전
const tenMinAgo = now - 10 * 60;

// 한국(KST) → 9 h 더해 ISO 문자열
console.log(new Date(now * 1000 + 9*3600_000).toISOString());
```

---

### 2. ISO 8601  
- `YYYY-MM-DDThh:mm:ssZ` 같은 **사람도 읽을 수 있는** 국제 표준.  
- 끝 `Z` = _UTC_.  시간대 오프셋도 붙일 수 있음(`+09:00`).  
- REST API·JSON 교환·로그 타임스탬프 기본값.

```js
const isoUTC = new Date().toISOString();            // 2025-04-26T09:00:00Z
const isoKST = new Date(Date.now()+9*3600_000)
                 .toISOString();                     // 2025-04-26T18:00:00Z
```

---

### 3. RFC 2822  
- `Tue, 26 Apr 2025 09:00:00 +0000` 형태.  
- **이메일 헤더**, **HTTP Date** 필드에서 여전히 사용.

```js
const rfcUtc = new Date().toUTCString();             // Sat, 26 Apr 2025 09:00:00 GMT
```

---

### 📌 개발 메모  
| 체크 | 이유 |
| ---- | ---- |
| **KST = UTC + 9 h** | 서버는 대개 UTC, 화면엔 변환해서 뿌리기. |
| 숫자 계산 → **Unix** | “N분 전” 피드, 만료 토큰 등. |
| 교환 포맷 → **ISO 8601** | 언어 / 타임존 상관없이 일관. |
| 헤더·메일 → **RFC 2822** | 브라우저·MTA 요구 형식. |
| DB 저장 | 정밀 필요 시 bigint(Unix ms) + 인덱스 편함. |

---
# 절대 경로 vs 상대 경로

> 경로는 \*\*무대(파일시스템/웹)\*\*에 따라 의미가 달라진다. “무대 → 기준점 → 해석 규칙”을 먼저 정리한다.

---

## 0. 용어 바로잡기 (무대 구분)

* **파일시스템 경로(Path)**: OS가 파일을 찾는 경로이다. POSIX(`/` 기반) vs Windows(`\\`와 드라이브 문자).
* **웹 경로(URL/URI)**: 브라우저가 리소스를 요청하는 주소이다.

  * **절대 URL**: `https://example.com/assets/app.js`처럼 **스킴+호스트** 포함.
  * **프로토콜 상대 URL**: `//example.com/app.js` (스킴 생략) — 혼합 콘텐츠 방지 목적. 현재는 **HTTPS 고정 권장**이라 드묾.
  * **루트 상대 경로(root‑relative)**: `/assets/app.js` — **사이트 루트** 기준.
  * **문서 상대 경로(document‑relative)**: `../img/a.png` — **현재 문서의 위치** 기준.

> 주의: 실무에서 “절대 경로”라고 부를 때 **OS 절대 경로**와 \*\*웹의 루트 상대 경로(`/...`)\*\*를 혼동하기 쉽다. 맥락을 명시한다.

---

## 1. 한눈 표 (핵심 요약)

| 구분           | 시작 형태                         | 기준                  | 대표 예                      | 장점           | 단점              |
| ------------ | ----------------------------- | ------------------- | ------------------------- | ------------ | --------------- |
| **OS 절대 경로** | `/` (POSIX), `C:\\` (Windows) | 파일시스템 루트            | `/var/www/html`           | 위치 불변, 명확    | 이식성 낮음, 하드코딩 위험 |
| **OS 상대 경로** | `./`, `../`, 이름               | **현재 작업 디렉터리(CWD)** | `../logs/app.log`         | 이식성 좋음       | CWD에 의존해 취약     |
| **절대 URL**   | `https://...`                 | 전체 인터넷              | `https://cdn.../main.css` | 어디서나 동일      | 도메인 변경 비용 큼     |
| **루트 상대**    | `/path`                       | **사이트 루트**          | `/assets/app.js`          | 라우트가 바뀌어도 안전 | 서브디렉토리 배포에 취약   |
| **문서 상대**    | `a/b.png`, `../a`             | **문서 위치**           | `../img/x.png`            | 리포지토리 이동 쉬움  | 구조 변경에 취약       |

---

## 2. 파일시스템에서의 절대/상대

### 2.1 POSIX vs Windows

* POSIX: `/home/user/file.txt`.
* Windows: `C:\\Users\\user\\file.txt` (URL에서는 **항상 `/`** 사용). 네트워크 공유는 `\\\\server\\share`.

### 2.2 경로 정규화/결합

* **정규화**: 중복 구분자, `.`/`..` 제거.
* **결합**: 기준 디렉터리 + 상대 경로 → 정규화.

```js
// Node.js (CJS)
const path = require('path');
const abs = path.resolve('/var/www', './assets/../img/logo.png'); // → /var/www/img/logo.png

// ESM
import { fileURLToPath } from 'url';
import path from 'path';
const __filename = fileURLToPath(import.meta.url);
const __dirname  = path.dirname(__filename);
const full = path.join(__dirname, 'public', 'index.html');
```
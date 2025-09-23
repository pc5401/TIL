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

### 2.3 안전한 파일 서빙 (디렉터리 트래버설 방지)

```js
import http from 'http';
import fs from 'fs/promises';
import path from 'path';

const root = path.resolve(process.cwd(), 'public');

function safeJoin(root, reqPath){
  const target = path.resolve(root, '.' + reqPath); // 정규화
  if (!target.startsWith(root)) throw new Error('Forbidden');
  return target;
}

http.createServer(async (req, res) => {
  try {
    const file = safeJoin(root, req.url === '/' ? '/index.html' : req.url);
    const data = await fs.readFile(file);
    res.writeHead(200); res.end(data);
  } catch (e) { res.writeHead(404); res.end('Not found'); }
}).listen(8080);
```

> 체크리스트: `path.resolve` → `startsWith(root)`로 범위 확인 → 심볼릭 링크 정책 결정 → 예외 처리.

---

## 3. 웹에서의 경로 해석 (HTML/CSS/JS 별 차이)

### 3.1 HTML에서의 기준점

* 기본 기준: **현재 문서 URL**.
* `<base href="/subapp/">`가 있으면 하이퍼링크와 **상대 URL 해석 기준**이 \*\*/<subapp/>\*\*이 된다.

  * 예: 문서가 `/blog/post.html`, `<base href="/v2/">`인 경우 `<a href="img/x.png">` → `/v2/img/x.png`.
  * **스크립트/CSS의 `srcset`·`fetch` 등도 base의 영향을 받는다.**

### 3.2 루트 상대 vs 문서 상대 (동작 예)

* 현재 문서: `https://example.com/app/page/profile.html`.

  * `src="/img/a.png"` → `https://example.com/img/a.png` (**루트 기준**).
  * `src="../img/a.png"` → `https://example.com/app/img/a.png` (**문서 기준**).

### 3.3 CSS `url()`의 기준

* **CSS 파일의 위치 기준**으로 해석된다.

  * CSS: `/css/main.css` 안의 `background:url('../img/bg.png')` → `/img/bg.png`.
  * 빌더(Vite/Webpack) 사용 시, `url()`은 빌드 파이프라인에서 **에셋 리라이트/복사**가 일어날 수 있다.

### 3.4 JS 모듈의 기준 (브라우저)

* `type="module"` 스크립트의 상대 import는 **해당 모듈 파일** 기준.

  * `import './utils.js'`는 현재 모듈 파일과 같은 폴더.
  * **Bare Specifier**(`import react from 'react'`)는 브라우저 기본 미지원 → **Import Map** 또는 빌더 사용.

```html
<script type="importmap">
{
  "imports": {
    "lodash": "https://cdn.skypack.dev/lodash-es"
  }
}
</script>
<script type="module">
  import _ from 'lodash';
  console.log(_.chunk([1,2,3], 2));
</script>
```

---

## 4. 서버·프레임워크 관점 (Express/Vite/Webpack 등)

### 4.1 Express 정적 제공과 마운트 경로

```js
app.use('/static', express.static(path.join(__dirname, 'public')));
// 브라우저에서는 /static/main.css 로 접근한다.
```

* \*\*템플릿에서는 루트 상대(`/static/...`)\*\*를 쓰면 라우트가 바뀌어도 안전하다.
* 앱이 서브경로(`/subapp/`)로 배치되면, **공용 접두사**를 환경변수/설정으로 추상화한다.

### 4.2 번들러의 공개 경로 (Public/Base)

* **Webpack**: `output.publicPath`
* **Vite**: `base` (`vite.config.ts`)
* **CRA**: `homepage`(package.json)

> 빌드산출물의 **상대/루트 경로**는 배포 위치(도메인 루트/서브디렉터리/CDN)에 맞춰 설정한다.

### 4.3 SPA 라우터 & 404 Fallback

* `history` 모드에서 **직접 새로고침**하면 `/route/x`를 서버가 처리해야 한다 → *모든 비정적 요청을 `index.html`로* 리라이트.
* 에셋은 **루트 상대**(`/assets/...`)로 두면 라우트와 무관하게 해석된다.

### 4.4 Service Worker 스코프

* 등록 파일의 경로가 **스코프**를 결정한다.

```js
navigator.serviceWorker.register('/sw.js'); // 전체 사이트
navigator.serviceWorker.register('/app/sw.js'); // /app/ 이하만
```

---

## 5. 이식성/보안/접근성 포인트

* **도메인 변경/서브패스 배포** 가능성 → 절대 URL 남용 금지, **루트 상대 or 구성 기반 경로**로.
* **디렉터리 트래버설**(`..`) 방지: 정규화 후 **허용 루트 검증**.
* **대소문자**: Windows는 보통 **대소문자 무시**, 리눅스는 **구분** → 리포지토리에서는 **소문자 일관**.
* **공백/비ASCII 문자**: URL 인코딩(`%20`) 이슈. 파일명 표준화.
* **CORS**: 절대 URL로 타 도메인 호출 시, 서버의 CORS 정책 필요.
* **SEO/시맨틱**: 내부 링크는 가능하면 \*\*절대 URL(정규화)\*\*로 사이트맵/OG 태그에 제공.

---

## 6. 결정 가이드 (실전 규칙)

1. **동일 도메인의 정적 에셋**: **루트 상대(`/assets/...`)** 권장.
2. **CSS 배경 이미지**: CSS 파일과 **문서적 결합**이 높으므로 **CSS 파일 기준 상대경로** 유지.
3. **JS 모듈 내부 상대 import**: 모듈 파일 기준 상대경로(`./`, `../`) 사용. 라이브러리는 **Bare Specifier + Import Map/번들러**.
4. **외부 리소스(CDN/APIs)**: **절대 URL(HTTPS)**.
5. **서버 코드**: OS **절대 경로**로 작업(환경변수/설정으로 루트 디렉터리 주입). 사용자 입력 경로는 정규화+검증.
6. **서브디렉터리 배포(예: `/app/`)}**: 빌더 `base/publicPath` 설정 + 템플릿 헬퍼 사용.

---

## 7. 자주 겪는 함정 & 해결책

| 증상                | 원인                               | 해결                                       |
| ----------------- | -------------------------------- | ---------------------------------------- |
| 로컬에선 되는데 서버 404   | CSS `url()`이 HTML 기준으로 착각        | CSS 기준 상대경로로 수정, 또는 빌드 설정 검토             |
| 서브경로 배포에서 이미지 404 | 루트 상대(`/img/a.png`)가 도메인 루트를 가리킴 | 배포 접두사 `/subapp/` 반영 또는 상대경로/`<base>` 적용 |
| 모듈 import 실패      | Bare Specifier 브라우저 미지원          | Import Map 또는 번들러 사용                     |
| 새로고침 시 SPA 404    | 서버가 라우트를 모름                      | 서버에서 모든 경로를 `index.html`로 리라이트           |
| 파일 다운로드 경로 공격     | `..` 포함 입력                       | 정규화 후 허용 루트 검증 + 화이트리스트                  |

---

## 8. 디버깅 체크리스트

* **DevTools → Network**: 실제 요청 URL, `base` 영향 확인.
* **Elements/Styles**: CSS `url()`의 계산된 경로 보기.
* **Coverage/SourceMap**: 번들러가 재배치한 에셋 경로 추적.
* **서버 로그**: 404/500 요청 라우트·정규화 값 확인.

---

# 레이아웃 (Layout) 방식 🗺️  

웹 페이지는 **요소를 어떻게 쌓고(Flow) 어떻게 겹칠지(Stacking)** 결정해야 한다. 여기서는 전통적 속성인 `display` · `position` · `float`를 **필수 개념·주의점·실전 팁**과 함께 정리한다.  

---

## 0. 흐름과 포맷팅 컨텍스트 한눈 정리

* **일반 흐름(normal flow)**: 문서가 기본 규칙대로 배치되는 상태이다.
* **포맷팅 컨텍스트(Formatting Context)**: 배치 규칙의 “영역”.

  * **IFC (Inline Formatting Context)**: 인라인 박스가 줄박스(line box) 안에서 배치된다. 공백/글꼴/`line-height`의 영향을 크게 받는다.
  * **BFC (Block Formatting Context)**: 블록 박스끼리 세로로 쌓인다. **부모가 BFC를 만들면 내부 float을 감싼다**(clearfix 효과), 외부와 **마진 겹침**이 차단된다.
  * **Flex / Grid / Table**: 각각 고유 규칙. Flex·Grid는 현대 레이아웃 1순위.
* **BFC를 만드는 대표 속성**: `overflow`가 `visible`이 아닌 값, `float`, `position`이 `absolute/fixed`, `display:inline-block/table-cell/flow-root`, `contain` 등.

> **요약**: 레이아웃 문제의 70%는 “**지금 이 요소가 어떤 포맷팅 컨텍스트 안에 있나?**”로 풀린다.

---

## 1. `display` — “이 박스는 어떤 성격인가?”

### 1) block / inline / inline‑block 핵심

| 값              | 줄바꿈  | 크기 지정  | 수직 여백    | 대표 태그            |
| -------------- | ---- | ------ | -------- | ---------------- |
| `block`        | 한다   | 가능     | 적용       | `div`, `p`, `h1` |
| `inline`       | 안 한다 | 사실상 불가 | 위아래 *무시* | `span`, `a`      |
| `inline‑block` | 안 한다 | 가능     | 적용       | `img`, `button`  |

* `inline`의 높이/패딩은 줄박스에 영향을 주지만 **상하 마진은 무시**된다. 수직 정렬은 `vertical-align` 사용.
* `inline-block`과 `float`의 `width:auto`는 **shrink-to-fit** 알고리즘을 사용한다. 내용 폭에 맞춰 “줄어드는” 특성 때문에 예기치 않은 줄바꿈이 생기면 `min-width`/`max-content`로 제어한다.

> **Tip** 인라인 요소의 가로 간격은 **HTML 소스 공백**도 포함한다. 연달아 쓸 때는 부모에 `font-size:0` → 자식에서 복구, 혹은 `<!-- -->` 공백 제거, 혹은 `letter-spacing:0` 임시 적용.

### 2) 실무에서 자주 쓰는 기타 display

* `display:none` — 렌더 트리에서 요소가 사라진다. `visibility:hidden`은 **공간은 남긴다**.
* `display:flow-root` — **현대식 clearfix**. 내부 float 감싸기 + 외부 마진 겹침 차단.
* `display:contents` — 요소의 **박스만 제거**하고 자식만 남긴다. 접근성 트리/스타일 상속에 영향이 있으니 폼 라벨·인터랙티브 요소엔 신중.
* `display:list-item` — 사용자 정의 마커(`::marker`) 꾸미기 가능.
* `display:table-*` — 구형 호환·특수 레이아웃에서 드물게.

### 3) 줄박스 & 인라인 디테일

* **줄 높이**: `line-height`는 인라인 박스 배치의 기준이다. 텍스트가 아닌 `img` 등 **replaced 요소**는 기본적으로 **baseline**에 정렬되며, 필요 시 `vertical-align:middle/top/bottom`으로 교정한다.
* **문자 방향/쓰기 모드**: `writing-mode`, `direction`에 따라 인라인 축이 바뀐다. 논리 속성(`margin-inline`, `inset-inline` 등)으로 방향성 대응.

---

## 2. `position` — “좌표계를 바꾼다”

> **기본 흐름(static)에서 빼거나, 새로운 ‘기준(containing block)’을 만든다.**

### 1) relative(껍데기) vs absolute(내용물)

```html
<div class="card">
  <span class="badge">NEW</span>
</div>
```

```css
.card  { position: relative; }
.badge { position: absolute; top: 8px; right: 8px; }
```

* `.card`는 원래 자리에서 **움직이지 않고 기준만 제공**한다.
* `.badge`는 흐름에서 빠지고, 좌표는 **가장 가까운 *positioned* 조상(보통 `.card`)의 padding box**를 기준으로 한다.

### 2) fixed & sticky 차이

| 값        | 기준               | 스크롤 시                          |
| -------- | ---------------- | ------------------------------ |
| `fixed`  | 기본은 **viewport** | 항상 고정                          |
| `sticky` | **자신의 스크롤 컨테이너** | 임계(`top/left…`) 닿으면 고정·벗어나면 해제 |

* **sticky 동작 조건**: 부모/조상에 `overflow:visible`이어야 하며, sticky 요소 **자체의 공간**이 있어야 한다.
* **fixed의 함정**: 조상에 `transform`/`filter`/`perspective`가 있으면 **그 조상이 기준**이 된다(모바일에서 특히 주의).

### 3) `inset`와 논리 속성

* `inset: <top> <right> <bottom> <left>`는 `top/right/bottom/left`의 축약형이다.
* 국제화·세로쓰기 대응: `inset-inline-start/end`, `inset-block-start/end` 사용.

### 4) 절대 중앙 정렬 3가지 패턴

```css
/* 1) calc 기반 */
.modal { position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%); }
/* 2) inset + margin:auto */
.modal { position: fixed; inset: 0; width: 320px; height: max-content; margin: auto; }
/* 3) Flex 컨테이너 활용 (권장) */
.overlay { position: fixed; inset: 0; display: grid; place-items: center; }
```

### 5) stacking context & `z-index`

* 새로운 **스택 컨텍스트** 생성 조건(일부): `position`+`z-index!=auto`, `opacity<1`, `transform`, `filter`, `mix-blend-mode`, `isolation:isolate`, `will-change` 등.
* **같은 컨텍스트 안**에서는 `z-index` 숫자대로 쌓인다. 컨텍스트가 다르면 상위/하위 컨텍스트 간 숫자 비교가 **무의미**하다.
* **치트시트(그림자 순서)**: 배경/테두리 → z<0 → 일반 콘텐츠 → positioned(z\:auto) → z>=0.

> **실전 팁**: 컴포넌트 루트에 `position:relative`를 주어 **독립된 좌표계**를 만든 뒤, 내부 장식물·뱃지·툴팁을 `absolute`로 배치하면 재사용성이 올라간다.

---

## 3. `float` — 퇴역했지만 여전히 쓰인다

### 1) 이미지 랩핑용 최소 패턴

```html
<img src="cat.jpg" class="float-l">
<p>텍스트가 이미지 옆으로 감싸 흐른다…</p>
```

```css
.float-l { float:left; margin:0 1rem 1rem 0; }
```

### 2) 부모 깔끔하게 씻기(clearfix)

```css
.clearfix::after {
  content:"";
  display:block;
  clear:both;
}
```

> **Tip** Flex · Grid 환경에서는 굳이 `float`를 쓸 일이 없다. 그러나 **리치 텍스트 CMS**처럼 사용자가 본문에 이미지를 삽입하는 경우 float 랩핑이 가장 간단하다.

---

## 4. 레이아웃 기초 “흐름 → 좌표 → 정렬” 3단계 사고법

1. **흐름(Flow)** — `display`로 요소 유형 결정  
2. **좌표(Coordinate)** — `position`으로 박스를 흐름 밖에 둘지, 고정할지 결정  
3. **정렬(Align / Justify)** — 주로 Flex · Grid에서 요소를 축과 교차축으로 배치  

---

## 5. DevTools 실전 디버깅

| 탭 | 활용 포인트 |
| --- | ---------- |
| **Elements → Layout** (Chrome) | `position` · `z-index`와 새 스택 컨텍스트 여부를 바로 확인 |
| **Contrast Checker** | fixed 헤더·푸터의 텍스트 가독성까지 테스트 |
| **Toggle device toolbar** | sticky header가 모바일 브라우저에서 의도대로 동작하는지 스크롤해 본다 |

---

## 6. 베스트 프랙티스 한눈에

* **컴포넌트 기준**으로 `position:relative`를 주고, 내부 데코레이션은 `absolute`로 배치해 **재사용성**을 높인다.  
* 전체 레이아웃은 **Flex → Grid** 순서로 고려하고, `float`와 무조건적인 `absolute` 배치는 마지막 수단으로 남긴다.  
* 스택 컨텍스트가 얽히면 `translateZ(0)` 해보기 전에 **구조를 먼저 의심**한다.  
* `fixed` 요소는 iOS 사파리와 안드로이드 웹뷰에서 **온갖 버그**가 많다. 가능하면 스크롤 내부 컨테이너에 `sticky`로 대체한다.  

---

## 7. 한 줄 정리

> “`display`로 성격을 정하고, `position`으로 좌표계를 바꾸고, 필요할 때만 `float`로 흐름을 뒤트는 것이 현대 CSS 레이아웃의 기본이다.”



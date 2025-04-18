# 레이아웃 (Layout) 방식 — 확장판 🗺️  

웹 페이지는 **요소를 어떻게 쌓고(Flow) 어떻게 겹칠지(Stacking)** 결정해야 한다. 여기서는 전통적 속성인 `display` · `position` · `float`를 **필수 개념·주의점·실전 팁**과 함께 정리한다.  

---

## 1. `display` — “이 박스는 어떤 성격인가?”

### 1) block / inline / inline‑block 핵심만

| 값 | 줄바꿈 | 크기 지정 | 수직 여백 | 대표 태그 |
| --- | --- | --- | --- | --- |
| `block` | 한다 | 가능 | 적용 | `div`, `p`, `h1` |
| `inline` | 안 한다 | 사실상 불가 | 위아래 *무시* | `span`, `a` |
| `inline‑block` | 안 한다 | 가능 | 적용 | `img`, `button` |

> **Tip** 인라인 요소의 가로 간격은 **HTML 소스의 공백**도 포함한다. 연달아 쓸 때는 `<!-- -->`로 공백을 지우거나 `letter‑spacing:0`을 잠시 줘서 해결한다.

### 2) 기타 display

* `display:none` ― 렌더 트리에서 요소 자체가 사라진다. `visibility:hidden`은 *공간은 남긴다*.
* `display:table-*` ― 옛 IE 호환·SEO 목적에서 드물게 사용.
* 현대 레이아웃 **1순위는 `flex` · `grid`**다. (별도 노트에서 자세히.)

---

## 2. `position` — “좌표계를 바꾼다”

> **기본 흐름(static flow)에서 빼거나, 새로운 ‘기준점(containing block)’을 만든다.**

### 1) 껍데기(static → relative) vs. 내용물(absolute)

```html
<div class="card">
  <span class="badge">NEW</span>
  …
</div>
```

```css
.card  { position: relative;      } /* 기준 */
.badge { position: absolute; top:8px; right:8px; }
```

* `.card`는 원래 자리에서 움직이지 않고 **기준만 제공**한다.  
* `.badge`는 레이아웃 흐름에서 빠지고, 좌표는 `.card`의 padding box를 기준.

### 2) fixed & sticky 차이

| 값 | 기준 | 스크롤 시 |
| --- | --- | -------- |
| `fixed` | `viewport` | 절대 고정 |
| `sticky` | **자신의 스크롤 컨테이너** | 임계 지점(`top`, `left`)에 닿으면 고정, 벗어나면 해제 |

> **함정** `position:sticky`가 동작하려면 **부모에 `overflow:visible`**이어야 한다.

### 3) stacking context & `z-index`

* 새로운 컨텍스트를 만드는 조건  
  `position:absolute|relative|fixed|sticky` + `z-index != auto`, `opacity<1`, `transform`, `filter` 등.
* 같은 컨텍스트 안에서는 `z-index` 숫자 순으로 쌓인다.  
* **디자인 컴포넌트 단위**로 컨텍스트를 자주 끊어 두면 예상치 못한 겹침 버그가 줄어든다.

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
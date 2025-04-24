# 🎨 색상 (Color) & 배경 (Background)

웹 요소의 **분위기·가독성·브랜드 아이덴티티**를 좌우하는 가장 직접적인 수단은 전경색(`color`)과 배경(`background`)입니다.  
아래 노트는 *원본 내용*에 모든 개념·예시를 **빠짐없이 포함**하면서, 추가 설명·실전 팁을 더해 한눈에 보기 좋게 정리했습니다.

---

## 1. 전경색 — `color`

```css
/* ① 16진수 ② rgb ③ rgba(알파) ④ hsl ⑤ 키워드 */
.primary   { color:#333; }
.danger    { color:rgb(255 0 0); }
.muted     { color:rgba(0 0 0 / .5); }
.accent    { color:hsl(210 80% 45%); }
.note      { color:rebeccapurple; }
```

| 포인트 | 메모 |
| ------ | ---- |
| **CSS Color 4** | `lab()`, `lch()`, `color-mix()` (최신 브라우저) |
| **키워드** | `currentColor`는 부모의 `color` 상속 |
| **접근성** | WCAG 2.1 AA 대비 비율 → 일반 텍스트 4.5 : 1 이상 |

---

## 2. 배경 속성 한눈표

| 속성 | 예시 | 설명 |
| ---- | ---- | ---- |
| `background-color` | `#f0f0f0` | 알파 포함 `rgba()` 가능 |
| `background-image` | `url(bg.png)`<br>`linear-gradient(#fff,#eee)` | 외부·로컬·가상 이미지 |
| `background-repeat` | `no-repeat`, `repeat-x` | 반복 축 제어 |
| `background-position` | `center center`, `20% 40px` | 키워드·백분율·길이 |
| `background-size` | `cover`, `contain`, `100px auto` | 크기/비율 |
| `background-attachment` | `scroll`(기본), `fixed`, `local` | 패럴랙스·고정 효과 |
| `background-origin` | `padding-box`, `border-box`, `content-box` | 반복 기준 시작점 |
| `background-clip` | `border-box`, `padding-box`, `text` | `text` → 글자 채우기 |
| `background-blend-mode` | `multiply`, `overlay` | 이미지+색상 혼합 |

### 🔹 단축 `background`

```css
.banner{
  background:#fff                       /* color              */
            url("pattern.png")          /* image              */
            no-repeat                   /* repeat             */
            center/50px auto            /* position / size    */
            fixed;                      /* attachment         */
}
```

* 쉼표(,)로 **멀티 배경** 가능 → 첫 번째가 위에, 마지막이 아래.

---

## 3. 배경 이미지 세부 제어

### - `background-repeat`

```css
.repeat-x   { background-repeat:repeat-x; }
.no-repeat  { background-repeat:no-repeat; }
```

### - `background-position`

```css
.logo{
  background:url(logo.svg) no-repeat;
  background-position:center center;   /* 또는 50% 50% */
}
```

### - `background-size`

```css
.hero     { background-size:cover; }   /* 요소 꽉 */
.thumbnail{ background-size:contain; } /* 전체 보이기 */
```

### - `background-attachment`

```css
.fixed-bg{
  background:url(stars.jpg) center/cover fixed;
}
```

---

## 4. 그라디언트 🌈 (배경 이미지 취급)

| 종류 | 예시 | 특징 |
| ---- | ---- | ---- |
| **선형** `linear-gradient()` | `linear-gradient(45deg,#ff0,#f00)` | 각도·방향 |
| **방사형** `radial-gradient()` | `radial-gradient(circle,#fff,#999)` | 원/타원 + 중심 |
| **반복 선형** `repeating-linear-gradient()` | `repeating-linear-gradient(90deg,#000 0 10px,#fff 10px 20px)` | 줄무늬 |
| **콘익** `conic-gradient()` | `conic-gradient(from 0deg, red, yellow, lime)` | 파이차트 효과 |

> 다른 배경 속성과 **동일 규칙**으로 `repeat`, `size`, `position` 등을 함께 사용.

---

## 5. 실전 예시

### 5-1. 텍스트에 그라디언트 채우기 ✨

```css
.heading{
  font-size:3rem;
  background:linear-gradient(90deg,#ff512f,#dd2476);
  -webkit-background-clip:text;  /* Safari */
  background-clip:text;
  color:transparent;
}
```

### 5-2. 패럴랙스 히어로 배너

```css
.hero{
  height:300px;
  background:
    linear-gradient(to bottom,rgba(0,0,0,.5),rgba(0,0,0,.2)),
    url("hero.jpg") center/cover fixed;
  display:flex; align-items:center; justify-content:center;
  color:#fff; text-align:center;
}
```

### 5-3. 배경 + 그라디언트 멀티 레이어

```css
.card{
  background:
    url(icon.svg) no-repeat 1rem 1rem / 32px,
    radial-gradient(circle at top right,#ffecd2,#fcb69f);
}
```

---

## 6. 반응형 / 다크 모드

```css
:root{
  --bg:#fff; --fg:#333;
}
@media (prefers-color-scheme:dark){
  :root{ --bg:#111; --fg:#f5f5f5; }
}
body{
  background:var(--bg);
  color:var(--fg);
}
```

* 이미지도 `image-set(url(light.jpg) 1x, url(dark.jpg) 1x type("image/jpeg") light)`로 조건적 로딩 가능(초안).

---

## 7. 접근성 & 퍼포먼스 체크리스트 ✅

1. **대비**: DevTools → *Accessibility → Contrast* 확인(최소 AA).  
2. **용량**: 큰 배경 이미지는 **압축 + 적절한 해상도**.  
3. **Lazy Load**: fold 아래 배경은 JS IntersectionObserver or `content-visibility:auto`.  
4. **인쇄 모드**: `@media print{ *{ background:none !important; } }`.  
5. **시맨틱 색 변수**: `--c-primary`, `--c-on-primary` 구조로 테마/다크모드 대응.

---

## 8. 예제 페이지 (원본 예시 유지)

```html
<!DOCTYPE html>
<html>
<head>
<style>
body{
  margin:0; font-family:sans-serif; color:#333;
}
.banner{
  background:
    linear-gradient(to bottom,rgba(0,0,0,.5),rgba(0,0,0,.2)),
    url("hero.jpg") no-repeat center/cover;
  height:300px; display:flex; align-items:center; justify-content:center;
  color:#fff; text-align:center;
}
.banner h1{ font-size:2rem; }
.highlight-section{
  background-color:#fffbcc; padding:20px; text-align:center;
}
.footer{
  background:#333; color:#fff; padding:10px; text-align:right;
}
</style>
</head>
<body>
  <div class="banner"><h1>배경 예시</h1></div>
  <div class="highlight-section"><p>배경색을 이용해 강조 구역을 표현한 예시</p></div>
  <div class="footer"><p>저작권 정보 © 2025</p></div>
</body>
</html>
```

---

## 9. 한 줄 정리

> **“충분한 대비 + 의도 있는 레이어”**만 지키면 색상·배경으로도 UX, 브랜드, 성능을 모두 잡을 수 있다. 🚀

# 🎨 색상 (Color) & 배경 (Background) 총정리

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

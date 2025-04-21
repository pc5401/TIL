
# 🌈 Flexbox 한 방 정리

> “**1 축**만 지배해도 80 %의 레이아웃이 해결된다.”

Flexbox는 **가로·세로 한 축**의 배치·정렬·공간 분배를 브라우저가 자동으로 계산해 주는 레이아웃 모듈이다.  
`float` 나 `inline‑block`에 비해 코드가 짧고 직관적이며, 반응형에서 빛을 발한다.

---

## 목차

1. 핵심 개념 & 용어  
2. Flex Container 속성 총람  
3. Flex Item 속성 총람  
4. 레이아웃 공식 • 동작 원리  
5. 실전 레시피 (코드 예시)  
6. 디버깅 & 함정 가이드  
7. 베스트 프랙티스 & 접근성  
8. Flexbox vs Grid 간단 비교  
9. 치트시트

---

## 1. 핵심 개념

| 용어 | 설명 |
| ---- | ---- |
| **Flex Container** | `display: flex` / `inline-flex` 선언된 부모 |
| **Flex Item** | 컨테이너의 **직계 자식** |
| **Main Axis** | `flex-direction`으로 결정되는 축 |
| **Cross Axis** | Main Axis에 수직인 축 |
| **Line** | wrap 시 형성되는 아이템 묶음(행·열) |

---

## 2. Flex Container 속성

| 속성 | 주요 값 | 비고 |
| ---- | ------- | ---- |
| `display` | `flex` • `inline-flex` | 요소를 Flex Container로 전환 |
| `flex-direction` | `row` 🔰 / `row-reverse` / `column` / `column-reverse` | Main Axis 방향 |
| `flex-wrap` | `nowrap` 🔰 / `wrap` / `wrap-reverse` | 줄바꿈 여부 |
| `flex-flow` | `<direction> <wrap>` | 위 두 속성 단축 |
| `justify-content` | `flex-start` 🔰 · `flex-end` · `center` · `space-between` · `space-around` · `space-evenly` | **Main Axis** 정렬 |
| `align-items` | `stretch` 🔰 · `flex-start` · `flex-end` · `center` · `baseline` | **Cross Axis** 정렬(단일 줄) |
| `align-content` | `stretch` 🔰 · `flex-start` · `center` · `space-between` … | 줄이 2 줄↑일 때 Cross Axis 정렬 |
| `gap` | `<row-gap> <column-gap>` | 아이템 간 격자 간격 |
| `row-gap / column-gap` | 개별 간격 | `gap`의 축 분리 버전 |
| `place-content` | `align-content` + `justify-content` | Grid와 동일 패턴 |

```css
.container{
  display:flex;
  flex-flow:row wrap;
  gap:24px 16px;
  justify-content:space-between;
  align-items:center;
}
```

---

## 3. Flex Item 속성

| 속성 | 기본 | 의미 |
| ---- | ---- | ---- |
| `order` | 0 | 시각 순서( DOM 순서 변경 X ) |
| `flex-grow` | 0 | 남은 공간 확대 비율 |
| `flex-shrink` | 1 | 부족 시 축소 비율 |
| `flex-basis` | auto | 기본 크기( px / % / auto ) |
| `flex` | `grow shrink basis` | 단축(예 `flex: 1` → `1 1 0`) |
| `align-self` | auto | 아이템별 Cross Axis 정렬 |
| `min/max-width` `min/max-height` | - | 축소·확대 한계 |
| `margin:auto` | - | 남은 공간 흡수 → 정렬 트릭 |

```css
.card      { flex:0 1 260px; }   /* 최소 260 px, 줄어들 수 있음 */
.card--big { flex-grow:2; }       /* 다른 카드보다 2 배 넓게 */
```

---

## 4. 레이아웃 공식 & 동작 원리  🛠️

1. **가용 공간 계산** (Main Axis)  
   컨테이너 패딩·보더·스크롤바를 제외한 너비/높이.
2. **Flex Basis 설정**  
   각 아이템의 `flex-basis` → `content size` → `auto (main size)` 순으로 결정.
3. **Grow / Shrink**  
   남거나 부족한 공간을 `flex-grow`·`flex-shrink` 비율대로 분배.
4. **Cross Axis 정렬**  
   한 줄 → `align-items`, 여러 줄 → `align-content`.
5. **Auto Margin 정렬**  
   남은 공간이 있으면 `margin:auto` 방향으로 모두 밀림.

> **Tip** `min-width:0`을 컨테이너·아이템에 넣어 두면 긴 단어·이미지가 폭을 밀어내는 버그를 예방한다.

---

## 5. 실전 레시피

### 5‑1 중앙 카드

```css
.wrapper{
  display:flex; justify-content:center; align-items:center;
  min-height:100vh; background:#fafafa;
}
.card{ width:320px; }
```

### 5‑2 로그인 모달(고정 너비 + 가변 폼)

```css
.modal{
  display:flex; flex-direction:column; gap:1rem;
  width:400px;
}
.modal > header{ flex:0; }
.modal > form  { flex:1; overflow:auto; }
```

### 5‑3 반응형 카드 그리드

```css
.cards{
  display:flex; flex-flow:row wrap; gap:2rem;
}
.card{
  flex:1 1 clamp(240px,25%,320px);   /* 최소 240, 최대 320 */
}
.nav{ margin-left:auto; } /* 💡 auto margin 밀기 */
```

### 5‑4 헤더(로고 + 메뉴 + 유틸)

```css
header{
  display:flex; align-items:center; gap:2rem;
}
.nav{ margin-left:auto; }       /* auto margin 밀기 */
.util{ display:flex; gap:1rem; }
```

### 5‑5 채팅 버블

```css
.message{
  display:flex; gap:.5rem; align-items:flex-end;
}
.avatar{ flex:0 0 40px; }
.text  { flex:1; }
.time  { flex:0; font-size:.75rem; }
```

---

## 6. 디버깅 & 흔한 함정

| 증상 | 원인 | 해결 |
| ---- | ---- | ---- |
| 카드가 한 줄을 넘어가지 않음 | `flex-wrap:nowrap` 기본 | `flex-wrap:wrap` 설정 |
| 이미지가 폭을 뚫고 나옴 | 아이템 축소 불가 | `min-width:0` 추가 후 `overflow:hidden` |
| 중앙 정렬이 안 됨 | `margin`이 간격을 차지 | `gap` 사용 또는 마진 제거 |
| `align-items`가 먹히지 않음 | 여러 줄일 때 | `align-content`로 변경 |
| 스크롤‑스냅 안 걸림 | Flex Item 스냅 지정 누락 | `scroll-snap-align:start` 적용 |
| 키보드 탭 순서가 엉망 | `order` 과다 사용 | 시맨틱 DOM 순서 유지, ARIA 점검 |

---

## 7. 베스트 프랙티스 & 접근성

1. **축 먼저 그린다** (Figma / 종이 스케치).  
2. 공백은 **`gap`** — 내부 여백은 **`padding`**.  
3. 중앙·우측 정렬은 `margin:auto` 트릭 활용.  
4. **중첩 Flex**로 복잡도를 단계별 관리.  
5. `order`는 시각 효과용 최소 사용 → 스크린리더 · 탭 순서 검증 필수.  
6. 컨테이너·아이템 모두 `min-width:0` 기본 적용.  
7. **접근성 글꼴 확대** 고려 시 `flex-basis` % 대신 `clamp()`·`min()` 사용.  
8. IE11 폴백은 `display:-ms-flexbox` + 구 스펙 속성, 그러나 가능하면 Graceful Degradation 문구 안내.

---

## 8. Flexbox vs Grid 한눈 비교

| 항목 | Flexbox | Grid |
| ---- | ------- | ---- |
| 차원 | **1 차원** (행 *또는* 열) | **2 차원** (행 + 열) |
| 주 용도 | Nav, 툴바, 카드 Row | 전체 페이지 레이아웃, 격자 |
| 항목 순서 | DOM 순 또는 `order` | `grid-template-areas`, `grid-row/column` |
| 성숙도 | 모든 브라우저 안정 | 최신 브라우저에서 권장 |
| 학습 곡선 | 낮음 | 중간 |

---

## 9. 치트시트 📝

| 카테고리 | Main Axis | Cross Axis |
|----------|----------|-----------|
| **정렬** | `justify-content` | `align-items` (1줄) / `align-content` (여러줄) |
| **줄바꿈** | `flex-wrap` |   |
| **사이 간격** | `gap` (row/column) |   |
| **아이템 개별** | `flex`, `order`, `align-self`, `margin:auto` |   |

---

### 📌 마무리...

> **“`flex-direction`으로 축을 결정하고, `gap`·`flex`·`auto margin`으로 공간을 분배하도록.”**

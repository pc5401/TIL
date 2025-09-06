# 🌈 Flexbox 한 방 정리

> “**1 축**만 지배해도 80 %의 레이아웃이 해결된다.”

Flexbox는 **가로·세로 한 축**의 배치·정렬·공간 분배를 브라우저가 자동으로 계산해 주는 레이아웃 모듈이다.  
`float` 나 `inline‑block`에 비해 코드가 짧고 직관적이며, 반응형에서 빛을 발한다.

---

## 목차

0. 멘탈 모델
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

## 0. 멘탈 모델

* **Container ↔ Item**: `display:flex | inline-flex`인 부모가 컨테이너, **직계 자식**이 아이템이다.
* **Main Axis / Cross Axis**: `flex-direction`이 축을 정한다. row면 가로가 Main, column이면 세로가 Main이다.
* **줄(Line)**: `flex-wrap:wrap`일 때 아이템 묶음(행/열) 단위를 말한다.
* **Auto Min Size**: Flex 아이템의 기본 `min-width/height`는 **auto**다. 내용이 줄바꿈을 막으면 축소가 안 된다 → **`min-width:0`** 또는 \*\*`overflow:hidden`\*\*으로 과도 확장을 막는다.

> **요약**: *축을 정하고 → 기본 크기(basis)를 잡고 → 남거나 부족한 공간을 grow/shrink로 분배*한다.

## 1. 핵심 개념

| 용어 | 설명 |
| ---- | ---- |
| **Flex Container** | `display: flex` / `inline-flex` 선언된 부모 |
| **Flex Item** | 컨테이너의 **직계 자식** |
| **Main Axis** | `flex-direction`으로 결정되는 축 |
| **Cross Axis** | Main Axis에 수직인 축 |
| **Line** | wrap 시 형성되는 아이템 묶음(행·열) |

---

## 2. Flex Container 속성 총람

| 속성                     | 주요 값(기본값 🔰)                                                                                               | 의미/비고                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------- |
| `display`              | `flex` · `inline-flex`                                                                                     | 컨테이너 전환                |
| `flex-direction`       | **`row`🔰** · `row-reverse` · `column` · `column-reverse`                                                  | Main 축 방향              |
| `flex-wrap`            | **`nowrap`🔰** · `wrap` · `wrap-reverse`                                                                   | 줄바꿈 여부                 |
| `flex-flow`            | `<direction> <wrap>`                                                                                       | 상단 2속성 단축              |
| `justify-content`      | **`flex-start`🔰** · `flex-end` · `center` · `space-between` · `space-around` · `space-evenly`             | **Main 축 정렬**          |
| `align-items`          | **`stretch`🔰** · `flex-start` · `flex-end` · `center` · `baseline`                                        | **Cross 축 정렬(단일 줄)**   |
| `align-content`        | **`stretch`🔰** · `flex-start` · `flex-end` · `center` · `space-between` · `space-around` · `space-evenly` | **여러 줄**일 때 Cross 축 정렬 |
| `gap`                  | `<row-gap> <column-gap>`                                                                                   | 아이템 간격. 마진보다 예측 가능     |
| `row-gap`/`column-gap` |                                                                                                            | 축별 간격 제어               |
| `place-content`        | `align-content` + `justify-content`                                                                        | 줄이 2줄↑에서 유용            |

```css
.container {
  display: flex;
  flex-flow: row wrap;
  gap: 24px 16px;
  justify-content: space-between;
  align-items: center;
}
```

> **Note**: Flex 아이템 사이에는 **마진 겹침이 없다**. 간격은 가능하면 `gap`을 쓰고, 내부 여백은 `padding`으로 관리한다.

---


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

### 5‑1. 화면 중앙 카드 (정중앙)

```css
.wrapper {
  display:flex; justify-content:center; align-items:center;
  min-height:100vh; background:#fafafa;
}
.card { width: 320px; }
```

### 5‑2. 로그인 모달 (고정 헤더 + 가변 폼)

```css
.modal {
  display:flex; flex-direction:column; gap:1rem;
  width: 400px; max-height: min(80vh, 720px);
}
.modal > header { flex: 0 0 auto; }
.modal > form   { flex: 1 1 auto; overflow:auto; min-height:0; }
```

### 5‑3. 반응형 카드 그리드(행 균등)

```css
.cards { display:flex; flex-wrap:wrap; gap:2rem; }
.card  { flex: 1 1 0; min-width: 240px; max-width: 320px; }
```

### 5‑4. 헤더(로고 · 메뉴 · 유틸)

```css
header { display:flex; align-items:center; gap:2rem; }
.nav    { margin-left:auto; }     /* 우측 밀기 */
.util   { display:flex; gap:1rem; }
```

### 5‑5. 채팅 버블(아바타 + 본문 + 시간)

```css
.message { display:flex; gap:.5rem; align-items:flex-end; }
.avatar  { flex: 0 0 40px; }
.text    { flex: 1 1 auto; min-width:0; }
.time    { flex: 0 0 auto; font-size:.75rem; }
```

### 5‑6. Sticky Footer 레이아웃

```css
.page   { min-height:100svh; display:flex; flex-direction:column; }
.main   { flex:1 1 auto; min-height:0; }
footer  { flex:0 0 auto; }
```

### 5‑7. 툴바 버튼 우측 정렬 (auto margin)

```css
.toolbar { display:flex; gap:1rem; }
.spacer  { margin-left:auto; }
```

### 5‑8. 가로 스크롤 카드 리스트 + 스냅

```css
.scroller {
  display:flex; gap:1rem; overflow:auto; scroll-snap-type:x mandatory; }
.card    { flex:0 0 80%; scroll-snap-align:start; }
```

---

## 6. 디버깅 & 흔한 함정

| 증상                  | 원인                    | 해결                                           |
| ------------------- | --------------------- | -------------------------------------------- |
| 한 줄만 유지되어 줄바꿈 안 됨   | 기본 `flex-wrap:nowrap` | `flex-wrap:wrap`                             |
| 이미지/텍스트가 폭을 밀어냄     | Auto min size(줄바꿈 없음) | 아이템 또는 컨테이너에 `min-width:0`/`overflow:hidden` |
| 중앙 정렬이 안 됨          | 마진/간격 혼용              | `gap` 사용, 정렬은 `justify/align`로               |
| `align-items`가 안 먹음 | 여러 줄 레이아웃             | `align-content`로 줄 묶음 정렬                     |
| 탭 이동/읽기 순서 이상       | `order` 남용            | DOM 순서 유지, ARIA 점검                           |
| 버튼 한 개만 우측 배치하고 싶음  | 공간 분배 미숙              | 해당 아이템에 `margin-left:auto`                   |
| column에서 세로 스크롤 안 됨 | 자식 min-height\:auto   | 스크롤 영역에 `min-height:0; overflow:auto`        |

> **DevTools**: Chrome **Layout** 탭에서 Main/Cross 축, gap, 아이템 크기·정렬을 즉시 시각화해 확인한다.

---

## 7. 베스트 프랙티스 & 접근성

1. **축 먼저 설계**: Figma/스케치에서 row/column을 먼저 잡는다.

2. **간격은 `gap`**: 외부 간격은 부모가, 내부 간격은 `padding`이 책임진다.

3. **중첩 Flex**: 큰 틀(row/column) → 내부(정렬/분배)로 단계화한다.

4. **`order` 최소화**: 시각 순서와 논리 순서를 분리하지 않는다. 필요한 경우 **포커스 순서**와 **ARIA**를 검증한다.

5. **Auto Min Size 대응**: 기본으로 `min-width:0`(row) / `min-height:0`(column)을 습관화한다.

6. **타이포 확대 대응**: 레이아웃 폭 기반은 `%`보다는 `clamp()`/`min()`을 섞어 탄력적으로 한다.

7. **성능**: 자주 변경되는 위치/크기는 `transform/opacity` 위주로 애니메이션하여 리플로우를 줄인다.
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


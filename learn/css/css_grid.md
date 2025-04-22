# 🌐 CSS Grid 완벽 가이드

> “행과 열을 동시에 설계하면 레이아웃 설계가 **퍼즐 맞추기**처럼 즐거워진다.”

CSS Grid Layout은 웹 표준 최초로 **2차원 배치**를 정식 지원한다.  
Flexbox가 한 축(1 차원)의 배치를 자동화했다면, Grid는 **행·열 두 축**을 한 번에 제어해 복잡한 페이지를 단순 선언으로 그려 낼 수 있다.

---

## 1. 개념 이해

| 용어 | 설명 |
| ---- | ---- |
| **Grid Container** | `display:grid` / `inline-grid` 선언된 부모 |
| **Grid Item** | 컨테이너 **직계 자식** |
| **트랙(Track)** | 행(Row) 또는 열(Column) **한 줄** |
| **선(Line)** | 트랙을 구분하는 **격자선**(1 번선, 2 번선…) |
| **셀(Cell)** | 행 × 열이 만나는 1 칸 |
| **영역(Area)** | 여러 셀을 합친 직사각형, `grid-template-areas` 이름으로 사용 |

---

## 2. Grid Container 속성 총람

| 속성 | 핵심 값 | 의미 & 팁 |
| ---- | ------- | -------- |
| `display` | `grid`·`inline-grid` | 블록 or 인라인 컨테이너 |
| `grid-template-columns` | `repeat(3, 1fr)` `200px auto 1fr` | **명시적 열** 정의 |
| `grid-template-rows` | `100px minmax(200px, auto)` | **명시적 행** 정의 |
| `grid-template-areas` | 문자열 패턴 | 시각적으로 영역 배치 |
| `grid-template` | `rows / columns` 단축 | 행·열·영역을 한 번에 |
| `grid-auto-columns` / `grid-auto-rows` | `100px` `min-content` | 암시적 트랙 크기 |
| `grid-auto-flow` | `row`(🔰) `column` `dense` | 자동 배치 방향·전략 |
| `gap` | `row column` | 행·열 간격 |
| `justify-items` / `align-items` | `start` `center` `stretch`(🔰) | **셀 내부** 정렬 |
| `justify-content` / `align-content` | `start` `center` `space-between` | **그리드 전체** 정렬 |

### 🍀 암시적(Implicit) 그리드
명시한 트랙을 넘어 아이템이 배치될 때 **자동으로** 생성되는 트랙.  
`grid-auto-columns`·`grid-auto-rows`로 크기를, `grid-auto-flow`로 배치 순서를 컨트롤한다.

```css
.container{
  display:grid;
  grid-template-columns:repeat(2,1fr); /* 2열만 명시 */
  grid-auto-rows:120px;                /* 넘어가면 120px 행 생성 */
  grid-auto-flow:row dense;            /* 빈칸을 앞으로 알뜰히 채움 */
}
```

---

## 3. Grid Item 속성 총람

| 속성 | 예시 | 설명 |
| ---- | ---- | ---- |
| `grid-column` | `2 / span 3` | 열 선 2에서 시작 → 3칸 차지 |
| `grid-row` | `auto / 5` | 자동 시작 → 선 5 이전까지 |
| `grid-area` | `header` 또는 `2 / 1 / span 2 / 4` | 영역 이름 or `row‑start / column‑start / row‑end / column‑end` |
| `justify-self` / `align-self` | `center` `end` `stretch` | **셀 내부** 개별 정렬 |
| `place-self` | `align justify` | 위 두 속성 단축 |
| `z-index` | `1` | 격자 위에 아이템 겹치기 |

```css
.feature{
  grid-column:1 / -1;     /* 첫 선 ➜ 마지막 선까지(전 열) */
  grid-row:span 2;        /* 현재 행 포함 2행 높이 */
  align-self:flex-end;    /* 셀 내부 아래 정렬 */
}
```

---

## 4. 실무 레이아웃 레시피

### 4‑1. Holy Grail 페이지

```css
.page{
  display:grid;
  grid-template:
    "header header" 80px
    "nav    main"  1fr
    "footer footer" 60px / 240px 1fr;
}
```

### 4‑2. 반응형 카드 Masonry(가변 행높이)

```css
.cards{
  display:grid;
  grid-template-columns:repeat(auto-fill, minmax(280px,1fr));
  grid-auto-rows:1px;          /* 계산 최소값 */
  grid-auto-flow:row dense;    /* 빈칸 채우기 */
}
.card{
  padding:1rem; background:#fff;
}
```

### 4‑3. 갤러리 12열 시스템

```css
.grid{
  display:grid;
  grid-template-columns:repeat(12, minmax(0,1fr));
  gap:1rem;
}
.col-6{ grid-column:span 6; }  /* 6 / 12 넓이 */
.col-4{ grid-column:span 4; }
```

### 4‑4. 격자선 이름 활용

```css
.sidebar{
  grid-column:sidebar-start / sidebar-end;
}
.container{
  display:grid;
  grid-template-columns:
    [sidebar-start] 240px [sidebar-end main-start] 1fr [main-end];
}
```

---

## 5. 함수 & 단위 더 맛보기

| 구문 | 쓰임새 | 예시 |
| ---- | ------ | ---- |
| `minmax(min,max)` | 최소~최대 범위 | `minmax(150px, 1fr)` |
| `repeat(auto-fill, …)` | **빈 칸이 있어도** 열 생성 | responsive 카드 |
| `repeat(auto-fit, …)` | 아이템 수만큼 열, 남는 공간 **늘림** | auto center |
| `fr` | 남은 공간 비율 | `2fr 1fr` (2:1 비율) |
| `min-content` / `max-content` | 가장 긴 단어 너비·컨텐츠 전체 너비 | 텍스트 기반 폭 |

---

## 6. Grid vs Flexbox 빠른 비교

| 항목 | Grid | Flexbox |
|----|-----|--------|
| 차원 | **2 차원** | 1 차원 |
| 축 제어 | 행·열 동시 | 한 축 |
| 레이아웃 유형 | 전체 페이지·앱 프레임·사진첩 | 내비·툴바·버튼 그룹 |
| 정렬 메커니즘 | 트랙 기반(선) | 항목 순서 |
| 학습 난이도 | ▲▲ | ▲ |

> **조합 사용**이 정석: *상위 구조*는 Grid, *내부 UI*는 Flex.

---

## 7. 디버깅 & 꿀팁 🛠️

1. **브라우저 DevTools** → “Grid” 배지 체크 → 격자선 번호 시각화.  
2. `minmax(0, 1fr)`로 **over‑flow**(긴 단어 밀림) 방지.  
3. `grid-auto-flow:dense`는 빈칸을 모아 채우지만 **DOM 순서 변경** 가능 → 접근성 주의.  
4. `subgrid`(Firefox · Safari 17+)로 **중첩 컨테이너**가 부모 트랙을 상속.  
5. IE 지원 필요 시 `@supports(display:grid)` 분기 or `autoplace` 폴백.  

---

## 8. 베스트 프랙티스 💡

* **시각적 설계 → 숫자 대신 의미**: `grid-template-areas`와 **격자선 이름**으로 가독성 UP.  
* **반응형은 열부터**: 컬럼을 `repeat(auto-fit,minmax())`로 선언하면 미디어쿼리 최소화.  
* **모바일 → 데스크톱**: `grid-template-areas`를 미디어쿼리에서 재정의, HTML 변경 無.  
* **간격은 `gap`**: 마진으로 만든 그리드는 행·열 합산이 번거롭다.  
* **레이어 겹치기**: 동일 셀 겹침 시 `z-index`로 스택 제어, CSS Grid도 stacking context 적용.  

---

## 9. 치트시트 📑

| 목표 | 속성 | 한 줄 팁 |
| ---- | ---- | -------- |
| 트랙 정의 | `grid-template-(rows|columns)` | `repeat(12,1fr)` |
| 영역 선언 | `grid-template-areas` | `"head head" "side main"` |
| 아이템 배치 | `grid-area, grid-row/column` | `span` 사용해 병합 |
| 간격 | `gap` | `gap:row col` |
| 자동 배치 | `grid-auto-flow` + `grid-auto-rows` | masonry 흉내 |
| 셀 내부 정렬 | `justify-self` / `align-self` | override `stretch` |
| 그리드 전체 정렬 | `justify-content` / `align-content` | 컨테이너 내 위치 |

---

### 📌 마무리리

> “행·열 격자를 선언하고, 아이템을 좌표·이름으로 **꽂아 넣으면** 복잡한 페이지도 마크업 변경 없이 완성된다.” 🚀

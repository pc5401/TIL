
# 🌟 Flexbox 완전 정복 노트

> “한 축(main axis)만 지배하면 레이아웃 고민의 80 %가 사라진다.”

---

## 0. 목차

1. Flexbox 탄생 배경  
2. 핵심 용어 & 축 이해  
3. **Flex Container** 속성 총정리  
4. **Flex Item** 속성 총정리  
5. 컨테이너 × 아이템 조합 예시    ┐  
6. UI 패턴 예제 (실전 코드)        │ 👈 **실습 추천!**  
7. 흔한 오류 & 디버깅 체크리스트 ┘  
8. 베스트 프랙티스 8선  
9. 미니 치트시트 (PDF 링크)  

---

## 1. 왜 Flexbox인가? 🤔

| 전통 방식 | 한계 |
|----------|------|
| `float`  | 본래 텍스트·이미지 래핑용, 정렬 로직 복잡 |
| `inline-block` | 공백 노이즈, 세로 정렬 번거로움 |
| 테이블 레이아웃 | 마크업 불순, 반응형 대응 난이도 |

→ **2017+ 브라우저**에서 Flexbox가 안정 지원되며 “수평/수직 중앙정렬”부터 “자동 줄바꿈 카드 그리드”까지 *한 방*에 처리 가능.

---

## 2. 핵심 용어 & 축

```
flex-direction: row;
┌──────── main axis (x) ────────┐
│ item 1  item 2  item 3 …      │
└──────── cross axis (y) ──────┘
```

* **Flex Container**: `display:flex` 선언된 부모  
* **Flex Item**: 직계 자식  
* **주 축**: `flex-direction` 방향  
* **교차 축**: 주 축에 수직인 축  

---

## 3. Flex Container 속성표

| 속성 | 주요 값 | 의미 & 팁 |
|------|---------|-----------|
| **display** | `flex` / `inline-flex` | 블록 or 인라인 컨테이너 |
| **flex-direction** | `row` (🔰)·`row-reverse`·`column`·`column-reverse` | 주 축 전환 |
| **flex-wrap** | `nowrap`(🔰)·`wrap`·`wrap-reverse` | 줄바꿈 여부 |
| **flex-flow** | `<direction> <wrap>` | 위 두 개 단축 |
| **justify-content** | `flex-start`(🔰)·`center`·`space-between` … | **주 축** 정렬 |
| **align-items** | `stretch`(🔰)·`center`·`baseline` … | **교차 축** 정렬 (단일 줄) |
| **align-content** | `stretch`(🔰)·`space-around` … | 줄이 2줄↑일 때 교차 축 정렬 |
| **row/column-gap** | `gap` | 아이템 간 격자 간격. IE11 미지원 |

```css
.gallery {
  display: flex;
  flex-flow: row wrap;
  gap: 24px 16px;      /* row 24, column 16 */
  justify-content: space-between;
  align-items: flex-start;
}
```

---

## 4. Flex Item 속성표

| 속성 | 기본 | 설명 |
|------|------|------|
| **flex-grow** | 0 | 남은 공간 비율 확대 |
| **flex-shrink** | 1 | 부족 시 축소 비율 |
| **flex-basis** | auto | 기본 크기(퍼센트/px) |
| **flex** | `grow shrink basis` | `flex:1` = `1 1 0` |
| **order** | 0 | 시각적 순서 |
| **align-self** | auto | item별 교차 축 정렬 |

```css
.card { flex: 0 1 260px; }   /* 최소 260px, 줄어들 수 있음 */
.card--feature { flex-grow: 2; }
```

---

## 5. 컨테이너 × 아이템 매트릭스

| 상황 | 설정 | 결과 |
|------|------|------|
| 버튼 3개 균등 분배 | `.btn{flex:1}` | 남은 공간 1:1:1 |
| 메시지 버블(좌측 고정, 우측 가변) | `.timestamp{flex:0} .content{flex:1}` | 시간 고정폭, 내용 유동 |
| 세로 네비게이션 | `flex-direction:column` + `gap` | 위→아래 스택 |

---

## 6. UI 패턴 실전 코드

### 6‑1) 완전 가운데 카드

```css
.wrapper{
  display:flex; justify-content:center; align-items:center;
  min-height:100vh;
}
.card{ width:320px; }
```

### 6‑2) 헤더(로고 + 내비 + 유틸 버튼)

```css
header{
  display:flex; align-items:center; gap:2rem;
}
.nav{ margin-left:auto; } /* 💡 auto margin 밀기 */
```

### 6‑3) 반응형 카드 그리드

```css
.cards{
  display:flex; flex-flow:row wrap; gap:2rem;
}
.card{
  flex:1 1 clamp(240px,25%,320px);
}
```

### 6‑4) Sticky 푸터

```css
body{
  display:flex; flex-direction:column; min-height:100vh;
}
main{ flex:1; }
footer{ flex:0 0 60px; }
```

---

## 7. 흔한 오류 & 디버깅

| 증상 | 대처 |
|------|------|
| 아이템 폭이 넘친다 | 컨테이너/아이템에 `min-width:0` 추가 |
| 정렬이 먹히지 않는다 | *단일 줄* → `align-items` / 다줄 → `align-content` |
| `gap` 브라우저 호환 | 구 IE 필요 시 마지막 아이템 `margin-right:0` 패턴 |
| DOM 순서와 시각 순서 불일치 | `order` 최소화 + 키보드 탭 순서 테스트 |

DevTools ‣ **Layout(Flex)** 탭 활성화 → 주 축/교차 축 시각 가이드 라인 ON.

---

## 8. 베스트 프랙티스 8선 🔑

1. **축 먼저 그린다** (Figma나 종이에 x ↔ y 표시).  
2. 공백은 `gap` → 내부 여백은 `padding`.  
3. `margin:auto`는 **정렬 도구**다: “한 쪽만 auto → 반대 끝 붙이기”.  
4. 반복 카드라면 `flex: 1 1 basis` 패턴으로 *최소* 폭만 설정.  
5. 이미지·input처럼 축소 불가 요소는 `flex-shrink:0`.  
6. Flex 안에 또 Flex → **nesting**으로 복잡도 ↓.  
7. 시맨틱 마크업 유지, 레이아웃은 CSS로 (접근성).  
8. Flex로 안 되는 다차원 배치는 **CSS Grid**를 고려.

---

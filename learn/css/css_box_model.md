# 박스 모델(Box Model) — 확장판 🌐

CSS 레이아웃의 모든 기반은 **박스**다. 박스를 완전히 이해하지 못하면 여백 계산·정렬·반응형 설계에서 계속 삐끗한다. 아래 정리를 **차근차근 읽고 직접 DevTools(요소 검사기)로 확인**해 보자.

---

## 1. 기본 네 겹 recap

| 계층 | 역할 | 기억 법 |
| --- | --- | --- |
| **콘텐츠(Content)** | 텍스트·이미지 등 실제 데이터가 들어간다. | `width`, `height`로 크기를 지정한다. |
| **패딩(Padding)** | 콘텐츠와 테두리 사이의 안쪽 여백이다. | 배경색·배경이미지가 여기까지 채워진다. |
| **테두리(Border)** | 패딩을 감싸는 경계선이다. | 굵기·스타일·색상을 조합한다. |
| **마진(Margin)** | 요소 밖의 바깥 여백이다. | 인접 박스 간 간격을 확보한다. |

```css
.box {
  width: 200px;            /* content */
  padding: 20px;           /* padding */
  border: 2px solid #333;  /* border  */
  margin: 10px;            /* margin  */
}

```

```
       ▲ margin
┌────────────────────────┐
│        border          │   ▲ border
│  ┌──────────────────┐  │
│  │     padding      │  │
│  │  ┌────────────┐  │  │
│  │  │  content   │  │  │
│  │  └────────────┘  │  │
│  └──────────────────┘  │
└────────────────────────┘

```

---

## 2. `box-sizing` 한 방 정리

| 값 | 계산 기준 | 특징 |
| --- | --- | --- |
| `content-box` *(기본)* | `width = content` | 실제 너비 = `content + padding + border` |
| `border-box` | `width = border` | **패딩·테두리 포함** 너비 고정 |

사이트 전체에서 레이아웃이 꼬이지 않게 하려면 초기화 파일에 다음과 같이 고정한다.

```css
*, *::before, *::after {
  box-sizing: border-box;
}

```

---

## 3. 마진 겹침(Margin Collapse)

> “마진 두 개가 만나면 더 큰 놈 한 장만 남는다.”
> 
- **수직 방향(block axis)** 에서만 발생한다.
- **인접 형제** 또는 **부모‑자식 관계**에서 적용된다.
- `overflow: hidden|auto|scroll`, `display:flex|grid|inline-block` 등은 새 **블록 포맷팅 컨텍스트(BFC)**를 만들어 겹침을 차단한다.

```css
section, article { margin-top: 40px; }

```

- `section + article` — **40 px**만 생긴다.
- 부모 `<div>`가 margin‑top을 가지면 가장 위의 자식과 겹쳐 부모 쪽에만 적용된다.

---

## 4. 인라인 vs. 블록 박스의 차이

| 구분 | 블록 박스 | 인라인 박스 |
| --- | --- | --- |
| 기본 표시 | `div`, `p`, `h1` | `span`, `a`, 텍스트 |
| 수직 마진 | 서로 겹친다(위) | **무시**된다(라인 높이에 포함 X) |
| 패딩·테두리 | 사방 적용 | 상하 적용 시 line‑height를 밀어내지만 시각적으로 ‘틈’이 생긴다. |
| 줄바꿈 | 앞뒤로 항상 줄바꿈 | 내용이 줄을 넘어가면 wrapping |

> 패딩·테두리가 필요한 인라인 요소는 display:inline-block이나 display:inline-flex로 바꿔 세로 여백을 안정적으로 확보한다.
> 

---

## 5. 논리 속성(Logical Properties)

글쓰기 방향·국제화에 대응하려면 물리적(`padding-left`)보다 **논리적** 속성을 습관화한다.

```css
.card {
  padding-block: 1rem 2rem;   /* top, bottom */
  padding-inline: 1.5rem;     /* left & right 또는 rtl이면 반대 */
  border-inline-start: 4px solid currentColor;
}

```

---

## 6. 박스와 레이아웃 모듈의 상호작용

### Flexbox

- 기본 축 기준으로 **패딩·테두리**가 항목 크기에 포함된다.
- `flex-basis` 기본값은 `auto` → `content‑box`에 의존한다.

### Grid

- *트랙 정의(줄/열)**는 `border-box` 개념이다.
- `minmax()` 내부에 `min-content`, `max-content`가 있을 때만 콘텐츠 크기에 접근한다.

### Multi‑column

- 각 column도 **자체 박스 컨텍스트**를 만든다. 마진 겹침이 일어나지 않는다.

---

## 7. 고급 속성 한눈에

| 속성 | 한 줄 메모 |
| --- | --- |
| `outline` | 박스를 흐름에 **영향 주지 않고** 감싸는 외곽선이다. 테두리와 합쳐지지 않는다. |
| `box-shadow` | 그림자이지만 `spread` 값으로 실질 두께처럼 사용할 수 있다. |
| `clip-path` | 박스 영역을 잘라내 시각적 형태를 바꾼다. 클릭 영역은 유지되지 않는다. |
| `filter` | `blur()` 등 적용해 박스 안 비주얼만 변형한다. |
| `aspect-ratio` | 높이를 지정하지 않고 **박스 비율**을 고정한다. |

---

## 8. DevTools 활용 팁

1. 요소를 선택하면 **Box Model 패널**에서 네 영역의 픽셀 값을 실시간 확인한다.

2. 드래그로 마진·패딩 값을 직접 수정해 레이아웃을 실험한다.

3. `Computed → Layout` 탭에서 **스크롤 스냅**, `writing‑mode` 등의 영향도 함께 확인한다.

---

## 9. 베스트 프랙티스

- **일관된 box‑sizing** 적용 후 레이아웃을 설계한다.
- 여백은 **마진으로 간격, 패딩으로 영역**을 확보한다는 원칙을 지킨다.
- **컴포넌트 단위**로 내부 여백(~패딩)까지 포함해 ‘자급자족’하도록 설계하면 상위 레이아웃에 끼치는 부작용을 줄일 수 있다.
- reset / normalize 단계에서 `margin:0`으로 초기화 후 필요한 곳에만 명시적으로 준다.

---

## 10. 한 문장 정리

> “콘텐츠는 패딩으로 숨 쉬고, 테두리로 드러나며, 마진으로 이웃과 거리를 둔다.”
> 

박스 모델을 손에 익히면 레이아웃 문제 대부분이 반쯤 풀린다. **DevTools로 눈으로 확인하고, 논리 속성으로 미래를 대비**하자.
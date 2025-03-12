# 색상(Color)와 배경(Background)

웹에서 요소의 시각적 분위기를 결정하는 중요한 요소로, **텍스트 색상**과 **배경** 설정이 있다.

각 속성을 적절히 조합하면 **가독성**, **미적 효과**, **브랜드 아이덴티티** 등을 높일 수 있다.

---

## 색상(Color)

### 1) `color`

텍스트 등의 **전경색**을 지정하는 속성이다.

```css
.color-example {
  color: #333; /* #RRGGBB (16진수) */
}
```

- `color: red;`처럼 이름 지정, `rgb(255, 0, 0)`, `rgba(255, 0, 0, 0.5)`, `hsl()`, `hsla()` 등 다양한 표현 가능
- **가독성**을 위해 배경색과 충분한 대비를 주는 것이 좋다.

## 배경(Background)

### 1) `background-color`

요소의 **배경색**을 지정한다.

```css
.bg-color-example {
  background-color: #f0f0f0;
}
```

- 투명도(알파 채널)를 포함하는 RGBA(`rgba(0, 0, 0, 0.3)`) 등도 사용 가능

### 2) `background-image`

요소의 **배경 이미지**를 지정한다.

```css
.bg-image-example {
  background-image: url("images/bg-pattern.png");
}
```

- 경로(`url()`)에 외부 이미지나 로컬 파일을 삽입
- **그라디언트**(`linear-gradient()`, `radial-gradient()`) 등 가상 배경도 지정 가능

### 3) `background-repeat`

배경 이미지를 어떻게 **반복**할지 결정한다.

- `repeat` (기본값): x, y축으로 반복
- `repeat-x`: x축(가로)으로만 반복
- `repeat-y`: y축(세로)로만 반복
- `no-repeat`: 반복 없이 한 번만 표시

```css
.bg-repeat-example {
  background-image: url("pattern.png");
  background-repeat: repeat-x;
}
```

### 4) `background-position`

배경 이미지를 요소 내에서 **어디에 배치**할지 결정한다.

- 값: `left top`, `center center`, `right bottom` 등 (키워드 사용)
- px, %, 기타 단위도 가능

```css
.bg-position-example {
  background-image: url("logo.png");
  background-repeat: no-repeat;
  background-position: center center;
}
```
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

### 5) `background-size`

배경 이미지의 **크기**를 조절한다.

- `auto`: 원본 크기
- `cover`: 요소를 가득 메우도록 확대·축소 (비율 유지)
- `contain`: 전체가 보이도록 크기를 맞춤 (비율 유지)
- px, %, 등 구체값으로 조절도 가능

```css
.bg-size-example {
  background-image: url("hero.jpg");
  background-size: cover;
}
```
### 6) `background-attachment`

배경 이미지를 **스크롤** 시 어떻게 처리할지 결정한다.

- `scroll`: 스크롤에 따라 배경 이미지도 같이 움직임 (기본값)
- `fixed`: 화면에 고정되어 움직이지 않음
- `local`: 요소의 스크롤에 맞춰 움직임

```css
.bg-attachment-example {
  background-image: url("fixed-bg.png");
  background-attachment: fixed;
  background-size: cover;
}
```

### 7) 단축 속성: `background`

여러 배경 속성을 **한 번에** 지정할 수 있다. 순서가 중요하지는 않지만, 보통 아래 순서로 나열한다.

1. `background-color`
2. `background-image`
3. `background-repeat`
4. `background-position`
5. `background-size`
6. `background-attachment`

```css
.bg-shorthand-example {
  background: #fff url("pattern.png") no-repeat center/50px auto fixed;
}
```

- `center/50px auto`는 `background-position: center; background-size: 50px auto;`와 동일
- 쉼표로 구분해 **여러 개의 배경**을 쌓을 수도 있다 (멀티 배경)

## 그라디언트(Gradient)

**배경 이미지**로 간주되어 `background-image` 속성에 함수 형태로 지정한다.

### 1) 선형 그라디언트(Linear Gradient)

```css
.linear-gradient-example {
  background-image: linear-gradient(to right, #ff0000, #0000ff);
}
```

- `to right`: 왼쪽에서 오른쪽으로 색 변화
- 방향을 `to top`, 각도(`45deg`) 등으로도 지정 가능
- 색상은 여러 단계로 추가 가능: `linear-gradient(to bottom, red, yellow, green)`

### 2) 방사형 그라디언트(Radial Gradient)

```css
.radial-gradient-example {
  background-image: radial-gradient(circle, #fff, #ccc, #999);
}
```

- `circle`, `ellipse` 등 형태 지정
- 중심부터 바깥쪽으로 색을 분산

그라디언트 자체는 **가상 이미지**이므로 `background-repeat`, `background-position` 등 다른 속성들과 함께 사용 가능하다.

---

## 예시 코드

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      margin: 0;
      font-family: sans-serif;
      color: #333;
    }

    .banner {
      /* 그라디언트 + 이미지 혼합 예시 */
      background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0.5),
        rgba(0, 0, 0, 0.2)
      ),
      url("hero.jpg") no-repeat center / cover;
      height: 300px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      color: #fff;
    }

    .banner h1 {
      font-size: 2rem;
    }

    .highlight-section {
      background-color: #fffbcc;
      padding: 20px;
      text-align: center;
    }

    .footer {
      background: #333;
      color: #fff;
      padding: 10px;
      text-align: right;
    }
  </style>
</head>
<body>
  <div class="banner">
    <h1>배경 예시</h1>
  </div>
  <div class="highlight-section">
    <p>배경색을 이용해 강조 구역을 표현한 예시</p>
  </div>
  <div class="footer">
    <p>저작권 정보 © 2025</p>
  </div>
</body>
</html>

```

---

## 정리

색상과 배경 관련 CSS 속성은 **간단한 설정**부터 **그라디언트**나 **복수 배경**을 활용한 **복합 효과**까지 다양하다.

웹 페이지의 **분위기**와 **가독성**을 결정하는 핵심 요소이므로 다음에 유의한다.

1. **텍스트 색상**과 **배경색** 간 **대비**를 충분히 줘서 시인성을 확보한다.
2. 배경 이미지를 사용할 때는 **반응형**(크기, 위치)과 **성능(용량)**을 고려한다.
3. **그라디언트**는 이미지 리소스 없이도 시각적 효과를 연출할 수 있어 강력하다.
4. 단축 속성(`background`)을 숙지해 **한 번**에 여러 설정을 직관적으로 작성한다.
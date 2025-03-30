# 애니메이션(Animation)과 트랜지션(Transition)

인터랙티브하고 **동적인 UI**를 구현하기 위해 CSS만으로도 간단한 애니메이션 효과를 적용할 수 있다.

가벼운 시각 효과부터 복잡한 모션까지 다양한 용도로 활용 가능하다.

---

## 트랜지션(Transition)

어떤 속성의 변화가 일어날 때, 해당 변화가 **점진적**으로 일어나도록 설정한다.

사용자 인터랙션(hover, focus 등)이나 자바스크립트 동작으로 CSS 속성이 바뀔 때 부드러운 전환 효과를 줄 수 있다.

### 1) `transition` 속성

- 주요 속성:
    - `transition-property`: 애니메이션 적용할 속성 (또는 `all`로 모든 속성)
    - `transition-duration`: 지속 시간 (s, ms)
    - `transition-timing-function`: 가속도 함수 (ease, linear, ease-in, ease-out, cubic-bezier 등)
    - `transition-delay`: 시작 지연 시간

```css
.box {
  width: 100px;
  height: 100px;
  background-color: blue;
  transition: background-color 0.3s ease, width 0.5s;
}
.box:hover {
  background-color: red;
  width: 200px;
}
```

위 예시에서 `.box`에 마우스를 올리면 **배경색**이 0.3초간 천천히 바뀌고, **너비**는 0.5초간 변경된다.

### 2) 짧은 예시

```css
.button {
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  transition: background-color 0.3s, transform 0.2s;
}
.button:hover {
  background-color: #555;
  transform: scale(1.05);
}
```

- 호버 시, 배경색이 부드럽게 바뀌고 약간 확대(`scale`)된다.

## 애니메이션(Animation)

- *Keyframes(키프레임)**를 정의하여 복잡하고 연속적인 움직임을 구현할 수 있다.

트랜지션이 “상태 A → 상태 B로 변화”에 초점을 둔다면, 애니메이션은 **여러 중간 단계**를 지정하여 세밀한 제어가 가능하다.

### 1) `@keyframes` 규칙

애니메이션의 **이름**과 **단계별 스타일**을 정의한다.

```css
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```

- `0%`부터 `100%` 사이에 **중간 단계**(`50%`, `25%`, 등)를 자유롭게 추가 가능

```css
@keyframes bounce {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0);
  }
}
```

- `translateY(-20px)`처럼 위로 튕겼다가 원래 위치로 돌아오는 등 **바운스** 효과

### 2) 애니메이션 속성

- `animation-name`: 적용할 `@keyframes` 이름
- `animation-duration`: 애니메이션이 한 번 재생되는 데 걸리는 시간
- `animation-timing-function`: 트랜지션과 동일하게 가속도(가감속) 곡선 지정
- `animation-delay`: 시작 지연 시간
- `animation-iteration-count`: 재생 횟수 (숫자 또는 `infinite`)
- `animation-direction`: 정방향(`normal`), 역방향(`reverse`), 왕복(`alternate`) 등
- `animation-fill-mode`: 애니메이션 전후 상태 유지 여부 (`none`, `forwards`, `backwards`, `both`)
- `animation-play-state`: 재생/일시정지(`running`, `paused`)

### 예시

```css
.fade-box {
  opacity: 0;
  animation-name: fadeIn;
  animation-duration: 2s;
  animation-timing-function: ease;
  animation-fill-mode: forwards; /* 애니메이션 끝난 후 최종 상태 유지 */
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

- `.fade-box`는 페이지 로드 시 2초 동안 서서히 나타남
- 끝나면 `opacity:1` 상태 유지한다.

### 3) 단축 속성: `animation`

`animation` 속성 하나로 여러 속성을 일괄 지정할 수 있다.

```css
.bounce-box {
  animation: bounce 1s ease-in-out 0s infinite alternate;
}
@keyframes bounce {
  0%   { transform: translateY(0); }
  50%  { transform: translateY(-30px); }
  100% { transform: translateY(0); }
}
```

- 순서: `animation-name duration timing-function delay iteration-count direction fill-mode play-state`
- 일부는 생략 가능

---

## 트랜지션 vs. 애니메이션

1. **트랜지션**
    - 속성이 **어떤 이벤트**(hover, focus, 클릭, 자바스크립트로 클래스 추가 등)로 바뀔 때, 그 변화 과정을 부드럽게 처리
    - “상태 A → 상태 B” **단일 전환**에 간단하게 사용
2. **애니메이션**
    - **독립적으로 여러 상태**(키프레임)를 정의하고, 시간 축에 따라 자동 재생
    - 반복, 왕복, 복잡한 모션 시 **유연하고 세밀하게 제어**

---

## 예시 코드

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .transition-button {
      background-color: #3498db;
      color: #fff;
      padding: 10px 20px;
      border: none;
      transition: background-color 0.3s ease;
      cursor: pointer;
    }
    .transition-button:hover {
      background-color: #1d6fa5;
    }

    .animation-box {
      width: 100px;
      height: 100px;
      background-color: coral;
      animation: scaling 2s infinite alternate;
    }
    @keyframes scaling {
      from { transform: scale(1); }
      to   { transform: scale(1.2); }
    }
  </style>
</head>
<body>
  <button class="transition-button">Hover me</button>
  <div class="animation-box"></div>
</body>
</html>
```

- 첫 버튼은 호버 시 배경색 변화가 **트랜지션**으로 부드럽게 일어남
- `.animation-box`는 2초 주기로 **커졌다 → 돌아왔다**를 반복(애니메이션)

## 주의사항 및 팁

1. **성능**
    - 애니메이션은 가능하면 **GPU 가속**이 가능한 속성(`transform`, `opacity`) 위주로 구현하는 것이 좋다.
    - `left`, `top`, `width`, `height` 등 레이아웃에 영향을 주는 속성은 성능 부담이 클 수 있음.
2. **유용한 타이밍 함수**
    - `ease`: 부드러운 시작과 끝
    - `linear`: 일정 속도
    - `ease-in`: 느리게 시작 -> 빠르게 끝
    - `ease-out`: 빠르게 시작 -> 느리게 끝
    - `cubic-bezier`: 직접 커브를 정의해 정교한 타이밍 제어
3. **호환성**
    - IE 구버전 등에서 일부 속성이 호환되지 않을 수 있으므로 필요 시 벤더 프리픽스(`webkit-`, `moz-` 등)를 고려
    - 최근 모던 브라우저 대부분은 프리픽스 없이도 잘 지원
4. **이벤트 제어**
    - 자바스크립트의 `transitionend`, `animationend` 이벤트를 통해 **애니메이션 완료 시점**을 처리 가능
    - UI 단계 제어나 반복 재생(추가 모션) 등을 만들 때 유용

## 결론

- **트랜지션**: 특정 속성이 바뀔 때 **자연스러운 전환**을 제공
- **애니메이션**: 키프레임 기반의 **복잡하거나 반복**되는 모션 구현
- 작은 시각 효과부터 페이지 전환, 로딩 화면 등에 다양하게 적용해 **동적인 사용자 경험**을 제공할 수 있다.
- 성능과 사용자 편의성(화면 깜빡임이나 과도한 모션 주의)을 고려하여 **적절히** 활용하는 것이 중요
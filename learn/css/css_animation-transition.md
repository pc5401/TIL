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
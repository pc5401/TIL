# 타이포그래피(Typography)와 폰트(Font)

웹 디자인에서 **글자**는 정보 전달의 핵심 요소이다. 좋은 타이포그래피는 가독성과 접근성을 높여 **사용자 경험**을 개선한다.

---

## 폰트 관련 주요 속성

### 1) `font-family`

글꼴(폰트) 종류를 지정한다.

웹 안전 폰트나, 웹 폰트 등을 사용할 수 있으며, 우선순위를 고려해 **쉼표로 나열**하는 습관이 중요하다.

```css
p {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

- **웹 안전 폰트**(Arial, Verdana, Times New Roman 등)는 모든 환경에서 대체로 지원됨
- 사용자 지정 폰트(웹 폰트)는 로딩을 위해 추가 설정이 필요 (`@font-face` 또는 Google Fonts 등)

### 2) `font-size`

글자 크기를 지정한다.

절대 단위(px)보다 **상대 단위(rem, em 등)**를 선호하는 편이 많다.

접근성과 반응형 디자인 측면에서도 유리하기 때문.

```css
p {
  font-size: 1rem; /* 예: HTML 루트(font-size: 16px) 기준 -> 16px */
}
```

- **절대 크기**(px)는 고정된 크기
- **상대 크기**(em, rem, %)는 상위(또는 루트) 폰트 크기를 기준으로 변경됨

### 3) `font-weight`

글자의 굵기를 지정한다.

`normal`, `bold`, 혹은 **숫자(100~900)**로 세분화할 수도 있다.

```css
strong {
  font-weight: 700; /* 보통 bold와 동일하게 사용됨 */
}

```
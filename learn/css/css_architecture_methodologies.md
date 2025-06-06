# CSS 구조화 방법론

프로젝트 규모가 커지면, 단순히 CSS 파일을 늘리는 것만으로는 유지보수가 어려워진다.

**CSS 구조화 방법론**은 클래스 작명 규칙, 코드 조직 방식 등을 표준화해 **일관성**, **확장성**, **가독성**을 개선하고, **스타일 충돌**을 최소화하기 위한 패턴들이다.

---

## 1. BEM (Block, Element, Modifier)

**BEM**은 러시아의 Yandex 사에서 고안한 방법론으로, `Block`, `Element`, `Modifier` 세 개념으로 스타일을 구조화한다.

1. **Block**
    - 독립적으로 재사용 가능한 UI 컴포넌트 단위
    - 예: `header`, `menu`, `button`, `form` 등
    - HTML 태그와 직접 1:1 대응하기보다는 의미 단위로 구분
2. **Element**
    - Block 안에서 기능적 역할을 하는 **하위 구성 요소**
    - 블록 없이는 존재할 수 없는 내부 요소
    - BEM 표기에서는 보통 `__`(더블 언더스코어)로 구분
    - 예: `header__logo`, `menu__item`, `button__icon`
3. **Modifier**
    - Block 또는 Element에 **상태나 변형**을 표시하기 위해 사용
    - BEM 표기에서는 보통 `_`(단일 언더스코어)로 구분
    - 예: `button_primary`, `menu__item_active`, `header__logo_small`

### 예시 코드 (BEM)

```html
<div class="menu">
  <ul class="menu__list">
    <li class="menu__item menu__item_active">
      <a href="#" class="menu__link">Home</a>
    </li>
    <li class="menu__item">
      <a href="#" class="menu__link">About</a>
    </li>
  </ul>
</div>
```

```css

.menu {
  /* 블록 스타일 */
  background-color: #333;
}
.menu__list {
  list-style: none;
  padding: 0;
}
.menu__item {
  display: inline-block;
}
.menu__item_active {
  /* 모디파이어(활성 상태) */
  font-weight: bold;
}
.menu__link {
  color: #fff;
  text-decoration: none;
}

```

- 클래스명만 봐도 **구조**가 명확히 드러나고, 충돌 위험이 적음
- **장점**: 네이밍을 규칙적으로 유지해, 대규모 프로젝트에서도 스타일을 **예측 가능한 방식**으로 공유 및 확장

## 2. OOCSS (Object Oriented CSS)

**OOCSS**는 “객체 지향 CSS”를 의미하며, 다음 두 가지 기본 원칙을 강조한다.

1. **구조(Structure)와 스킨(Skin)의 분리**
    - 박스 모델, 레이아웃 등 구조적 속성과, 색상·배경 등의 시각적 스타일을 분리해 재사용성 향상
2. **컨테이너에서 독립적인 블록**
    - 요소가 배치될 **컨테이너(부모 요소)**에 관계없이 **독립적**으로 동작해야 한다.

### 예시

```css
/* 구조: padding, border, float 등 */
.card {
  padding: 20px;
  border: 1px solid #ccc;
  float: left;
  width: 200px;
}

/* 스킨: 색상, 배경, 폰트 등 */
.card-default {
  background-color: #fff;
  color: #333;
}
.card-primary {
  background-color: #3498db;
  color: #fff;
}

```

- `.card`는 레이아웃을 정의, `.card-default`나 `.card-primary`는 **시각적 스킨**만 변경
- HTML에서 `<div class="card card-primary">...</div>`처럼 **조합** 가능

## 3. SMACSS (Scalable and Modular Architecture for CSS)

**SMACSS**는 Jonathan Snook가 제안한 방법론으로, CSS를 다섯 가지 범주로 나눈다.

1. **Base**
    - HTML 태그에 대한 **기본 스타일**(초기화, 타이포그래피 기본값 등)
    - 예: `html, body { margin: 0; padding: 0; }`, `a { text-decoration: none; }`
2. **Layout**
    - 페이지 주요 **레이아웃 구성** 요소 (header, footer, sidebar, main 등)
    - 예: `.l-header`, `.l-footer` 등
3. **Module**
    - 재사용 가능 **모듈** 단위 (navbar, card, form, widget 등)
    - 프로젝트에서 가장 많이 생기는 부분
4. **State**
    - *상태(visible, hidden, active 등)**를 나타내는 클래스
    - 예: `.is-active`, `.is-hidden` 등
    - 자바스크립트로 토글되는 상태를 표현
5. **Theme**
    - 사이트의 스킨, 테마 관련 스타일 (색상, 폰트, 브랜딩 등)
    - 예: `.theme-dark`, `.theme-light`

### 예시 구조

```
/css
  /base
    _reset.css
    _typography.css
  /layout
    _header.css
    _footer.css
    _grid.css
  /modules
    _card.css
    _nav.css
  /state
    _states.css
  /theme
    _dark-theme.css
main.css
```

- 이렇게 파일을 **역할별**로 분할하고, 최종 빌드시 하나로 합침
- 클래스 네이밍에서 `l-`, `m-`, `is-` 등을 접두어로 사용해 구분하기도 함

## 4. 그 외 방법론·컨벤션

- **ITCSS (Inverted Triangle CSS)**: 전역, 설정, 툴, 제네릭, 컴포넌트, 유틸리티 계층으로 점진적이고 확장성 높게 구성
- **Atomic CSS**: 미세 단위(원자) 수준의 역할별 클래스를 조합해서 UI 구성
    - 예: `mt-4` (margin-top: 1rem), `flex-center` 등
    - TailwindCSS 같은 유틸리티 퍼스트 프레임워크가 대표적 예
- **ABEM**: BEM의 확장판, “Atomic BEM” 등 다양한 변형도 존재

## 비교 및 활용

1. **BEM**
    - **가장 보편적**이고, 네이밍에 대한 체계가 분명
    - 중·대형 프로젝트에서 혼선을 줄여줌
    - 클래스가 길어질 수 있으나 가독성을 위해 감수
2. **OOCSS**
    - **객체 지향**으로 재사용성 집중, 구조/스킨 분리
    - 다른 방법론(예: SMACSS, BEM)과 혼합해서 쓰기 쉬움
3. **SMACSS**
    - **카테고리**별로 코드 분할, 대규모 팀 프로젝트에 적합
    - 레이아웃, 모듈, 상태 등 역할 구분이 명확
4. **선택**
    - 팀 규모, 프로젝트 성격, 개발 문화 등에 따라 방법론을 선택하거나 **조합**해서 사용
    - 최근에는 **BEM + SMACSS** 조합, 혹은 **유틸리티 퍼스트 프레임워크(TailwindCSS)** 같이 다른 접근 방식을 취하기도 함

---

## 실제 적용 예시

**BEM + SMACSS** 혼합 예시:

```css
/* base/_reset.css (SMACSS Base) */
html, body {
  margin: 0;
  padding: 0;
}

/* layout/_header.css (SMACSS Layout) */
.l-header {
  background: #333;
  color: #fff;
}

/* modules/_menu.scss (SMACSS Module + BEM) */
.menu {
  &__list {
    display: flex;
  }
  &__item {
    margin-right: 1rem;
  }
  &__link {
    color: #fff;
    text-decoration: none;
  }
  &__item_active .menu__link {
    font-weight: bold;
  }
}

/* state/_states.css (SMACSS State) */
.is-hidden {
  display: none;
}

/* theme/_dark.css (SMACSS Theme) */
body.dark-theme {
  background-color: #222;
  color: #ccc;
}

```

- 디렉터리 구조를 SMACSS로 조직
- 클래스 네이밍은 BEM 사용
- 결과: 정돈된 구조, 용도별 분리, 협업 시 파편화 줄어듦

## 결론

- **CSS 구조화 방법론**을 적용하면, 클래싱 전략이 **명확**해지고 **규모가 커져도** 유지보수가 쉬워진다.
- **BEM**은 가장 널리 알려진 클래스 네이밍 방식이고, **OOCSS**와 **SMACSS**는 **코드 조직** 측면에서 유용한 원칙을 제공한다.
- 프로젝트 특성과 팀 컨벤션에 맞춰 **하나** 또는 **조합**을 채택해, **일관된 규칙** 하에 CSS를 작성하면 혼란과 중복이 크게 줄어든다.
- 결국 중요한 것은 **일관성**과 **명확성**이며, 어떤 방법론을 쓰든 팀 전체가 합의하고 준수하도록 유도하는 것이 핵심
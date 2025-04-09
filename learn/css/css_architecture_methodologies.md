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
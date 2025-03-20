# 반응형 웹(Responsive Web)과 미디어 쿼리(Media Queries)

현대 웹에서는 데스크톱, 태블릿, 모바일 등 다양한 화면 크기와 디바이스 환경을 지원해야 한다.

**반응형 웹**은 화면 크기에 따라 디자인과 레이아웃이 유연하게 변화하도록 설계하는 기법이다.

이때 가장 중요한 도구가 **미디어 쿼리(Media Queries)**이다.

---

## 반응형 웹(Responsive Web)

1. **개념**
    - 단 하나의 웹 페이지가 **다양한 화면 크기**(데스크톱, 태블릿, 모바일)에 따라 **자동**으로 레이아웃을 조절
    - 추가적인 별도 페이지(모바일 전용 페이지 등)를 만들지 않고 **유지보수**가 용이
    - 사용자 경험(UX) 향상, 접근성 개선
2. **핵심 구성요소**
    - **유동적인 레이아웃(Fluid Layout)**: `%`, `vw` 등의 상대 단위를 적극 활용해 너비를 동적으로 조정
    - **유연한 이미지(Flexible Images)**: `max-width: 100%;` 처럼 이미지가 부모 요소를 넘치지 않도록 처리
    - **미디어 쿼리(Media Queries)**: 특정 조건(해상도, 뷰포트 너비 등)에 따라 CSS 규칙을 달리 적용
3. **기본 메타 태그**
    
    ```html
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    ```
    
    - 모바일 장치에서 사이트가 제대로 축소·확대 없이 보이도록 하는 설정
    - `width=device-width`는 기기 화면의 **논리적 픽셀 폭**에 맞춤
    - `initial-scale=1.0`은 초기 확대비율을 100%로 설정

## 미디어 쿼리(Media Queries)

CSS에서 뷰포트(화면)의 속성(너비, 높이, 해상도 등)에 따라 **조건부 스타일**을 적용하는 기술이다.

1. **기본 문법**
    
    ```css
    @media (조건) {
      /* 조건을 만족할 때 적용할 CSS */
    }
    ```
    
    - 조건은 보통 `screen`(화면), `print`(인쇄) 등 **미디어 타입**과 `(min-width: 768px)` 같은 **특성**의 조합이다.
2. **주요 속성(Feature) 예시**
    - `width`, `min-width`, `max-width`
    - `height`, `min-height`, `max-height`
    - `orientation` (가로: landscape, 세로: portrait)
    - `resolution` (dpi, dppx) 등
    - 예: `@media screen and (min-width: 768px) { ... }`
    - 예: `@media print { ... }` (인쇄 전용 스타일)
3. **Breakpoints(중단점)**
    - 일반적으로 화면 너비에 따라 **중단점**을 설정
    - 예: 576px(모바일), 768px(태블릿), 992px(작은 데스크톱), 1200px(일반 데스크톱) 등
    - 프레임워크(Bootstrap 등)에서도 비슷한 기준을 사용
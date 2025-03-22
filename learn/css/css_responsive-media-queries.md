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

**사용 예시**

```css
/* 모바일(최대 767px) 이하일 때 */
@media (max-width: 767px) {
  .header {
    font-size: 14px;
  }
  .nav {
    display: none;
  }
}

/* 태블릿(768px 이상 991px 이하) 범위 */
@media (min-width: 768px) and (max-width: 991px) {
  .header {
    font-size: 16px;
  }
  .nav {
    display: block;
  }
}

/* 데스크톱(992px 이상) */
@media (min-width: 992px) {
  .header {
    font-size: 18px;
  }
  .nav {
    float: right;
  }
}

```

- 가령 `.header`, `.nav` 등의 스타일을 뷰포트 너비에 따라 다르게 적용

---

## 반응형 구현 시 주의점

1. **이미지와 미디어 요소**
    - `img { max-width: 100%; height: auto; }`로 설정하여 부모 컨테이너 범위 넘침 방지
    - 비디오나 iframe도 비슷하게 반응형으로 처리 가능(`wrapper` 안에 `position: relative; padding-bottom: ...%` 기법 등)
2. **폰트 크기와 줄바꿈(line-break)**
    - 작은 화면에서 가독성을 위해 폰트 크기, 줄간격(line-height)을 조절
    - 너무 긴 문장은 줄바꿈 처리가 필요
3. **터치 영역 크기**
    - 모바일 기기는 터치로 조작하므로 버튼·링크 등의 터치 영역을 충분히 크게 잡아야 한다.
    - 일반적으로 최소 40~44px 정도 권장
4. **성능**
    - 모바일 데이터 환경에서는 이미지 등 리소스가 크면 로딩이 길어질 수 있다.
    - 반응형 이미지(`<picture>` 태그, `srcset`, `sizes` 등)를 활용해 기기에 맞는 이미지 제공
5. **테스트**
    - 실제 기기(또는 DevTools)에서 반드시 화면 회전, 다른 OS/브라우저 환경 등을 테스트
    - 경계값(브레이크포인트) 근처에서 레이아웃이 깨지지 않는지 검사
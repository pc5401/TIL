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

## 예시 코드

아래 예시는 간단한 **헤더/본문/푸터** 레이아웃을 반응형으로 구성한 것이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>반응형 웹 예시</title>
  <style>
    /* 기본 스타일 */
    body {
      margin: 0;
      font-family: sans-serif;
    }

    header, main, footer {
      padding: 20px;
      text-align: center;
    }

    header {
      background-color: #333;
      color: #fff;
    }

    main {
      background-color: #f0f0f0;
    }

    footer {
      background-color: #ccc;
    }

    /* 작은 화면 (모바일)에서는 전체 너비에 맞춰 하나의 열(컬럼)로 레이아웃 */
    @media (max-width: 767px) {
      main {
        font-size: 14px;
      }
      .responsive-image {
        width: 100%;
        height: auto;
      }
    }

    /* 중간 화면 (태블릿) 이상에서는 폰트 키우고, 이미지 크기 조절 */
    @media (min-width: 768px) {
      main {
        font-size: 16px;
      }
      .responsive-image {
        width: 50%;
        height: auto;
      }
    }

    /* 큰 화면 (데스크톱)에서 헤더/본문/푸터 레이아웃 조정 */
    @media (min-width: 992px) {
      header, main, footer {
        text-align: left;
        padding: 40px;
      }
      main {
        max-width: 960px;
        margin: 0 auto;
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>반응형 웹 예시</h1>
  </header>
  <main>
    <p>이 예시는 화면 크기에 따라 글자 크기와 레이아웃이 달라진다.</p>
    <img src="https://via.placeholder.com/800x400" alt="예시 이미지" class="responsive-image" />
  </main>
  <footer>
    <p>Footer 영역</p>
  </footer>
</body>
</html>

```

### 정리
- 반응형 웹은 단일 페이지로 다양한 디바이스를 대응하며, 유지보수성과 일관성을 높이는 설계 방식이다.

- 미디어 쿼리는 CSS의 강력한 기능으로, 뷰포트 크기(또는 기타 조건)에 따라 다른 스타일을 적용한다.

- 유동적인 레이아웃, 이미지 등과 결합해 크로스 디바이스에서 최적의 사용자 경험을 제공할 수 있다.

- 화면 회전(orientation)이나 해상도(dpi) 같은 고급 특성도 조건에 포함할 수 있으니, 구체적인 사용 시나리오에 맞게 활용하면 된다.

- 마지막으로 테스트와 성능 최적화가 중요하다. 실제 기기에서 동작이 매끄러운지 반드시 확인해야 한다.
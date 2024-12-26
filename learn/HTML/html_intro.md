# HTML 개요

HTML(HyperText Markup Language)은 웹페이지의 구조와 콘텐츠를 정의하는 마크업 언어이다

1991년 팀 버너스 리(Tim Berners-Lee)가 제안한 이후, 웹의 표준이 되어 발전을 거듭해왔다

브라우저는 HTML 문서를 해석해 화면에 표시하며, 이 과정을 통해 사용자는 웹페이지와 상호작용한다

## HTML의 특징

1. **구조와 의미 부여**
    
    HTML은 문서의 구조를 정의하는 동시에 요소(element)에 의미를 부여한다
    
    예를 들어 `<header>`는 문서의 머리말, `<nav>`는 내비게이션, `<section>`은 콘텐츠의 구분 등으로 사용된다
    
2. **레이아웃이 아닌 콘텐츠 중심**
    
    HTML은 콘텐츠가 어떤 의미를 갖는지를 나타내는 데 집중해야 한다
    
    디자인이나 배치는 주로 CSS를 통해 구현한다
    
3. **웹 표준 준수 중요성**
    
    HTML을 웹 표준에 맞춰 작성하면 다양한 브라우저와 플랫폼에서 일관성 있는 화면을 볼 수 있다
    
    접근성(Accessibility)과 검색엔진 최적화(SEO)에도 도움이 된다
    
4. **확장성과 호환성**
    
    HTML5가 등장하면서 최신 브라우저들의 기능을 활용할 수 있게 되었다
    
    오디오, 비디오, 캔버스, SVG 등의 미디어 요소를 별도 플러그인 없이 사용할 수 있다
    

## HTML 문서 예시

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>HTML 소개</title>
</head>
<body>
  <header>
    <h1>HTML 개요</h1>
  </header>

  <section>
    <h2>HTML이란 무엇인가</h2>
    <p>HTML은 웹페이지의 뼈대를 구성하는 마크업 언어이다</p>
  </section>

  <footer>
    <p>Copyright © 2024</p>
  </footer>
</body>
</html>

```

1. `<!DOCTYPE html>`은 HTML5 문서임을 선언하는 구문이다
2. `<html>` 태그는 문서의 최상위 요소이며, `lang="ko"`로 문서의 언어가 한국어임을 명시한다
3. `<head>` 요소에는 문서 메타정보, 제목(`<title>`), CSS나 스크립트 참조 등이 들어간다
4. `<body>` 요소에는 실제 화면에 표시될 콘텐츠를 작성한다
5. `<header>`, `<section>`, `<footer>`와 같은 태그는 HTML5에서 제공하는 시맨틱 태그이며, 문서를 의미 단위별로 구분한다

## 정리

HTML은 웹 개발의 출발점이며, 구조와 의미 부여에 집중해야 한다

CSS, JavaScript와 함께 사용되어 현대 웹을 구성하는 핵심 요소가 된다

반응형 디자인, 접근성, SEO 등을 고려하기 위해서는 HTML을 표준에 맞춰 정확히 작성하는 습관이 중요하다
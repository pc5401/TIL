# CSS 개요

CSS(Cascading Style Sheets)는 웹 문서의 시각적 표현을 담당하는 스타일 언어이다. 구조와 표현을 분리함으로써 유지보수성과 재사용성을 높일 수 있다. 대표적으로 다음과 같은 특징이 있다.

- 선택자와 속성을 사용해 HTML 요소의 스타일을 지정한다.  
- **박스 모델**을 기반으로 레이아웃을 구성한다.  
- **플렉스 박스**와 **그리드 레이아웃** 같은 현대적인 레이아웃 방식을 지원한다.  
- **미디어 쿼리**를 통해 반응형 웹 디자인을 구현할 수 있다.  
- 애니메이션과 트랜지션을 이용해 동적인 효과를 줄 수 있다.  

## 예시 코드

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>CSS 개요 예시</title>
  <style>
    /* 기본적인 CSS 작성 예시이다 */
    body {
      margin: 0;
      padding: 0;
      font-family: sans-serif;
    }

    /* 클래스를 이용한 스타일 지정이다 */
    .container {
      width: 80%;
      margin: 0 auto;
      border: 1px solid #ccc;
    }

    /* 가상 클래스와 가상 요소를 활용한 예시이다 */
    .btn:hover {
      background-color: #eee;
    }

    .title::after {
      content: " - 추가 텍스트";
      color: #666;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="title">CSS 개요</h1>
    <button class="btn">버튼</button>
    <p>이 문서는 CSS의 전반적인 내용을 간단히 다루고 있다.</p>
  </div>
</body>
</html>
```

- `body`에서 여백과 패딩을 제거해 기본 스타일을 통일한다.
- `.container` 클래스는 중앙 정렬, 너비 설정, 테두리 등을 설정한다.
- `.btn` 클래스는 `:hover` 가상 클래스를 사용해 마우스 올림 시 배경색이 변하도록 한다.
- `.title` 클래스는 `::after` 가상 요소를 통해 텍스트가 추가로 보이도록 한다.

## 주의점과 팁

- 스타일 충돌을 방지하기 위해 **명확한 선택자**를 사용한다.
- 레이아웃을 쉽게 구성하려면 **플렉스 박스**나 **그리드 레이아웃**을 고려한다.
- 모든 요소가 **박스 모델**을 따르므로 `box-sizing` 속성을 잘 활용한다.
- **반응형**을 위해선 `%`, `vw`, `vh` 등 유동적인 단위를 사용하거나 **미디어 쿼리**를 작성한다.
- 애니메이션 효과나 트랜지션은 **페이지 접근성**을 저해하지 않는 선에서 사용한다.

# 박스 모델(Box Model)

박스 모델은 웹 페이지에서 요소를 배치하고 크기를 계산하는 기본 단위이다. 모든 요소는 직사각형 박스로 구성되며, 다음과 같은 구성 요소로 이루어진다.

1. **콘텐츠 영역(Content)**  
   실제 글자나 이미지가 들어가는 영역이다.

2. **패딩(Padding)**  
   콘텐츠 영역과 테두리(Border) 사이의 내부 여백이다.

3. **테두리(Border)**  
   요소의 테두리 선이다. 두께, 색상, 스타일 등을 지정할 수 있다.

4. **마진(Margin)**  
   요소와 다른 요소 사이의 외부 여백이다.


## box-sizing

요소의 너비와 높이를 계산할 때, 패딩과 테두리를 포함할지 여부를 결정하는 속성이다.

- `content-box`: 기본값이다. 요소의 총 크기를 계산할 때 패딩과 테두리는 제외한다.  
- `border-box`: 요소의 총 크기에 패딩과 테두리를 포함한다. 레이아웃 계산에 편리하다.

## 예시 코드

```css
.box-default {
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  margin: 10px;
  box-sizing: content-box; /* 기본값 */
}

.box-border {
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  margin: 10px;
  box-sizing: border-box;
}
```

- .box-default는 content-box를 사용한다. 콘텐츠 영역만 200px로 계산되고, 패딩과 테두리는 별도로 계산된다.
- .box-border는 border-box를 사용한다. 패딩과 테두리를 포함해 총 너비가 200px로 계산된다.

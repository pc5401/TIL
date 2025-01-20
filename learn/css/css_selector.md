# 선택자(Selector)

선택자는 HTML 요소에 스타일을 적용하기 위해 요소를 특정할 때 사용한다. 원하는 요소를 정확히 지칭함으로써 CSS 충돌을 줄이고, 유지보수를 쉽게 만든다.

## 기본 선택자

- **태그 선택자(Tag Selector)**  
  태그 이름으로 요소를 선택한다.  
  ```css
  p {
    color: blue;
  }
  ```

- **클래스 선택자(Class Selector)**
  
  클래스명을 가진 요소를 선택한다. 여러 요소에 공통 스타일을 적용할 때 유용하다.
  
  ```css
  .highlight {
    background-color: yellow;
  
  ```
  
- **아이디 선택자(ID Selector)**
  
  문서 내에서 유일한 식별자(`#id`)를 가진 요소를 선택한다. 문서에 중복되지 않도록 주의해야 한다.
  
  ```css
  #header {
    font-weight: bold;
  }
  ```
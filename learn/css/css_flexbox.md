# Flexbox

Flexbox는 1차원(가로 혹은 세로) 레이아웃을 손쉽게 구성할 수 있게 하는 CSS 레이아웃 방식이다.

전통적인 `float` 기반 레이아웃보다 **정렬, 공간 분배, 순서 변경** 등이 훨씬 유연하고 직관적이다.

---

## 기본 개념

1. **Flex Container**
    
    Flexbox 레이아웃을 사용할 부모 요소
    
    - `display: flex;` 또는 `display: inline-flex;`로 설정
    - 내부 자식 요소들은 **Flex Item**이 된다.
2. **Flex Item**
    
    Flex 컨테이너 내부의 **직계 자식 요소**
    
    - 컨테이너가 정해준 규칙에 따라 배치된다.
3. **주 축(Main Axis)과 교차 축(Cross Axis)**
    - **주 축**: `flex-direction`에 의해 결정되는 축. (기본값: 가로 축)
    - **교차 축**: 주 축에 **수직**인 축.
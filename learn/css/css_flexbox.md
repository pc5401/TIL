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

## Flex Container 주요 속성

### 1) `display: flex;`

자식 요소들을 Flex Item으로 만든다.

인라인 요소에 적용할 때는 `display: inline-flex;`를 사용한다.

```css
.container {
  display: flex;
  /* 또는 display: inline-flex; */
}
```

### 2) `flex-direction`

아이템들이 놓이는 **축의 방향**을 결정한다.

- `row` (기본값): 왼쪽→오른쪽 (가로 정렬)
- `row-reverse`: 오른쪽→왼쪽
- `column`: 위→아래 (세로 정렬)
- `column-reverse`: 아래→위

```css
.container {
  display: flex;
  flex-direction: row; /* 기본값 */
}
```

### 3) `flex-wrap`

한 줄에 아이템을 **강제로** 배치할지, 여러 줄로 **넘길지**를 결정한다.

- `nowrap` (기본값): 모든 아이템을 한 줄에 배치
- `wrap`: 공간이 부족하면 다음 줄로 넘어감
- `wrap-reverse`: 줄바꿈 순서가 반대

```css
.container {
  flex-wrap: wrap;
}
```

### 4) `justify-content`

**주 축(main axis)** 방향에서 아이템을 어떻게 정렬할지 결정한다.

- `flex-start` (기본값): 시작점 정렬
- `flex-end`: 끝점 정렬
- `center`: 중앙 정렬
- `space-between`: 아이템들 사이에 균등한 간격, 양 끝은 붙음
- `space-around`: 아이템 양 옆에 동일 간격
- `space-evenly`: 아이템 간 및 양 끝 모두 균등 간격

```css
.container {
  display: flex;
  justify-content: space-between;
}
```
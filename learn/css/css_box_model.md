# 박스 모델(Box Model)

CSS에서 요소는 모두 **박스(box)** 형태로 표현되며, 이 박스를 구성하는 요소를 알아두면 레이아웃을 정확하게 제어할 수 있다. 박스 모델은 다음과 같은 네 부분으로 구성된다.

1. **콘텐츠(content)** 영역
2. **패딩(padding)** 영역
3. **테두리(border)** 영역
4. **마진(margin)** 영역

```css
/* 기본적인 박스 스타일 예시 */
.box {
  width: 200px;
  padding: 20px;
  border: 2px solid #333;
  margin: 10px;
}
```

---

## 박스 모델의 구조

1. **콘텐츠(Content)**
    - 실제 텍스트나 이미지, 기타 콘텐츠가 들어가는 영역이다.
    - `width`와 `height` 속성을 이용해 콘텐츠 영역의 크기를 지정할 수 있다.
2. **패딩(Padding)**
    - 콘텐츠 주위의 **안쪽 여백**이다.
    - `padding` 속성으로 설정하며, 콘텐츠와 테두리 사이의 간격을 조절한다.
    - 배경색이나 배경 이미지는 패딩 영역까지 확장되어 보인다.
3. **테두리(Border)**
    - 패딩 바깥을 둘러싸는 **경계선**이다.
    - `border` 속성으로 두께, 스타일, 색상을 설정할 수 있다.
    - 테두리는 요소를 시각적으로 구분하거나 강조하는 용도로 사용한다.
4. **마진(Margin)**
    - 테두리 바깥쪽의 **바깥 여백**이다.
    - `margin` 속성으로 요소 간의 간격을 조절한다.
    - 인접한 박스(형제 요소)와의 거리를 결정하며, 배경색에는 영향을 주지 않는다.

----

## `box-sizing` 속성

CSS에서는 기본적으로 **콘텐츠 영역**을 기준으로 `width`와 `height`가 계산되는 `content-box` 모델을 사용한다. 패딩이나 테두리를 포함하지 않기 때문에, 실제 요소의 전체 너비와 높이는 `width + padding + border`가 된다.

```css
/* 기본 설정 (content-box) */
.box1 {
  box-sizing: content-box; /* 생략 가능 */
  width: 200px;
  padding: 20px;
  border: 2px solid #333;
}
```

- `.box1`의 **실제 요소 너비** = `200px(콘텐츠) + 20px(패딩 양쪽 합계 40px) + 2px(테두리 양쪽 합계 4px)` = 244px.

이를 명확하게 관리하고 싶다면 `box-sizing: border-box;`를 사용해 패딩과 테두리를 포함하여 `width`가 계산되도록 할 수 있다.

```css
/* border-box 모델 예시 */
.box2 {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 2px solid #333;
}
```

- `.box2`의 **실제 요소 너비** = `200px`(패딩, 테두리를 포함).
- 결과적으로 콘텐츠 영역의 너비는 200px에서 `(테두리 + 패딩)`만큼 줄어든 크기가 된다.

프로젝트 전체적으로 `border-box`를 적용하면 레이아웃 계산이 편해진다.

```css
/* 모든 요소에 border-box 적용 */
* {
  box-sizing: border-box;
}
```
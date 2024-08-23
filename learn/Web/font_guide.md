# 폰트를 활용한 웹 개발 가이드

[예시 폰트 : Pretendard](https://github.com/orioncactus/pretendard)
- `Pretendard`는 크로스 플랫폼에서 일관된 타이포그래피를 제공하는 현대적인 글꼴이다. 
- 웹 개발하면서 font 와 관련된 경험을 한 것을 정리해보겠다.

## 1. 로컬 폰트 사용
- 로컬 폰트는 폰트를 직접 서버에 호스팅하기 위해, 사용자 디바이스에 다운로드하여 사용하는 경우이다. 

### 장점
- 빠른 로드 시간 : 폰트 파일이 서버에서 직접 제공되므로, 외부 서버와의 추가 네트워크 요청 없이 빠르게 로드될 수 있다.
- 오프라인 접근 가능: 인터넷 연결이 끊겨도 폰트를 사용할 수 있다.
- 일관된 폰트 제공: 외부 서버의 변화나 장애로 인한 폰트 불일치를 방지할 수 있다.
- 커스터마이징 가능: 폰트를 직접 수정하거나 필요한 서브셋만 추출하여 로딩 시간을 최적화할 수 있다.

### 단점
- 초기 다운로드 크기: 폰트 파일을 로컬에 저장하면, 사용자가 처음 페이지를 로드할 때 폰트 파일을 함께 다운로드해야 하므로 초기 페이지 로딩 시간이 길어질 수 있다.
- 유지보수 비용: 폰트 파일을 관리하고 업데이트하는 작업이 필요하다. 폰트의 버전이 업데이트되면, 이를 수동으로 교체해야 한다.
- 브라우저 캐싱 문제: 브라우저 캐싱 설정이 잘못되면, 폰트가 필요 이상으로 자주 다시 다운로드될 수 있다.
- 꽤나 용량이 크다.

```css
@font-face {
    font-family: 'Pretendard';
    src: url('/path/to/fonts/Pretendard-Regular.woff2') format('woff2'),
         url('/path/to/fonts/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
}

body {
    font-family: 'Pretendard', sans-serif;
}
```

## 2. 웹 폰트 사용
- 웹 폰트를 사용하면 외부 CDN에서 폰트를 로드하여 사용한다. 
- 예시로 사용된 Pretendard는 다양한 CDN을 통해 제공되며, 간단한 링크나 `@import` 문을 통해 손쉽게 적용할 수 있다.
### 장점
- 적은 초기 로드 크기: 사용자는 폰트 파일을 외부 서버에서 불러오므로, 초기 페이지 로딩 시 필요한 리소스가 줄어든다. 또한, 웹 폰트 제공자는 종종 다양한 서브셋을 제공하여 필요에 따라 폰트 크기를 최적화할 수 있다.
- 자동 업데이트: 외부 폰트 제공자는 폰트의 버전 관리를 자동으로 해준다. 따라서 최신 버전이 자동으로 적용된다.
- 광범위한 캐싱: 웹 폰트는 CDN(Content Delivery Network)을 통해 제공되는 경우가 많아, 사용자의 브라우저에 이미 캐시된 폰트를 재사용할 가능성이 높다.
- 다양한 브라우저 호환성: 웹 폰트 제공자는 일반적으로 다양한 브라우저와 디바이스에서의 호환성을 유지하기 위해 폰트를 최적화한다.

### 단점
- 의존성 증가: 외부 서버에 의존하므로, 해당 서버가 다운되거나 속도가 느리면 폰트 로딩이 지연되거나 실패할 수 있다.
- 인터넷 연결 필요: 외부 폰트를 사용하려면 인터넷 연결이 필요하다. 오프라인 환경에서는 폰트가 제대로 로딩되지 않을 수 있다.
- 일관성 문제: 외부 서버의 폰트 버전이 변경되거나, 네트워크 문제로 인해 폰트가 일관되게 표시되지 않을 수 있다.
- 사용자 프라이버시 문제: 웹 폰트를 제공하는 외부 서버(특히 Google Fonts 등)로 사용자 정보가 전송될 수 있어, 일부 사용자는 프라이버시 우려를 가질 수 있다.


```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
```

```css
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css");

body {
    font-family: 'Pretendard', sans-serif;
}
```

## 3. 가변 폰트 사용
참고 링크
[Variable fonts (가변 폰트)](https://wit.nts-corp.com/2019/10/07/5686)
[구글: 가변 폰트의 놀라운 활용법](https://yozm.wishket.com/magazine/detail/1239/)
가변 폰트는 `font-weight`를 범위로 지정할 수 있어 다양한 굵기를 한 번에 사용할 수 있다. 가변 폰트를 사용하면 웹 페이지의 퍼포먼스가 향상되며, 특히 가변 다이나믹 서브셋을 사용하면 폰트 파일의 용량을 더욱 줄일 수 있다.

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
```

```css
body {
    font-family: 'Pretendard Variable', sans-serif;
    font-weight: 100 900;
}
```
- Pretendard Variable 폰트를 적용하여 font-weight 속성에 100에서 900까지의 다양한 두께를 사용할 수 있도록 설정
- 브라우저가 가변 폰트의 특성을 이해하고, 요청된 굵기에 맞춰 폰트를 렌더링하는 방식으로 진행된다.

## 4. 다이나믹 서브셋과 가변 다이나믹 서브셋
다이나믹 서브셋은 웹 폰트 로딩 시 사용된 글자만 포함된 폰트를 생성하여 전송함으로써 파일 크기를 최소화한다. 가변 다이나믹 서브셋은 여기에 가변 폰트를 결합하여 다양한 굵기와 스타일을 표현하면서도 최적의 퍼포먼스를 유지할 수 있게 한다.

### 다이나믹 서브셋 예시:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.min.css">
```

### 가변 다이나믹 서브셋 예시:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

## 5. font-weight 값 관리
Pretendard는 9가지 굵기 옵션을 제공하여 폰트의 굵기를 세부적으로 조정할 수 있다. 이를 통해 타이포그래피를 보다 정교하게 관리할 수 있다.

```css
h1 {
    font-family: 'Pretendard', sans-serif;
    font-weight: 700;
}

p {
    font-family: 'Pretendard', sans-serif;
    font-weight: 400;
}
```

## 6. 폰트 패밀리 설정
다양한 환경에서 일관된 폰트 경험을 제공하려면 시스템 폰트와 조합하여 font-family를 설정하는 것이 좋다.

```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Pretendard Variable', 'Pretendard', Roboto, 'Noto Sans KR', 'Segoe UI', sans-serif;
}
```

## 7. Next.js에서의 사용
Next.js와 같은 프레임워크에서도 Pretendard를 로컬 폰트로 활용할 수 있다. 이를 통해 프레임워크의 장점을 극대화할 수 있다.

```javascript
import localFont from 'next/font/local'

const pretendard = localFont({
  src: './fonts/PretendardVariable.woff2',
  display: 'swap',
  weight: '45 920',
});
```

## 결론
Pretendard 폰트를 웹 개발에 적용함으로써 가독성과 성능을 모두 잡을 수 있다. 로컬 폰트, 웹 폰트, 가변 폰트, 다이나믹 서브셋 등 다양한 방법을 활용하여 프로젝트에 맞는 최적의 폰트 전략을 수립하자. 이를 통해 웹 페이지의 디자인과 퍼포먼스를 동시에 향상시킬 수 있다.

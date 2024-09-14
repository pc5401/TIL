# 폰트를 활용한 웹 개발 가이드

웹 개발을 하면서 **폰트**의 활용은 사용자 경험과 디자인 품질에 큰 영향을 미친다. 특히 크로스 플랫폼에서 일관된 타이포그래피를 제공하는 폰트가 요즘 많은데 이 같은 폰트를 사용하면 더욱 효과적이다.(나는 이번에 **Pretendard** 폰트를 사용했다.) 이번 가이드에서는 폰트와 관련된 경험을 정리하고, 웹 개발에 적용하는 방법을 살펴보겠다.

## 목차

1. [로컬 폰트 사용](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [장점](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [단점](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [적용 예시](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
2. [웹 폰트 사용](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [장점](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [단점](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [적용 예시](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
3. [가변 폰트 사용](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [장점](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [단점](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [적용 예시](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
4. [다이나믹 서브셋과 가변 다이나믹 서브셋](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
    - [적용 예시](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
5. [font-weight 값 관리](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
6. [폰트 패밀리 설정](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
7. [Next.js에서의 사용](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)
8. [결론](https://www.notion.so/EC2-mysql-f93f6d80380e40aa9a7d3f22442f2dee?pvs=21)

---

## 1. 로컬 폰트 사용

로컬 폰트는 폰트 파일을 직접 서버에 호스팅하고, 사용자의 디바이스에 다운로드하여 사용하는 방식이다.

### 장점

- **빠른 로드 시간**: 폰트 파일이 서버에서 직접 제공되므로 외부 서버와의 추가 네트워크 요청 없이 빠르게 로드할 수 있다.
- **오프라인 접근 가능**: 인터넷 연결이 끊겨도 폰트를 사용할 수 있다.
- **일관된 폰트 제공**: 외부 서버의 변화나 장애로 인한 폰트 불일치를 방지할 수 있다.
- **커스터마이징 가능**: 폰트를 직접 수정하거나 필요한 서브셋만 추출하여 로딩 시간을 최적화할 수 있다.

### 단점

- **초기 다운로드 크기**: 폰트 파일을 로컬에 저장하면, 사용자가 처음 페이지를 로드할 때 폰트 파일을 함께 다운로드해야 하므로 초기 로딩 시간이 길어질 수 있다.
- **유지보수 비용**: 폰트 파일을 관리하고 업데이트하는 작업이 필요하다. 폰트 버전이 업데이트되면 이를 수동으로 교체해야 한다.
- **브라우저 캐싱 문제**: 브라우저 캐싱 설정이 잘못되면 폰트가 필요 이상으로 자주 다시 다운로드될 수 있다.
- **파일 용량 증가**: 폰트 파일 자체의 용량이 커서 전체 페이지 크기가 증가할 수 있다.

### 적용 예시

```css
@font-face {
    font-family: 'Pretendard';
    src: url('/fonts/Pretendard-Regular.woff2') format('woff2'),
         url('/fonts/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
}

body {
    font-family: 'Pretendard', sans-serif;
}
```

위 예시는 폰트 파일을 `/fonts` 디렉토리에 저장하고, `@font-face`를 사용하여 로드하는 방식이다.

---

## 2. 웹 폰트 사용

웹 폰트는 외부 CDN(Content Delivery Network)에서 폰트를 로드하여 사용하는 방식이다. Pretendard는 다양한 CDN을 통해 제공되며, 간단한 `<link>` 태그나 `@import` 문을 통해 적용할 수 있다.

### 장점

- **적은 초기 로드 크기**: 폰트 파일을 외부 서버에서 불러오므로 초기 페이지 로딩 시 필요한 리소스가 줄어든다.
- **자동 업데이트**: 외부 폰트 제공자는 폰트의 버전 관리를 자동으로 해주므로 최신 버전이 자동으로 적용된다.
- **광범위한 캐싱**: CDN을 통해 제공되기 때문에 사용자의 브라우저에 이미 캐시된 폰트를 재사용할 가능성이 높다.
- **다양한 브라우저 호환성**: 웹 폰트 제공자는 다양한 브라우저와 디바이스에서의 호환성을 유지하기 위해 폰트를 최적화한다.

### 단점

- **의존성 증가**: 외부 서버에 의존하므로 해당 서버가 다운되거나 속도가 느리면 폰트 로딩이 지연되거나 실패할 수 있다.
- **인터넷 연결 필요**: 외부 폰트를 사용하려면 인터넷 연결이 필요하다. 오프라인 환경에서는 폰트가 제대로 로딩되지 않을 수 있다.
- **일관성 문제**: 외부 서버의 폰트 버전이 변경되거나 네트워크 문제로 인해 폰트가 일관되게 표시되지 않을 수 있다.
- **사용자 프라이버시 우려**: 웹 폰트를 제공하는 외부 서버로 사용자 정보가 전송될 수 있어 일부 사용자는 프라이버시에 대한 우려를 가질 수 있다.

### 적용 예시

### `<link>` 태그 사용

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
```

### `@import` 문 사용

```css
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css");

body {
    font-family: 'Pretendard', sans-serif;
}
```

---

## 3. 가변 폰트 사용

가변 폰트(Variable Font)는 하나의 폰트 파일로 다양한 굵기와 스타일을 표현할 수 있는 기술이다. `font-weight`나 `font-stretch` 등의 속성을 범위로 지정하여 다양한 변화를 줄 수 있다.

### 장점

- **파일 크기 감소**: 여러 굵기나 스타일의 폰트를 하나의 파일로 제공하므로 전체 폰트 파일의 용량이 줄어든다.
- **유연한 디자인**: 디자인 요구에 따라 폰트의 굵기나 너비 등을 세밀하게 조절할 수 있다.
- **퍼포먼스 향상**: 필요한 폰트 파일 수가 줄어들어 로딩 속도가 개선된다.

### 단점

- **브라우저 지원 제한**: 일부 오래된 브라우저에서는 가변 폰트를 지원하지 않을 수 있다.
- **복잡한 구현**: 가변 폰트의 특성을 이해하고 적절히 활용하려면 추가적인 학습이 필요하다.

### 적용 예시

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css">
```

```css
body {
    font-family: 'Pretendard Variable', sans-serif;
    font-weight: 100 900;
}
```

위 예시는 `Pretendard Variable` 폰트를 적용하여 `font-weight` 속성에 100에서 900까지의 다양한 두께를 사용할 수 있도록 설정한 것이다.

---

## 4. 다이나믹 서브셋과 가변 다이나믹 서브셋

다이나믹 서브셋은 웹 폰트 로딩 시 실제로 사용된 글자만 포함된 폰트를 생성하여 전송함으로써 파일 크기를 최소화하는 기술이다. 가변 다이나믹 서브셋은 여기에 가변 폰트를 결합하여 다양한 굵기와 스타일을 표현하면서도 최적의 퍼포먼스를 유지할 수 있게 한다.

### 적용 예시

### 다이나믹 서브셋

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pretendard-dynamic-subset@latest/pretendard.css">
```

### 가변 다이나믹 서브셋

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pretendard-variable-dynamic-subset@latest/pretendard.css">
```

---

## 5. font-weight 값 관리

Pretendard는 100부터 900까지 9가지 굵기 옵션을 제공하여 폰트의 굵기를 세부적으로 조정할 수 있다. 이를 통해 타이포그래피를 보다 정교하게 관리할 수 있다.

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

---

## 6. 폰트 패밀리 설정

다양한 환경에서 일관된 폰트 경험을 제공하려면 시스템 폰트와 조합하여 `font-family`를 설정하는 것이 좋다.

```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Pretendard Variable', 'Pretendard', Roboto, 'Noto Sans KR', 'Segoe UI', sans-serif;
}
```

위 예시는 다양한 운영체제와 브라우저에서 최적의 폰트를 사용할 수 있도록 설정한 것이다.

---

## 7. Next.js에서의 사용

Next.js와 같은 프레임워크에서도 Pretendard를 로컬 폰트로 활용할 수 있다. 이를 통해 프레임워크의 장점을 극대화할 수 있다.

```jsx
import localFont from 'next/font/local'

const pretendard = localFont({
  src: './fonts/PretendardVariable.woff2',
  display: 'swap',
  weight: '100 900',
});
```

위 코드는 Next.js에서 `next/font`를 사용하여 로컬 폰트를 설정하는 예시이다.

---

## 결론

웹 개발에서 폰트 선택과 적용은 사용자 경험과 디자인의 완성도를 높이는 중요한 요소이다. Pretendard와 같은 폰트를 활용하여 로컬 폰트, 웹 폰트, 가변 폰트, 다이나믹 서브셋 등 다양한 방법을 적용하면 가독성과 퍼포먼스를 모두 향상시킬 수 있다. 프로젝트의 특성과 요구 사항에 맞는 최적의 폰트 전략을 수립하여 더욱 완성도 높은 웹 서비스를 제공하자.
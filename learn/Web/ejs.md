# EJS와 Express 통합 사용법

### EJS 기본 사용법

EJS 템플릿에서는 `<% %>` 태그를 사용하여 JavaScript 코드를 HTML에 삽입할 수 있다. 예를 들어, 특정 조건에 따라 HTML을 렌더링하려면 다음과 같이 작성한다:

```html
<% if (user) { %>
  <h2><%= user.name %></h2>
<% } %>
```

위 코드에서는 `user` 객체가 존재할 경우, 해당 사용자의 이름을 `<h2>` 태그 안에 출력하게 된다. `<%= %>` 태그는 데이터를 HTML로 출력하며, HTML 이스케이프가 자동으로 적용된다.

## EJS와 Express 설정

Express에서 EJS를 사용하려면 먼저 EJS를 설치해야 한다. npm 또는 yarn을 통해 설치할 수 있다:

```bash
npm install ejs
```

또는

```bash
yarn add ej
```

설치 후, Express 앱에서 EJS를 템플릿 엔진으로 설정할 수 있다:

```jsx
let express = require('express');
let app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  res.render('index', {foo: 'FOO'});
});

app.listen(4000, () => console.log('Example app listening on port 4000!'));
```

위 코드에서는 `index.ejs` 템플릿을 렌더링하여 "Hello FOO"라는 텍스트가 출력된다.

## EJS의 주요 함수

EJS는 템플릿을 컴파일하고 렌더링하기 위한 다양한 함수를 제공한다:

- `ejs.compile(str, options)`: 문자열을 EJS 템플릿으로 컴파일한다.
- `template(data)`: 컴파일된 템플릿에 데이터를 전달하여 HTML을 생성한다.
- `ejs.render(str, data, options)`: 문자열 템플릿과 데이터를 사용하여 즉시 HTML을 렌더링한다.
- `ejs.renderFile(filename, data, options, callback)`: 파일로부터 템플릿을 읽어 데이터를 적용한 후 렌더링된 HTML을 반환한다.

이 함수들을 활용하면, 파일에서 직접 템플릿을 불러오거나, 문자열로 정의된 템플릿을 동적으로 컴파일하여 HTML을 생성할 수 있다.

## EJS 옵션 설정

EJS는 템플릿 동작을 세밀하게 조정할 수 있는 다양한 옵션을 제공한다. 대표적인 옵션은 다음과 같다:

- `cache`: 컴파일된 템플릿을 캐시하여 성능을 향상시킨다.
- `filename`: 캐싱 및 `include` 기능에서 사용되는 파일 이름을 설정한다.
- `root`: `include` 경로의 기준이 되는 프로젝트 루트를 설정한다.
- `views`: `include` 시 사용할 경로 배열을 설정한다.
- `compileDebug`: 디버그 정보를 포함할지 여부를 설정한다.
- `delimiter`: 내부 구분자로 사용할 문자를 설정한다. 기본값은 `%`.
- `strict`: 엄격 모드에서 함수가 생성되도록 설정한다.
- `async`: 비동기 렌더링을 활성화하여 `async/await` 문법을 사용할 수 있게 한다.

### Express에서 EJS 옵션 설정 방법

Express에서 EJS에 옵션을 설정하는 방법은 여러 가지가 있다:

1. **뷰 옵션(View options) 설정**: `app.set`을 사용하여 전역 EJS 옵션을 설정할 수 있다. 이를 통해 한 번의 설정으로 모든 템플릿에 동일한 옵션을 적용할 수 있다.
    
    ```jsx
    app.set('view options', {delimiter: '?'});
    ```
    
2. **커스텀 렌더 함수(Custom render function)**: `render` 함수를 재정의하여 특정 옵션을 사용하도록 커스터마이즈할 수 있다.
    
    ```jsx
    let ejsOptions = {delimiter: '?'};
    app.engine('ejs', (path, data, cb) => {
      ejs.renderFile(path, data, ejsOptions, cb);
    });
    ```
    
3. **앱 로컬(App locals)**: `app.locals`에 설정된 속성은 모든 렌더링 시 자동으로 EJS 옵션으로 전달된다.
    
    ```jsx
    app.locals.delimiter = '?';
    ```
    
4. **데이터와 함께 옵션 전달**: 렌더링 시 각 템플릿에 개별적으로 옵션을 전달할 수 있다.
    
    ```jsx
    app.get('/', (req, res) => {
      res.render('index', {foo: 'FOO', delimiter: '?'});
    });
    ```
    

## EJS 태그의 종류와 용도

EJS에서는 다양한 태그를 사용하여 템플릿 내에서 데이터를 처리하고 렌더링할 수 있다:

- `<% %>`: 제어 흐름을 위한 스크립트 태그.
- `<%_ %>`: 앞의 공백을 제거하는 스크립트 태그.
- `<%= %>`: HTML로 이스케이프된 값을 출력하는 태그.
- `<%- %>`: 이스케이프되지 않은 값을 출력하는 태그.
- `<%# %>`: 주석 태그, 렌더링되지 않는다.
- `<%%>`: 리터럴 `<%`를 출력하는 태그.
- `%>`: 일반적인 닫기 태그.
- `%>`: 뒤에 오는 개행을 제거하는 태그.
- `_-%>`: 뒤의 모든 공백을 제거하는 태그.

### Include 기능으로 컴포넌트화된 템플릿 구성

EJS의 `include` 기능을 사용하면, 반복되는 UI 요소를 별도의 파일로 분리하여 재사용할 수 있다. 예를 들어, 네비게이션 바와 같은 공통 UI를 `navbar.ejs` 파일로 분리하여 사용할 수 있다:

```
<!-- navbar.ejs -->
<nav class="navbar">
  <ul class="navbar-blocks">
    <% for (var i = 0; i < links.length; i++) { %>
      <li class="nav-icon">
        <a href="<%= links[i].href %>" class="nav-link">
          <%= links[i].icon %>
          <span class="link-text"><%= links[i].text %></span>
        </a>
      </li>
    <% } %>
  </ul>
</nav>
```

그리고 `main.ejs` 파일에서 이를 포함하여 사용할 수 있다:

```
<!-- main.ejs -->
<html>
  <head>
    <title>Homepage</title>
  </head>
  <body>
    <% include navbar.ejs %>
    <script>
      const links = [
        { href: '/', icon: '<svg>...</svg>', text: 'Home' },
        { href: 'collection', icon: '<svg>...</svg>', text: 'Collection' },
        { href: 'live', icon: '<svg>...</svg>', text: 'Live' }
      ];
    </script>
  </body>
</html>
```

페이지가 로드되면, 네비게이션 바 컴포넌트가 마치 원래의 HTML 코드의 일부인 것처럼 표시된다.

## 커맨드 라인 인터페이스(CLI) 지원

EJS는 커맨드 라인에서도 사용할 수 있는 도구를 제공한다. 이를 통해 템플릿을 컴파일하고 렌더링할 수 있으며, 다양한 옵션을 제공한다. 예시:

```bash
$ ejs -p [ -c ] ./template_file.ejs -o ./output.html
$ ejs ./test/fixtures/user.ejs name=Lerxst
$ ejs -n -l _ ./some_template.ejs -f ./data_file.js
```

이 명령어들은 템플릿을 파일에서 읽어 들여 렌더링된 HTML을 파일로 출력하거나, JSON 데이터 파일을 사용하여 템플릿을 렌더링하는 데 사용될 수 있다.

## 캐싱 기능

EJS는 기본적으로 중간 JavaScript 함수의 캐싱 기능을 제공하여 성능을 최적화할 수 있다. 예를 들어, `lru-cache` 라이브러리를 사용하여 LRU 캐싱을 적용할 수 있다:

```jsx
let ejs = require('ejs');
let LRU = require('lru-cache');
ejs.cache = LRU(100); // 100개의 항목을 캐싱하는 LRU 캐시
```

캐시를 지워야 할 경우 `ejs.clearCache()`를 호출할 수 있으며, 필요에 따라 캐시의 크기를 조정할 수 있다.

## 레이아웃 구성

EJS는 블록 기능을 직접 지원하지 않지만, `include` 기능을 활용하여 헤더, 푸터 등을 포함하는 방식으로 레이아웃을 구성할 수 있다. 예를 들어, 다음과 같이 레이아웃을 구성할 수 있다:

```
<%- include('header'); -%>
<h1>Title</h1>
<p>My page</p>
<%- include('footer'); -%>
```

이 방식으로 각 페이지에서 동일한 헤더와 푸터를 사용할 수 있으며, 레이아웃을 쉽게 유지 관리할 수 있다.

## 클라이언트 사이드에서 EJS 사용

EJS는 서버뿐만 아니라 클라이언트 사이드에서도 사용할 수 있다. 클라이언트 사이드에서 EJS를 사용하려면 EJS 스크립트를 HTML 페이지에 포함시키면 된다:

```html
<div id="output"></div>
<script src="ejs.min.js"></script>
<script>
  let people = ['geddy', 'neil', 'alex'];
  let html = ejs.render('<%= people.join(", "); %>', {people: people});
  document.getElementById('output').innerHTML = html;
</script>
```

이 방식으로 클라이언트에서 동적으로 HTML을 생성할 수 있다. 다만, 클라이언트 사이드에서는 파일 시스템 접근이 불가능하므로 `ejs.renderFile`은 사용할 수 없으며, `include` 기능도 콜백을 통해 별도로 처리해야 한다.
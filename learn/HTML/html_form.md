# 폼 태그(<form>와 입력 요소

HTML 폼(`<form>`)은 사용자에게 입력을 받을 수 있는 인터페이스를 제공하며, 이를 서버로 전송해 처리할 수 있도록 해준다

로그인, 회원가입, 게시글 작성 등 사용자 입력이 필요한 모든 작업에서 핵심적으로 사용된다

## 1) 폼의 기본 구조 (`<form>`)

```html
<form action="/submit" method="POST">
  <label for="username">아이디</label>
  <input type="text" id="username" name="username">

  <label for="password">비밀번호</label>
  <input type="password" id="password" name="password">

  <button type="submit">로그인</button>
</form>
```

1. `<form>`: 폼 영역을 나타내는 태그
    - `action`: 폼 데이터를 전송할 서버의 URL(엔드포인트)을 지정
    - `method`: 데이터 전송 방식(`GET`, `POST`, `PUT` 등)을 지정 (기본값: `GET`)
2. `<label>`: 입력 필드에 대한 설명을 제공하는 태그
    - 접근성을 위해 `for` 속성과 입력 요소(`id`)를 연결해주는 것이 좋다
3. `<input type="text" name="username">`: 텍스트를 입력받는 기본 요소
    - `name`: 서버 측에서 해당 필드의 값을 식별하는 데 사용
    - `id`: `<label for="id명">`과 연결하거나 JavaScript에서 요소를 선택하는 데 사용
4. `<button type="submit">`: 폼을 서버로 전송(submit)하는 버튼

---

## 2) 다양한 입력 타입

HTML5부터는 더 다양한 `type` 속성이 도입되어, 브라우저 수준에서 사용자 입력을 제어할 수 있게 되었다

1. **텍스트 입력 (`text`)**
    - 기본적인 한 줄짜리 텍스트 입력 필드
2. **비밀번호 (`password`)**
    - 입력 문자가 가려지는 필드
3. **이메일 (`email`)**
    - 이메일 형식 검사(유효성) 등이 적용될 수 있다 (브라우저마다 다름)
4. **URL (`url`)**
    - URL 형식 검사 적용
5. **숫자 (`number`)**
    - 숫자만 입력하도록 하는 필드 (증가·감소 화살표 UI 제공)
6. **날짜·시간 (`date`, `time`, `datetime-local` 등)**
    - 달력이나 시간 선택 UI를 제공 (브라우저마다 형태가 다를 수 있음)
7. **체크박스 (`checkbox`)**
    - 여러 항목 중 다중 선택이 가능
8. **라디오 버튼 (`radio`)**
    - 여러 항목 중 한 가지만 선택 가능(같은 `name`으로 묶임)
9. **파일 (`file`)**
    - 로컬에서 파일을 선택하고 업로드하기 위한 필드

예시:

```html
<label for="useremail">이메일</label>
<input type="email" id="useremail" name="useremail" placeholder="example@domain.com" required>

<label>
  <input type="radio" name="gender" value="male" checked> 남성
</label>
<label>
  <input type="radio" name="gender" value="female"> 여성
</label>

<label for="profile">프로필 사진 업로드</label>
<input type="file" id="profile" name="profile">
```

- `placeholder`: 필드에 힌트를 표시
- `required`: 브라우저 단에서 입력이 필수임을 검사
- `checked`: 체크박스나 라디오 버튼의 기본 선택 상태 지정

---

## 3) 선택 목록 (`<select>` 와 `<option>`)

드롭다운 목록을 제공하려면 `<select>`와 `<option>`을 사용한다

```html
<label for="country">국가 선택</label>
<select id="country" name="country">
  <option value="KR">한국</option>
  <option value="US">미국</option>
  <option value="JP">일본</option>
</select
```

- `<option>` 태그의 `value` 속성은 서버로 전달될 실제 값
- `<select multiple>` 속성을 부여하면 여러 항목을 선택할 수 있다

---

## 4) 텍스트 영역 (`<textarea>`)

여러 줄 입력이 필요한 경우 `<textarea>`를 사용한다

```html
<label for="comment">댓글</label>
<textarea id="comment" name="comment" rows="5" cols="40" placeholder="최대 300자까지 입력 가능"></textarea>
```

- `rows`, `cols`: 기본 표시 크기를 지정 (CSS로도 조절 가능)
- 태그 사이에 기본 문구를 삽입하면 초기 텍스트가 된다

---

## 5) 폼 전송과 유효성 검사

- **서버 사이드 유효성 검사**: 폼 제출 후 서버 측에서 데이터 검증 (필수)
- **클라이언트 사이드 유효성 검사**: HTML5 `required`, `pattern` 등의 속성과 JS 스크립트로 1차 검증
    - 예: `<input type="text" pattern="[A-Za-z0-9]{4,12}">`

예시:

```html
<form action="/register" method="POST">
  <input type="text" name="userid" required pattern="[A-Za-z0-9]{4,12}" placeholder="영문, 숫자 4~12자">
  <button type="submit">가입하기</button>
</form>
```

- 브라우저는 패턴(regex)을 만족하지 못하면 폼을 전송하지 않는다 (브라우저마다 동작 방식 다를 수 있음)

---

## 6) 예시

```html
<form action="/signup" method="POST">
  <h2>회원 가입</h2>

  <label for="username">아이디</label>
  <input type="text" id="username" name="username" required>

  <label for="email">이메일</label>
  <input type="email" id="email" name="email" placeholder="example@domain.com" required>

  <label for="password">비밀번호</label>
  <input type="password" id="password" name="password" minlength="6" required>

  <label for="bio">자기소개</label>
  <textarea id="bio" name="bio" rows="5" cols="40"></textarea>

  <label for="job">직업</label>
  <select id="job" name="job">
    <option value="dev">개발자</option>
    <option value="designer">디자이너</option>
    <option value="pm">기획/PM</option>
  </select>

  <button type="submit">가입 완료</button>
</form>
```

- `minlength`, `maxlength` 등을 사용하면 입력 길이를 제어할 수 있다
- `<form>` 안에서는 원하는 만큼 다양한 입력 요소를 배치 가능

---

## 요약

1. `<form>`과 입력 요소들은 사용자와 상호작용하는 핵심 수단이다
2. `method="GET"` 혹은 `POST`를 적절히 사용해 서버로 데이터를 전송한다
3. HTML5에서 제공하는 다양한 `type`으로 브라우저 기본 유효성 검사를 활용할 수 있다
4. `<select>`와 `<textarea>`를 사용해 드롭다운, 여러 줄 입력 등의 옵션을 제공한다
5. 반드시 **서버 사이드 유효성 검사**를 해 안전한 데이터 처리를 보장해야 한다
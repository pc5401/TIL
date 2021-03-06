

[toc]

# 2022-01-12 복습(마크다운 + CLI )

## 마크다운

#### 1. 제목



\# 띄어쓰기로 사용할 수 있다. #의 개수로 제목의 사이즈(중요도 혹은 수준)조절

글시를 키우려고 #을 사용하는 게 아니라, 문서의 구조를 확립하기 위해 사용합니다.

[toc]사용해서 목차를 만들 수 있습니다.



#### 2. 리스트

\- , \* , \+ 뒤에 띄어쓰기로 순서 없는 리스트를 사용할 수 있습니다.

- 순서 없는 리스트
  - 탭을 한 번 누르면 리스트 안에 다시 리스트를 만들 수 있어요!
    - 여러번도 가능합니다. (다만 점 모양은 검정색 네모(3번째꺼)가 한계)
- shift tab을 누르게 되면 들여쓰기(indentation)이 한칸 물러나게 됩니다.



#### 3. 코드 블럭

```python
print(" ```에 사용하는 프로그래밍 언어를 입력하게 되면 해당 언어에 맞게 코드블럭이 표시됩니다. ")
```

`print("hello world")` 이렇게 \` 를 단어 양쪽에 붙이면 불록화가 된다.



#### 4. 이미지

\!\[이미지 이름](이미지 주소)

입력하면 된다. 

#### 5. 링크

\[보여질 이름](url)

ctrl + 클릭으로 이동 가능

ex [들여쓰기란?](https://ko.wikipedia.org/wiki/%EB%93%A4%EC%97%AC%EC%93%B0%EA%B8%B0)

#### 6. 테이블

| 컬럼1  |   컬럼2    | 컬럼3 |      |      |
| :----: | :--------: | :---: | ---- | ---- |
| 이렇게 | 할 수 있어 |       |      |      |
|        |            |       |      |      |
|        |            |       |      |      |

#### 7. 인용문

\> 하고 띄어쓰면 인용문이다.

> 봐 인용문~

#### 8. 수평선

\--- 짝대기 3개를 많이 쓴다. \*, \_ 도 가능하지만, shift를 클릭해야하기 때문에 비추다.

#### 9. 강조

이탤릭체는 \* 를 원하는 구역 양쪽에 배치 *이탤릭체*

볼드체는 \*\*를 양쪽에 배치 **볼드체 **

그럼 \* 3개는 ***볼드와 이탤릭체***를 동시에 

---

***

~~취소선~~

## CLI

#### 개념

> CLI(Command Line interface)

우리가 평소 사용하는 GUI 와 달리 코드(명령어)로 컴퓨터와 상호작용하는 방법이다.

#### 1. 홈 디텍토리

- 내 계정이 있는 디렉토리를 의미합니다. c:\users\(유저이름)

#### 2. 상대경로 vs 절대경로

- 상대경로 : 내 위치에 따라서 접근하는 곳이 바뀔 수 있음 
  - ex. 203호로 갈 경우 반포주공인지 아님 은마아파트인지에 따라 접근하는 곳이 바뀜
- 절대경로 : 어디서 접근하던지 바뀌지 않음
  - ex. 사랑시 고백구 행복동 천국 아파트 1004동 203호 어디로 갈지 확실함

#### 3. 디렉토리 지칭

- `..`은 부모 디렉토리를 지칭
- `.` 은 현재 디렉토리를 가리킵니다.

#### 4. 명령어

- ls
  - list segment
  - 현재 폴더에 어떤 파일이 있는지 확인
- cd
  - change directory
  - cd { 폴더 }
  - cd `..` 을 하게 되면 부모 디렉토리로 이동하게 됩니다!
- mkdir
  - 폴더로이동하겠어!
  - cd {폴더}
    - {폴더}를 생성하겠어 
- touch
  - touch {파일}
  - {파일}을 생성한다
  - 반드시 확장자를 포함해야 한다
- start {파일}
  - 파일 실행
  - Mac은 `open` 이다
- mv {파일1}{파일2}
  - {파일1}을 {파일2} 로 바꾸겠어
  - mv {파일}{폴더}
    - {파일}을 {폴더}로 옮기겠어
- rm {파일}
  - 파일 지우기
  - 휴지통으로 가지 않고 바로 지워짐
- rm -r {폴더}
  - 폴더 지우기 -r(recursive)

## 220113 복습

- 초기세팅
  - git config --global user.name {유저네임}
  - git config --global user.email {유저이메일}
  - git config --global -l
    - 설정 확인

| 초기에 한 번만 해도 된다. but 잊지 말자.

- git init

  - 깃을 시작한다!
  - 이걸 실행하면 `.git` 이라는 숨긴 폴더가 생성된다. 
  - `.git` 폴더를 삭제하면 git 이 삭제된다.

- git add {파일}

  - 파일을 staging area에 올려 놓는다!
  - (처음 만든 파일은 깃이 관리를 하기 시작한다)
  - git add .
    - 을 하게되면 해당 폴더의 모든 아이들을 추가합니다!

- git status

  - 깃이 관리하고 있는 파일들의 상태를 확인한다

- git commit -m "메시지"

  - "메시지"라는 변경사항을 담아서 코밋을 남긴다
    - `git commit -am "메세지"` 라고 하면 `add`와 `commit`이 같이된다. 근데 실수할 수 있으니 걍 add 하자

- git commit

  - 만 한 경우에는 vim 에디터가 나옵니다
  - `i`를 입력하시면 insert 모드가 되어 입력이 가능합니다.
  - `esc`를 눌러 insert모드에서 나옵니다
  - `:wq`를 입력하여 저장하고 나옵니다. (이상하게 난 qw 라고 바꿔서 헷갈리더라.)
  - enter를 누번 눌러 내용을 구체적으로 작성 가능합니다!(additional)

- git log

  - 코밋 상태를 확인한다

  - git log --oneline

    - 코밋 상태를 한줄로 확인한다

  - git log -{숫자}

    - 숫자개의 코밋만 확인한다

  - git log --oneline --all --graph 

    - 전체 코밋 상태가 그래프로 연결되어 출력된다.

    



#### 깃허브와 연결

- git init

- 깃허브 레포 만들기
  - 레포의 주소 복사하기( 가운데에 버튼이 있습니다!)

- git remote add origin {url}
  - 깃허브 주소를 'origin'이라는 별명으로 원격으로 연결할거야!
  - `add` 가 들어간다.(자주 까먹음) 
- git remote -v
  - 원격으로 어디에 연결되어있는지 확인할게!
- git push origin master
  - origin이란 별명을 가진 깃허브 레포의 master브랜치에 push 할꺼야!
  - git push -u origin master
    - origin master는 계속 사용하니 설정을 저장하여 이후에는 생략할꺼야!
    - 이후에는 `git push`만 해도 push가 가능합니다!
    - 하지만, 다른 브렌치에서 작업하면 다시 `origin` `master` 를 입력해야 한다.



### clone

- git clone {url}

  - 깃이 아닌 상태에서 깃허브의 레포지토리를 복사해 오는 것
  - 최초 1회만 하면 됩니다!

  1. `git clone {url}` -> 레포 이름으로 폴더를 생성하여서 clone
  2. `git clone {url} .` -> git bash가 실행된 폴더에 clone
  3. `git clone {url} {폴더이름}` -> 폴더이름을 생성하여 clone

- git pull

  - 최초의 clone 이후 (또는 이미 깃인 상태에서) 깃허브의 코밋으로 최신화 시킨다
  - 자주 pull 하는 습관을 가지자.

### branch

- git branch
  - 어떤 브랜치가 존재하는지, *이 있는게 현재 브랜치
- git branch {브랜치이름}
  - 브랜치를 만듦
- git switch {브랜치이름}
  - 해당 브랜치로 옮김
  - git switch -c {브랜치이름}
    - 브랜치를 만듦과 동시에 해당 브랜치로 옮김
- git checkout {브랜치이름}
  - `switch`랑 같은 역할을 한다. 이게 구버전 
- git branch -d {브랜치이름}
  - 브랜치 삭제
- git merge {브랜치이름} 
  - 현재 브랜치에서 {브랜치이름}을 병합시킴
  - CONFLICT (pull도 마찬가지)
    - A'B + AB' = A'B'
    - A' +Ã = CONFLICT!
      - 해결 후 add, commit

code(vscode)로 들어가서 해결하면 눈에 잘 띈다.

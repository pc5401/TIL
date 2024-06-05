# git 기초

### git 처음과 기본

- git 버젼 확인
  - git — version
- 초기세팅
  - git config --global user.name {유저네임}
  - git config --global user.email {유저이메일}
  - git config --global -l
    - 설정 확인

> 초기에 한 번만 해도 된다. but 잊지 말자.

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

### **깃허브와 연결**

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

### **clone**

- git clone {url}
  - 깃이 아닌 상태에서 깃허브의 레포지토리를 복사해 오는 것
  - 최초 1회만 하면 됩니다!
  1. `git clone {url}` -> 레포 이름으로 폴더를 생성하여서 clone
  2. `git clone {url} .` -> git bash가 실행된 폴더에 clone
  3. `git clone {url} {폴더이름}` -> 폴더이름을 생성하여 clone
- git pull
  - 최초의 clone 이후 (또는 이미 깃인 상태에서) 깃허브의 코밋으로 최신화 시킨다
  - 자주 pull 하는 습관을 가지자.

### **branch**

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

## **추가로 알아두면 좋을 git 명령어들**

### **reset, restore**

- `git reset {옵션} {커밋}`
  
  - 특정 커밋으로 되돌아간다. 이 때 변경사항은 모두 사라질 수 있다.
  - `--soft`: 변경사항을 유지한다.
  - `--mixed`: staging area의 변경사항을 제거한다.
  - `--hard`: 모든 변경사항을 제거한다.

예시)

```shell
# 상황 : 최근 커밋에서 파일을 실수로 추가하여 수정이 필요함
git reset --soft HEAD~1
# 최근 커밋을 제거하고, 변경사항은 유지됨

git reset --hard HEAD~1
# 최근 커밋을 제거하고 모든 변경사항을 삭제함
```

### **revert**

- `git revert {커밋}`
  
  - 특정 커밋을 취소하는 새로운 커밋을 만든다. 기록을 보존한다.

예시)

```shell
# 상황: 이전 커밋이 잘못되었지만, 기록을 보존하고 싶음
git revert abc1234
# abc1234는 되돌리려는 해시. 
```

### restore

- `git restore {파일}`
  
  - 작업 디렉토리의 변경사항을 취소한다.
  - `--staged`: 스테이징 영역의 변경사항을 취소한다.
  - `--source {커밋}`: 특정 커밋의 상태로 파일을 복원한다.

예시)

```shell
# 상황: 특정 파일에서 최근 변경사항을 취소하고 원래 상태로 복원하고 싶음
git restore example.txt # example.txt 파일의 작업 디렉토리 변경사항을 취소
git restore --staged example.txt #  example.txt 파일을 스테이징 영역에서 제거하고, 워킹 디렉토리 상태로 되돌
git restore --source abc123 example.txtabc123은 복원하려는 커밋의 해시



```

### **stash**

- `git stash`
  - 현재 작업 중인 변경사항을 임시로 저장하고, 깨끗한 작업 디렉토리를 유지한다.
- `git stash pop`
  - 마지막으로 저장한 stash를 적용하고, stash에서 제거한다.
- `git stash list`
  - 저장된 stash 목록을 확인한다.
- `git stash apply {stash@{n}}`
  - 특정 stash를 적용한다. 목록에서 `stash@{n}` 형태로 확인할 수 있다.

### **tag**

- `git tag {태그명}`
  - 특정 커밋에 태그를 추가한다.
- `git tag -a {태그명} -m "메시지"`
  - 주석이 달린 태그를 추가한다.
- `git push origin {태그명}`
  - 원격 저장소에 태그를 푸시한다.
- `git push origin --tags`
  - 원격 저장소에 모든 태그를 푸시한다.

### **변경사항 비교**

- `git diff`
  - 작업 디렉토리와 스테이징 영역의 변경사항을 비교한다.
- `git diff --staged`
  - 스테이징 영역과 마지막 커밋의 변경사항을 비교한다.
- `git diff {커밋1} {커밋2}`
  - 두 커밋 간의 변경사항을 비교한다.

## **원격 저장소 관리**

- `git remote rename {기존 이름} {새 이름}`
  - 원격 저장소의 이름을 변경한다.
- `git remote remove {이름}`
  - 원격 저장소를 제거한다.

## **기타 유용한 팁**

- `.gitignore`
  - 깃이 무시할 파일이나 디렉토리를 지정한다.
    예시:
    
    ```bash
    *.log
    build/
    temp/
    ```

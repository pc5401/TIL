# 기본 명령어

## man : 명령어 도움말

> 기본 형식: man <명령어>



옵션

- `-k` : 메뉴얼 통합 검색
- `-s` [section-number] : 해당 섹션에서 메뉴얼 보기(생략 가능)
    - section-number
        1.  User Commands
        2. System Calls
        3. Subroutines
        4. Devices
        5. File Formats

네비게이션(이동)

- space : next page
- enter : next line
- b : backward
- q : quit

예시
```bash
    man ls
    man -k delete
    man -s userdel
    ```

## ls : 파일 목록보기

> 기본 형식: ls <옵션> <파일|디렉토리>
> 

옵션

- `-a` : dot(.) 로 시작하는 숨겨진 파일까지 모두 표시
- `-l` : 파일, 디렉터리의 자세한 정보(type, permision, link, size, owner)  표시
- `-R` : 하위 디렉토리까지 모두 출력
- `-d` : 디렉토리 내용이 아닌 디렉토리 자체를 출력

예시

```bash
ls
ls -l
ls -a
ls -l /tmp
ls -ald /tmp
ls -R /usr/local
ls -alh
```

## mkdir : 디렉토리 생성

> 기본 형식: mkdir <옵션> <디렉토리_이름>


옵션

- `-m` : 퍼미션 설정
- `-p` : 존재하지 않는 parent directories 같이 생성

```bash
mkdir dir1 # dir1 디렉토리를 생성
mkdir /home/ubuntu/bin
mkdir -p par1/dir1 # par1 디렉토리를 생성하고, 하위에 dir1을 생성
mkdir ~/tmp-dir
mkdir -p ~/dir/subdir/subsubdir
```

참고 :  `~/`은 계정의 디렉토리를 함축적으로 의미

- 다시 말해 루트폴더 ( / ) 로부터 사용자폴더(username)까지의 경로를 축약한 형태

## rmdir : 디렉토리 삭제

> 기본 형식: rmdir <옵션> <디렉토리_이름>
 
- 비어 있는 디렉토리만 삭제 가능

옵션

- `-p` : **비어 있는** parent directories 함께 삭제

```bash
rmdir /home/ubuntu/bin
rmdir ~/tmp-dir
rmdir -p ~/dir/subdir/subsubdir
rmdir share
```

## cd : 디렉토리 이동

> 기본 형식: cd <디렉토리_이름>
 

아규먼트

`~` : HOME 디렉토리 이동

`-` : Previous directory 이동

```bash
# 지정한 디렉토리로 이동(상대경로)
cd ./A/B/C
cd /A/B/C
cd .. # 상위 디렉토리로 이동
cd - # 이전 디렉토리로 이동
cd ~; pwd
cd $HOME
```

## cp : 파일 복사

> 기본 형식: cp <옵션> 원본파일이름 목적지파일이름
 

옵션

- `-i` : 복사할 때 overwrite 할 것인지 질문 (그냥 습관처럼 쓰자)
- `-f` : 복사할 때 overwrite 질문 없이 무조건 덮어쓰기
- `-r` : 디렉토리 복사
- `-R` : 디렉토리의 하위 파일을 모두 복사

```bash
cp a.file b.file # a.file을 b.file로 복사합니다. 
cp -R source_dir target_dir # source_dir를 target_dir로 복사
cp /source_dir/a.file . # a.file 이름 그대로 현재 디렉토리에 복사

# 여러개 파일 복사시 목적지는 반드시 디렉터리로 복사
cp a.file b.file c.file target_dir 
cp -r conf.d conf.d.backup # 디렉토리는 -r 옵션 필수
```

## mv : 파일 이동하기 + 이름 변경에도 활용!!

> 기본 형식: mv <옵션> 원본파일이름 새이름
 

옵션

- `-i` : 이름을 바꿀 때 overwrite 할 것인지 질문
- `-f` : 이름을 바꿀 때 overwrite 질문 없이 무조건 덮어쓰기

```bash
mv source.file target.file # source.file을 target.file로 이름을 변경
mv -i passwd hosts.file #  overwrite 할 것인지 질문
mv passwd /tmp/passwd
mv conf.d setup.d
```

## rm : 파일 삭제 - 주의하면서 사용

> 기본 형식: rm <옵션> 파일이름
 

옵션

- `-i` : 삭제할 때 삭제 여부를 한 번 더 질문
- `-f` : 파일을 삭제할 때 질문 없이 무조건 삭제
- `-r` : 하위 내용을 포함한 디렉토리를 삭제

```bash
rm a.file # 파일을 삭제

rm aaa # 파일이 존재하지 않는 경우 오류가 발생
rm: cannot remove ‘aaa’: No such file or directory

$ rm -f aaa # -f 옵션을 이용하면 파일이 없어도 오류가 발생X

$ rm -rf a_directory # 디렉토리를 삭제
```
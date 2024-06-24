# wsl2(우분투)에서 node.js 로컬 환경 구축

##### 설치한 `wsl2` 를 이용 안 한다는 생각에 node.js 개발 환경을 구축하려고 도전했다.

## WSL2 개요 및 설치 방법

- Windows에서 WSL2를 설치하고 설정하는 방법
  
  - WSL2는 Windows 10에서 리눅스 커널을 실행할 수 있게 하는 기능이다. 이를 통해 개발자들은 Windows 환경에서 리눅스 도구와 애플리케이션을 사용할 수 있다.
  - WSL2를 설치하려면, Windows 기능 켜기/끄기에서 "Windows Subsystem for Linux"를 활성화하고, PowerShell에서 `wsl --install` 명령어를 실행한다.
  - 기본적으로 Ubuntu가 설치된다. 

- 초기 설정
  
  - 초기 설정에서는 사용자 계정과 비밀번호를 설정하고, 기본적인 패키지 업데이트를 진행한다.

- 기본 명령어: 틈틈이 하자.
  
  ```shell
  sudo apt update
  sudo apt upgrade -y
  ```
  
  - `sudo apt update` : 새롭게 릴리스된 소프트웨어 패키지 버전을 알 수 있게 한다. 정기적으로 실행해서 최신 패키지를 설치하자.
  
  - `sudo apt upgrade -y` : `upgrade`는 현재 설치된 패키지를 최신 버전으로 업그레이드하는 명령어

- node 환경 구축할 때 필요한 패키지
  
  ```shell
  sudo apt install curl build-essential -y
  ```
  
  - `sudo apt install curl build-essential -y` : `curl`과 `build-essential` 패키지를 설치한다. `curl`은 데이터 전송 도구이고, `build-essential`은 소프트웨어 컴파일 도구
    
    - `build-essential` 패키지는 C와 C++ 컴파일러, 그리고 다른 필수적인 컴파일 도구들을 포함하고 있다.
    
    - **nvm 설치**: nvm을 설치할 때 `curl`이 사용된다.

## nvm 설정 및 Node.js 설치

- nvm 레포지토리

[GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions](https://github.com/nvm-sh/nvm)

구글에 nvm 검색해서 최신 버전을 확인해보자(2024-06-26)

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

- nvm 설치 스크립트를 실행한 후, 설치 확인

```shell
source ~/.bashrc
nvm --version
```

- 원래는 로그인 할 때, 재실행되지만... `source ~/.bashrc` 를 해서 `nvm` 초기화 코드를 현재 쉘 세션에 적용하자. 이제 nvm 명령어 사용 가능. 

- node 설치 : 원하는 버전으로
  
  ```shell
  nvm install 20.15.0
  ```

- 설치된 Node.js 버전을 사용하려면 nvm use 버전 명령어를 실행

- nvm을 통해 설치된 Node.js에는 npm(Node Package Manager)이 포함되어 있다. npm을 사용하여 필요한 패키지를 설치하고 관리할 수 있다.

##### 기본 npm 명령어 사용법

- 프로젝트 초기화: npm init
- 패키지 설치: npm install package-name
- 전역 패키지 설치: npm install -g package-name



#### Vim 기본 설정

- .vimrc 파일 생성 및 기본 설정 추가
  
  - Vim의 설정을 저장하는 파일은 `.vimrc`이다. 홈 디렉토리에 `.vimrc` 파일을 생성하여 설정을 추가할 수 있다.
    
    ```shell
    touch ~/.vimrc 
    vim ~/.vimrc
    ```
  
  - 기본 설정 예시:
    
    ```vim
    syntax on
    filetype plugin indent on
    set number
    set relativenumber
    set tabstop=4
    set shiftwidth=4
    set expandtab
    set clipboard=unnamedplus
    ```

#### vim-plug를 이용한 플러그인 관리

- vim-plug 설치 방법
  
  - vim-plug는 Vim에서 플러그인을 쉽게 관리할 수 있게 해주는 도구이다. vim-plug를 설치하려면 다음 명령어를 실행한다.
    
    ```shell
    curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    ```

- 플러그인 설치 및 설정 방법
  
  - `.vimrc` 파일에 다음과 같이 플러그인 목록을 추가한다.
    
    ```vim
    call plug#begin('~/.vim/plugged')
    
    " Node.js, React 관련 플러그인
    Plug 'pangloss/vim-javascript'
    Plug 'maxmellon/vim-jsx-pretty'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    
    " 일반적인 편의성 플러그인
    Plug 'scrooloose/nerdtree'
    Plug 'tpope/vim-fugitive'
    Plug 'airblade/vim-gitgutter'
    Plug 'ctrlpvim/ctrlp.vim'
    Plug 'tpope/vim-commentary'
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    
    call plug#end()
    
    " 기본 설정
    syntax on
    filetype plugin indent on
    set number
    set relativenumber
    set tabstop=4
    set shiftwidth=4
    set expandtab
    set clipboard=unnamedplus
    
    ```
  
  - Vim을 열고 `:PlugInstall` 명령어를 실행하여 플러그인을 설치한다.



#### plugin 참고

```vim
call plug#begin('~/.vim/plugged')

" Node.js, React 관련 플러그인
Plug 'pangloss/vim-javascript'       " JavaScript 구문 강조 및 지원 플러그인
Plug 'maxmellon/vim-jsx-pretty'      " JSX 구문 강조 및 지원 플러그인 (React.js)
Plug 'neoclide/coc.nvim', {'branch': 'release'} " 코드 자동 완성 및 언어 서버 프로토콜(LSP) 지원 플러그인

" 일반적인 편의성 플러그인
Plug 'scrooloose/nerdtree'           " 파일 탐색기 플러그인
Plug 'tpope/vim-fugitive'            " Git 통합 플러그인 (Git 명령어를 Vim 내에서 실행)
Plug 'airblade/vim-gitgutter'        " Git 변경 사항을 표시해주는 플러그인
Plug 'ctrlpvim/ctrlp.vim'            " 파일 검색을 위한 플러그인 (Fuzzy Finder)
Plug 'tpope/vim-commentary'          " 간편한 주석 처리 플러그인
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } } " Fuzzy Finder 인터페이스를 제공하는 플러그인
Plug 'junegunn/fzf.vim'              " Fzf와 통합된 Vim 인터페이스를 제공하는 플러그인

call plug#end()

" 기본 설정
syntax on                      " 구문 강조 활성화
filetype plugin indent on      " 파일 타입에 따른 플러그인 및 인덴트 활성화
set number                     " 행 번호 표시
set relativenumber             " 상대 행 번호 표시
set tabstop=4                  " 탭 간격을 4로 설정
set shiftwidth=4               " 자동 들여쓰기 간격을 4로 설정
set expandtab                  " 탭을 스페이스로 변환
set clipboard=unnamedplus      " 시스템 클립보드와 연동

```



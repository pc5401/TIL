# 네트워크 관리



## ifconfig : 네트워크 인터페이스 설정

> 기본 형식: ifconfig <인터페이스> <옵션>

옵션

- `up` : 인터페이스 활성화
- `down` : 인터페이스 비활성화

예시

```bash
`ifconfig eth0 up # eth0 인터페이스 활성화 ifconfig eth0 down # eth0 인터페이스 비활성화 ifconfig eth0 192.168.1.100 netmask 255.255.255.0 # eth0에 IP 주소 및 서브넷 마스크 설정`
```





## ping : 네트워크 연결 테스트

> 기본 형식: ping <옵션> <호스트>

옵션

- `-c <count>` : 지정한 횟수만큼 패킷 전송

예시

```bash
ping google.com # google.com으로 패킷 전송
ping -c 4 google.com # google.com으로 4번 패킷 전송
#
```



> 기본 형식: netstat <옵션>

옵션

- `-a` : 모든 연결 및 포트 표시
- `-t` : TCP 연결만 표시
- `-u` : UDP 연결만 표시

예시

```bash
netstat -a # 모든 연결 및 포트 표시
netstat -t # TCP 연결만 표시
netstat -u # UDP 연결만 표시
```

## traceroute : 경로 추적

> 기본 형식: traceroute <호스트>

설명

- 네트워크 패킷이 목적지에 도달하는 경로를 추적

예시

```bash
traceroute google.com # google.com까지의 경로 추적
```

### 패키지 관리

## apt-get : 패키지 설치 및 관리 (Debian 계열)

> 기본 형식: apt-get <옵션> <패키지>

옵션

- `update` : 패키지 목록 업데이트
- `upgrade` : 설치된 모든 패키지 업그레이드
- `install` : 패키지 설치
- `remove` : 패키지 삭제

예시

```bash
sudo apt-get update # 패키지 목록 업데이트
sudo apt-get upgrade # 모든 패키지 업그레이드
sudo apt-get install vim # vim 패키지 설치
sudo apt-get remove vim # vim 패키지 삭제
```

## yum : 패키지 설치 및 관리 (RHEL 계열)

> 기본 형식: yum <옵션> <패키지>

옵션

- `update` : 패키지 목록 업데이트 및 모든 패키지 업그레이드
- `install` : 패키지 설치
- `remove` : 패키지 삭제

예시

```bash
sudo yum update # 패키지 목록 업데이트 및 모든 패키지 업그레이드
sudo yum install vim # vim 패키지 설치
sudo yum remove vim # vim 패키지 삭제
```

# 디스크 관리

## df : 파일 시스템 디스크 공간 사용량 확인

> 기본 형식: df <옵션>

옵션

- `-h` : 사람이 읽기 쉬운 형식으로 출력

예시

```bash
df -h # 사람이 읽기 쉬운 형식으로 디스크 사용량 출력
```

## du : 디스크 사용량 확인



> 기본 형식: du <옵션> <디렉토리>

옵션

- `-h` : 사람이 읽기 쉬운 형식으로 출력
- `-s` : 요약된 총계만 표시

예시

```bash
du -h /home/user # /home/user 디렉토리의 디스크 사용량 출력
du -sh /home/user # /home/user 디렉토리의 요약된 총계만 출력
```
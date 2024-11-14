# 네트워크 관리
## ifconfig : 네트워크 인터페이스 설정

> 기본 형식: ifconfig <인터페이스> <옵션>
> 

### 옵션

- `up` : 인터페이스 활성화
- `down` : 인터페이스 비활성화
- `<IP 주소>` : 인터페이스에 IP 주소 할당
- `netmask <서브넷 마스크>` : 서브넷 마스크 설정
- `mtu <크기>` : 최대 전송 단위 설정

### 예시

```bash
ifconfig eth0 up               # eth0 인터페이스 활성화
ifconfig eth0 down             # eth0 인터페이스 비활성화
ifconfig eth0 192.168.1.100    # eth0에 IP 주소 할당
ifconfig eth0 netmask 255.255.255.0  # eth0에 서브넷 마스크 설정
ifconfig eth0 mtu 1500         # eth0의 MTU 설정
```

## ip : 고급 네트워크 인터페이스 관리

> 기본 형식: ip <명령어> <옵션>
> 

### 주요 명령어

- `addr` : 주소 관련 작업
- `link` : 네트워크 링크 관련 작업
- `route` : 라우팅 테이블 관리
- `neigh` : 이웃 테이블 관리

### 예시

```bash
ip addr show                   # 모든 네트워크 인터페이스의 주소 정보 표시
ip link set eth0 up            # eth0 인터페이스 활성화
ip link set eth0 down          # eth0 인터페이스 비활성화
ip addr add 192.168.1.100/24 dev eth0  # eth0에 IP 주소 및 서브넷 마스크 할당
ip route add default via 192.168.1.1   # 기본 게이트웨이 설정
```

## ping : 네트워크 연결 테스트

> 기본 형식: ping <옵션> <호스트>
> 

### 옵션

- `c <count>` : 지정한 횟수만큼 패킷 전송
- `i <interval>` : 패킷 전송 간격 설정 (초 단위)
- `t <ttl>` : TTL(Time To Live) 설정

### 예시

```bash
ping google.com               # google.com으로 패킷 전송
ping -c 4 google.com          # google.com으로 4번 패킷 전송
ping -i 2 google.com          # 2초 간격으로 패킷 전송
ping -t 64 google.com         # TTL을 64로 설정하여 패킷 전송
```

## netstat : 네트워크 연결 및 포트 상태 확인

> 기본 형식: netstat <옵션>
> 

### 옵션

- `a` : 모든 연결 및 포트 표시
- `t` : TCP 연결만 표시
- `u` : UDP 연결만 표시
- `l` : 수신 대기 중인 소켓 표시
- `n` : 숫자 형식으로 주소 및 포트 표시
- `p` : 각 소켓과 연관된 프로세스 표시

### 예시

```bash
netstat -a                     # 모든 연결 및 포트 표시
netstat -t                     # TCP 연결만 표시
netstat -u                     # UDP 연결만 표시
netstat -l                     # 수신 대기 중인 소켓 표시
netstat -n                     # 숫자 형식으로 주소 및 포트 표시
netstat -p                     # 소켓과 연관된 프로세스 
```

## traceroute : 경로 추적

> 기본 형식: traceroute <호스트>
> 

### 옵션

- `m <max_ttl>` : 최대 홉 수 설정
- `n` : 호스트 이름을 해석하지 않고 숫자 IP로 표시

### 예시

```bash
traceroute google.com          # google.com까지의 경로 추적
traceroute -m 20 google.com    # 최대 20홉까지 경로 추적
traceroute -n google.com       # 숫자 IP로 경로 추적
```

## ss : 소켓 상태 조사

> 기본 형식: ss <옵션>
> 

### 옵션

- `t` : TCP 소켓 표시
- `u` : UDP 소켓 표시
- `l` : 수신 대기 중인 소켓 표시
- `n` : 숫자 형식으로 주소 및 포트 표시
- `p` : 각 소켓과 연관된 프로세스 표시

### 예시

```bash
ss -t                         # TCP 소켓 표시
ss -u                         # UDP 소켓 표시
ss -l                         # 수신 대기 중인 소켓 표시
ss -n                         # 숫자 형식으로 주소 및 포트 표시
ss -p                         # 소켓과 연관된 프로세스 표시
ss -tunlp                     # TCP, UDP, 수신 대기, 숫자, 프로세스 표시
```

## nmap : 네트워크 탐색 및 보안 감사

> 기본 형식: nmap <옵션> <호스트>
> 

### 옵션

- `sS` : TCP SYN 스캔
- `sU` : UDP 스캔
- `p <포트>` : 특정 포트 스캔
- `A` : 고급 탐지 (OS, 버전, 스크립트)
- `v` : 상세 출력

### 예시

```bash
nmap -sS google.com                # TCP SYN 스캔으로 google.com 스캔
nmap -sU google.com                # UDP 스캔으로 google.com 스캔
nmap -p 80,443 google.com          # 포트 80과 443 스캔
nmap -A google.com                  # 고급 탐지로 google.com 스캔
nmap -v google.com                  # 상세 출력으로 google.com 스캔
```
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
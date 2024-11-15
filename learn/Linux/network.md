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

# 패키지 관리

## apt-get : 패키지 설치 및 관리 (Debian 계열)

> 기본 형식: apt-get <옵션> <패키지>
> 

### 옵션

- `update` : 패키지 목록 업데이트
- `upgrade` : 설치된 모든 패키지 업그레이드
- `install` : 패키지 설치
- `remove` : 패키지 삭제
- `autoremove` : 더 이상 필요 없는 패키지 자동 삭제
- `purge` : 패키지 및 설정 파일 삭제

### 예시

```bash

sudo apt-get update                # 패키지 목록 업데이트
sudo apt-get upgrade               # 모든 패키지 업그레이드
sudo apt-get install vim           # vim 패키지 설치
sudo apt-get remove vim            # vim 패키지 삭제
sudo apt-get autoremove            # 불필요한 패키지 자동 삭제
sudo apt-get purge vim             # vim 패키지 및 설정 파일 삭제
```

## yum : 패키지 설치 및 관리 (RHEL 계열)

> 기본 형식: yum <옵션> <패키지>
> 

### 옵션

- `update` : 패키지 목록 업데이트 및 모든 패키지 업그레이드
- `install` : 패키지 설치
- `remove` : 패키지 삭제
- `search` : 패키지 검색
- `info` : 패키지 정보 표시
- `clean` : 캐시 정리

### 예시

```bash
sudo yum update                    # 패키지 목록 업데이트 및 모든 패키지 업그레이드
sudo yum install vim               # vim 패키지 설치
sudo yum remove vim                # vim 패키지 삭제
sudo yum search vim                # vim 관련 패키지 검색
sudo yum info vim                  # vim 패키지 정보 표시
sudo yum clean all                 # 모든 캐시 정
```

## dnf : 패키지 관리 (Fedora 및 최신 RHEL 계열)

> 기본 형식: dnf <옵션> <패키지>
> 

### 옵션

- `update` : 패키지 목록 업데이트 및 모든 패키지 업그레이드
- `install` : 패키지 설치
- `remove` : 패키지 삭제
- `search` : 패키지 검색
- `info` : 패키지 정보 표시
- `autoremove` : 더 이상 필요 없는 패키지 자동 삭제

### 예시

```bash
sudo dnf update                    # 패키지 목록 업데이트 및 모든 패키지 업그레이드
sudo dnf install vim               # vim 패키지 설치
sudo dnf remove vim                # vim 패키지 삭제
sudo dnf search vim                # vim 관련 패키지 검색
sudo dnf info vim                  # vim 패키지 정보 표시
sudo dnf autoremove                # 불필요한 패키지 자동 삭
```

# 디스크 관리

## df : 파일 시스템 디스크 공간 사용량 확인

> 기본 형식: df <옵션>
> 

### 옵션

- `h` : 사람이 읽기 쉬운 형식으로 출력
- `a` : 모든 파일 시스템 포함
- `T` : 파일 시스템 유형 표시
- `i` : inode 사용량 표시

### 예시

```bash
df -h                            # 사람이 읽기 쉬운 형식으로 디스크 사용량 출력
df -a                            # 모든 파일 시스템의 디스크 사용량 출력
df -T                            # 파일 시스템 유형과 함께 디스크 사용량 출력
df -i                            # inode 사용량 출력
```

## du : 디스크 사용량 확인

> 기본 형식: du <옵션> <디렉토리>
> 

### 옵션

- `h` : 사람이 읽기 쉬운 형식으로 출력
- `s` : 요약된 총계만 표시
- `a` : 모든 파일과 디렉토리 표시
- `c` : 총합계 표시

### 예시

```bash
du -h /home/user                 # /home/user 디렉토리의 디스크 사용량 출력
du -sh /home/user                # /home/user 디렉토리의 요약된 총계만 출력
du -ah /home/user                # /home/user 디렉토리의 모든 파일과 디스크 사용량 출력
du -shc /home/user               # /home/user 디렉토리의 요약된 총계와 총합계 출력
```

## lsblk : 블록 장치 목록 표시

> 기본 형식: lsblk <옵션>
> 

### 옵션

- `f` : 파일 시스템 정보 표시
- `a` : 모든 블록 장치 표시
- `o <열>` : 표시할 열 지정

### 예시

```bash
lsblk                            # 모든 블록 장치 목록 표시
lsblk -f                         # 파일 시스템 정보와 함께 블록 장치 표시
lsblk -a                         # 모든 블록 장치 표시 (숨겨진 장치 포함)
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT # 지정된 열만 표시
```

## fdisk : 디스크 파티션 관리

> 기본 형식: fdisk <옵션> <디스크>
> 

### 주요 명령어 (fdisk 대화형 명령어)

- `m` : 도움말 표시
- `p` : 파티션 테이블 표시
- `n` : 새 파티션 생성
- `d` : 기존 파티션 삭제
- `t` : 파티션 유형 변경
- `w` : 변경 사항 저장 및 종료
- `q` : 변경 사항 저장 없이 종료

### 예시

```bash
sudo fdisk /dev/sda              # /dev/sda 디스크의 파티션 관리 시작
# 대화형 명령어 사용:
# m - 도움말
# p - 파티션 테이블 표시
# n - 새 파티션 생성
# d - 파티션 삭제
# w - 변경 사항 저장
```

## mkfs : 파일 시스템 생성

> 기본 형식: mkfs.<파일 시스템> <옵션> <디바이스>
> 

### 주요 파일 시스템 유형

- `mkfs.ext4` : ext4 파일 시스템 생성
- `mkfs.vfat` : FAT32 파일 시스템 생성
- `mkfs.ntfs` : NTFS 파일 시스템 생성

### 예시

```bash
sudo mkfs.ext4 /dev/sda1         # /dev/sda1에 ext4 파일 시스템 생성
sudo mkfs.vfat /dev/sda2         # /dev/sda2에 FAT32 파일 시스템 생성
sudo mkfs.ntfs /dev/sda3         # /dev/sda3에 NTFS 파일 시스템 생성
```

## mount : 파일 시스템 마운트

> 기본 형식: mount <옵션> <디바이스> <마운트 지점>
> 

### 옵션

- `t <파일 시스템>` : 파일 시스템 유형 지정
- `o <옵션>` : 마운트 옵션 지정

### 예시

```bash
sudo mount /dev/sda1 /mnt        # /dev/sda1을 /mnt에 마운트
sudo mount -t ext4 /dev/sda1 /mnt # ext4 파일 시스템으로 /dev/sda1을 /mnt에 마운트
sudo mount -o ro /dev/sda1 /mnt   # 읽기 전용으로 /dev/sda1을 /mnt에 마운트
```

## umount : 파일 시스템 마운트 해제

> 기본 형식: umount <옵션> <마운트 지점 또는 디바이스>
> 

### 옵션

- `l` : 지연 해제
- `f` : 강제 해제

### 예시

```bash
sudo umount /mnt                   # /mnt 마운트 해제
sudo umount /dev/sda1               # /dev/sda1 마운트 해제
sudo umount -l /mnt                # 지연 해제로 /mnt 마운트 해제
sudo umount -f /dev/sda1            # 강제 해제로 /dev/sda1 마운트 해제
```

## parted : 고급 디스크 파티션 관리

> 기본 형식: parted <옵션> <디스크>
> 

### 주요 명령어 (parted 대화형 명령어)

- `help` : 도움말 표시
- `print` : 파티션 테이블 표시
- `mklabel` : 파티션 테이블 생성
- `mkpart` : 새 파티션 생성
- `rm` : 파티션 삭제
- `resizepart` : 파티션 크기 조정

### 예시

```bash
sudo parted /dev/sda             # /dev/sda 디스크의 파티션 관리 시작
# 대화형 명령어 사용:
# help - 도움말
# print - 파티션 테이블 표시
# mklabel gpt - GPT 파티션 테이블 생성
# mkpart primary ext4 0% 50% - 새 파티션 생성
# rm 1 - 첫 번째 파티션 삭제
# resizepart 1 100% - 첫 번째 파티션을 디스크 끝까지 확장
```

# 추가 유용한 디스크 관리 명령어

## ls -l /dev/disk/by-uuid/ : UUID를 통한 디스크 식별

> 기본 형식: ls -l /dev/disk/by-uuid/
> 

### 설명

- 각 디스크 파티션의 UUID를 확인하여 파일 시스템을 식별할 때 유용

### 예시

```bash
ls -l /dev/disk/by-uuid/         # UUID별로 디스크 파티션 목록 표시
```

## blkid : 블록 장치의 속성 표시

> 기본 형식: blkid <디바이스>
> 

### 설명

- 블록 장치의 파일 시스템 유형, UUID, 레이블 등 속성 표시

### 예시

```bash
sudo blkid /dev/sda1              # /dev/sda1의 속성 표시
sudo blkid                         # 모든 블록 장치의 속성 표시
```

## lsof : 열린 파일 목록 및 관련 프로세스 확인

> 기본 형식: lsof <옵션>
> 

### 옵션

- `+D <디렉토리>` : 특정 디렉토리 내의 열린 파일 표시
- `i` : 네트워크 연결과 관련된 열린 파일 표시
- `u <사용자>` : 특정 사용자가 연 열린 파일 표시

### 예시

```bash
sudo lsof +D /home/user            # /home/user 디렉토리 내의 열린 파일 표시
sudo lsof -i                       # 네트워크 연결과 관련된 열린 파일 표시
sudo lsof -u username               # 특정 사용자가 연 열린 파일 표시
```
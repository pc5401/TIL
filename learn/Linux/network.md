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

# 시스템 모니터링 및 관리

## top : 실시간 시스템 모니터링

> 기본 형식: top
> 

### 설명

- CPU, 메모리 사용량 등 시스템 리소스 실시간 모니터링

### 예시

```bash
top                                # 실시간 시스템 모니터링 시작
```

## htop : 향상된 대화형 프로세스 뷰어

> 기본 형식: htop
> 

### 설명

- top의 대안으로, 사용자 친화적인 인터페이스와 추가 기능 제공

### 예시

```bash
htop                               # htop 실행
```

## vmstat : 시스템 가상 메모리 상태 확인

> 기본 형식: vmstat <옵션>
> 

### 옵션

- `<지연 시간>` : 업데이트 간격 설정 (초 단위)
- `<횟수>` : 업데이트 횟수 설정

### 예시

```bash
vmstat 5 3                         # 5초 간격으로 3번 시스템 상태 출력
```

## iostat : CPU 및 I/O 통계 확인

> 기본 형식: iostat <옵션>
> 

### 옵션

- `<지연 시간>` : 업데이트 간격 설정 (초 단위)
- `<횟수>` : 업데이트 횟수 설정

### 예시

```bash
iostat 5 3                          # 5초 간격으로 3번 CPU 및 I/O 통계 출력
```

## free : 메모리 사용량 확인

> 기본 형식: free <옵션>
> 

### 옵션

- `h` : 사람이 읽기 쉬운 형식으로 출력
- `m` : 메모리 사용량을 MB 단위로 출력
- `g` : 메모리 사용량을 GB 단위로 출력

### 예시

```bash
free -h                             # 사람이 읽기 쉬운 형식으로 메모리 사용량 출력
free -m                             # MB 단위로 메모리 사용량 출력
free -g                             # GB 단위로 메모리 사용량 출력
```

# 파일 및 디렉토리 관리

## cp : 파일 및 디렉토리 복사

> 기본 형식: cp <옵션> <원본> <대상>
> 

### 옵션

- `r` : 디렉토리 및 하위 디렉토리 재귀적 복사
- `p` : 파일의 속성(권한, 소유자 등) 보존
- `i` : 덮어쓰기 전에 확인
- `v` : 복사 과정 상세 출력

### 예시

```bash
cp file1.txt /backup/             # file1.txt를 /backup/으로 복사
cp -r dir1 /backup/               # dir1 디렉토리를 /backup/으로 재귀적 복사
cp -p file1.txt /backup/          # file1.txt를 속성 보존하여 /backup/으로 복사
cp -i file1.txt /backup/          # 덮어쓰기 전에 확인
cp -v file1.txt /backup/          # 복사 과정 상세 출
```

## mv : 파일 및 디렉토리 이동 또는 이름 변경

> 기본 형식: mv <옵션> <원본> <대상>
> 

### 옵션

- `i` : 덮어쓰기 전에 확인
- `v` : 이동 과정 상세 출력

### 예시

```bash
mv file1.txt /backup/             # file1.txt를 /backup/으로 이동
mv file1.txt file2.txt            # file1.txt의 이름을 file2.txt로 변경
mv -i file1.txt /backup/          # 덮어쓰기 전에 확인
mv -v file1.txt /backup/          # 이동 과정 상세 출력
```

## rm : 파일 및 디렉토리 삭제

> 기본 형식: rm <옵션> <파일/디렉토리>
> 

### 옵션

- `r` : 디렉토리 및 하위 디렉토리 재귀적 삭제
- `f` : 강제 삭제 (확인 없이)
- `i` : 삭제 전에 확인
- `v` : 삭제 과정 상세 출력

### 예시

```bash
rm file1.txt                      # file1.txt 삭제
rm -r dir1                        # dir1 디렉토리 및 하위 디렉토리 삭제
rm -f file1.txt                   # file1.txt를 강제 삭제
rm -i file1.txt                   # 삭제 전에 확인
rm -rv dir1                        # dir1 디렉토리를 재귀적이고 상세하게 삭제
```

## mkdir : 디렉토리 생성

> 기본 형식: mkdir <옵션> <디렉토리>
> 

### 옵션

- `p` : 상위 디렉토리가 없으면 함께 생성
- `v` : 생성 과정 상세 출력

### 예시

```bash
mkdir newdir                       # newdir 디렉토리 생성
mkdir -p /path/to/newdir           # /path/to/newdir 디렉토리 생성 (상위 디렉토리도 함께)
mkdir -v newdir                    # newdir 디렉토리를 상세하게 생성
```

## rmdir : 빈 디렉토리 삭제

> 기본 형식: rmdir <옵션> <디렉토리>
> 

### 옵션

- `p` : 상위 디렉토리까지 빈 경우 함께 삭제

### 예시

```bash
rmdir emptydir                    # emptydir 빈 디렉토리 삭제
rmdir -p /path/to/emptydir        # /path/to/emptydir와 상위 디렉토리가 빈 경우 함께 삭제
```

## find : 파일 및 디렉토리 검색

> 기본 형식: find <경로> <옵션> <동작>
> 

### 옵션

- `name <패턴>` : 이름으로 검색
- `type <타입>` : 파일 타입으로 검색 (f: 파일, d: 디렉토리 등)
- `size <크기>` : 파일 크기로 검색
- `mtime <날짜>` : 수정 날짜로 검색

### 예시

```bash
find /home/user -name "*.txt"                # /home/user 내의 모든 .txt 파일 검색
find /var/log -type f -size +10M             # /var/log 내의 크기가 10MB 초과인 파일 검색
find / -mtime -7                              # 지난 7일 내에 수정된 모든 파일 검색
find /home/user -type d -name "backup"        # /home/user 내의 backup 디렉토리 검색
```

# 사용자 및 권한 관리

## chmod : 파일 및 디렉토리 권한 변경

> 기본 형식: chmod <옵션> <권한> <파일/디렉토리>
> 

### 권한 표현 방식

- **숫자 방식**: `chmod 755 file`
    - 읽기(r)=4, 쓰기(w)=2, 실행(x)=1
    - 소유자: 7 (rwx), 그룹: 5 (r-x), 기타: 5 (r-x)
- **기호 방식**: `chmod u+rwx,g+rx,o+rx file`

### 옵션

- `R` : 재귀적으로 권한 변경
- `v` : 변경 과정 상세 출력

### 예시

```bash
chmod 755 script.sh                 # script.sh의 권한을 rwxr-xr-x로 변경
chmod u+rwx,g+rx,o+rx script.sh     # 소유자에게 rwx, 그룹과 기타에 r-x 권한 부여
chmod -R 700 /secure/               # /secure/ 디렉토리 및 하위 디렉토리의 권한을 rwx------로 변경
chmod -v 755 script.sh               # 변경 과정을 상세하게 출력
```

## chown : 파일 및 디렉토리 소유자 변경

> 기본 형식: chown <옵션> <소유자>:<그룹> <파일/디렉토리>
> 

### 옵션

- `R` : 재귀적으로 소유자 변경
- `v` : 변경 과정 상세 출력

### 예시

```bash
sudo chown user:group file.txt           # file.txt의 소유자를 user, 그룹을 group으로 변경
sudo chown -R user:group /home/user      # /home/user 디렉토리 및 하위 디렉토리의 소유자와 그룹 변경
sudo chown -v user:group file.txt        # 변경 과정을 상세하게 출력
```

## useradd : 사용자 추가

> 기본 형식: useradd <옵션> <사용자명>
> 

### 옵션

- `m` : 홈 디렉토리 생성
- `d <디렉토리>` : 홈 디렉토리 경로 지정
- `s <쉘>` : 기본 쉘 지정
- `G <그룹>` : 추가 그룹 지정

### 예시

```bash
sudo useradd -m newuser                     # newuser 사용자 추가 및 홈 디렉토리 생성
sudo useradd -m -d /home/newuser -s /bin/bash newuser  # 사용자 추가 시 홈 디렉토리와 쉘 지정
sudo useradd -m -G sudo newuser             # newuser 사용자를 sudo 그룹에 추가
```

## passwd : 사용자 비밀번호 설정 및 변경

> 기본 형식: passwd <옵션> <사용자명>
> 

### 옵션

- `-stdin` : 표준 입력으로 비밀번호 설정 (보안상 권장되지 않음)

### 예시

```bash
sudo passwd newuser                         # newuser 사용자의 비밀번호 설정 또는 변경
echo "newpassword" | sudo passwd --stdin newuser  # newuser 사용자의 비밀번호를 "newpassword"로 설정 (비권장)
```

## su : 사용자 전환

> 기본 형식: su <옵션> <사용자명>
> 

### 옵션

- `` : 로그인 쉘로 전환
- `c <명령>` : 특정 명령 실행 후 종료

### 예시

```bash
su -                                     # 루트 사용자로 전환하여 로그인 쉘 시작
su -l newuser                            # newuser 사용자로 전환하여 로그인 쉘 시작
su -c "ls /root"                         # 루트 사용자로 전환하여 /root 디렉토리 목록 표시 후 종
```

## sudo : 권한 상승 및 명령어 실행

> 기본 형식: sudo <옵션> <명령어>
> 

### 옵션

- `u <사용자>` : 지정한 사용자로 명령어 실행
- `s` : 쉘을 루트 권한으로 실행
- `i` : 로그인 쉘을 루트 권한으로 실행

### 예시

```bash
sudo apt-get update                      # 루트 권한으로 패키지 목록 업데이트
sudo -u newuser ls /home/newuser         # newuser 권한으로 /home/newuser 디렉토리 목록 표시
sudo -s                                  # 루트 권한으로 쉘 실행
sudo -i                                  # 루트 로그인 쉘 실행
```

# 네트워크 파일 전송 및 관리

## scp : 안전한 파일 복사

> 기본 형식: scp <옵션> <원본> <대상>
> 

### 옵션

- `r` : 디렉토리 및 하위 디렉토리 재귀적 복사
- `P <포트>` : SSH 포트 지정
- `i <키 파일>` : SSH 키 파일 지정
- `v` : 복사 과정 상세 출력

### 예시

```bash
scp file1.txt user@remote:/backup/               # 로컬의 file1.txt를 원격 호스트의 /backup/으로 복사
scp -r /local/dir user@remote:/backup/           # 로컬의 /local/dir 디렉토리를 원격 호스트의 /backup/으로 재귀적 복사
scp -P 2222 file1.txt user@remote:/backup/       # SSH 포트 2222를 사용하여 file1.txt 복사
scp -i ~/.ssh/id_rsa file1.txt user@remote:/backup/ # 특정 SSH 키를 사용하여 file1.txt 복사
scp -v file1.txt user@remote:/backup/           # 복사 과정을 상세하게 출력
```
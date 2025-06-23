## NCloud 프라이빗 서버에서 MySQL 설치 · 퍼블릭 접근 설정 노트

> 예전에 “설치 → 보안 강화 → 원격 접속” 순으로 **명령어의 의미**와 **배경지식**을 함께 정리했었음. *결과만* 기록하지 않고 **왜 그렇게 하는지**를 남겨 두지 않았던 거 같아서 다시 한 번 정리함.

---

## 0. 사전 준비

- **서버 정보**
  
  - OS : Ubuntu 22.04 LTS
  
  - 퍼블릭 IP : `200.255.152.255` (예시)

- **작업용 PC**
  
  - OpenSSH Client, MySQL Client가 설치돼 있어야 한다.

- **네트워크**
  
  - NCloud 보안그룹(또는 VPC 방화벽)에서 **SSH 22/tcp**와 **MySQL 3306/tcp**를 허용해 둔다.
  
  - 처음에는 **내 IP만** 열어 두고, 확인 후 범위를 최소화한다.

---

## 1. SSH로 서버 접속

```bash
ssh your_username@200.255.152.255
```

- `ssh` : 로컬-PC에서 원격 호스트에 **암호화된 세션**을 생성한다.

- 최초 접속 시 서버의 **HostKey 지문**을 저장하고, 이후 동일 키가 아니면 경고를 띄운다.

> **팁** : `~/.ssh/config`에 별칭을 등록해 두면 `ssh ncloud-db`처럼 간단히 접속할 수 있다.

---

## 2. 패키지 인덱스 업데이트

```bash
sudo apt update
```

- `apt`가 **패키지 메타데이터**(패키지명·버전·의존성 목록)를 최신 레포지토리에서 다시 받아온다.

- 새로 설치할 패키지가 최신 안정판으로 지정되도록 *반드시* 먼저 실행한다.

---

## 3. MySQL 서버 설치

```bash
sudo apt install mysql-server
```

- `mysql-server` 메타 패키지가 **MySQL 8.x**와 서비스 스크립트를 설치한다.

- 설치 과정에서 시스템-D 서비스가 자동 등록되며, 기본 설정으로 **로컬(127.0.0.1) 바인딩** 상태로 구동된다.

```bash
systemctl status mysql   # 활성 상태 확인
```

---

## 4. MySQL 초기 보안 강화

```bash
sudo mysql_secure_installation
```

`mysql_secure_installation`은 **대화형 스크립트**로 다음 작업을 일괄 처리한다.

| 질문                             | 의미                                    | 권장 답     |
| ------------------------------ | ------------------------------------- | -------- |
| Validate Password Component 설치 | 비밀번호 복잡도 검사 플러그인 활성화                  | Y        |
| 새 root 비밀번호                    | Unix root와 별개인 **MySQL root** 계정 비밀번호 | 강력한 비밀번호 |
| 익명 사용자 제거                      | `''@localhost` 계정 삭제                  | Y        |
| 원격 root 로그인 차단                 | root는 로컬 접속만 허용                       | Y        |
| 테스트 DB 제거                      | `test` DB 및 권한 삭제                     | Y        |
| 권한 테이블 재로드                     | 변경 사항 즉시 적용                           | Y        |

> **정리** : “루트 잠그기 → 불필요한 계정·DB 삭제 → 정책 플러그인 활성화” 세 단계를 자동화한 스크립트이다.

---

## 5. MySQL 원격 접속 허용

### 5-1. `mysqld.cnf` 편집

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

```ini
# 기존
bind-address = 127.0.0.1

# 변경
bind-address = 0.0.0.0        # 모든 인터페이스에서 수신
```

- **bind-address** : mysqld가 **TCP 요청**을 수신할 NIC를 지정한다.

- `0.0.0.0`을 쓰면 *모든* 인터페이스를 열지만, **방화벽·보안그룹**에서 접근을 제한하여 안전을 확보한다.

### 5-2. 서비스 재시작

```bash
sudo systemctl restart mysql
```

- 설정 파일 변경은 **데몬 재기동** 시점에만 적용된다.

- 변경 후에는 `ss -tlnp | grep 3306`으로 **LISTEN** 상태와 바인딩 인터페이스를 검증한다.

---

## 6. 데이터베이스·테이블 준비

```bash
sudo mysql -uroot -p
```

```sql
CREATE DATABASE my_db
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;
```

- **utf8mb4**는 MySQL이 지원하는 *완전한* 4-바이트 UTF-8 인코딩이다. 이모지 저장이 가능하다.

- 이후 테이블 스키마는 ERD를 기반으로 `CREATE TABLE` 구문을 실행한다.

---

## 7. 전용 계정 생성 · 권한 최소화

```sql
CREATE USER 'api_server'@'203.0.113.5'
  IDENTIFIED BY '★StrongPassw0rd!';
GRANT ALL PRIVILEGES ON my_db.* TO 'api_server'@'203.0.113.5';
FLUSH PRIVILEGES;
```

- `user@host` 구문에서 **host**는 클라이언트 주소를 지정한다.
  
  - CIDR 와일드카드(`'api'@'203.0.113.%'`)도 가능하다.

- **원칙** : 서비스 코드가 요구하는 최소 권한만 부여한다.
  
  - 읽기 전용 API라면 `GRANT SELECT`만 주는 편이 안전하다.

---

## 8. UFW 방화벽 설정

```bash
sudo ufw allow from 203.0.113.5 to any port 22   # SSH
sudo ufw allow from 203.0.113.5 to any port 3306 # MySQL
sudo ufw enable
sudo ufw status numbered
```

- UFW는 **iptables → nftables** 규칙을 관리하는 간단한 CLI이다.

- 번호가 매겨진 규칙을 확인하고 필요 없으면 `ufw delete <번호>`로 제거한다.

- **세션 차단 위험**을 방지하려면 다른 SSH 창에서 연결을 유지한 채 규칙을 적용하고, 접속이 끊기지 않는지 확인한다.

---

## 9. 원격 접속 테스트

```bash
mysql -uapi_server -p -h 200.255.152.255 my_db
```

- 접속 성공 시 `mysql>` 프롬프트가 뜨면 설정이 완료된 것이다.

- 실패할 경우 **세 가지**를 순서대로 확인한다.
  
  1. 계정·비밀번호·호스트 정의가 정확한지 (`mysql.user` 테이블)
  
  2. `bind-address`와 포트가 열려 있는지 (`ss -tlnp`)
  
  3. 방화벽·보안그룹 인바운드 규칙이 허용 중인지

---

## 10. SSH 터널링로 안전한 접속

```bash
ssh -L 3306:localhost:3306 your_username@200.255.152.255
```

- `-L [LOCAL_PORT]:[REMOTE_HOST]:[REMOTE_PORT]` 형식이다.

- 로컬 PC에서 `127.0.0.1:3306`으로 접속하면 암호화된 채널을 통해 원격 MySQL로 전달된다.

- MySQL 포트를 외부에 전혀 열지 않고도 **보안·편의**를 모두 얻을 수 있다.

---

## 11. 추가 보안 조치

1. **SSH 키 인증**을 사용해 비밀번호 로그인을 비활성화한다.

2. `fail2ban`을 설치해 SSH·MySQL 로그인 실패를 감시한다.

3. 정기 백업을 위해 `mysqldump` 혹은 `mysqlsh dumpInstance`를 cron에 등록한다.

4. 클라우드 콘솔에서 **백업 스냅샷** 기능을 활성화한다.

5. MySQL 8.0.34 이상은 **인바운드 TLS**를 기본 지원하므로, CA 인증서를 적용해 **암호화 쿼리**를 활성화한다.

---

## 마무리

- 설치 이후에는 **버전 관리**(`apt list --upgradable`)와 **로그 모니터링**(`/var/log/mysql/error.log`)을 습관처럼 확인한다.

- 모든 설정은 *보안 → 가용성 → 성능* 순으로 우선순위를 두고 조정한다.

- 이 문서를 토대로 실제 인프라에 맞춰 **IP·권한·백업 정책**을 세밀하게 최적화한다.

> 
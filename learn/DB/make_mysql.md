# 클라우드 프라이빗 서버에 MySQL 설정 및 퍼블릭 접근 구성하기

NCloud의 프라이빗 서버에 MySQL을 설치하고 퍼블릭에서 접근할 수 있도록 설정을 했는데, 그 과정을 정리했다.

## 1. SSH를 통해 NCloud Ubuntu 서버에 접속

터미널에서 다음 명령을 사용하여 서버에 접속한다.

```bash
ssh your_username@200.255.152.255
```

- `your_username`: 서버의 사용자 이름
- `200.255.152.255`: 서버의 공인 IP 주소 (예시)

## 2. 패키지 인덱스 업데이트

패키지 목록을 최신 상태로 업데이트한다.

```bash
sudo apt update
```

## 3. MySQL 서버 설치

MySQL 서버를 설치한다.

```bash
sudo apt install mysql-server
```

## 4. MySQL 보안 설정

MySQL의 기본 보안을 강화하기 위해 다음 명령을 실행한다.

```bash
sudo mysql_secure_installation
```

### 설정 내용:

- **Validate Password Plugin 설정:** `Y`
- **root 비밀번호 설정:** `1`
    - 보통 비밀번호 수준으로 설정
- **익명 사용자 제거:** `Y`
- **원격 root 로그인 비활성화:** `Y`
    - root 계정의 원격 접속을 비활성화
- **테스트 데이터베이스 제거:** `Y`
- **권한 테이블 다시 로드:** `Y`

## 5. MySQL 원격 접속 설정

기본적으로 MySQL은 로컬 호스트(`127.0.0.1`)에서만 접속을 허용한다. 원격에서 MySQL에 접속하려면 설정을 변경해야 한다.

### 5.1. MySQL 설정 파일 수정

설정 파일을 열어 `bind-address`를 수정한다.

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

### 설정 변경:

```
bind-address = 0.0.0.0  # 모든 IP에서의 접속을 허용 (보안상 위험할 수 있음
```

**주의:** 모든 IP에서 접속을 허용하면 보안에 취약할 수 있다. 특정 IP만 허용하려면 해당 IP를 지정한다.

예시:

```
bind-address = 192.168.1.100  # 특정 IP로 제한
```

### 5.2. MySQL 서비스 재시작

설정을 반영하기 위해 MySQL 서비스를 재시작한다.

```bash
sudo systemctl restart mysql
```

## 6. 데이터베이스 및 테이블 생성

### 6.1. root 사용자로 MySQL에 접속

```bash
sudo mysql -u root -p
```

### 6.2. 데이터베이스 생성

```sql
CREATE DATABASE my_db;
```

- `my_db`: 생성할 데이터베이스 이름 (예시)

### 6.3. 테이블 생성

테이블 생성은 [ERD](https://www.notion.so/ERD-f0ff9cb3ad2640559cb05f3668667f3f?pvs=21)를 참고한다.

## 7. 사용자 생성 및 권한 부여

### 7.1. `api_server` 사용자 생성

강력한 비밀번호로 `api_server` 사용자를 생성하고, 특정 IP에 권한을 부여한다.

```sql
CREATE USER 'api_server'@'203.0.113.5' IDENTIFIED BY 'Your_Strong_Password';
GRANT ALL PRIVILEGES ON my_db.* TO 'api_server'@'203.0.113.5';
FLUSH PRIVILEGES;
```

- `203.0.113.5`: API 서버의 IP 주소 (예시)
- `Your_Strong_Password`: 강력한 비밀번호로 설정

## 8. MySQL에서 로그아웃

```sql
EXIT
```

## 9. 방화벽 설정 (필요한 경우)

MySQL 포트를 외부에서 접근할 수 있도록 방화벽을 설정한다.

### 9.1. UFW 활성화

```bash
sudo ufw enable
```

### 9.2. SSH 포트(22) 허용

```bash
sudo ufw allow from 203.0.113.5 to any port 22
```

- `203.0.113.5`: API 서버의 IP 주소 (예시)

### 9.3. MySQL 포트(3306) 허용

```bash
sudo ufw allow from 203.0.113.5 to any port 3306
```

### 9.4. 방화벽 상태 확인

```bash
sudo ufw status
```

**예상 출력:**

```
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       203.0.113.5
3306                       ALLOW       203.0.113.5
```

**참고:** 방화벽 설정 시 실수로 SSH 포트(22)를 차단하면 서버에 접속할 수 없게 되므로 주의한다. 방화벽 설정 후 접속 가능 여부를 반드시 확인한다.

## 10. API 서버에서 DB 서버 MySQL 접속 테스트

API 서버에서 MySQL에 접속하여 설정이 제대로 되었는지 테스트한다.

```bash
mysql -u 'api_server' -p -h 200.255.152.255 my_db
```

- `200.255.152.255`: DB 서버의 IP 주소 (예시)
- `my_db`: 데이터베이스 이름 (예시)

접속 후 `Your_Strong_Password`를 입력하여 정상적으로 접속되는지 확인한다.

## 11. SSH 터널링 설정

원격 접속 시 보안을 강화하기 위해 SSH 터널링을 설정한다.

### 11.1. SSH 터널링 명령 실행

클라이언트 머신에서 다음 명령을 실행하여 SSH 터널을 설정한다.

```bash
ssh -L 3306:localhost:3306 your_username@200.255.152.255
```

- `3306:localhost:3306`: 로컬 포트 3306을 서버의 로컬 포트 3306과 연결
- `your_username`: 서버의 사용자 이름
- `200.255.152.255`: 서버의 공인 IP 주소 (예시)

### 11.2. 로컬에서 MySQL 접속

터널링이 설정된 상태에서 로컬 머신에서 MySQL에 접속한다.

```bash
mysql -u 'api_server' -p -h 127.0.0.1 my_db
```

- `127.0.0.1`: 로컬 호스트 주소
- `my_db`: 데이터베이스 이름 (예시)

## 추가 보안 권장 사항

1. **SSH 키 인증 사용:**
    - 비밀번호 대신 SSH 키를 사용하여 서버에 접속하면 보안이 강화된다.
    - SSH 키 생성 및 설정 방법
2. **MySQL 사용자 권한 최소화:**
    - `api_server` 사용자에게 필요한 최소한의 권한만 부여한다.
    - 예를 들어, 읽기 전용 권한이 필요하다면 `GRANT SELECT`만 부여할 수 있다.
3. **보안 그룹 및 네트워크 ACL 설정:**
    - 클라우드 제공자가 제공하는 보안 그룹이나 네트워크 ACL을 활용하여 추가적인 네트워크 접근 제어를 설정한다.
4. **정기적인 보안 업데이트:**
    - 서버와 MySQL의 보안 패치를 정기적으로 업데이트하여 최신 보안 위협에 대비한다.
5. **모니터링 및 로그 관리:**
    - MySQL 접속 로그를 주기적으로 모니터링하고, 의심스러운 활동이 감지되면 즉시 대응할 수 있도록 설정한다.

## 결론

이 단계를 통해 NCloud의 프라이빗 서버에 MySQL을 설치하고 퍼블릭에서 안전하게 접근할 수 있도록 설정할 수 있다. 보안을 최우선으로 고려하며, 필요한 경우 추가적인 보안 조치를 취하는 것이 중요하다. 앞으로도 클라우드 서버 관리와 관련된 다양한 내용을 지속적으로 학습하고 정리할 예정이다.
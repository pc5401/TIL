# MySQL 권한 관리 및 백업/복구

## MySQL 권한 관리

### 사용자 생성

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```
- `username`: 생성할 사용자의 이름.
- `host`: 사용자가 접속할 수 있는 호스트. 예를 들어, 로컬 호스트의 경우 localhost를 사용.
- `password`: 사용자의 비밀번호.

### 권한 부여

```sql
GRANT ALL PRIVILEGES ON database.* TO 'username'@'host';
```
- `ALL PRIVILEGES`: 모든 권한을 부여. 특정 권한을 부여하려면 SELECT, INSERT, UPDATE, DELETE 등으로 대체.
- `database.*`: 특정 데이터베이스 및 모든 테이블에 권한을 부여. 특정 테이블에만 권한을 부여하려면 database.table로 지정.

### 권한 적용

```sql
FLUSH PRIVILEGES;
```
- 권한 변경 사항을 즉시 적용.

### 권한 수정

특정 권한만 부여하거나 회수할 수 있다.

```sql
GRANT SELECT, INSERT ON database.* TO 'username'@'host';
REVOKE INSERT ON database.* FROM 'username'@'host';
```

### 사용자 삭제

```sql
DROP USER 'username'@'host';
```

### 권한 조회

```sql
SHOW GRANTS FOR 'username'@'host';
```
- 특정 사용자에게 부여된 모든 권한을 조회

### 사용자 및 권한 관리 팁
- 최소 권한 원칙: 사용자에게 필요한 최소한의 권한만 부여하여 보안을 강화.
- 역할 기반 권한 부여: 비슷한 역할을 하는 사용자 그룹에 대해 공통된 권한 세트를 부여.
- 정기적인 권한 검토: 주기적으로 사용자의 권한을 검토하여 필요하지 않은 권한을 회수.

## 백업과 복구

### 데이터베이스 백업

```shell
mysqldump -u username -p database_name > backup_file.sql
```

- `mysqldump`: MySQL 데이터를 백업하는 명령어.
- `-u username`: 데이터베이스에 접속할 사용자 이름.
- `-p`: 비밀번호를 묻도록 지정.
- `database_name`: 백업할 데이터베이스 이름.
- `> backup_file.sql`: 백업 파일의 이름 및 경로.

#### 추가 옵션:

- `--single-transaction`: InnoDB 테이블을 사용하는 경우 백업 중 트랜잭션 일관성을 유지.
- `--routines`: 저장 프로시저와 함수를 백업.
- `--triggers`: 트리거를 백업.

### 특정 테이블 백업
```shell
mysqldump -u username -p database_name table_name > table_backup.sql
```
### 백업 파일 압축

백업 파일을 압축하면 저장 공간을 절약할 수 있다.

```shell
mysqldump -u username -p database_name | gzip > backup_file.sql.gz
```

### 데이터베이스 복구

```shell
mysql -u username -p database_name < backup_file.sql
```

- `mysql`: MySQL 명령어 라인 클라이언트.
- `-u username`: 데이터베이스에 접속할 사용자 이름.
- `-p`: 비밀번호를 묻도록 지정.
- `database_name`: 복구할 데이터베이스 이름.
- `< backup_file.sql`: 복구할 백업 파일.

### 압축된 백업 파일 복구
```shell
gunzip < backup_file.sql.gz | mysql -u username -p database_name
```

### 전체 데이터베이스 서버 백업
서버의 모든 데이터베이스를 백업하려면 --all-databases 옵션을 사용합니다.

``` shell
mysqldump -u username -p --all-databases > all_databases_backup.sql
```

### 백업 및 복구 자동화
- 스크립트를 작성하여 정기적으로 백업을 수행하고, crontab을 사용하여 스케줄링할 수 있습니다.
- 예를 들어, 매일 자정에 백업 스크립트를 실행하도록 설정할 수 있습니다.
백업 스크립트 예제:

``` shell
#!/bin/bash
mysqldump -u username -p'password' --all-databases > /path/to/backup/all_databases_backup_$(date +\%F).sql
```

크론잡 설정 예제:

```shell
0 0 * * * /path/to/backup_script.sh
```
이렇게 하면 백업과 복구, 그리고 사용자 권한 관리를 더욱 효과적으로 수행할 수 있다.
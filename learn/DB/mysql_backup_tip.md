

# 권한 관리 ― 최소 권한 원칙을 기준으로

### 1 사용자 생성 `CREATE USER`

```sql
CREATE USER 'alice'@'203.0.113.10' IDENTIFIED BY '★StrongPassw0rd!';
```

| 파트               | 의미                                  |
| ---------------- | ----------------------------------- |
| `'alice'`        | MySQL 내부 로그인 이름. OS 계정과 무관하다.       |
| `'203.0.113.10'` | 접속을 허용할 클라이언트 호스트(정확한 IP 또는 와일드카드). |
| `IDENTIFIED BY`  | 로그인 시 사용할 해시 패스워드를 저장한다.            |

> **TIP** : 호스트를 `%`(전부 허용)로 두지 말고, *정확한 IP 또는 대역* 으로 제한한다.

---

### 2 권한 부여 `GRANT`

```sql
GRANT SELECT, INSERT
ON sales_db.*
TO 'alice'@'203.0.113.10';
FLUSH PRIVILEGES;
```

- `SELECT, INSERT` : **정밀하게** 필요한 권한만 나열한다.

- `sales_db.*` : `sales_db` 아래 모든 테이블에 적용.

- `FLUSH PRIVILEGES` : 8.0부터는 필요 없지만, *습관적으로* 적어 두면 버전이 달라도 안전하다.

> **ALL PRIVILEGES**를 쓰고 싶을 때 → “*정말로 DBA 권한이 필요한가?*” 를 먼저 자문한다.

---

### 3 권한 회수 `REVOKE`

```sql
REVOKE INSERT
ON sales_db.*
FROM 'alice'@'203.0.113.10';
```

- 추가 권한이 필요 없게 되면 즉시 회수한다.

- 회수 후에도 `SHOW GRANTS`로 결과를 확인해야 안심할 수 있다.

---

### 4 사용자 삭제 `DROP USER`

```sql
DROP USER 'alice'@'203.0.113.10';
```

- **뷰·프로시저**의 DEFINER가 해당 계정을 참조하는지 먼저 확인한다.
  
  - 남아 있으면 오류가 나므로 `ALTER … DEFINER`로 변경 후 삭제.

---

### 5 권한 조회 `SHOW GRANTS`

```sql
SHOW GRANTS FOR 'alice'@'203.0.113.10';
```

- 결과를 그대로 복사해 두면 “*권한 스냅샷*”이 된다.

- 권한 변경 전후 diff 비교가 가능해 감사 로그 대용으로도 유용하다.

---

### 6 추가 팁

1. **역할 기반 계정** :
   
   - `readonly_user`, `writer_user`처럼 역할별 사용자 + 비밀번호 로테이션 스크립트를 운영.

2. **서비스 분리** :
   
   - API, 배치, BI 툴은 서로 다른 계정을 사용해 로그 추적과 문제 원인 파악을 쉽게 한다.

3. **정기 점검** (분기 1회 추천) :
   
   ```sql
   SELECT user, host
   FROM   mysql.user
   WHERE  account_locked = 'N';
   ```
   
   - *존재하지만 쓰이지 않는* 계정을 잠그거나 삭제한다.

---

##하면, 문제는 “언제든 복구 가능”한 **사소한 사건**이 된다.

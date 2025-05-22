# ☝️ 싱글톤 패턴 (Singleton) — *주니어 개발자의 꼼꼼 노트*

> **키워드** : “프로세스(또는 인터프리터) 안에 **단 하나의 인스턴스**”
> 전역처럼 편하게 쓰지만 **캡슐화**까지 챙기고 싶은 상황에서 등장.

---

## 0. 언제 실제로 쓰였나?

| 사례                 | 왜 싱글톤인가?                        |
| ------------------ | ------------------------------- |
| **로깅 Logger**      | 여러 모듈이 동시에 호출 → 로그 파일 핸들 하나만 유지 |
| **DB 커넥션 풀**       | 커넥션 풀 객체는 한 곳에서 관리해야 효율         |
| **앱 설정 Config**    | 실행 중 변하지 않는 설정 값을 어디서든 읽기       |
| **게임 엔진 : 이벤트 버스** | 전역 메시지 큐 하나로 컴포넌트 연결            |

---

## 1. Python 구현 여러 가지

### 1-1. 가장 단순 — *“한 번만 생성”* 방법

```python
class SingletonSimple:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: str) -> None:
        self.value = value
```

```python
a = SingletonSimple("A")
b = SingletonSimple("B")
print(a is b, a.value, b.value)   # True B B  (두 객체는 동일, 마지막 인자만 반영)
```

> 초기화가 **두 번 호출**될 수 있다는 점은 단점. (`__init__`은 호출마다 실행됨)

---

### 1-2. 모듈 자체를 싱글톤처럼

```python
# config.py
import json, pathlib
_cfg = json.loads(pathlib.Path("config.json").read_text())

def get(key: str):            # 전역 getter
    return _cfg[key]
```

```python
# anywhere.py
from config import get
print(get("DB_HOST"))
```

> 파이썬 모듈은 **최초 import 1회만 로드**되므로 사실상 싱글톤.

---

### 1-3. 데코레이터 버전 (thread-safe)

```python
from functools import wraps
from threading import Lock

def singleton(cls):
    instances, lock = {}, Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with lock:                       # 이중 체크
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class Settings:
    def __init__(self):
        print("read heavy config file…")
```

# 🎮 Command Pattern — “요청을 객체로 캡슐화”

> **의도**
> 실행하고 싶은 **행동(요청)** 을 **객체**로 만들면
> → 나중에 호출·큐잉·취소·재실행을 **유연**하게 다룰 수 있다.

---

## 1. 배경 & 사용처

| 상황                | 문제                               | Command 해결책               |
| ----------------- | -------------------------------- | ------------------------- |
| GUI 버튼 / 메뉴 / 단축키 | 클릭마다 다른 로직 → UI 코드에 `if/elif` 난무 | 버튼이 **커맨드 객체**만 실행        |
| 실행 취소(Undo) 기능    | ‘반대로’ 하는 코드를 곳곳에 작성              | 커맨드에 `execute / undo` 메서드 |
| 작업 큐 / 매크로        | 작업을 일단 저장 후 순차 실행                | 요청을 큐에 객체로 저장             |

---

## 2. 구조

```
Client ──▶ Invoker (Button)
                  │
                  ▼
             Command (interface)
             ├── execute()
             ├── undo() (옵션)
                  │
    ┌─────────────┴─────────────┐
ConcreteCommandA         ConcreteCommandB
       │                           │
       ▼                           ▼
  Receiver (실제 작업 수행 객체)
```

* **Command** : `execute()` (필수) + `undo()` (선택)
* **ConcreteCommand** : Receiver에 실제 동작 위임
* **Invoker** : 버튼·메뉴·스케줄러 등 → `command.execute()` 호출
* **Client** : ConcreteCommand를 만들어 Invoker 에 주입

---

## 3. Python 예제 — **텍스트 에디터 Undo/Redo**

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# ---------- Receiver ----------
class Document:
    def __init__(self) -> None:
        self.content: List[str] = []

    def insert(self, text: str) -> None:
        self.content.append(text)

    def remove_last(self) -> str:
        return self.content.pop()

    def show(self) -> None:
        print("".join(self.content))


# ---------- Command Interface ----------
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...


# ---------- Concrete Commands ----------
class InsertCommand(Command):
    def __init__(self, doc: Document, text: str) -> None:
        self.doc, self.text = doc, text

    def execute(self) -> None:
        self.doc.insert(self.text)

    def undo(self) -> None:
        self.doc.remove_last()


# ---------- Invoker ----------
class Editor:
    def __init__(self) -> None:
        self._undo_stack: List[Command] = []
        self._redo_stack: List[Command] = []

    def run(self, cmd: Command):
        cmd.execute()
        self._undo_stack.append(cmd)
        self._redo_stack.clear()          # 새 분기 시작

    def undo(self):
        if self._undo_stack:
            cmd = self._undo_stack.pop()
            cmd.undo()
            self._redo_stack.append(cmd)

    def redo(self):
        if self._redo_stack:
            cmd = self._redo_stack.pop()
            cmd.execute()
            self._undo_stack.append(cmd)


# ---------- Client ----------
if __name__ == "__main__":
    doc = Document()
    editor = Editor()

    editor.run(InsertCommand(doc, "Hello "))
    editor.run(InsertCommand(doc, "Command "))
    editor.run(InsertCommand(doc, "Pattern!"))
    doc.show()          # Hello Command Pattern!

    editor.undo(); doc.show()   # Hello Command
    editor.undo(); doc.show()   # Hello
    editor.redo(); doc.show()   # Hello Command
```

---

## 4. 장 · 단점

| 👍 장점                                     | ⚠️ 단점                        |
| ----------------------------------------- | ---------------------------- |
| 실행/취소/재실행, 로그, 큐잉 등 **행동 이력 관리** 쉬움       | 커맨드 클래스가 많아질 수 있음            |
| **Invoker ↔ 작업 로직 분리** → UI·네트워크·스케줄러 재사용 | 간단한 요청엔 오버헤드                 |
| 매크로(다중 명령), 트랜잭션 조합 가능                    | 상태 저장 방식(`undo`) 설계가 까다로울 때도 |

---

## 5. 패턴 맛보기 비교

| 패턴            | 공통         | 차이                                    |
| ------------- | ---------- | ------------------------------------- |
| **Strategy**  | 객체로 행동 캡슐화 | **알고리즘 교체**가 목적, 실행/취소 개념 없음          |
| **Observer**  | 메시지 전달     | Observer는 알림 브로드캐스트, Command는 *실행 객체* |
| **Prototype** | 객체를 복사     | Command는 행동, Prototype은 데이터           |

---

## 6. 실전 레시피

1. **GUI** : 버튼 `on_click = SaveCommand(doc)`
2. **게임 엔진** : 플레이어 입력 → 커맨드 큐 기록 후 리플레이, 네트워크 동기화
3. **작업 큐 / Celery** : Task 객체 자체가 Command, 브로커가 Invoker
4. **쉘 매크로** : 여러 Command를 리스트로 묶어 `MacroCommand`

---

### 정리

> “행동을 객체로 만들면, **언제·어디서·어떻게** 실행할지 자유로워진다.” 🚀


# 🎭 Facade Pattern — “복잡한 서브시스템을 한 문으로 감싸기”

> **한 줄 요약**
> 여러 개의 덩치 큰 API 묶음을 **얇은 단일 인터페이스**로 노출해
> 클라이언트가 **필요 없는 내부 디테일**을 몰라도 쓰게 만든다.

---

## 1. 언제 쓰면 좋은가?

| 상황                        | 문제                       | Facade로 해결                       |
| ------------------------- | ------------------------ | -------------------------------- |
| 외부 라이브러리 호출부가 코드 곳곳에 섞임   | 의존성·초기화 순서가 드러남          | 서브시스템 초기화/호출을 **Facade** 내부로 이동  |
| 복잡한 모듈(멀티미디어, 복합 DB 트랜잭션) | 함수·클래스 수십 개 중 몇 가지만 자주 씀 | “**간단(high-level) 메서드**” 단 하나 제공 |
| 신규 팀원이 API 전부 이해해야 작업     | 학습 비용 ↑                  | 문서화된 Facade만 익히면 OK              |

---

## 2. 구조 요약 (텍스트)

```
Client ──▶ Facade ──┬─▶ SubsystemA
                    ├─▶ SubsystemB
                    └─▶ SubsystemC
```

* **Subsystem** : 실제 복잡 로직을 가진 클래스 집합
* **Facade** : 클라이언트가 필요한 “단순 메서드”만 노출, 내부에서 서브시스템 호출 순서를 조율

---

## 3. Python 예제 — “🎥 비디오 컨버터”

> 서브시스템(코덱 추출, 디코더, 인코더, Muxer)을 숨기고
> `convert(filename, target_format)` 한 줄만 보여 주는 Facade

```python
# --- Subsystems ---------------------------
class FileReader:
    def read(self, path): ...

class VideoDecoder:
    def decode(self, raw): ...

class AudioDecoder:
    def decode(self, raw): ...

class VideoEncoder:
    def encode(self, frames, fmt): ...

class AudioEncoder:
    def encode(self, frames, fmt): ...

class Muxer:
    def mux(self, v_stream, a_stream, out_path): ...

# --- Facade -----------------------------------------
class VideoConverter:
    def convert(self, src: str, dst_format: str) -> str:
        print("[Facade] Converting…")

        raw = FileReader().read(src)
        v_frames = VideoDecoder().decode(raw)
        a_frames = AudioDecoder().decode(raw)

        v_str = VideoEncoder().encode(v_frames, dst_format)
        a_str = AudioEncoder().encode(a_frames, dst_format)

        out = src.rsplit(".", 1)[0] + "." + dst_format
        Muxer().mux(v_str, a_str, out)

        print("[Facade] Done →", out)
        return out


# --- Client code ------------------------------------
if __name__ == "__main__":
    converter = VideoConverter()
    converter.convert("lecture.mov", "mp4")


```

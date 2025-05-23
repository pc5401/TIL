# IP 주소와 서브넷팅 정리 🌐

---

## 1. IPv4 vs IPv6

| 항목 | IPv4 | IPv6 |
|:---|:---|:---|
| 주소 길이 | 32비트 (4 옥텟) | 128비트 (8 블록) |
| 표기법 | 점-십진수 (192.168.1.1) | 콜론-16진수 (2001:db8::7334) |
| 주소 수 | 약 43억 (2³²) | 사실상 무한 (2¹²⁸) |
| 특징 | NAT 필요, 주소 부족 | IPSec 기본 내장, 자동구성(SLAAC) 가능 |

> IPv4는 **NAT**로 주소를 아껴 사용하지만, IPv6는 주소가 넘칠 만큼 많기 때문에 NAT 없이 직접 통신 가능.

---

## 2. IPv4 주소 구조와 클래스

| 클래스 | 첫 옥텟 범위 | 네트워크/호스트 구분 | 기본 서브넷 마스크 | 예시 |
|:---|:---|:---|:---|:---|
| A | 1 ~ 126 | N.H.H.H | 255.0.0.0 | 10.0.0.1 |
| B | 128 ~ 191 | N.N.H.H | 255.255.0.0 | 172.16.0.1 |
| C | 192 ~ 223 | N.N.N.H | 255.255.255.0 | 192.168.1.1 |
| D | 224 ~ 239 | 멀티캐스트 | - | - |
| E | 240 ~ 255 | 실험용 | - | - |

> **클래스 A, B, C**까지만 실제 사용. 요즘은 **CIDR**로 비트 단위로 나누는 게 일반적.

---

## 3. 서브넷 마스크와 서브넷팅 기본

| 구분 | 설명 |
|:---|:---|
| 서브넷 마스크 | IP 주소를 네트워크/호스트로 나누는 기준. 연속된 1(네트워크), 그 뒤 0(호스트) |
| 서브넷팅 | 하나의 큰 네트워크를 여러 작은 네트워크(서브넷)로 나누는 것 |

| 항목 | 공식 |
|:---|:---|
| 서브넷 수 | 2ⁿ (n=서브넷 비트 수) |
| 각 서브넷 호스트 수 | 2ʰ - 2 (h=호스트 비트 수) |

> `-2` 하는 이유는 네트워크 주소와 브로드캐스트 주소가 빠지기 때문.

---

## 4. CIDR (Classless Inter-Domain Routing)

| 항목 | 설명 |
|:---|:---|
| 정의 | IP 주소 뒤에 슬래시(`/`)와 서브넷 마스크 비트 수를 붙이는 표기법 |
| 예시 | 192.168.1.0/24 (앞 24비트 네트워크, 뒤 8비트 호스트) |
| 장점 | 유연한 주소 관리, 라우팅 테이블 크기 축소 |

---

## 5. VLSM (Variable Length Subnet Mask)

| 항목 | 설명 |
|:---|:---|
| 정의 | 각 서브넷에 필요한 크기만큼 다른 길이의 서브넷 마스크를 적용하는 방법 |
| 장점 | 주소 공간 최적화, 낭비 최소화 |
| 주의점 | 설계 순서가 중요. 큰 네트워크부터 먼저 배정하고 남는 범위에 작은 서브넷 배치. |

---

## 6. 프라이빗 IP와 퍼블릭 IP

| 구분 | IP 범위 |
|:---|:---|
| 프라이빗 A | 10.0.0.0 ~ 10.255.255.255 |
| 프라이빗 B | 172.16.0.0 ~ 172.31.255.255 |
| 프라이빗 C | 192.168.0.0 ~ 192.168.255.255 |

- 프라이빗 IP는 **인터넷 직접 통신 불가**, NAT를 통해 퍼블릭 IP로 변환 필요.
- 퍼블릭 IP는 **인터넷 직접 통신 가능**.

---

## 7. 특별한 IP 주소

| 종류 | IPv4 주소 | 설명 |
|:---|:---|:---|
| 루프백 | 127.0.0.1 | 내 컴퓨터 자신을 가리킴 (localhost) |
| 브로드캐스트 | 서브넷 최댓값 (예: 192.168.1.255) | 네트워크 내 모든 호스트 대상 |
| 네트워크 주소 | 서브넷 시작값 (예: 192.168.1.0) | 네트워크 자체를 식별 |

---

## 8. 서브넷팅 실습 ✏️

### 실습 1: /24를 4개 서브넷으로 나누기

**문제**
- 네트워크: 192.168.10.0/24
- 요구사항: 4개의 서브넷 필요

**풀이**
1. 필요한 서브넷 수 = 4 → 2² = 4 → 서브넷 비트 2개 추가
2. 새 마스크 = /26 (24+2)
3. 새 서브넷당 호스트 수 = 2⁶ - 2 = 62

| 서브넷 번호 | 네트워크 주소 | 호스트 범위 | 브로드캐스트 주소 |
|:---|:---|:---|:---|
| 1 | 192.168.10.0/26 | 192.168.10.1 ~ 192.168.10.62 | 192.168.10.63 |
| 2 | 192.168.10.64/26 | 192.168.10.65 ~ 192.168.10.126 | 192.168.10.127 |
| 3 | 192.168.10.128/26 | 192.168.10.129 ~ 192.168.10.190 | 192.168.10.191 |
| 4 | 192.168.10.192/26 | 192.168.10.193 ~ 192.168.10.254 | 192.168.10.255 |

---

### 실습 2: VLSM 적용 예제

**문제**
- 네트워크: 10.0.0.0/24
- 요구사항
  - A: 50호스트
  - B: 30호스트
  - C: 20호스트

**풀이**
1. 큰 네트워크부터 설계
2. 계산
    - A: 2⁶ = 64 > 50 → /26 필요
    - B: 2⁵ = 32 > 30 → /27 필요
    - C: 2⁵ = 32 > 20 → /27 필요

| 서브넷 | 네트워크 주소 | 서브넷 마스크 | 호스트 범위 |
|:---|:---|:---|:---|
| A | 10.0.0.0/26 | 255.255.255.192 | 10.0.0.1 ~ 10.0.0.62 |
| B | 10.0.0.64/27 | 255.255.255.224 | 10.0.0.65 ~ 10.0.0.94 |
| C | 10.0.0.96/27 | 255.255.255.224 | 10.0.0.97 ~ 10.0.0.126 |

> 나머지 IP 블록은 나중에 다른 용도로 할당 가능.

---

## 정리 ✨

- **IPv4**는 NAT 필요, **IPv6**는 거의 무한.
- **서브넷 마스크**로 네트워크와 호스트를 나눈다.
- **CIDR**로 네트워크를 유연하게 관리.
- **VLSM**으로 서브넷마다 필요한 만큼만 할당.
- 서브넷팅을 통해 **주소 낭비 줄이고**, **네트워크 관리**를 쉽게 한다.
- 실습은 반드시 "필요 서브넷 수", "호스트 수"를 먼저 계산하고 계획해야 한다.

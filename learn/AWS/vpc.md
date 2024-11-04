# AWS VPC 학습 연습 노트

---

### **1. VPC란?**

- **VPC (Virtual Private Cloud)**: Amazon이 제공하는 사용자 전용의 가상 네트워크.
- **주요 특징**:
    - **논리적 분리**: 다른 사용자들의 네트워크와 완전히 분리되어 독립적으로 운영됨.
    - **AWS 서비스 통합**: EC2 같은 다양한 AWS 서비스 리소스를 VPC 내에서 실행.
    - **서브넷 분할**: VPC를 더 작은 범위의 서브넷으로 나눌 수 있어 유연한 네트워크 설계 가능.

---

### **2. VPC의 역사**

- **EC2 Classic**:
    - VPC 도입 이전에 사용되던 단일 네트워크 망.
    - **제한 사항**: VPC에 비해 성능 및 보안이 낮아 2013년 12월 4일 이후 생성된 계정에서는 사용 불가.
    - **마이그레이션 권장**: 보안과 성능 향상을 위해 VPC로 이전 권장.
- **Default VPC**:
    - 루트 계정 생성 시 각 리전에 자동으로 하나씩 생성됨.
    - **기본 설정**: EC2 인스턴스 생성 시 VPC를 지정하지 않으면 기본 VPC에서 시작.
    - **관리**:
        - 삭제 가능하지만 사용자가 직접 생성할 수 없고, AWS Support를 통해 요청해야 함.

---

### **3. VPC의 주요 특징**

- **리전 기반 서비스**: VPC는 특정 리전에 속함.
- **AZ 기반 서비스**: 서브넷, EC2, ENI 등은 가용 영역(AZ)에 속함.
- **보안**:
    - 기본적으로 외부 통신 차단.
    - 필요 시 **인터넷 게이트웨이** 연결로 외부와의 통신 가능.
    - **VPC 피어링**, **VPG 연결**, **VPC Service Endpoint** 등을 통해 다양한 네트워크 연결 방식 지원.

---

### **4. VPC 생성 과정**

1. **리전 선택**: VPC는 특정 리전에 생성됨.
2. **VPC 생성**:
    - **CIDR 지정**: VPC에서 사용할 사설 IP 주소 범위 설정 (예: 10.0.0.0/16).
    - **VPC 이름**: 구분하기 쉬운 명확한 이름 설정.
3. **인터넷 게이트웨이 생성 및 연결**: VPC에 인터넷 접근을 위해 필요.
4. **서브넷 생성**: 필요에 따라 VPC를 여러 서브넷으로 분할.

---

### **5. CIDR (Classless Inter-Domain Routing)**

- **정의**: 클래스 기반 주소의 한계를 극복하기 위해 IP 주소를 유연하게 할당할 수 있도록 설계된 방식.
- **표기법**: `xxx.xxx.xxx.xxx/n` (예: 10.1.0.0/16)
    - **상위 n 비트**: 네트워크 식별.
    - **하위 비트**: 호스트 식별.
- **AWS CIDR 규칙**:
    - **VPC**: 16 ~ 28 비트 프리픽스 사용.
    - **서브넷**: VPC의 부분집합으로 지정 가능하며, 사용 가능한 IP는 전체 범위에서 5개 제외.
    - **특이사항**: AWS는 앞의 4개, 마지막 1개의 주소를 내부 용도로 사용.
- **CIDR 예제**:
    - `56.3.26.84/32` - IP 1개
    - `0.0.0.0/0` - 모든 주소
    - `10.1.0.0/16` - 65,536개 IP
    - `10.1.1.0/24` - 256개 IP
    - `10.1.16.0/20` - 2,048개 IP

---

### **6. 서브넷 (Subnet)**

- **정의**: VPC 내에서 IP 주소 범위를 분할한 작은 네트워크 단위.
- **특징**:
    - **AZ 소속**: 반드시 하나의 가용 영역(AZ)에 속해야 함.
    - **라우팅 테이블 연결**: 각 서브넷은 하나의 라우팅 테이블과 연결되어야 함.
    - **고유한 NACL**: 각 서브넷은 고유한 네트워크 ACL을 가짐.
    - **CIDR 중복 불가**: 같은 VPC 내의 서브넷끼리는 CIDR 범위가 중첩되지 않음.
    - **사용 사례**:
        - **Public Subnet**: 인터넷과 연결 가능.
        - **Private Subnet**: 인터넷과 직접 연결 불가, NAT를 통해 간접적으로 접근 가능.
        - **보안 서브넷**: VPN 전용, 인터넷과 완전히 분리된 서브넷.

---

### **7. 라우팅 테이블 (Routing Table)**

- **정의**: 서브넷 내 트래픽 흐름을 제어하는 규칙 집합.
- **구성 요소**:
    - **Destination**: 트래픽의 목적지 IP 범위.
    - **Target**: 트래픽을 전달할 대상 (인터넷 게이트웨이, NAT 게이트웨이, VPC 피어링 등).
- **특징**:
    - **기본 라우팅 테이블**: VPC 생성 시 기본 라우팅 테이블이 자동으로 생성됨.
    - **추가 라우팅 테이블**: 필요에 따라 여러 개의 라우팅 테이블을 생성하여 서브넷에 할당 가능.
    - **라우팅 우선순위**: 가장 구체적인 라우팅 규칙이 우선 적용됨.
- **예시 라우팅 규칙**:
    
    ```bash
    Destination     Target
    10.0.0.0/16    local
    0.0.0.0/0      IGW (Internet Gateway)
    ```
    

---

### **8. 퍼블릭 서브넷 vs 프라이빗 서브넷**

- **퍼블릭 서브넷 (Public Subnet)**:
    - **인터넷 접근**: 인터넷 게이트웨이를 통해 외부와 직접 통신 가능.
    - **사용 사례**: 웹 서버, 로드 밸런서 등 외부와 통신이 필요한 리소스.
- **프라이빗 서브넷 (Private Subnet)**:
    - **인터넷 접근**: 직접적으로는 불가능, NAT 인스턴스 또는 NAT 게이트웨이를 통해 간접적으로 인터넷 접근.
    - **사용 사례**: 데이터베이스 서버, 애플리케이션 서버 등 외부 접근이 필요 없는 리소스.
- **보안 서브넷 (Secure Subnet)**:
    - **정의**: VPN 전용 서브넷으로, 인터넷과 완전히 분리됨.
    - **사용 사례**: 민감한 정보 저장, 내부 네트워크 전용 리소스.

---

### **9. NAT 인스턴스 및 NAT 게이트웨이**

- **NAT 인스턴스**:
    - **설정 과정**:
        1. NAT 인스턴스 생성.
        2. 보안 그룹 설정 확인.
        3. 내부 방화벽 규칙 변경 (IP Masquerade).
        4. EC2 인스턴스의 Src/Dst 체크 비활성화.
        5. 프라이빗 서브넷의 라우팅 테이블 수정.
    - **사용 목적**: 프라이빗 서브넷 내 리소스가 인터넷에 접근할 수 있도록 지원.
- **NAT 게이트웨이**:
    - **장점**: 고가용성, 관리 용이성.
    - **설정 과정**:
        1. NAT 게이트웨이 생성 및 퍼블릭 서브넷에 배치.
        2. 프라이빗 서브넷의 라우팅 테이블을 NAT 게이트웨이로 수정.

---

### **10. VPC 피어링 (VPC Peering)**

- **정의**: 두 개의 VPC를 직접 연결하여 네트워크 트래픽을 주고받을 수 있도록 함.
- **특징**:
    - **동일 리전 또는 다른 리전**의 VPC 간 연결 가능.
    - **다른 계정의 VPC**와도 연결 가능.
    - **단순 연결**: 설정이 쉽고 간단함.
- **설정 과정**:
    1. 피어링 연결 생성.
    2. 라우팅 테이블 수정하여 트래픽 경로 설정.
    3. 연결 테스트를 통해 정상 작동 확인.
- **주의 사항**:
    - **간접 연결 불가**: A와 B, B와 C가 피어링 되어 있어도 A와 C는 직접 통신 불가.

---

### **11. VPC 보안**

- **Best Practice**: 라우팅 테이블, NACL, 보안 그룹을 모두 활용하여 다층 보안 구축.
- **네트워크 ACL (NACL)**:
    - **역할**: 서브넷 수준에서 트래픽을 허용(allow) 또는 차단(deny)할 수 있음.
    - **특징**:
        - 상태 비저장 (stateless).
        - 규칙을 순서대로 평가.
        - 간단한 보안 규칙 설정에 적합.
- **보안 그룹 (Security Groups)**:
    - **역할**: 인스턴스 수준에서 인바운드 및 아웃바운드 트래픽을 제어.
    - **특징**:
        - 상태 저장 (stateful).
        - 모든 규칙을 한꺼번에 평가.
        - 세부적인 보안 규칙 설정 가능.
- **NACL vs 보안 그룹**:
    
    
    | **NACL** | **보안 그룹** |
    | --- | --- |
    | 상태 비저장 | 상태 저장 |
    | 규칙 순차 평가 | 규칙을 한꺼번에 평가 |
    | 간단한 규칙 | 세부적인 규칙 |
    | 서브넷에 적용 | 인스턴스(그룹)에 적용 |

---

### **12. VPC 운영 전략**

- **서비스별 분리**: 각 서비스별로 별도의 VPC 운영.
- **환경별 분리**: 테스트 환경, 프로덕션 환경 등을 별도의 VPC로 분리.
- **기능별 분리**: 예를 들어, 웹 서버 전용 VPC, 데이터베이스 전용 VPC 등으로 나누어 관리.

---

### **13. 추가 참고 자료**

- **AWS VPC 공식 문서**: [AWS VPC Documentation](https://aws.amazon.com/ko/documentation/vpc/)
- **CIDR 설명**: https://namu.wiki/w/CIDR
- **NAT 인스턴스 설정**: [AWS NAT Instance Guide](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_NAT_Instance.html)
# database 소개

## data란
> DIKW 피라미드

`DIKW 피라미드`라는 데이터 속성을 이해하기 좋게 정리한 모델이 있다. 데이터(Data), 정보(Information), 지식(Knowledge), 지혜(Wisdom)의 네 가지 계층으로 이루어진 개념적 모델이다. 이 피라미드는 데이터가 정보로, 정보가 지식으로, 그리고 지식이 지혜로 발전해 나가는 과정을 설명한다. 각 단계는 이전 단계의 내용을 바탕으로 점진적으로 축적되며, 최종적으로는 지혜를 통해 의사결정과 문제 해결에 이르게 된다.
![DIKW 피라미드](https://itwiki.kr/images/e/e4/DIKW_%ED%94%BC%EB%9D%BC%EB%AF%B8%EB%93%9C.png)
> 출처 IT 위키
### 1. 데이터 (Data)

데이터는 가장 기초적인 수준으로, 단순한 사실이나 숫자, 기록된 값 등을 의미한다. 데이터 자체는 맥락 없이 존재하며, 별다른 의미나 가치를 가지지 않는다. 예를 들어, 온도계에 기록된 숫자 "30도"는 데이터의 전형적인 예시이다. 데이터는 그 자체로는 유용하지 않지만, 나중에 정보로 변환될 수 있는 잠재력을 지닌다.

### 2. 정보 (Information)

정보는 데이터에 의미나 맥락이 부여된 상태를 말한다. 데이터를 이해하고 해석함으로써 정보를 도출할 수 있다. 예를 들어, "30도"라는 데이터가 "오늘 서울의 기온은 30도이다"라는 문장으로 해석될 때, 이는 정보로 변환된다. 이 단계에서는 데이터가 사용자가 이해할 수 있는 형태로 변환되며, 특정 상황에서 유의미한 결론을 도출할 수 있는 상태가 된다.

### 3. 지식 (Knowledge)

지식은 정보를 바탕으로 패턴, 통찰, 그리고 이해를 얻은 상태를 의미한다. 여러 정보들이 연관되고 종합되면서 더 높은 수준의 이해가 가능해지며, 이는 특정 주제나 문제에 대한 깊이 있는 인식으로 이어진다. 예를 들어, "기온이 30도일 때 더위로 인해 사람들은 실내에서 활동하기를 선호한다"는 지식은 여러 날의 기온 정보와 그에 따른 행동 패턴을 분석하여 얻은 것이다. 지식은 의사결정의 기초가 되는 중요한 역할을 한다.

### 4. 지혜 (Wisdom)

지혜는 지식을 바탕으로 올바른 판단과 결정을 내릴 수 있는 능력을 의미한다. 지혜는 단순히 알고 있는 것을 넘어서, 상황에 맞게 지식을 활용하고 최선의 선택을 할 수 있는 능력이다. 이는 경험과 깊은 이해에서 비롯되며, 장기적인 관점에서 최적의 결과를 도출하는 것을 목표로 한다. 예를 들어, "기온이 30도 이상일 때는 외출을 자제하고 실내 활동을 권장하는 것이 좋다"는 판단은 지혜의 예시이다. 지혜는 궁극적으로 지식이 실생활에서 가치 있게 활용되는 단계로, 개인이나 조직의 성과와 직결된다.


## RDBMS 이전의 DBMS

데이터베이스 관리 시스템(DBMS)은 데이터를 체계적으로 저장하고 관리하기 위한 시스템이다. RDBMS(관계형 데이터베이스 관리 시스템)가 등장하기 이전에도 다양한 DBMS 모델이 존재했으며, 각 모델은 나름의 장점과 단점을 가지고 있었다. 이러한 시스템들은 주로 어플리케이션에 종속적이며, 데이터 관리가 복잡하고 단순한 검색 기능만을 제공하는 경우가 많았다.

## RDBMS 이전의 DBMS

### 1. 리스트 기반 모델 (List -> Flat Records)

리스트 기반 모델은 데이터를 단순한 리스트 또는 평면 레코드(flat records) 형식으로 저장하는 방식이다. 이 모델에서는 데이터가 선형적으로 저장되며, 특정 조건에 맞는 데이터를 찾기 위해서는 리스트를 순차적으로 검색해야 한다. 데이터 구조가 매우 단순하여 구현이 쉬운 장점이 있지만, 데이터의 양이 많아지면 검색과 관리가 비효율적으로 변하는 단점이 있다.

### 2. 계층형 데이터베이스 (Binary Tree -> Hierarchical DB)

계층형 데이터베이스는 트리 구조, 특히 이진 트리(binary tree) 형태로 데이터를 저장한다. 이 구조에서는 데이터가 부모-자식 관계를 가지며, 각 부모 노드는 여러 자식 노드를 가질 수 있다. 계층형 DBMS는 특정 데이터 경로에 대한 빠른 접근이 가능하지만, 데이터가 복잡하게 얽혀 있는 경우 트리 구조가 비대해져 관리가 어려워질 수 있다. 또한, 부모-자식 관계로 제한되기 때문에 복잡한 데이터 관계를 표현하는 데 한계가 있다.

### 3. 네트워크 데이터베이스 (Graph -> Network DB)

네트워크 데이터베이스는 그래프 구조를 이용해 데이터를 저장한다. 이 모델에서는 각 데이터가 여러 노드와 다중 경로로 연결될 수 있으며, 관계를 좀 더 유연하게 정의할 수 있다. 네트워크 DBMS는 복잡한 데이터 관계를 표현할 수 있지만, 구조가 복잡해지고 관리가 어려워지는 단점이 있다. 이 모델도 특정 어플리케이션에 종속적이며, 데이터 검색이 단순한 경우에 비해 복잡한 경우 성능이 저하될 수 있다.

### 특징

이러한 초기 DBMS 모델들은 주로 특정 어플리케이션의 요구에 맞추어 설계되었으며, 데이터베이스 구조가 복잡하고 유연성이 떨어지는 경우가 많았다. 또한, 검색 기능도 비교적 단순하여, 복잡한 질의(query)를 처리하는 데 한계가 있었다.

## RDBMS (Relational Database Management System)

### 1. 관계형 데이터 모델의 등장

1970년대에 E.F. Codd는 "A Relational Model of Data for Large Shared Data Banks"라는 논문을 통해 관계형 데이터 모델을 제안했다. 이 모델은 데이터를 행(row)과 열(column)로 구성된 테이블(table) 형태로 저장하며, 이러한 테이블 간의 관계를 정의할 수 있는 방식으로 설계되었다. 관계형 모델의 핵심은 데이터의 관계를 수학적 집합 이론에 기반하여 표현할 수 있다는 점이다. 이로 인해 데이터의 검색과 관리가 훨씬 효율적이고 유연해졌다.

### 2. IBM System R과 Berkeley Postgres

관계형 데이터베이스의 초기 구현으로 IBM의 System R과 Berkeley의 Postgres가 대표적이다. System R은 SQL이라는 새로운 질의 언어를 도입하여, 관계형 데이터베이스의 이론을 실제로 구현한 첫 번째 시스템 중 하나였다. Berkeley Postgres는 그 이후로도 지속적으로 발전하여, 오늘날의 PostgreSQL로 이어지는 중요한 기초가 되었다.

### 3. RDBMS의 확산

1970년대 이후로 RDBMS는 데이터 저장을 위해 가장 널리 사용되는 시스템이 되었다. 관계형 데이터베이스는 그 유연성과 확장성 덕분에 다양한 산업에서 폭넓게 채택되었으며, 오늘날에도 데이터 관리의 표준으로 자리잡고 있다. 오라클, MySQL, MS-SQL, PostgreSQL 등의 다양한 RDBMS 솔루션들이 시장을 주도하고 있으며, 이들 시스템은 트랜잭션 지원, 데이터 무결성, 동시성 제어 등의 중요한 기능을 제공한다.

### 4. 트랜잭션 지원

RDBMS의 중요한 특징 중 하나는 트랜잭션을 지원한다는 점이다. 트랜잭션은 데이터베이스 작업의 논리적 단위로, ACID(Atomicity, Consistency, Isolation, Durability) 속성을 보장함으로써 데이터의 일관성과 무결성을 유지한다. 이로 인해 RDBMS는 금융, 은행, 전자상거래와 같은 고신뢰성이 요구되는 애플리케이션에서 필수적인 역할을 한다.
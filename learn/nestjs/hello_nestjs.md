# hello nestjs 

## Nest.js 가 나온 이유

- **코드 구조화 필요성**: Node.js와 Express.js를 사용한 개발에서 코드의 구조화와 유지보수가 어려운 문제가 발생했다.
- **타입 안전성 추구**: 타입스크립트를 기반으로 한 프레임워크를 통해 코드의 안정성과 오류를 사전에 방지하고자 했다.
- **모듈러 아키텍처 제공**: 대규모 애플리케이션 개발 시 모듈화된 구조를 제공하여 개발 효율성을 높이기 위해 등장했다.
- **Angular의 철학 적용**: 프런트엔드에서 성공적으로 사용된 Angular의 디자인 패턴과 철학을 백엔드 개발에 도입했다.

## Nest.js의 장단점

### 장점

- **타입스크립트 기반**: 타입 안전성과 코드 자동 완성 기능을 통해 개발 생산성이 향상된다.
- **모듈러 구조**: 모듈, 컨트롤러, 서비스 등의 구조로 코드의 재사용성과 유지보수성이 높아진다.
- **데코레이터 사용**: 데코레이터를 활용한 선언적 프로그래밍으로 코드 가독성이 향상된다.
- **풍부한 기능 제공**: 미들웨어, 파이프, 가드 등 다양한 기능을 내장하고 있어 추가적인 라이브러리 사용을 최소화한다.

### 단점

- **학습 곡선이 높다**: Angular나 타입스크립트에 익숙하지 않은 개발자에게는 초기 진입 장벽이 존재한다.
- **복잡성 증가**: 작은 규모의 프로젝트에서는 불필요한 복잡성을 가져올 수 있다.
- **커뮤니티 규모**: Express.js 등에 비해 비교적 작은 커뮤니티로 인한 정보 부족이 있을 수 있다.

## 다른 웹 프레임워크와의 비교

### Express.js vs Nest.js

| 항목 | **Express.js** | **Nest.js** |
| --- | --- | --- |
| **철학과 구조** | 최소한의 코어로 구성된 유연한 프레임워크이다. | 구조화와 모듈화를 강조하는 프레임워크로, Angular의 영향을 받았다. |
| **타입스크립트 지원** | 자바스크립트 기반이지만 타입스크립트 사용 가능하다. | 기본적으로 타입스크립트를 사용하도록 설계되었다. |
| **유연함** | 매우 유연하여 개발자가 원하는 대로 구조를 설계할 수 있다. | 일정한 구조와 패턴을 따르도록 설계되어 있다. |
| **확장성** | 필요한 기능을 미들웨어로 추가하여 확장한다. | 내장된 기능과 모듈 시스템을 통해 쉽게 확장할 수 있다. |
| **학습 곡선** | 간단하고 직관적이어서 배우기 쉽다. | 구조와 개념이 복잡하여 학습에 시간이 필요하다. |
| **커뮤니티 규모** | 대규모의 커뮤니티와 풍부한 자료가 존재한다. | 비교적 작은 커뮤니티지만 빠르게 성장하고 있다. |

### Spring vs Nest.js

| 항목 | **Spring** | **Nest.js** |
| --- | --- | --- |
| **언어와 플랫폼** | 자바 기반의 프레임워크로, JVM에서 동작한다. | 타입스크립트 기반으로, Node.js 런타임에서 실행된다. |
| **생태계와 활용 분야** | 오랜 역사와 방대한 생태계를 가지고 있으며, 엔터프라이즈급 애플리케이션에 적합하다. | 모던한 웹 개발에 적합하고, 자바스크립트 생태계를 활용할 수 있다. |
| **성능과 확장성** | 안정성과 확장성이 뛰어나지만, 비교적 무겁다. | 비동기 I/O를 활용하여 경량이고 높은 성능을 낸다. |
| **유연함** | 다양한 설정과 구성이 가능하지만, 복잡할 수 있다. | 일정한 구조를 따르지만, 필요한 부분만 선택적으로 사용 가능하다. |
| **커뮤니티 규모** | 매우 큰 커뮤니티와 풍부한 자료가 존재한다. | 빠르게 성장하는 커뮤니티로, 최신 기술에 대한 지원이 활발하다. |
| **학습 곡선** | 방대한 기능으로 인해 학습에 시간이 필요하다. | Angular와 유사한 구조로, 프런트엔드 개발자에게는 친숙하다. |

## NestJS의 엔진: Express와 Fastify 비교

NestJS는 기본적으로 HTTP 서버로 **Express**를 사용하지만, **Fastify**를 엔진으로 선택하여 사용할 수도 있다.

### Express와 Fastify 비교

| 항목 | **Express** | **Fastify** |
| --- | --- | --- |
| **성능** | 안정적이지만 상대적으로 느리다. | 비동기 처리를 최적화하여 높은 성능을 제공한다. |
| **플러그인 생태계** | 방대한 미들웨어와 플러그인을 보유하고 있다. | 필요한 대부분의 플러그인을 지원하지만, Express에 비해 적다. |
| **사용 방법** | 기본 엔진으로, 추가 설정 없이 사용 가능하다. | `@nestjs/platform-fastify` 패키지를 설치하여 사용한다. |
| **타사 모듈 지원** | Express 기반으로 작성된 미들웨어를 바로 사용할 수 있다. | 일부 Express 미들웨어는 호환되지 않을 수 있다. |
| **커뮤니티 규모** | 매우 큰 커뮤니티와 풍부한 자료가 존재한다. | 비교적 작은 커뮤니티지만 빠르게 성장하고 있다. |

### 참고 : 엔진 선택 및 사용 방법

- **Express 사용 시**:
    
    ```bash
    nest new my-app
    ```
    
    기본 설정으로 Express 엔진을 사용한다.
    
- **Fastify 사용 시**:
    1. 프로젝트 생성 후 `@nestjs/platform-fastify` 패키지 설치:
        
        ```bash
        npm install @nestjs/platform-fastify
        ```
        
    2. `main.ts` 파일 수정:
        
        ```tsx
        import { NestFactory } from '@nestjs/core';
        import { AppModule } from './app.module';
        import { FastifyAdapter, NestFastifyApplication } from '@nestjs/platform-fastify';
        
        async function bootstrap() {
          const app = await NestFactory.create<NestFastifyApplication>(
            AppModule,
            new FastifyAdapter(),
          );
          await app.listen(3000);
        }
        bootstrap();
        ```
        

## 프레임워크 선택 시 고려해야 할 요소 비교

| 요소 | **Express.js** | **Nest.js** | **Spring** |
| --- | --- | --- | --- |
| **유연함** | 매우 유연하여 자유로운 설계 가능하다. | 일정한 구조를 따르도록 권장한다. | 다양한 설정과 구성이 가능하지만 복잡하다. |
| **확장성** | 미들웨어를 통해 기능 확장한다. | 모듈 시스템과 내장 기능으로 확장성 높다. | 엔터프라이즈급 애플리케이션에 적합하다. |
| **커뮤니티 규모** | 매우 큰 커뮤니티와 자료가 존재한다. | 빠르게 성장하는 커뮤니티이다. | 매우 큰 커뮤니티와 자료가 존재한다. |
| **성능** | 일반적인 성능을 제공한다. | 비동기 처리를 통해 높은 성능을 낸다. | 안정적이지만 무거울 수 있다. |
| **학습 곡선** | 배우기 쉽다. | 구조와 개념이 복잡하여 학습 필요하다. | 방대한 기능으로 인해 학습 필요하다. |
| **타입스크립트 지원** | 추가 설정이 필요하다. | 기본적으로 타입스크립트를 사용한다. | 자바 기반으로 타입 안정성을 제공한다. |
| **생태계** | 방대한 미들웨어와 플러그인이 있다. | 필요한 기능 대부분이 내장되어 있다. | 방대한 라이브러리와 프레임워크가 있다. |

## 정리하면

Nest.js는 현대적인 웹 애플리케이션 개발을 위한 강력한 도구이다. 타입스크립트와 모듈러 아키텍처를 통해 코드의 안정성과 유지보수성을 높일 수 있다. 

프로젝트의 규모, 팀의 기술 스택, 성능 요구 사항 등에 따라 적절한 프레임워크와 엔진을 선택하는 것이 중요하다. Express.js는 간단하고 유연한 개발에, Fastify는 높은 성능이 필요한 경우에 적합하다.


## NestJS 설치 및 프로젝트 설정

### NestJS CLI 설치

NestJS는 CLI(Command Line Interface)를 제공하여 프로젝트 생성과 관리가 용이하다. CLI를 설치하여 개발을 시작한다.

```bash
npm install -g @nestjs/cli
```

### 로컬 CLI 사용

```bash
npm install --save-dev @nestjs/cli
```

> 참고: 팀원과 함께 작업하는 경우, 전역 설치 대신 로컬 개발 의존성으로 설치하여 버전 일관성을 유지하는 것도 하나의 방법이다.
> 

### npx로 바로 사용(일회성 느낌)

```jsx
npx @nestjs/cli@latest
```

> `npx`를 사용하여 최신 버전의 `@nestjs/cli`를 즉석에서 다운로드하고 실행할 수 있다.(버전 불일치 조심)
> 

### 새로운 프로젝트 생성

NestJS CLI를 사용하여 새로운 프로젝트를 생성한다.

```bash
nest new 프로젝트명
```

또는 로컬 설치한 경우:

```bash
npx nest new 프로젝트명
```

명령어를 실행하면 패키지 매니저(npm 또는 yarn)를 선택하라는 메시지가 나타난다. 원하는 패키지 매니저를 선택하면 프로젝트 생성과 함께 의존성 설치가 자동으로 진행된다.

### 엔진 선택 및 설정

NestJS는 기본적으로 Express 엔진을 사용하지만, Fastify를 선택하여 사용할 수도 있다.

### Express 엔진 사용

별도의 설정 없이 기본적으로 Express 엔진을 사용하여 개발을 시작할 수 있다.

### Fastify 엔진 사용

Fastify 엔진을 사용하려면 추가 패키지를 설치하고 설정을 변경해야 한다.

### 개발 서버 실행

프로젝트 디렉토리에서 다음 명령어를 실행하여 개발 서버를 시작한다.

```bash
npm run start
```

개발 모드로 실행하여 코드 변경 시 자동으로 재시작되도록 하려면 다음 명령어를 사용한다.

```bash
npm run start:dev
```

### 프로젝트 구조 이해

NestJS는 모듈, 컨트롤러, 서비스 등의 구조로 구성되어 있다.

- **모듈(Module)**: 관련된 기능을 묶는 단위로, 애플리케이션을 모듈화하여 관리한다.
- **컨트롤러(Controller)**: 요청을 처리하고 응답을 반환하는 역할을 한다.
- **서비스(Service)**: 비즈니스 로직을 처리하며, 컨트롤러에서 호출된다.

### 추가 패키지 설치 및 설정

프로젝트의 필요에 따라 추가적인 패키지를 설치하여 기능을 확장할 수 있다.

### 예시: TypeORM과 MySQL 연동

ORM(Object-Relational Mapping) 도구인 TypeORM을 사용하여 데이터베이스와 연동할 수 있다.

1. 패키지 설치:
    
    ```bash
    
    npm install --save @nestjs/typeorm typeorm mysql2
    ```
    
2. `app.module.ts` 파일에 TypeORM 모듈을 임포트하고 설정을 추가한다.
    
    ```tsx
    import { Module } from '@nestjs/common';
    import { TypeOrmModule } from '@nestjs/typeorm';
    
    @Module({
      imports: [
        TypeOrmModule.forRoot({
          type: 'mysql',
          host: 'localhost',
          port: 3306,
          username: '사용자명',
          password: '비밀번호',
          database: '데이터베이스명',
          entities: [__dirname + '/**/*.entity{.ts,.js}'],
          synchronize: true,
        }),
        // 다른 모듈들
      ],
      controllers: [],
      providers: [],
    })
    export class AppModule {}
    
    ```
    

### 예시: 환경 변수 관리

`@nestjs/config` 패키지를 사용하여 환경 변수를 관리할 수 있다.

1. 패키지 설치:
    
    ```bash
    npm install --save @nestjs/config
    ```
    
2. `app.module.ts` 파일에 ConfigModule을 임포트하고 설정한다.
    
    ```tsx
    import { Module } from '@nestjs/common';
    import { ConfigModule } from '@nestjs/config';
    
    @Module({
      imports: [
        ConfigModule.forRoot({
          isGlobal: true,
        }),
        // 다른 모듈들
      ],
      controllers: [],
      providers: [],
    })
    export class AppModule {}
    ```
    
3. 프로젝트 루트에 `.env` 파일을 생성하고 환경 변수를 정의한다.
    
    ```makefile
    DATABASE_HOST=localhost
    DATABASE_PORT=3306
    ```
    
4. 코드에서 환경 변수를 사용하려면 `ConfigService`를 주입받아 사용한다.
    
    ```tsx
    import { Injectable } from '@nestjs/common';
    import { ConfigService } from '@nestjs/config';
    
    @Injectable()
    export class SomeService {
      constructor(private configService: ConfigService) {
        const dbHost = this.configService.get<string>('DATABASE_HOST');
      }
    }
    ```
    

### 스크립트 및 의존성 관리

프로젝트의 `package.json` 파일에 스크립트를 추가하여 개발 편의성을 높일 수 있다.

```json
{
  "scripts": {
    "start": "nest start",
    "start:dev": "nest start --watch",
    "build": "nest build",
    "format": "prettier --write \"src/**/*.ts\"",
    "lint": "eslint \"{src,apps,libs,test}/**/*.ts\" --fix",
    "test": "jest"
  }
}
```

팀원들과의 협업 시에는 `package-lock.json` 또는 `yarn.lock` 파일을 버전 관리 시스템에 포함하여 의존성 버전을 일치시킨다.

### Node.js 버전 관리

프로젝트별로 Node.js 버전을 통일하기 위해 `.nvmrc` 파일을 생성할 수 있다.

```
// .nvmrc
14
```

> 위와 같이 `.nvmrc` 파일에 숫자 `14`를 작성하면, nvm은 Node.js의 **최신 패치 버전**인 **14.x.x** 버전을 사용하게 된다.
> 

팀원들은 `nvm`을 사용하여 지정된 버전의 Node.js를 설치하고 사용할 수 있다.

```bash
nvm install 14
nvm use 14
```

## 정리하면,

NestJS는 강력하고 유연한 백엔드 개발 프레임워크로, 설치와 설정이 비교적 간단하다. 프로젝트의 요구 사항에 따라 다양한 엔진과 패키지를 활용하여 효율적인 개발이 가능하다. 모듈러 구조와 타입스크립트를 기반으로 한 NestJS를 통해 유지보수성과 확장성이 뛰어난 애플리케이션을 개발할 수 있다.

팀원과의 협업을 위해 의존성 관리와 개발 환경 설정을 철저히 하고, 필요한 경우 로컬 개발 의존성으로 패키지를 설치하여 버전 일관성을 유지한다. 또한, Node.js 버전 관리 도구를 사용하여 동일한 개발 환경을 구축한다.

이러한 설치 및 설정 과정을 통해 NestJS의 강력한 기능을 최대한 활용할 수 있으며, 현대적인 웹 애플리케이션 개발에 큰 도움이 된다.
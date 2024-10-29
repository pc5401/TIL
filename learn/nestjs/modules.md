# 모듈 (Modules)
> 공식문서 : https://docs.nestjs.com/modules , chatgpt로 번역

모듈은 `@Module()` 데코레이터로 주석이 달린 클래스이다. `@Module()` 데코레이터는 Nest가 애플리케이션 구조를 조직하는 데 사용하는 메타데이터를 제공한다.

각 애플리케이션에는 최소 하나의 모듈, 즉 루트 모듈이 존재한다. 루트 모듈은 Nest가 애플리케이션 그래프를 구축하는 출발점으로 사용된다. 이 그래프는 Nest가 모듈과 프로바이더 간의 관계 및 의존성을 해결하는 내부 데이터 구조다. 매우 작은 애플리케이션은 이론적으로 루트 모듈 하나만 가질 수 있지만, 일반적인 경우는 아니다. 모듈은 컴포넌트를 조직하는 효과적인 방법으로 강력히 권장되며, 대부분의 애플리케이션에서는 관련된 기능 세트를 캡슐화하는 여러 모듈을 사용하게 된다. 이는 코드의 복잡성을 관리하고 SOLID 원칙에 따라 개발하는 데 도움이 된다.

`@Module()` 데코레이터는 모듈을 설명하는 객체 하나를 받는다:

- **providers**: Nest 인젝터에 의해 인스턴스화되고 최소 이 모듈 내에서 공유될 수 있는 프로바이더들.
- **controllers**: 이 모듈에서 정의된 컨트롤러들.
- **imports**: 이 모듈에서 필요한 프로바이더들을 내보내는 다른 모듈들의 목록.
- **exports**: 이 모듈에서 제공되는 프로바이더들 중 다른 모듈에서 사용할 수 있도록 내보내는 프로바이더들의 부분 집합. 프로바이더 자체나 그 토큰을 사용할 수 있다.

모듈은 기본적으로 프로바이더를 캡슐화한다. 이는 현재 모듈의 일부가 아니거나 내보내지 않는 모듈에서 프로바이더를 주입할 수 없음을 의미한다. 따라서 모듈의 내보낸 프로바이더는 모듈의 공개 인터페이스(API)로 간주할 수 있다.

## 기능 모듈 (Feature Modules)

`CatsController`와 `CatsService`는 같은 애플리케이션 도메인에 속한다. 이들이 밀접하게 관련되어 있기 때문에 기능 모듈로 이동하는 것이 의미 있다. 기능 모듈은 특정 기능에 관련된 코드를 조직하여 코드의 구조를 유지하고 명확한 경계를 설정한다. 이는 애플리케이션의 규모나 팀의 성장에 따라 복잡성을 관리하고 SOLID 원칙에 따라 개발하는 데 도움을 준다.

예를 들어, `CatsModule`을 생성해보자.

> 힌트: CLI를 사용하여 모듈을 생성하려면 $ nest g module cats 명령을 실행하면 된다.
> 

이제 `CatsModule`을 루트 모듈(`AppModule`)에 임포트해야 한다.

```tsx
// app.module.ts

import { Module } from '@nestjs/common';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
})
export class AppModule {}

```

디렉토리 구조는 다음과 같다:

```lua
src
├── cats
│   ├── dto
│   │   └── create-cat.dto.ts
│   ├── interfaces
│   │   └── cat.interface.ts
│   ├── cats.controller.ts
│   ├── cats.module.ts
│   └── cats.service.ts
├── app.module.ts
└── main.ts
```

## 공유 모듈 (Shared Modules)

모듈은 기본적으로 싱글턴이다. 즉, 여러 모듈에서 동일한 프로바이더 인스턴스를 공유할 수 있다. `CatsService`를 여러 모듈에서 사용하려면 `CatsModule`에서 이를 내보내야 한다.

```tsx
// cats/cats.module.ts

import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
  exports: [CatsService],
})
export class CatsModule {}
```

이제 다른 모듈에서 `CatsModule`을 임포트하면 `CatsService`를 사용할 수 있으며, 모든 모듈에서 동일한 `CatsService` 인스턴스를 공유하게 된다. 이는 메모리 사용을 줄이고, 상태 일관성을 유지하는 데 도움이 된다.

## 모듈 재내보내기 (Module Re-exporting)

모듈은 내부 프로바이더를 내보낼 수 있을 뿐만 아니라, 임포트한 모듈들도 재내보낼 수 있다. 예를 들어, `CoreModule`이 `CommonModule`을 임포트하고 다시 내보낼 수 있다.

```tsx
@Module({
  imports: [CommonModule],
  exports: [CommonModule],
})
export class CoreModule {}
```

## 글로벌 모듈 (Global Modules)

같은 세트를 여러 모듈에서 임포트해야 하는 경우, 글로벌 모듈을 사용할 수 있다. `@Global()` 데코레이터를 사용하여 모듈을 글로벌 스코프로 설정하면, 해당 모듈을 임포트할 필요 없이 전역적으로 프로바이더를 사용할 수 있다.

```tsx
import { Module, Global } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Global()
@Module({
  controllers: [CatsController],
  providers: [CatsService],
  exports: [CatsService],
})
export class CatsModule 
```

> 경고: 모든 것을 글로벌로 만드는 것은 좋은 설계 결정이 아니다. 글로벌 모듈은 필요한 보일러플레이트를 줄이기 위해 사용되며, 일반적으로 모듈의 API를 소비자에게 제공하기 위해 임포트 배열을 사용하는 것이 선호된다.
> 

## 동적 모듈 (Dynamic Modules)

동적 모듈은 커스터마이징 가능한 모듈을 쉽게 생성할 수 있게 해준다. 예를 들어, `DatabaseModule`을 동적으로 정의할 수 있다.

```tsx
// database/database.module.ts

import { Module, DynamicModule } from '@nestjs/common';
import { createDatabaseProviders } from './database.providers';
import { Connection } from './connection.provider';

@Module({
  providers: [Connection],
  exports: [Connection],
})
export class DatabaseModule {
  static forRoot(entities = [], options?): DynamicModule {
    const providers = createDatabaseProviders(options, entities);
    return {
      module: DatabaseModule,
      providers: providers,
      exports: providers,
    };
  }
}
```

동적 모듈을 글로벌로 설정하려면 `@Global()` 데코레이터를 사용할 수 있다.

```tsx
{
  global: true,
  module: DatabaseModule,
  providers: providers,
  exports: providers,
}
```

모듈을 임포트하고 설정하는 방법:

```tsx
import { Module } from '@nestjs/common';
import { DatabaseModule } from './database/database.module';
import { User } from './users/entities/user.entity';

@Module({
  imports: [DatabaseModule.forRoot([User])],
})
export class AppModule {}
```

## 결론

모듈은 NestJS 애플리케이션의 구조를 조직하는 핵심 요소이다. `@Module()` 데코레이터를 사용하여 프로바이더, 컨트롤러, 임포트 및 내보내기를 정의함으로써, 애플리케이션의 복잡성을 관리하고 기능별로 코드를 캡슐화할 수 있다. 기능 모듈, 공유 모듈, 글로벌 모듈, 동적 모듈 등 다양한 모듈 유형을 활용하여 유지보수성과 확장성이 뛰어난 애플리케이션을 개발할 수 있다.

Nest의 IoC 컨테이너는 모듈과 프로바이더 간의 의존성을 자동으로 해결하여 개발자가 비즈니스 로직에 집중할 수 있도록 돕는다. 모듈의 다양한 사용법과 주입 방식을 이해하고 적절히 활용하면, 더욱 견고하고 효율적인 백엔드 애플리케이션을 구축할 수 있다.
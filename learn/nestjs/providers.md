# 프로바이더 (Providers)
> 공식문서 :  https://docs.nestjs.com/providers , chatgpt로 번역

프로바이더는 Nest의 기본 개념이다. 많은 기본 Nest 클래스들은 프로바이더로 취급할 수 있으며, 서비스, 레포지토리, 팩토리, 헬퍼 등이 이에 해당한다. 프로바이더의 주요 개념은 의존성으로 주입할 수 있다는 점이다. 이는 객체들이 서로 다양한 관계를 형성할 수 있고, 이 객체들을 연결하는 작업을 Nest 런타임 시스템에 맡길 수 있다는 의미이다.

## 서비스 (Services)

간단한 `CatsService`를 만들어보자. 이 서비스는 데이터 저장과 검색을 담당하며, `CatsController`에서 사용된다. 따라서 프로바이더로 정의하기에 적합하다.

```tsx
// cats.service.ts

import { Injectable } from '@nestjs/common';
import { Cat } from './interfaces/cat.interface';

@Injectable()
export class CatsService {
  private readonly cats: Cat[] = [];

  create(cat: Cat) {
    this.cats.push(cat);
  }

  findAll(): Cat[] {
    return this.cats;
  }
}
```

> 힌트: CLI를 사용하여 서비스를 생성하려면 $ nest g service cats 명령을 실행하면 된다.
> 

`CatsService`는 하나의 속성과 두 개의 메서드를 가진 기본 클래스이다. 새로운 기능은 `@Injectable()` 데코레이터를 사용한 것이다. `@Injectable()` 데코레이터는 `CatsService`가 Nest의 IoC 컨테이너에 의해 관리될 수 있는 클래스임을 선언한다. 예제에서는 `Cat` 인터페이스도 사용된다.

```tsx
// interfaces/cat.interface.ts

export interface Cat {
  name: string;
  age: number;
  breed: string;
}
```

이제 `CatsService`를 `CatsController`에서 사용해보자.

```tsx
// cats.controller.ts

import { Controller, Get, Post, Body } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';
import { CatsService } from './cats.service';
import { Cat } from './interfaces/cat.interface';

@Controller('cats')
export class CatsController {
  constructor(private catsService: CatsService) {}

  @Post()
  async create(@Body() createCatDto: CreateCatDto) {
    this.catsService.create(createCatDto);
  }

  @Get()
  async findAll(): Promise<Cat[]> {
    return this.catsService.findAll();
  }
}
```

`CatsService`는 클래스 생성자를 통해 주입된다. `private` 키워드를 사용하면 `catsService` 멤버를 선언과 초기화를 동시에 할 수 있다.

## 의존성 주입 (Dependency Injection)

Nest는 의존성 주입(Dependency Injection) 패턴을 중심으로 설계되었다. TypeScript의 타입 기능 덕분에 의존성을 타입만으로 쉽게 관리할 수 있다. 예를 들어, 아래와 같이 `CatsController`의 생성자에서 `CatsService`를 주입받는다.

```tsx
constructor(private catsService: CatsService) {}
```

Nest는 `CatsService`의 인스턴스를 생성하고, 이를 `CatsController`의 생성자에 주입한다. 만약 싱글턴 패턴을 사용한다면, 이미 생성된 인스턴스를 반환한다.

## 스코프 (Scopes)

프로바이더는 보통 애플리케이션 라이프사이클과 동기화된 생명주기를 가진다. 애플리케이션이 부트스트랩될 때 모든 프로바이더가 인스턴스화되고, 애플리케이션이 종료될 때 각 프로바이더가 소멸된다. 하지만 요청 기반 생명주기를 가지는 프로바이더도 만들 수 있다. 이를 통해 요청마다 새로운 인스턴스를 생성할 수 있다. 자세한 내용은 스코프 제어를 참조한다.

## 커스텀 프로바이더 (Custom Providers)

Nest는 내장된 IoC 컨테이너가 프로바이더 간의 관계를 해결한다. 프로바이더를 정의하는 여러 방법이 있다: 평범한 값, 클래스, 비동기 또는 동기 팩토리 등을 사용할 수 있다. 다양한 예제는 공식 문서를 참고한다.

## 선택적 프로바이더 (Optional Providers)

때때로 의존성이 반드시 해결될 필요가 없다. 예를 들어, 클래스가 설정 객체에 의존하지만, 설정이 제공되지 않으면 기본 값을 사용해야 하는 경우가 있다. 이런 경우 의존성은 선택적이 된다. `@Optional()` 데코레이터를 사용하여 프로바이더가 선택적임을 표시할 수 있다.

```tsx
import { Injectable, Optional, Inject } from '@nestjs/common';

@Injectable()
export class HttpService<T> {
  constructor(@Optional() @Inject('HTTP_OPTIONS') private httpClient: T) {}

```

위 예제에서는 `HTTP_OPTIONS`라는 커스텀 토큰을 사용하여 프로바이더를 주입받는다. `@Optional()` 데코레이터를 사용하여 이 의존성이 선택적임을 명시했다.

## 프로퍼티 기반 주입 (Property-based Injection)

지금까지는 생성자 기반 주입을 사용했지만, 특정 상황에서는 프로퍼티 기반 주입이 유용할 수 있다. 예를 들어, 최상위 클래스가 여러 프로바이더에 의존할 때, 서브 클래스에서 생성자를 통해 이를 전달하는 것이 번거로울 수 있다. 이럴 때 `@Inject()` 데코레이터를 프로퍼티 레벨에서 사용할 수 있다.

```tsx
import { Injectable, Inject } from '@nestjs/common';

@Injectable()
export class HttpService<T> {
  @Inject('HTTP_OPTIONS')
  private readonly httpClient: T;
}
```

> 경고: 클래스가 다른 클래스를 상속하지 않는 경우, 항상 생성자 기반 주입을 선호해야 한다. 생성자는 필요한 의존성을 명확하게 나타내며, @Inject를 사용한 프로퍼티 주입보다 가시성이 높다.
> 

## 프로바이더 등록 (Provider Registration)

프로바이더를 정의하고, 이를 사용하는 컨트롤러에 주입하려면 프로바이더를 모듈에 등록해야 한다. 이를 위해 `app.module.ts` 파일을 수정하여 `providers` 배열에 서비스를 추가한다.

```tsx
// app.module.ts

import { Module } from '@nestjs/common';
import { CatsController } from './cats/cats.controller';
import { CatsService } from './cats/cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class AppModule {}
```

이제 Nest는 `CatsController`의 의존성을 해결할 수 있다.

프로젝트 디렉토리 구조는 다음과 같다:

```css
src
├── cats
│   ├── dto
│   │   └── create-cat.dto.ts
│   ├── interfaces
│   │   └── cat.interface.ts
│   ├── cats.controller.ts
│   └── cats.service.ts
├── app.module.ts
└── main.ts
```

## 수동 인스턴스화 (Manual Instantiation)

지금까지 Nest의 DI 시스템을 통해 대부분의 의존성 해결을 자동으로 처리했다. 그러나 특정 상황에서는 프로바이더를 수동으로 가져오거나 인스턴스화해야 할 수 있다. 예를 들어, 부트스트랩 함수 내에서 프로바이더를 동적으로 가져오려면 모듈 참조를 사용할 수 있다. 자세한 내용은 독립 실행형 애플리케이션에서 확인할 수 있다.

## 결론

프로바이더는 NestJS 애플리케이션의 핵심 요소로, 의존성 주입을 통해 객체 간의 관계를 효율적으로 관리한다. 서비스, 레포지토리, 헬퍼 등 다양한 클래스를 프로바이더로 사용할 수 있으며, 이를 통해 코드의 재사용성과 유지보수성을 높일 수 있다. Nest의 IoC 컨테이너는 프로바이더 간의 의존성을 자동으로 해결하여 개발자가 비즈니스 로직에 집중할 수 있도록 돕는다. 프로바이더의 다양한 사용법과 주입 방식을 이해하고 적절히 활용하면, 더욱 견고하고 확장 가능한 백엔드 애플리케이션을 개발할 수 있다.
# 미들웨어 (Middleware)
> 공식문서 : https://docs.nestjs.com/middleware , chatgpt로 번역


미들웨어는 라우트 핸들러 전에 호출되는 함수다. 미들웨어 함수는 요청(request)과 응답(response) 객체에 접근할 수 있으며, 애플리케이션의 요청-응답 사이클에서 다음 미들웨어 함수인 `next()`를 호출할 수 있다. 다음 미들웨어 함수는 일반적으로 `next`라는 변수로 표시된다.

Nest의 미들웨어는 기본적으로 Express 미들웨어와 동일하다. 공식 Express 문서의 설명을 참고하면 미들웨어의 기능을 이해할 수 있다:

## 미들웨어의 역할

미들웨어 함수는 다음 작업을 수행할 수 있다:

- **코드 실행**: 임의의 코드를 실행할 수 있다.
- **요청 및 응답 객체 변경**: 요청과 응답 객체를 수정할 수 있다.
- **요청-응답 사이클 종료**: 요청-응답 사이클을 종료할 수 있다.
- **다음 미들웨어 호출**: 스택의 다음 미들웨어 함수를 호출할 수 있다.

현재 미들웨어 함수가 요청-응답 사이클을 종료하지 않으면, 반드시 `next()`를 호출하여 제어를 다음 미들웨어로 전달해야 한다. 그렇지 않으면 요청이 멈추게 된다.

## 커스텀 미들웨어 구현

Nest에서는 커스텀 미들웨어를 함수 또는 `@Injectable()` 데코레이터가 붙은 클래스로 구현할 수 있다. 클래스 미들웨어는 `NestMiddleware` 인터페이스를 구현해야 하며, 함수 미들웨어는 특별한 요구사항이 없다. 클래스 방식을 사용하여 간단한 미들웨어를 구현해보자.

```tsx
// logger.middleware.ts

import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log('요청 발생...');
    next();
  }

```

> 경고: Express와 Fastify는 미들웨어를 다르게 처리하며, 다른 메서드 시그니처를 제공한다. 자세히 알아보기
> 

## 의존성 주입 (Dependency Injection)

Nest의 미들웨어는 의존성 주입을 완벽하게 지원한다. 프로바이더나 다른 의존성을 동일한 모듈 내에서 주입받을 수 있으며, 이는 생성자를 통해 이루어진다.

```tsx
constructor(private catsService: CatsService) {}
```

Nest는 `CatsService`의 인스턴스를 생성하여 미들웨어 클래스의 생성자에 주입한다. 싱글턴 패턴을 사용하는 경우, 이미 생성된 인스턴스를 반환한다.

## 미들웨어 적용

모듈 클래스의 `@Module()` 데코레이터 내에는 미들웨어를 설정할 위치가 없다. 대신, 모듈 클래스는 `NestModule` 인터페이스를 구현하고 `configure()` 메서드를 사용하여 미들웨어를 설정한다. 다음은 `AppModule`에 `LoggerMiddleware`를 설정하는 예제다.

```tsx
// app.module.ts

import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes('cats');
  }
}
```

위 예제에서는 `/cats` 경로에 대한 모든 요청에 `LoggerMiddleware`를 적용했다. 특정 요청 메서드에만 미들웨어를 적용하려면 `forRoutes()` 메서드에 경로와 요청 메서드를 지정할 수 있다.

```tsx
// app.module.ts

import { Module, NestModule, RequestMethod, MiddlewareConsumer } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes({ path: 'cats', method: RequestMethod.GET });
  }
}
```

> 힌트: configure() 메서드는 비동기적으로 작성할 수 있으며, async/await를 사용할 수 있다.
> 

## 라우트 와일드카드

패턴 기반 라우트도 지원된다. 예를 들어, 애스터리스크(`*`)는 와일드카드로 사용되며, 특정 문자 조합을 매칭할 수 있다.

```tsx
consumer
  .apply(LoggerMiddleware)
  .forRoutes({
    path: 'ab*cd',
    method: RequestMethod.ALL,
  });
```

`'ab*cd'` 경로는 `abcd`, `ab_cd`, `abecd` 등을 매칭한다. 문자 `?`, `+`, `*`, `()`는 정규식의 일부로 해석되며, 하이픈(`-`)과 점(`.`)은 문자 그대로 해석된다.

> 경고: Fastify는 최신 버전의 path-to-regexp 패키지를 사용하여 와일드카드 애스터리스크(*)를 더 이상 지원하지 않는다. 대신 매개변수((.*), :splat*)를 사용해야 한다.
> 

## 미들웨어 소비자 (Middleware Consumer)

`MiddlewareConsumer`는 미들웨어를 관리하는 도우미 클래스다. `forRoutes()` 메서드는 단일 문자열, 여러 문자열, `RouteInfo` 객체, 컨트롤러 클래스 등을 인수로 받을 수 있다. 주로 컨트롤러 클래스를 전달하여 특정 컨트롤러에 미들웨어를 적용한다.

```tsx
// app.module.ts

import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';
import { CatsController } from './cats/cats.controller';

@Module({
  imports: [CatsModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes(CatsController);
  }
}
```

> 힌트: apply() 메서드는 하나 이상의 미들웨어를 인수로 받을 수 있다.
> 

## 라우트 제외

특정 경로를 제외하고 미들웨어를 적용할 수 있다. `exclude()` 메서드를 사용하여 제외할 경로를 지정한다.

```tsx
consumer
  .apply(LoggerMiddleware)
  .exclude(
    { path: 'cats', method: RequestMethod.GET },
    { path: 'cats', method: RequestMethod.POST },
    'cats/(.*)',
  )
  .forRoutes(CatsController)
```

위 예제에서는 `GET /cats`, `POST /cats`, `cats/*` 경로를 제외하고 `CatsController`의 나머지 경로에 `LoggerMiddleware`를 적용한다.

> 힌트: exclude() 메서드는 path-to-regexp 패키지를 사용하여 와일드카드 매개변수를 지원한다.
> 

## 함수형 미들웨어 (Functional Middleware)

클래스 기반 미들웨어 대신 함수형 미들웨어를 사용할 수 있다. 클래스가 단순한 경우, 함수형 미들웨어가 더 간단하고 효율적일 수 있다.

```tsx
// logger.middleware.ts

import { Request, Response, NextFunction } from 'express';

export function logger(req: Request, res: Response, next: NextFunction) {
  console.log('요청 발생...');
  next();
}
```

`AppModule`에서 함수형 미들웨어를 적용하는 방법:

```tsx
// app.module.ts

consumer
  .apply(logger)
  .forRoutes(CatsController);
```

> 힌트: 의존성이 필요 없는 단순한 미들웨어는 함수형 미들웨어를 사용하는 것이 좋다.
> 

## 여러 미들웨어 적용

여러 개의 미들웨어를 순차적으로 적용하려면 `apply()` 메서드에 쉼표로 구분된 리스트를 전달한다.

```tsx
consumer.apply(cors(), helmet(), logger).forRoutes(CatsController);
```

## 글로벌 미들웨어 (Global Middleware)

모든 라우트에 미들웨어를 적용하려면 애플리케이션 인스턴스에서 `use()` 메서드를 사용한다. 이는 `main.ts` 파일에서 설정할 수 있다.

```tsx
// main.ts

const app = await NestFactory.create(AppModule);
app.use(logger);
await app.listen(process.env.PORT ?? 3000);
```

> 힌트: 글로벌 미들웨어에서는 의존성 주입 컨테이너에 접근할 수 없으므로, 함수형 미들웨어를 사용하는 것이 좋다. 또는 클래스 미들웨어를 사용하고 forRoutes('*')로 설정하여 글로벌하게 적용할 수 있다.
> 

## 결론

미들웨어는 NestJS 애플리케이션에서 요청을 처리하기 전에 추가적인 작업을 수행할 수 있게 해준다. 미들웨어를 통해 요청 로깅, 인증, 데이터 파싱 등 다양한 기능을 구현할 수 있으며, 함수형 또는 클래스 기반으로 유연하게 구성할 수 있다. Nest의 미들웨어 시스템은 Express와 호환되며, 의존성 주입을 지원하여 코드의 재사용성과 유지보수성을 높여준다. 다양한 미들웨어 적용 방법을 이해하고 적절히 활용하면, 더욱 견고하고 효율적인 백엔드 애플리케이션을 개발할 수 있다.
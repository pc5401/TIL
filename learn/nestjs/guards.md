# 가드 (Guards)

가드는 `@Injectable()` 데코레이터로 주석된 클래스이며, `CanActivate` 인터페이스를 구현한다.

## 가드의 역할

가드는 단일 책임을 가진다. 특정 조건(예: 권한, 역할, ACL 등)에 따라 주어진 요청이 라우트 핸들러에 의해 처리될지 여부를 결정한다. 이는 주로 **권한 부여 (Authorization)**라고 불린다. 전통적인 Express 애플리케이션에서는 권한 부여와 **인증 (Authentication)**을 미들웨어가 처리한다. 인증은 토큰 검증이나 요청 객체에 속성을 첨부하는 작업으로, 특정 라우트 컨텍스트와 강하게 연결되지 않아 미들웨어가 적합하다.

그러나 미들웨어는 본질적으로 "똑똑하지 않다". `next()` 함수를 호출한 후 어떤 핸들러가 실행될지 알지 못한다. 반면, 가드는 `ExecutionContext` 인스턴스에 접근할 수 있어 다음에 실행될 핸들러를 정확히 알 수 있다. 가드는 예외 필터, 파이프, 인터셉터와 유사하게 요청/응답 사이클의 정확한 지점에 처리 로직을 개입시킬 수 있으며, 선언적으로 이를 수행할 수 있다. 이는 코드의 중복을 줄이고 선언적이게 유지하는 데 도움이 된다.

> 힌트: 가드는 모든 미들웨어 이후, 그러나 인터셉터나 파이프 이전에 실행된다.
> 

## 권한 부여 가드 (Authorization Guard)

권한 부여는 가드의 주요 사용 사례이다. 특정 라우트는 충분한 권한을 가진 호출자(주로 특정 인증된 사용자)에게만 접근이 허용되어야 한다. 아래는 인증된 사용자를 가정하고 토큰을 추출 및 검증하여 요청을 진행할지 여부를 결정하는 `AuthGuard` 예제이다.

```tsx
typescript
코드 복사
// auth.guard.ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { Observable } from 'rxjs';

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(
    context: ExecutionContext,
  ): boolean | Promise<boolean> | Observable<boolean> {
    const request = context.switchToHttp().getRequest();
    return validateRequest(request);
  }
}

```

> 힌트: 실제 애플리케이션에서 인증 메커니즘을 구현하는 방법에 대한 예제는 해당 챕터를 참조한다. 보다 정교한 권한 부여 예제는 별도의 페이지를 참고한다.
> 

`validateRequest()` 함수 내부 로직은 필요에 따라 간단하거나 복잡하게 구현할 수 있다. 주요 목적은 가드가 요청/응답 사이클에 어떻게 개입하는지를 보여주는 것이다.

모든 가드는 `canActivate()` 함수를 구현해야 한다. 이 함수는 현재 요청이 허용되는지 여부를 나타내는 `boolean` 값을 반환해야 한다. 비동기적으로 반환할 수도 있으며, Nest는 반환 값을 기반으로 다음 동작을 제어한다.

- `true`를 반환하면 요청이 처리된다.
- `false`를 반환하면 요청이 거부된다.

## 실행 컨텍스트 (Execution Context)

`canActivate()` 함수는 단일 인수인 `ExecutionContext` 인스턴스를 받는다. `ExecutionContext`는 `ArgumentsHost`를 상속하며, 이는 이전에 예외 필터 챕터에서 다룬 바 있다. 위 예제에서는 `ArgumentsHost`의 헬퍼 메서드를 사용하여 요청 객체에 접근한다. `ExecutionContext`는 현재 실행 중인 프로세스에 대한 추가 정보를 제공하며, 이를 통해 더 일반적인 가드를 구축할 수 있다.

## 역할 기반 인증 (Role-based Authentication)

아래는 특정 역할을 가진 사용자만 접근할 수 있도록 하는 `RolesGuard`의 예제이다. 먼저 기본 가드 템플릿을 작성한 후, 이를 확장하여 역할 기반 인증을 구현한다.

### `RolesGuard` 예제

```tsx
// roles.guard.ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { Reflector } from '@nestjs/core';
import { Roles } from './roles.decorator';

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const roles = this.reflector.get<string[]>('roles', context.getHandler());
    if (!roles) {
      return true;
    }
    const request = context.switchToHttp().getRequest();
    const user = request.user;
    return matchRoles(roles, user.roles);
  }
}
```

> 힌트: 사용자에게 할당된 역할은 일반적으로 요청 객체에 user 속성으로 첨부된다. 이는 커스텀 인증 가드나 미들웨어에서 설정된다.
> 

### 커스텀 메타데이터 데코레이터 (`@Roles`)

```tsx
// roles.decorator.ts
import { SetMetadata } from '@nestjs/common';

export const Roles = (...roles: string[]) => SetMetadata('roles', roles);
```

### `Roles` 데코레이터 사용 예

```tsx
// cats.controller.ts
import { Controller, Post, UseGuards, Body } from '@nestjs/common';
import { RolesGuard } from './roles.guard';
import { Roles } from './roles.decorator';
import { CreateCatDto } from './create-cat.dto';

@Controller('cats')
@UseGuards(RolesGuard)
export class CatsController {
  @Post()
  @Roles('admin')
  async create(@Body() createCatDto: CreateCatDto) {
    this.catsService.create(createCatDto);
  }
}
```

## 가드 바인딩 (Binding Guards)

가드는 컨트롤러 수준, 메서드 수준 또는 글로벌 수준으로 바인딩할 수 있다. `@UseGuards()` 데코레이터를 사용하여 특정 가드를 바인딩하는 예는 다음과 같다.

### 컨트롤러 수준에서 가드 바인딩

```tsx
// cats.controller.ts
import { Controller, UseGuards } from '@nestjs/common';
import { RolesGuard } from './roles.guard';

@Controller('cats')
@UseGuards(RolesGuard)
export class CatsController {}
```

### 메서드 수준에서 가드 바인딩

```tsx
// cats.controller.ts
import { Controller, Get, UseGuards } from '@nestjs/common';
import { RolesGuard } from './roles.guard';

@Controller('cats')
export class CatsController {
  @Get()
  @UseGuards(RolesGuard)
  findAll() {
    return this.catsService.findAll();
  }
}
```

### 글로벌 가드 설정

글로벌 가드를 설정하면 애플리케이션 전체의 모든 컨트롤러와 라우트 핸들러에 적용된다.

```tsx
// main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { RolesGuard } from './roles.guard';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalGuards(new RolesGuard());
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

또는 모듈 내에서 글로벌 가드를 설정할 수 있다.

```tsx
// app.module.ts
import { Module } from '@nestjs/common';
import { APP_GUARD } from '@nestjs/core';
import { RolesGuard } from './roles.guard';

@Module({
  providers: [
    {
      provide: APP_GUARD,
      useClass: RolesGuard,
    },
  ],
})
export class AppModule {}
```

## 결론

가드는 NestJS 애플리케이션에서 요청의 권한을 결정하는 중요한 역할을 한다. 미들웨어와 달리, 가드는 실행 컨텍스트에 접근하여 특정 라우트 핸들러의 실행 여부를 결정할 수 있다. 역할 기반 인증과 같은 복잡한 권한 부여 로직을 구현할 때 유용하며, `@UseGuards()` 데코레이터를 통해 쉽게 바인딩할 수 있다. 글로벌 가드를 설정하여 애플리케이션 전체에 일관된 권한 부여 정책을 적용할 수도 있다. 가드를 적절히 활용하면 코드의 가독성과 유지보수성이 향상된다.
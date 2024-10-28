# 컨트롤러 (Controllers)

> 공식문서 :  https://docs.nestjs.com/controllers , chatgpt로 번역
> 

컨트롤러는 들어오는 요청을 처리하고 클라이언트에게 응답을 반환하는 역할을 한다.

컨트롤러의 목적은 애플리케이션에 대한 특정 요청을 수신하는 것이다. 라우팅 메커니즘은 어떤 컨트롤러가 어떤 요청을 받을지 결정한다. 일반적으로 각 컨트롤러는 여러 라우트를 가지며, 서로 다른 라우트는 다양한 동작을 수행할 수 있다.

기본적인 컨트롤러를 생성하기 위해 클래스와 데코레이터를 사용한다. 데코레이터는 클래스에 필요한 메타데이터를 연결하고, Nest가 라우팅 맵을 생성하여 요청을 해당 컨트롤러에 매핑할 수 있게 한다.

> 힌트: 검증이 내장된 CRUD 컨트롤러를 빠르게 생성하려면 CLI의 CRUD 생성기인 nest g resource [name] 명령을 사용할 수 있다.
> 

## 라우팅

`@Controller()` 데코레이터를 사용하여 기본 컨트롤러를 정의한다. 선택적으로 경로 프리픽스(prefix)를 지정할 수 있다. 경로 프리픽스를 사용하면 관련된 라우트 세트를 그룹화하고 반복적인 코드를 줄일 수 있다. 예를 들어, 고양이 엔티티와 상호 작용을 관리하는 라우트를 `/cats` 경로 아래에 그룹화할 수 있다.

> 힌트: CLI를 사용하여 컨트롤러를 생성하려면 $ nest g controller [name] 명령을 실행하면 된다.
> 

`@Get()` 데코레이터는 특정 엔드포인트에 대한 핸들러를 생성한다. 라우트 경로는 컨트롤러에 선언된 프리픽스와 메서드의 데코레이터에 지정된 경로를 결합하여 결정된다. 위 예제에서는 `GET /cats` 요청이 `findAll()` 메서드로 라우팅된다.

응답은 기본적으로 상태 코드 200과 함께 반환되며, 이는 단순한 문자열이다. Nest는 두 가지 방식으로 응답을 조작할 수 있다:

1. **표준 방식 (권장됨)**: 요청 핸들러가 객체나 배열을 반환하면 JSON으로 직렬화된다. 원시 타입(문자열, 숫자 등)을 반환하면 값만 전송된다.
2. **라이브러리별 방식**: `@Res()` 데코레이터를 사용하여 라이브러리별 응답 객체를 주입할 수 있다. 예를 들어, Express의 응답 객체를 직접 조작할 수 있다.

> 경고: @Res() 또는 @Next()를 사용할 경우, 해당 핸들러는 라이브러리별 모드로 전환되며, 표준 응답 처리는 비활성화된다. 두 방식을 동시에 사용하려면 @Res({ passthrough: true }) 옵션을 설정해야 한다.
> 

## 요청 객체

핸들러는 클라이언트 요청의 세부 정보에 접근할 수 있다. `@Req()` 데코레이터를 사용하여 요청 객체를 주입받을 수 있다.

```tsx
import { Controller, Get, Req } from '@nestjs/common';
import { Request } from 'express';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(@Req() request: Request): string {
    return '모든 고양이를 반환합니다';
  }
}
```

Express의 타입 지원을 활용하려면 `@types/express` 패키지를 설치해야 한다. 대부분의 경우 `@Body()`, `@Query()`와 같은 전용 데코레이터를 사용하는 것이 편리하다.

| 데코레이터 | 객체 |
| --- | --- |
| `@Request()`, `@Req()` | `req` |
| `@Response()`, `@Res()`* | `res` |
| `@Next()` | `next` |
| `@Session()` | `req.session` |
| `@Param(key?: string)` | `req.params` / `req.params[key]` |
| `@Body(key?: string)` | `req.body` / `req.body[key]` |
| `@Query(key?: string)` | `req.query` / `req.query[key]` |
| `@Headers(name?: string)` | `req.headers` / `req.headers[name]` |
| `@Ip()` | `req.ip` |
| `@HostParam()` | `req.hosts` |
- `@Res()`는 `@Response()`의 별칭이다. `@Res()`를 사용할 경우, 응답 객체를 직접 조작해야 하며, 이는 플랫폼 종속적이 되고 테스트가 어려워질 수 있다.

## 리소스 처리

다양한 HTTP 메서드에 대한 데코레이터를 사용하여 CRUD 기능을 구현할 수 있다. 예를 들어, `@Post()`, `@Get()`, `@Put()`, `@Delete()` 데코레이터를 사용하여 고양이 리소스를 생성, 조회, 수정, 삭제하는 엔드포인트를 정의할 수 있다.

```tsx
import { Controller, Get, Post, Put, Delete, Body, Param, Query } from '@nestjs/common';
import { CreateCatDto, UpdateCatDto, ListAllEntities } from './dto';

@Controller('cats')
export class CatsController {
  @Post()
  create(@Body() createCatDto: CreateCatDto): string {
    return '새로운 고양이를 추가합니다';
  }

  @Get()
  findAll(@Query() query: ListAllEntities): string {
    return `모든 고양이를 반환합니다 (제한: ${query.limit}마리)`;
  }

  @Get(':id')
  findOne(@Param('id') id: string): string {
    return `ID #${id}인 고양이를 반환합니다`;
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateCatDto: UpdateCatDto): string {
    return `ID #${id}인 고양이를 업데이트합니다`;
  }

  @Delete(':id')
  remove(@Param('id') id: string): string {
    return `ID #${id}인 고양이를 삭제합니다`;
  }
}
```

Nest는 표준 HTTP 메서드에 대한 데코레이터를 제공한다: `@Get()`, `@Post()`, `@Put()`, `@Delete()`, `@Patch()`, `@Options()`, `@Head()`. 또한, `@All()` 데코레이터는 모든 HTTP 메서드를 처리하는 엔드포인트를 정의한다.

## 라우트 와일드카드

패턴 기반 라우트도 지원된다. 애스터리스크(`*`)는 와일드카드로 사용되며, 특정 문자 조합을 매칭할 수 있다.

```tsx
@Get('ab*cd')
findAll(): string {
  return '이 라우트는 와일드카드를 사용합니다';
}
```

`'ab*cd'` 경로는 `abcd`, `ab_cd`, `abecd` 등을 매칭한다. 문자 `?`, `+`, `*`, `()`는 정규식의 일부로 해석되며, 하이픈(`-`)과 점(`.`)은 문자 그대로 해석된다.

> 경고: 라우트 중간의 와일드카드는 Express에서만 지원된다.
> 

## 상태 코드

응답의 상태 코드는 기본적으로 항상 200이며, POST 요청의 경우 201이다. `@HttpCode(...)` 데코레이터를 사용하여 이를 변경할 수 있다.

```tsx
@Post()
@HttpCode(204)
create(): string {
  return '새로운 고양이를 추가합니다';
}
```

> 힌트: @nestjs/common 패키지에서 HttpCode를 가져와야 한다.
> 

상태 코드는 다양한 요인에 따라 동적으로 변경될 수 있다. 이 경우, 라이브러리별 응답 객체(`@Res()`)를 사용하거나 예외를 던질 수 있다.

## 헤더

커스텀 응답 헤더를 지정하려면 `@Header()` 데코레이터를 사용하거나, 라이브러리별 응답 객체를 통해 직접 설정할 수 있다.

```tsx
@Post()
@Header('Cache-Control', 'none')
create(): string {
  return '새로운 고양이를 추가합니다';
}
```

> 힌트: @nestjs/common 패키지에서 Header를 가져와야 한다.
> 

## 리디렉션

특정 URL로 응답을 리디렉션하려면 `@Redirect()` 데코레이터를 사용하거나, 라이브러리별 응답 객체를 통해 직접 설정할 수 있다. `@Redirect()`는 두 개의 인자(`url`, `statusCode`)를 받으며, 둘 다 선택 사항이다. `statusCode`를 생략하면 기본값은 302(Found)이다.

```tsx
@Get()
@Redirect('https://nestjs.com', 301)
redirectToNest(): void {}
```

동적으로 상태 코드나 리디렉션 URL을 결정하려면 `HttpRedirectResponse` 인터페이스를 따르는 객체를 반환할 수 있다.

```tsx
@Get('docs')
@Redirect('https://docs.nestjs.com', 302)
getDocs(@Query('version') version: string) {
  if (version && version === '5') {
    return { url: 'https://docs.nestjs.com/v5/' };
  }
}
```

## 라우트 파라미터

동적 데이터를 요청의 일부로 받을 때는 라우트 파라미터를 사용한다. `@Param()` 데코레이터를 사용하여 파라미터에 접근할 수 있다.

```tsx
@Get(':id')
findOne(@Param('id') id: string): string {
  return `ID #${id}인 고양이를 반환합니다`;
}
```

> 힌트: 파라미터가 있는 라우트는 정적 경로 이후에 선언해야 한다. 이는 파라미터화된 경로가 정적 경로로 향하는 트래픽을 가로채지 않도록 하기 위함이다.
> 

## 서브도메인 라우팅

`@Controller()` 데코레이터의 `host` 옵션을 사용하여 특정 호스트에 대한 요청을 처리할 수 있다.

```tsx
@Controller({ host: 'admin.example.com' })
export class AdminController {
  @Get()
  index(): string {
    return '관리자 페이지';
  }
}
```

호스트 파라미터를 사용하여 동적 값을 캡처할 수도 있다.

```tsx
@Controller({ host: ':account.example.com' })
export class AccountController {
  @Get()
  getInfo(@HostParam('account') account: string): string {
    return account;
  }
}
```

> 경고: Fastify는 중첩된 라우터를 지원하지 않으므로, 서브도메인 라우팅 시 Express 어댑터를 사용하는 것이 좋다.
> 

## 스코프

Nest에서는 거의 모든 것이 들어오는 요청 간에 공유된다. 이는 데이터베이스 연결 풀, 전역 상태를 가진 싱글턴 서비스 등이 포함된다. Node.js는 요청/응답 멀티스레드 무상태 모델을 따르지 않으므로, 싱글턴 인스턴스를 사용하는 것이 안전하다.

요청 기반의 컨트롤러 수명이 필요한 경우, 예를 들어 GraphQL 애플리케이션에서 요청별 캐싱, 요청 추적, 멀티 테넌시 등을 구현할 때 스코프를 제어할 수 있다. 자세한 내용은 스코프 제어를 참조한다.

## 비동기 처리

Nest는 비동기 함수를 지원한다. 비동기 함수는 `Promise`를 반환해야 하며, Nest는 이를 자동으로 처리한다.

```tsx
@Get()
async findAll(): Promise<any[]> {
  return [];
}
```

또한, Nest는 RxJS의 Observable 스트림을 반환할 수도 있다.

```tsx
@Get()
findAll(): Observable<any[]> {
  return of([]);
}
```

두 접근 방식 모두 유효하며, 요구 사항에 맞게 선택할 수 있다.

## 요청 페이로드

POST 라우트 핸들러에서 클라이언트 매개변수를 받기 위해 `@Body()` 데코레이터를 사용한다. DTO(Data Transfer Object) 클래스를 정의하여 데이터의 구조를 명확히 할 수 있다.

```tsx
export class CreateCatDto {
  name: string;
  age: number;
  breed: string;
}
```

`CatsController`에서 DTO를 사용한다.

```tsx
@Post()
async create(@Body() createCatDto: CreateCatDto): string {
  return '새로운 고양이를 추가합니다';
}
```

> 힌트: ValidationPipe를 사용하여 허용된 속성만 받도록 설정할 수 있다. CreateCatDto 예제에서는 name, age, breed 속성만 허용된다.
> 

## 에러 처리

에러 처리는 별도의 챕터에서 다룬다. 예외 필터를 참고한다.

## 전체 리소스 샘플

다양한 데코레이터를 사용하여 기본 컨트롤러를 구현한 예제이다.

```tsx
import { Controller, Get, Query, Post, Body, Put, Param, Delete } from '@nestjs/common';
import { CreateCatDto, UpdateCatDto, ListAllEntities } from './dto';

@Controller('cats')
export class CatsController {
  @Post()
  create(@Body() createCatDto: CreateCatDto): string {
    return '새로운 고양이를 추가합니다';
  }

  @Get()
  findAll(@Query() query: ListAllEntities): string {
    return `모든 고양이를 반환합니다 (제한: ${query.limit}마리)`;
  }

  @Get(':id')
  findOne(@Param('id') id: string): string {
    return `ID #${id}인 고양이를 반환합니다`;
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateCatDto: UpdateCatDto): string {
    return `ID #${id}인 고양이를 업데이트합니다`;
  }

  @Delete(':id')
  remove(@Param('id') id: string): string {
    return `ID #${id}인 고양이를 삭제합니다`;
  }
}
```

> 힌트: Nest CLI는 보일러플레이트 코드를 자동으로 생성하여 개발자 경험을 단순화한다. 자세한 내용은 Nest CLI 문서를 참고한다.
> 

## 시작하기

컨트롤러를 정의한 후, Nest는 해당 컨트롤러를 인식하지 못하므로 모듈에 추가해야 한다. 컨트롤러는 항상 모듈에 속하므로, `@Module()` 데코레이터의 `controllers` 배열에 포함시킨다.

```tsx
import { Module } from '@nestjs/common';
import { CatsController } from './cats/cats.controller';

@Module({
  controllers: [CatsController],
})
export class AppModule {}
```

`@Module()` 데코레이터를 사용하여 모듈 클래스에 메타데이터를 추가하면, Nest는 어떤 컨트롤러를 마운트해야 하는지 알 수 있다.

## 라이브러리별 접근 방식

Nest의 표준 응답 조작 방식 외에도, 라이브러리별 응답 객체를 사용할 수 있다. `@Res()` 데코레이터를 사용하여 특정 응답 객체를 주입받아 직접 조작할 수 있다.

```tsx
import { Controller, Get, Post, Res, HttpStatus } from '@nestjs/common';
import { Response } from 'express';

@Controller('cats')
export class CatsController {
  @Post()
  create(@Res() res: Response): void {
    res.status(HttpStatus.CREATED).send();
  }

  @Get()
  findAll(@Res() res: Response): void {
    res.status(HttpStatus.OK).json([]);
  }
}
```

이 접근 방식은 응답 객체에 대한 완전한 제어를 제공하지만, 몇 가지 단점이 있다:

- 코드가 플랫폼 종속적이 된다.
- 테스트가 어려워진다.
- Nest의 Interceptors 및 데코레이터와의 호환성이 떨어진다.

이를 해결하기 위해 `passthrough` 옵션을 사용할 수 있다.

```tsx
@Get()
findAll(@Res({ passthrough: true }) res: Response): any[] {
  res.status(HttpStatus.OK);
  return [];
}
```

이렇게 하면 응답 객체를 조작하면서도 Nest의 표준 응답 처리를 유지할 수 있다.

## 결론

컨트롤러는 NestJS 애플리케이션에서 핵심적인 역할을 하며, 들어오는 요청을 처리하고 적절한 응답을 반환한다. 데코레이터를 활용하여 라우트를 정의하고, 다양한 HTTP 메서드를 지원하며, 요청 파라미터와 페이로드를 쉽게 처리할 수 있다. 라이브러리별 응답 객체를 사용할 때는 주의가 필요하며, 표준 방식과의 균형을 잘 맞추는 것이 중요하다.

NestJS의 컨트롤러를 이해하고 적절히 활용하면, 효율적이고 유지보수하기 쉬운 백엔드 애플리케이션을 개발할 수 있다.
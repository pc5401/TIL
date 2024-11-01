# 예외 필터 (Exception Filters)
> 공식문서 : https://docs.nestjs.com/exception-filters , chatgpt로 번역

NestJS는 애플리케이션 전반에서 발생하는 모든 처리되지 않은 예외를 처리하는 내장 예외 계층을 제공합니다. 예외 필터는 이러한 예외를 잡아내고, 적절한 사용자 친화적인 응답을 자동으로 전송하는 역할을 합니다. 이 장에서는 예외 필터의 개념, 사용법, 커스텀 예외 필터 작성 방법 등을 다룹니다.

## 예외 필터란?

예외 필터는 애플리케이션의 요청-응답 사이클에서 예외가 발생했을 때 이를 잡아내고 처리하는 역할을 하는 컴포넌트입니다. 예외 필터를 통해 예외 발생 시 로그를 남기거나, 특정 형식의 응답을 클라이언트에 전송할 수 있습니다.

NestJS는 기본적으로 모든 예외를 처리하는 글로벌 예외 필터를 제공하며, 이를 통해 애플리케이션 전반에서 일관된 예외 처리가 가능합니다.

## 기본 글로벌 예외 필터

NestJS는 기본적으로 `HttpException` 및 그 하위 클래스의 예외를 처리하는 글로벌 예외 필터를 제공합니다. 인식되지 않은 예외(즉, `HttpException`이나 그 하위 클래스가 아닌 예외)는 기본 예외 필터에 의해 다음과 같은 JSON 응답으로 처리됩니다:

```json
{
  "statusCode": 500,
  "message": "Internal server error"
}
```

### 힌트

글로벌 예외 필터는 `http-errors` 라이브러리를 부분적으로 지원합니다. 즉, `statusCode`와 `message` 속성을 포함하는 예외는 자동으로 적절한 응답으로 변환됩니다.

## 표준 예외 던지기

NestJS는 `@nestjs/common` 패키지에서 제공하는 `HttpException` 클래스를 사용하여 표준 HTTP 예외를 던질 수 있습니다. 이는 HTTP REST/GraphQL API 기반 애플리케이션에서 일반적인 오류 상황에 대해 표준 HTTP 응답 객체를 전송하는 데 권장됩니다.

### 예제: `HttpException` 사용

```tsx
// src/cats/cats.controller.ts

import { Controller, Get, HttpException, HttpStatus } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  async findAll() {
    throw new HttpException('Forbidden', HttpStatus.FORBIDDEN);
  }
}
```

클라이언트가 이 엔드포인트를 호출하면 다음과 같은 응답을 받게 됩니다:

```json
{
  "statusCode": 403,
  "message": "Forbidden"
}
```

### `HttpException` 생성자 인자

- **response**: JSON 응답 본문을 정의하며, 문자열 또는 객체일 수 있습니다.
- **status**: HTTP 상태 코드를 정의합니다.

### 전체 응답 본문 오버라이드

```tsx
// src/cats/cats.controller.ts

import { Controller, Get, HttpException, HttpStatus } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  async findAll() {
    try {
      await this.service.findAll();
    } catch (error) {
      throw new HttpException({
        status: HttpStatus.FORBIDDEN,
        error: 'This is a custom message',
      }, HttpStatus.FORBIDDEN, {
        cause: error,
      });
    }
  }
}
```

응답 예시:

```json
{
  "status": 403,
  "error": "This is a custom message"
}
```

## 커스텀 예외 만들기

기본 `HttpException` 클래스를 확장하여 커스텀 예외를 만들 수 있습니다. 이를 통해 예외의 재사용성과 코드의 가독성을 높일 수 있습니다.

### 예제: `ForbiddenException` 커스텀 예외

```tsx
// src/cats/exceptions/forbidden.exception.ts

import { HttpException, HttpStatus } from '@nestjs/common';

export class ForbiddenException extends HttpException {
  constructor() {
    super('Forbidden', HttpStatus.FORBIDDEN);
  }
}
```

### 컨트롤러에서 커스텀 예외 사용

```tsx
// src/cats/cats.controller.ts

import { Controller, Get, UseFilters } from '@nestjs/common';
import { ForbiddenException } from './exceptions/forbidden.exception';

@Controller('cats')
export class CatsController {
  @Get()
  async findAll() {
    throw new ForbiddenException();
  }
}
```

## 내장 HTTP 예외

NestJS는 기본적으로 여러 가지 내장 HTTP 예외를 제공합니다. 이들은 `HttpException`을 상속하며, 다양한 HTTP 상태 코드를 나타냅니다. 주요 내장 예외는 다음과 같습니다:

- `BadRequestException`
- `UnauthorizedException`
- `NotFoundException`
- `ForbiddenException`
- `NotAcceptableException`
- `RequestTimeoutException`
- `ConflictException`
- `GoneException`
- `HttpVersionNotSupportedException`
- `PayloadTooLargeException`
- `UnsupportedMediaTypeException`
- `UnprocessableEntityException`
- `InternalServerErrorException`
- `NotImplementedException`
- `ImATeapotException`
- `MethodNotAllowedException`
- `BadGatewayException`
- `ServiceUnavailableException`
- `GatewayTimeoutException`
- `PreconditionFailedException`

### 예제: `BadRequestException` 사용

```tsx
import { Controller, Get, BadRequestException } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  async findAll() {
    throw new BadRequestException('Invalid request data');
  }
}
```

응답 예시:

```json
{
  "statusCode": 400,
  "message": "Invalid request data",
  "error": "Bad Request"
}
```

### 예외에 옵션 추가

예외는 `options` 인자를 통해 `cause` 및 `description`을 추가할 수 있습니다.

```tsx
throw new BadRequestException('Something bad happened', {
  cause: new Error(),
  description: 'Some error description',
})
```

응답 예시:

```json
{
  "message": "Something bad happened",
  "error": "Some error description",
  "statusCode": 400

```

## 예외 필터 구현

기본 예외 필터 외에도, 커스텀 예외 필터를 작성하여 예외 처리 로직을 세부적으로 제어할 수 있습니다. 예외 필터를 통해 로그를 남기거나, 응답 형식을 커스터마이징할 수 있습니다.

### 커스텀 예외 필터 예제

```tsx
// src/common/filters/http-exception.filter.ts

import { ExceptionFilter, Catch, ArgumentsHost, HttpException } from '@nestjs/common';
import { Request, Response } from 'express';

@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();
    const status = exception.getStatus();

    response
      .status(status)
      .json({
        statusCode: status,
        timestamp: new Date().toISOString(),
        path: request.url,
      });
  }
}
```

### 예외 필터 바인딩

### 메서드 스코프

특정 컨트롤러의 메서드에 예외 필터를 적용할 수 있습니다.

```tsx
// src/cats/cats.controller.ts

import { Controller, Post, Body, UseFilters } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';
import { HttpExceptionFilter } from './filters/http-exception.filter';
import { ForbiddenException } from './exceptions/forbidden.exception';

@Controller('cats')
export class CatsController {
  @Post()
  @UseFilters(new HttpExceptionFilter())
  async create(@Body() createCatDto: CreateCatDto) {
    throw new ForbiddenException();
  }
}
```

### 컨트롤러 스코프

컨트롤러 전체에 예외 필터를 적용할 수 있습니다.

```tsx
// src/cats/cats.controller.ts

import { Controller, UseFilters } from '@nestjs/common';
import { HttpExceptionFilter } from './filters/http-exception.filter';

@UseFilters(new HttpExceptionFilter())
@Controller('cats')
export class CatsController {
  // 모든 메서드에 예외 필터 적용
}
```

### 글로벌 스코프

애플리케이션 전체에 예외 필터를 적용할 수 있습니다. 이는 `main.ts` 파일에서 설정할 수 있습니다.

```tsx
// src/main.ts

import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { HttpExceptionFilter } from './common/filters/http-exception.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalFilters(new HttpExceptionFilter());
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap()
```

> 경고: 글로벌 미들웨어는 모든 컨트롤러와 메서드에 적용됩니다. DI 컨테이너 외부에서 인스턴스를 생성할 경우, 의존성 주입이 불가능하므로 함수형 미들웨어를 사용하는 것이 좋습니다. 또는 클래스 미들웨어를 사용하고 forRoutes('*')로 설정하여 글로벌하게 적용할 수 있습니다.
> 

### `APP_FILTER` 토큰을 사용한 글로벌 필터 등록

모듈 내에서 글로벌 예외 필터를 등록할 수도 있습니다.

```tsx
// src/app.module.ts

import { Module } from '@nestjs/common';
import { APP_FILTER } from '@nestjs/core';
import { HttpExceptionFilter } from './common/filters/http-exception.filter';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
  providers: [
    {
      provide: APP_FILTER,
      useClass: HttpExceptionFilter,
    },
  ],
})
export class AppModule {}
```

## 모든 예외 잡기

`@Catch()` 데코레이터의 인자 없이 예외 필터를 정의하면 모든 예외를 잡을 수 있습니다.

### 예제: 모든 예외 잡기

```tsx
// src/common/filters/catch-everything.filter.ts

import {
  ExceptionFilter,
  Catch,
  ArgumentsHost,
  HttpException,
  HttpStatus,
} from '@nestjs/common';
import { HttpAdapterHost } from '@nestjs/core';

@Catch()
export class CatchEverythingFilter implements ExceptionFilter {
  constructor(private readonly httpAdapterHost: HttpAdapterHost) {}

  catch(exception: unknown, host: ArgumentsHost): void {
    const { httpAdapter } = this.httpAdapterHost;

    const ctx = host.switchToHttp();

    const httpStatus =
      exception instanceof HttpException
        ? exception.getStatus()
        : HttpStatus.INTERNAL_SERVER_ERROR;

    const responseBody = {
      statusCode: httpStatus,
      timestamp: new Date().toISOString(),
      path: httpAdapter.getRequestUrl(ctx.getRequest()),
    };

    httpAdapter.reply(ctx.getResponse(), responseBody, httpStatus);
  }
}
```

> 경고: 특정 타입의 예외를 잡는 필터와 모든 예외를 잡는 필터를 결합할 경우, 모든 예외를 잡는 필터가 먼저 선언되어야 특정 필터가 올바르게 작동합니다.
> 

## 상속을 통한 예외 필터 확장

기본 `BaseExceptionFilter`를 상속하여 예외 필터를 확장할 수 있습니다.

### 예제: `AllExceptionsFilter` 상속

```tsx
// src/common/filters/all-exceptions.filter.ts

import { Catch, ArgumentsHost } from '@nestjs/common';
import { BaseExceptionFilter } from '@nestjs/core';

@Catch()
export class AllExceptionsFilter extends BaseExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    super.catch(exception, host);
  }
}
```

### 글로벌 필터로 등록

```tsx
// src/main.ts

import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { AllExceptionsFilter } from './common/filters/all-exceptions.filter';
import { HttpAdapterHost } from '@nestjs/core';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const { httpAdapter } = app.get(HttpAdapterHost);
  app.useGlobalFilters(new AllExceptionsFilter(httpAdapter));
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

또는 `APP_FILTER` 토큰을 사용하여 모듈 내에서 등록할 수 있습니다.

```tsx
// src/app.module.ts

import { Module } from '@nestjs/common';
import { APP_FILTER } from '@nestjs/core';
import { AllExceptionsFilter } from './common/filters/all-exceptions.filter';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
  providers: [
    {
      provide: APP_FILTER,
      useClass: AllExceptionsFilter,
    },
  ],
})
export class AppModule {}
```

## 요약

- **예외 필터의 역할**: 애플리케이션 전반에서 발생하는 예외를 잡아내고, 적절한 응답을 클라이언트에 전송합니다.
- **기본 글로벌 예외 필터**: `HttpException` 및 그 하위 클래스를 처리하며, 인식되지 않은 예외는 기본적으로 500 상태 코드와 메시지를 반환합니다.
- **표준 예외 던지기**: `HttpException` 클래스를 사용하여 표준 HTTP 예외를 던질 수 있습니다. `HttpStatus` 열거형을 활용하여 상태 코드를 지정합니다.
- **커스텀 예외**: `HttpException`을 상속하여 커스텀 예외를 정의할 수 있습니다.
- **커스텀 예외 필터**: `ExceptionFilter` 인터페이스를 구현하거나 `BaseExceptionFilter`를 상속하여 커스텀 예외 필터를 작성할 수 있습니다.
- **예외 필터 바인딩**: 메서드, 컨트롤러, 또는 글로벌 스코프로 예외 필터를 적용할 수 있습니다.
- **모든 예외 잡기**: `@Catch()` 데코레이터를 빈 인자로 사용하여 모든 예외를 잡을 수 있습니다.
- **상속을 통한 필터 확장**: 기본 예외 필터를 상속하여 기능을 확장할 수 있습니다.

예외 필터를 적절히 활용하면 애플리케이션의 예외 처리 로직을 일관되고 효율적으로 관리할 수 있습니다. 커스텀 예외 필터를 작성하여 로그를 남기거나, 클라이언트에 전송되는 오류 응답을 커스터마이징함으로써 보다 견고하고 사용자 친화적인 백엔드 애플리케이션을 구축할 수 있습니다.
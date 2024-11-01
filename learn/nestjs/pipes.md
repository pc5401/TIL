# 파이프 (Pipes)

파이프는 `@Injectable()` 데코레이터로 주석된 클래스이며, `PipeTransform` 인터페이스를 구현한다.

## 파이프의 주요 용도

1. **변환 (Transformation):** 입력 데이터를 원하는 형태로 변환한다. 예를 들어, 문자열을 정수로 변환하는 경우.
2. **검증 (Validation):** 입력 데이터를 평가하여 유효하면 그대로 통과시키고, 유효하지 않으면 예외를 던진다.

파이프는 컨트롤러 라우트 핸들러가 처리하는 인수에 대해 작동한다. Nest는 메서드가 호출되기 직전에 파이프를 개입시키며, 파이프는 메서드에 전달될 인수를 받아 처리한다. 변환 또는 검증 작업은 이 시점에 이루어지며, 그 후에 라우트 핸들러가 호출된다.

## 내장 파이프

Nest는 기본적으로 아홉 가지의 내장 파이프를 제공한다. 이들은 `@nestjs/common` 패키지에서 내보낸다.

- `ValidationPipe`
- `ParseIntPipe`
- `ParseFloatPipe`
- `ParseBoolPipe`
- `ParseArrayPipe`
- `ParseUUIDPipe`
- `ParseEnumPipe`
- `DefaultValuePipe`
- `ParseFilePipe`

### `ParseIntPipe` 사용 예

`ParseIntPipe`는 문자열을 정수로 변환하는 변환 용도의 파이프이다. 변환에 실패하면 예외를 던진다.

```tsx
@Get(':id')
async findOne(@Param('id', ParseIntPipe) id: number) {
  return this.catsService.findOne(id);
}
```

위 예제에서 `GET /cats/abc` 요청 시 다음과 같은 예외가 발생한다.

```json
{
  "statusCode": 400,
  "message": "Validation failed (numeric string is expected)",
  "error": "Bad Request"
}
```

## 파이프 바인딩

파이프를 사용하려면 파이프 클래스의 인스턴스를 적절한 컨텍스트에 바인딩해야 한다. 메서드 파라미터 수준에서 파이프를 바인딩하는 예는 다음과 같다.

```tsx
@Get(':id')
async findOne(@Param('id', ParseIntPipe) id: number) {
  return this.catsService.findOne(id);
}
```

옵션을 전달하여 내장 파이프의 동작을 커스터마이징할 수도 있다.

```tsx
@Get(':id')
async findOne(
  @Param('id', new ParseIntPipe({ errorHttpStatusCode: HttpStatus.NOT_ACCEPTABLE }))
  id: number,
) {
  return this.catsService.findOne(id);
}
```

쿼리 파라미터에도 파이프를 바인딩할 수 있다.

```tsx
@Get()
async findOne(@Query('id', ParseIntPipe) id: number) {
  return this.catsService.findOne(id);
}
```

### `ParseUUIDPipe` 사용 예

```tsx
@Get(':uuid')
async findOne(@Param('uuid', new ParseUUIDPipe()) uuid: string) {
  return this.catsService.findOne(uuid);
}
```

## 커스텀 파이프

Nest는 자체적인 커스텀 파이프를 작성할 수 있게 한다. 예를 들어, 간단한 검증 파이프를 작성해보자.

### 간단한 `ValidationPipe` 예제

```tsx
import { PipeTransform, Injectable, ArgumentMetadata } from '@nestjs/common';

@Injectable()
export class ValidationPipe implements PipeTransform {
  transform(value: any, metadata: ArgumentMetadata) {
    return value;
  }
}
```

### 스키마 기반 검증

Zod 라이브러리를 사용하여 스키마 기반 검증을 구현할 수 있다.

```tsx
import { PipeTransform, ArgumentMetadata, BadRequestException } from '@nestjs/common';
import { ZodSchema } from 'zod';

export class ZodValidationPipe implements PipeTransform {
  constructor(private schema: ZodSchema) {}

  transform(value: unknown, metadata: ArgumentMetadata) {
    try {
      const parsedValue = this.schema.parse(value);
      return parsedValue;
    } catch (error) {
      throw new BadRequestException('Validation failed');
    }
  }
}
```

### `@UsePipes()` 데코레이터로 파이프 바인딩

```tsx
@Post()
@UsePipes(new ZodValidationPipe(createCatSchema))
async create(@Body() createCatDto: CreateCatDto) {
  this.catsService.create(createCatDto);
}
```

### 클래스 기반 검증 (`class-validator`)

`class-validator`와 `class-transformer` 라이브러리를 사용하여 데코레이터 기반 검증을 구현할 수 있다.

```tsx
import { IsString, IsInt } from 'class-validator';

export class CreateCatDto {
  @IsString()
  name: string;

  @IsInt()
  age: number;

  @IsString()
  breed: string;

```

```tsx
import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common';
import { validate } from 'class-validator';
import { plainToInstance } from 'class-transformer';

@Injectable()
export class ValidationPipe implements PipeTransform<any> {
  async transform(value: any, { metatype }: ArgumentMetadata) {
    if (!metatype || !this.toValidate(metatype)) {
      return value;
    }
    const object = plainToInstance(metatype, value);
    const errors = await validate(object);
    if (errors.length > 0) {
      throw new BadRequestException('Validation failed');
    }
    return value;
  }

  private toValidate(metatype: Function): boolean {
    const types: Function[] = [String, Boolean, Number, Array, Object];
    return !types.includes(metatype);
  }
}
```

### 글로벌 파이프 설정

글로벌 파이프를 설정하여 애플리케이션 전체에 적용할 수 있다.

```tsx
// main.ts
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(new ValidationPipe());
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

또는 모듈 내에서 설정할 수도 있다.

```tsx
// app.module.ts
import { Module } from '@nestjs/common';
import { APP_PIPE } from '@nestjs/core';

@Module({
  providers: [
    {
      provide: APP_PIPE,
      useClass: ValidationPipe,
    },
  ],
})
export class AppModule {}
```

## 변환 용도의 파이프

파이프는 입력 데이터를 원하는 형식으로 변환할 수 있다. 예를 들어, 문자열을 정수로 변환하거나 기본 값을 제공하는 경우가 있다.

### 커스텀 `ParseIntPipe` 예제

```tsx
import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common';

@Injectable()
export class ParseIntPipe implements PipeTransform<string, number> {
  transform(value: string, metadata: ArgumentMetadata): number {
    const val = parseInt(value, 10);
    if (isNaN(val)) {
      throw new BadRequestException('Validation failed');
    }
    return val;
  }
}
```

```tsx
@Get(':id')
async findOne(@Param('id', new ParseIntPipe()) id: number) {
  return this.catsService.findOne(id);
}
```

### 기본 값 제공

`DefaultValuePipe`를 사용하여 파라미터에 기본 값을 제공할 수 있다.

```tsx
@Get()
async findAll(
  @Query('activeOnly', new DefaultValuePipe(false), ParseBoolPipe) activeOnly: boolean,
  @Query('page', new DefaultValuePipe(0), ParseIntPipe) page: number,
) {
  return this.catsService.findAll({ activeOnly, page });
}
```

## 결론

파이프는 NestJS에서 입력 데이터를 변환하고 검증하는 데 중요한 역할을 한다. 내장 파이프를 활용하거나 커스텀 파이프를 작성하여 애플리케이션의 요구 사항에 맞게 데이터를 처리할 수 있다. 글로벌 파이프 설정을 통해 애플리케이션 전반에 일관된 데이터 처리를 적용할 수 있으며, 파이프를 적절히 활용하면 코드의 가독성과 유지보수성이 향상된다.
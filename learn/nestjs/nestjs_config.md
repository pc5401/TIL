## 1. 개요

Express나 다른 Node 개발할 때, 환경변수를 `dotenv`로 관리했지만, NestJS에서는 `@nestjs/config` 모듈을 활용하는 것이 권장된다. `.env` 파일을 사용하는 것은 동일해서 어렵지 않다.

---

## 2. 왜 `@nestjs/config`를 사용할까?

NestJS는 자체적인 환경변수 관리 솔루션인 `@nestjs/config` 모듈을 제공한다. 이는 NestJS의 모듈 시스템과 통합되어 더 편리하고 구조적인 환경변수 관리를 가능하게 한다.

**주요 이유:**

- **통합성:** NestJS의 모듈 시스템과 자연스럽게 통합된다.
- **유효성 검사:** 환경 변수의 유효성을 검사할 수 있는 기능을 제공한다.
- **유연성:** 다양한 환경별 `.env` 파일을 손쉽게 관리할 수 있다.
- **전역 사용:** `isGlobal` 옵션을 통해 애플리케이션 전체에서 `ConfigService`를 쉽게 사용할 수 있다.

## 3. 설정 방법

환경별로 `.env` 파일을 분리하여 관리하고, `@nestjs/config` 모듈을 설정하는 방법을 설명한다. 우리의 환경은 `dev`와 `local`로 구분하였으며, 프로덕션 환경은 클라우드 설정을 통해 관리한다.

### 예시. `.env` 파일 구성

프로젝트 루트 디렉토리에 여러 환경별 `.env` 파일을 생성한다.

- `.dev.env`
    
    ```makefile
    # 서버 설정
    PORT=3000
    
    # 데이터베이스 설정
    DB_HOST=dev-db.example.com
    DB_PORT=3306
    DB_USERNAME=dev_user
    DB_PASSWORD=dev_password
    DB_DATABASE=dev_db
    
    # OAuth 설정
    GITHUB_CLIENT_ID=your_github_client_id
    GITHUB_CLIENT_SECRET=your_github_client_secret
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    NAVER_CLIENT_ID=your_naver_client_id
    NAVER_CLIENT_SECRET=your_naver_client_secret
    
    ```
    
- `.local.env`
    
    ```makefile
    # 서버 설정
    PORT=3000
    
    # 데이터베이스 설정
    DB_HOST=localhost
    DB_PORT=3306
    DB_USERNAME=local_user
    DB_PASSWORD=local_password
    DB_DATABASE=local_db
    
    # OAuth 설정
    GITHUB_CLIENT_ID=your_github_client_id
    GITHUB_CLIENT_SECRET=your_github_client_secret
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    NAVER_CLIENT_ID=your_naver_client_id
    NAVER_CLIENT_SECRET=your_naver_client_secret
    
    ```
    
- `.env` (기본 환경, 프로덕션에서는 별도로 관리)
    
    ```makefile
    # 서버 설정
    PORT=3000
    
    # 데이터베이스 설정
    DB_HOST=prod-db.example.com
    DB_PORT=3306
    DB_USERNAME=prod_user
    DB_PASSWORD=prod_password
    DB_DATABASE=prod_db
    
    # OAuth 설정
    GITHUB_CLIENT_ID=your_github_client_id
    GITHUB_CLIENT_SECRET=your_github_client_secret
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    NAVER_CLIENT_ID=your_naver_client_id
    NAVER_CLIENT_SECRET=your_naver_client_secret
    ```
    

개발환경이 여러 가지인 경우 이를 동적으로 관리할 수 있다.

다양한 환경에서 `NODE_ENV`를 설정하기 위해 `cross-env` 모듈을 사용한다고 하는데, `cross-env`는 아직 설치하지 않았다.

## 4. 사용 방법

환경 변수를 사용하는 방법에는 여러 가지가 있다. 기본적으로 `process.env`를 직접 사용하는 방법과 `ConfigService`를 사용하는 방법이 있다.

### 4.1. `ConfigService` 사용하기 (권장)

NestJS의 `ConfigService`를 사용하면, 타입 안전성과 유효성 검사를 활용할 수 있어 더욱 안전하게 환경 변수를 관리할 수 있다.

**서비스에서 `ConfigService` 사용 예시:**

```tsx
// users.service.ts
import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class UsersService {
  constructor(private readonly configService: ConfigService) {}

  private readonly gatewayDomain: string = this.configService.get<string>('GATEWAY_DOMAIN', 'localhost');

  // 나머지 서비스 로직
}
```

**주요 포인트:**

- `ConfigService`를 주입하여 사용.
- `get<T>(key: string, defaultValue?: T)` 메서드를 통해 환경 변수 값을 가져옴.
- 두 번째 인자로 기본값을 설정할 수 있어, 환경 변수가 정의되지 않았을 때 기본값을 사용할 수 있다.

### 4.2. `process.env` 직접 사용하기

필요에 따라 `process.env`를 직접 사용할 수도 있다. 하지만 이 방법은 타입 안전성이 없고, 환경 변수의 유효성을 보장하기 어려워 권장되지 않는다.

```tsx
const port = process.env.PORT || 3000;
```

### 4.3. `isGlobal` 설정의 장점

`ConfigModule`을 전역으로 설정(`isGlobal: true`)하면, 애플리케이션의 모든 모듈에서 별도의 설정 없이 `ConfigService`를 사용할 수 있다. 이는 코드의 중복을 줄이고, 환경 변수 접근을 일관성 있게 유지하는 데 도움이 된다.

## 5. 유효성 검사하기 (추가)

환경 변수가 올바르게 설정되었는지 확인하는 것은 중요하다. 잘못된 환경 변수 값은 애플리케이션의 예기치 않은 동작을 초래할 수 있다. NestJS에서는 `class-validator`와 `class-transformer`를 활용하여 환경 변수의 유효성을 검사할 수 있다.

### 5.1. 유효성 검사 설정

**`env.validation.ts` 작성:**

```tsx
// src/util/validate/env.validation.ts
import { plainToClass } from 'class-transformer';
import { IsEnum, IsNumber, IsString, validateSync } from 'class-validator';

enum Environment {
  Local = 'local',
  Dev = 'dev',
  Prod = 'prod',
}

class EnvironmentVariables {
  @IsEnum(Environment)
  NODE_ENV: Environment;

  @IsNumber()
  PORT: number;

  @IsString()
  DB_HOST: string;

  @IsNumber()
  DB_PORT: number;

  @IsString()
  DB_USERNAME: string;

  @IsString()
  DB_PASSWORD: string;

  @IsString()
  DB_DATABASE: string;

  // 추가적인 환경 변수들...
}

export function validate(config: Record<string, unknown>) {
  const validatedConfig = plainToClass(EnvironmentVariables, config, { enableImplicitConversion: true });
  const errors = validateSync(validatedConfig, { skipMissingProperties: false });

  if (errors.length > 0) {
    throw new Error(errors.toString());
  }
  return validatedConfig;
}
```

### 5.2. `ConfigModule`에 유효성 검사 통합

`app.module.ts` 파일을 수정하여 유효성 검사 함수를 `ConfigModule`에 통합한다.

```tsx
// app.module.ts
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { CategoriesModule } from './categories/categories.module';
import { StreamingModule } from './streaming/streaming.module';
import { VideosModule } from './videos/videos.module';
import { validate } from './util/validate/env.validation';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: `.${process.env.NODE_ENV}.env`,
      validate, // 유효성 검사 함수 추가
    }),
    AuthModule,
    UsersModule,
    CategoriesModule,
    StreamingModule,
    VideosModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

**주요 포인트:**

- `validate` 함수를 `ConfigModule.forRoot`에 추가하여 애플리케이션 시작 시 환경 변수의 유효성을 검사.
- 유효성 검사에 실패하면 애플리케이션이 시작되지 않고 에러를 던진다.

### 5.3. 필수 패키지 설치

유효성 검사를 위해 `class-validator`와 `class-transformer` 패키지를 설치해야 한다.

```bash
npm install class-validator class-transformer
```
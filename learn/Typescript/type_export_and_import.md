# 타입스크립트의 타입 import, export 하기

## import, export

### 타입 변수의 외부 사용: `import`와 `export`

TypeScript에서는 작성한 타입 변수나 함수를 다른 파일에서 사용하기 위해 JavaScript의 `import`와 `export` 문법을 그대로 사용할 수 있다. `import`와 `export` 문법을 처음 접하는 경우 간략하게 설명하겠다.

### 기본 `import`와 `export` 사용법

다른 파일에서 정의한 변수나 함수를 사용하려면 `export`와 `import`를 사용한다. 예를 들어, `constants.ts` 파일에서 변수를 내보내고 `app.ts` 파일에서 이를 가져와 사용하는 경우는 다음과 같다.

```tsx
// constants.ts
export const APP_NAME = 'TypeScriptApp';
export const VERSION = '1.0.0';
```

```tsx
// app.ts
import { APP_NAME, VERSION } from './constants';

console.log(`Welcome to ${APP_NAME} v${VERSION}`)
```

1. **내보내기 (`export`)**: 변수를 다른 파일에서 사용할 수 있도록 내보내려면 변수나 함수 정의 앞에 `export` 키워드를 붙인다.
2. **가져오기 (`import`)**: 내보낸 변수를 사용하려면 `import { 변수명 } from '파일경로'` 형식으로 가져온다. 파일 경로는 현재 디렉토리를 기준으로 `./`부터 시작하며, `.ts` 확장자는 생략한다.

```tsx
import * as Constants from './constants';
console.log(Constants.APP_NAME);
console.log(Constants.VERSION);
```

변수명을 일일이 쓰기 귀찮을 경우 `import * as` 문법을 사용하여 해당 파일의 모든 `export`된 변수를 한 번에 가져올 수 있다. 이는 네임스페이스와 유사하게 동작하여 변수명 중복 문제를 방지할 수 있다.

**참고**: `export default` 문법도 존재하지만, 이는 별도의 설명이 필요하므로 나중에 참고하도록 한다.

### 타입의 `import`와 `export`

타입도 `export`와 `import`를 동일하게 사용할 수 있다. 예를 들어, 타입을 다른 파일에서 사용하려면 다음과 같이 작성한다.

```tsx
// types.ts
export type UserRole = 'admin' | 'user' | 'guest';
export interface UserProfile {
  username: string;
  age: number;
  role: UserRole;
}
```

```tsx
// main.ts
import { UserRole, UserProfile } from './types';

let currentUserRole: UserRole = 'admin';
let user: UserProfile = {
  username: 'johndoe',
  age: 28,
  role: 'admin',
};
```

타입도 변수와 마찬가지로 `export` 키워드를 사용하여 내보내고, `import` 키워드를 사용하여 가져올 수 있다.

### 로컬 타입 생성

다른 파일에서 사용하지 않고, 해당 파일 내에서만 사용하고 싶은 타입은 `export` 키워드를 붙이지 않으면 된다. 이렇게 하면 해당 타입은 해당 파일 내에서만 접근 가능하다.

```tsx
// internalTypes.ts
type InternalID = string | number;

const generateID = (): InternalID => {
  return Math.random() > 0.5 ? 'ID_' + Math.floor(Math.random() * 1000) : Math.floor(Math.random() * 1000);
};

const id = generateID();
console.log(id
```

외부 파일에서는 `InternalID` 타입을 사용할 수 없다.

### 네임스페이스 (`namespace`) 사용

TypeScript 1.5 버전 이하에서는 `import`와 `export` 문법이 없었기 때문에 네임스페이스(`namespace`)를 사용하여 타입을 분리하였다. 네임스페이스를 사용하면 변수명 중복 문제를 효과적으로 방지할 수 있다.

```tsx
// models.ts
namespace Models {
  export interface Person {
    firstName: string;
    lastName: string;
    age: number;
  }

  export type ID = string | number;
}
```

```tsx
// app.ts
/// <reference path="./models.ts" />

const person: Models.Person = {
  firstName: 'Jane',
  lastName: 'Doe',
  age: 25,
};

const personID: Models.ID = 'JD123';

console.log(person);
console.log(personID);
```

네임스페이스를 사용하면 `Models.Person`과 같이 네임스페이스명을 접두사로 붙여 타입을 사용할 수 있다. 이는 변수명 중복을 방지하고, 코드의 가독성을 높이는 데 도움이 된다.

**참고**: ES6 이후 `import`와 `export` 문법이 도입되면서 네임스페이스의 사용 빈도는 줄었지만, 여전히 특정 상황에서는 유용하게 사용될 수 있다.

### 과거의 `module` 키워드

옛날에는 `namespace` 대신 `module` 키워드를 사용하였으나, 현재는 `namespace`가 표준으로 자리잡았다. 이를 참고하여 네임스페이스를 사용할 때 혼동하지 않도록 한다.
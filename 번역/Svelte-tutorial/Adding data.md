# 1. Introduction / b. Adding data

일부 정적 마크업을 단순히 렌더링하는 컴포넌트는 그다지 흥미롭지 않습니다. 데이터를 한번 넣어봅시다.

우선, 컴포넌트에 스크립트 태그를 넣고 `name` 변수를 선언합니다:

```html
<script>
  let name = 'world';
</script>

<h1>Hello world!</h1>
```

이제 우리는 `name`을 마크업에서 참조할 수 있습니다.  

```html
<h1>Hello {name}!</h1>
```

중괄호 안에서, 우리는 우리가 원하는 JavaScript를 모두 넣을 수 있습니다. 더 큰 인사말을 위해 name.toUpperCase()로 이름을 변경해 보세요.

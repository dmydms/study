# 1. Introduction / c. Dynamic attributes

글자들을 조정하기 위해서 단순히 중괄호를 쓸 수 있는 것 처럼, 구성 요소의 attributes를 관리하기 위해서 역시 중괄호를 사용할 수 있습니다. 

우리의 이미지는 src가 없습니다. - 한번 넣어봅시다:  

``` html
<img src={src}>
```

더 낫군요. 하지만 Svelte는 warning을 줍니다:  
`A11y: <img> element should have an alt attribute`

웹 앱들을 만들 때, 예를들어 시력이나 운동장애가 있거나, 좋은 하드웨어나 원활한 인터넷이 없는 사람들을 포함하여 여러가지 가능성이 있는 사용자들이 접근할 수 있게 만드는 것이 가장 중요하다. 접근성(줄여서 a11y)을 똑바로 얻기가 항상 쉽지만은 않지만, Svelte는 만약 당신이 접근성이 떨어지는 마크업을 작성한다면, 당신에게 경고를 줌으로써 도움을 줄 것이다.

이 경우에(주어진 예제 코드), 스크린 리더기를 사용하는 사람들 또는 느리거나 연결이 잘 안되는 인터넷을 가진 사람들을 위해 이미지를 설명하는 `alt` 속성이 누락되었습니다.  

```html
<img src={src} alt="A man dances.">
```

우리는 속성들 안에 중괄호를 사용할 수 있습니다. "{name} dances."로 바꿔보세요 - `<script>` 블록에 name 변수를 선언하는 것을 잊지마세요.  

## Shorthand attributes

src={src} 처럼 name과 value가 같은 속성은 흔합니다. Svelte는 이러한 경우에 편리한 shorthand를 제공할 것 입니다:  

```html
<img {src} alt="A man dances.">
```

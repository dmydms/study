<!-- 1. Introduction / d. Styling -->
HTML에서 처럼, `<style>` 태그를 당신의 컴포넌트에 추가할 수 있습니다. `<p>` 태그에 몇몇 스타일들을 추가해봅시다. 

``` html
<p>This is a paragraph.</p>

<style>
  p {
    color: purple;
    font-family: 'Comic Sans MS', cursive;
    font-size: 2em;
  }
</style>
```

중요한 점은, 이러한 규칙들은 컴포넌트 범위로 동작합니다. 다음 단계에서 볼 내용들 때문에, 앱 모든 곳에 있는 `<p>` 엘리먼트의 스타일을 갑자기 바꿀 수 없을 것 입니다.  

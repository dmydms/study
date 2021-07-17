# Svelte vs React

- 컴포넌트 작성이 매우 편리하고, 작성해야하는 코드의 양이 현저히 적음.
  - React는 컴포넌트를 만들기 위해서 hook method, class 에 대한 이해가 필요하고 컴포넌트를 생성할 때마다 반복적으로 작성해줘야하는 코드가 꽤 있는데 svelte는 매우 적음.
- 공식 문서, 튜토리얼 등이 쉽고 직관적임
  - 컴포넌트 작성 규칙도 Vanila js 를 사용하던 사람이면 금방 익힐 수 있는 수준.
  - 문서, 튜토리얼 등이 React에 비해서 쉬움. 
  - life cycle도 react에 비해서 익히기 가벼운 느낌..? 

- html/css/vanila js 에 가까운 코드를 작성할 수 있음
  - cf. React에 너무 익숙해지면, 온전한 Javascript를 알기에는 살짝 멀어지는 느낌.
- 상태관리 하는 코드가 매우 간결하고 불필요한 hook method를 사용하지 않을 수 있음
  - React - const [count, setCount] = useState(0)
  - Svelte - const count = 0 (`reactive declaration` ($)을 사용하면 리액트랑 비교도 안되게 간결하게 코드를 작성할 수 있는 듯)
- Top-level element가 한개일 필요가 없음
  - React에서는 컴포넌트마다 한개의 태그(<>, \<div\> .. )가 여러개의 태그를 감싸줘야하는 규칙이 있지만, svelte는 그렇지 않음

- virtual DOM 이 없음
  - 명확하게 뭐가 좋은지 크게 와닿진 않지만, React의 경우 virtual DOM이 있어서 virtual DOM 자체를 알아야한다는 것 자체도 짐처럼 느껴짐
  - 그리고 virtual DOM을 사용해서 장점이 뚜렷하게 느껴진다거나, 서칭을 했을 때 당장 알아들을 수 있을만큼 와닿는 장점을 잘 모르겠음 
  - cf. 
    " Virtual DOM이 있는 이유는 React나 Vue가 겉보기에는 reactive 하지만 내부 구현은 reactive하지 않아서, 상태가 바뀌면 매번 전체를 다시 평가해야 하기 때문(Svelte를 개발한 R. Harris의 [Rethinking Reactivity](https://www.youtube.com/watch?v=gJ2P6hGwcgo) 강연 참고). 이 과정의 비효율을 최소화하기 위해서 실제 DOM이 아닌 Virtual DOM에서 연산을 하고, 연산이 끝나면 DOM을 한 번에 갱신하는 방식으로 실행됨. 그런데 Svelte는 실제로 reactive하게 작동하기 때문에 이런 과정이 필요하지 않음. Virtual DOM이 없기 때문에 속도가 빠르고 메모리 사용량이 적고 (관련 코드도 없기 때문에) 네트워크로 전송되는 코드의 양도 줄어든다는 장점이 있음. 그런데 세 가지 장점 모두 현재 프로젝트에서는 크게 중요치 않아 보임. "
<br/>
<br/>

**Q. props thrilling?** 
리액트를 사용할 때, 여러개의 컴포넌트에 걸쳐서 데이터를 내리는 상황이 왔을 때 어떻게 하는지? 

"부모-자식 관계에서 여러 데이터를 주고 받을 일이 많다면 Context API, 부모-자식 관계와 관련 없이 데이터를 주고 받아야 한다면 Store API 사용하기. Context API는 되도록 최소한으로 쓰는 게 좋은 것 같음."
<br/>
<br/>

**Q, Type Script와 같은 타입 체크 도구를 어떻게 쓰는지?** 
도입이 어렵다는 이야기를 보았음

"작년까지 좀 어려움이 있었으나, 2020년 7월 이후([Svelte <3 TypeScript](https://svelte.dev/blog/svelte-and-typescript))에 많이 좋아짐." 
<br/>
<br/>

**Q. 와닿을 만한 단점이 있었는지?** 
"vscode + svelte + eslint + prettier + typescript 조합에서 문제가 안 생기게 하는데 어려움을 겪었음. 하지만 조합을 잘 찾아서 괜찮음"




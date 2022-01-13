# onMount
- 모든 컴포넌트의 lifecycle은 컴포넌트가 생성될 때 시작되고, 컴포넌트가 소멸할 때 끝남.
- `onMount`는 컴포넌트가 DOM에 처음 렌더링 된 후에 실행. 
- SSR 때문에, `fetch`를 `<script>`의 최상위에 두는 것이 아니라 `onMount` 안에 둘 것을 추천.

- `onDestroy`를 제외하고, lifecycle 함수들은 SSR 동안은 실행되지 않음. 이것은 DOM에 마운트된 후 지연 로드되어야 하는 데이터를 가져오기를 피할 수 있음.

- [lifecycle 함수들은 콜백 함수가 컴포넌트 객체에 바인드 하기 위해서 컴포넌트가 초기화되는 동안 호출되어야한다.](#q1)

- 만약 `onMount` 콜백 함수가 함수를 리턴한다면, 해당 함수는 컴포넌트가 소멸할 때 호출될 것이다. 

## 질문 <a id="q1"></a>
- Lifecycle functions must be called while the component is initialising so that the callback is bound to the component instance — not (say) in a setTimeout.
  - 해석 및 전달하고자 하는 의미를 정확하게 모르겠음.
  - 해석: lifecycle 함수들은 콜백 함수가 컴포넌트 객체에 바인드 하기 위해서 컴포넌트가 초기화되는 동안 호출되어야한다.
# 1. Introduction / a. Basics

## 소개

Svelte 튜토리얼에 오신걸 환영합니다. 이 튜토리얼은 당신이 빠르고, 작은 웹 애플리케이션을 쉽게 만들기 위해서 알아야하는 모든것을 가르쳐 줄 것입니다.  

당신은 또한 [API docs](https://svelte.dev/docs)와 [예제](https://svelte.dev/examples#hello-world)들을 참고할 수 있습니다. 또는, 당신의 로컬 컴퓨터에서 직접 조작을 하는 것에 실증을 느낀다면, 60초만에 빠르게 [시작하는 방법](https://svelte.dev/blog/the-easiest-way-to-get-started)도 있습니다.  

## Svelte란 무엇인가요?

Svelte는 웹 애플리케이션들을 빠르게 빌드해주는 도구입니다.  

이는 React와 Vue같은 자바스크립트의 프레임워크들과 비슷하며, 매끄럽고 상호작용하는(interactive) 사용자 인터페이스 구축을 쉽게 하기 위한 목표를 공유합니다.  

그러나 중요한 다른점이 있습니다: Svelte는 실행 시간(run time)에 애플리케이션 코드를 해석하는 것이 아니라, 빌드 시간(build time)에 이상적인 JavaScript로 변환합니다. 이것의 의미는 당신은 프레임워크의 추상화의 성능 비용을 지불할 필요가 없다는 말이며, 또한 당신의 앱이 처음 로드될 때 패널티를 받을 필요도 없다는 것을 의미합니다.  

Svelte로 당신의 전체 앱을 빌드할 수 있고 또한 이미 존재하는 코드베이스에 Svelte를 점진적으로 추가할 수도 있습니다. 또한 기존 프레임워크에서 종속성 오버헤드(overhead of a dependency) 없이 작업 어디로든지 독립형 패키지로서 컴포넌트를 이동시킬 수 있습니다.  

## 튜토리얼 사용법

Svelte를 이해하기 위해서 HTML, CSS 그리고 JavaScript에 대한 기본 지식이 필요합니다.

튜토리얼을 진행하다 보면, 새로운 기능을 설명하기 위해서 설계된 작은 예제를 발견하게 될 것 입니다. 이후 챕터는 이전 챕터의 지식을 바탕으로 만들어지며, 그래서 처음부터 끝까지 진행할 것을 추천합니다. 만약 필요하다면, 상단 드롭다운을 통해서 이동할 수 있습니다. ('Introduction / Basics' 를 클릭하세요.)

각각의 튜토리얼 챕터에는 지시 사항에 어려움을 겪을 때 클릭할 수 있는 '보여주세요' 버튼이 있습니다. 너무 의존하지는 마세요; 어디에 제시된 코드블럭을 두어야 할 지 이해함으로써, 그리고 직접 에디터에 코드블럭을 타이핑 해보면서 빠르게 배울 수 있을겁니다.

## 컴포넌트 이해

Svelte에서는, 애플리케이션이 하나 또는 하나 이상의 컴포넌트로 구성됩니다. In Svelte, an application is composed from one or more components. A component is a reusable self-contained block of code that encapsulates HTML, CSS and JavaScript that belong together, written into a `.svelte` file.(해석 다시하기. 이해 못함.) 코드 에디터에서 'hello world' 예시는 간단한 컴포넌트입니다.  

# [Webpack](https://webpack.js.org/concepts/modules/)

## Modules
출처, https://webpack.js.org/concepts/modules/
modular programming(프로그램의 기능을 독립적으로 분리하는 것을 강조하는 소프트웨어 설계 기법) 에서, 개발자들은 프로그램을 모듈이라고 불리는 기능의 discrete chunk로 쪼갭니다. 

각각의 모듈은 인증, 디버깅 그리고 사소한 테스팅을 만드는 전체 프로그램보다 작은 표면적을 가지고 있습니다. 잘 써여진 모듈들은 견고한 추상화와 캡슐화 경계를 제공하고, 그럼으로 인해서 각 모듈은 전체 application에 걸쳐서 일관된 디자인과 명확한 목적을 가집니다. 

Node.js는 처음부터 대부분 modular programming을 지원했습니다. 그러나 웹에서는 모듈들에 대한 지원이 더디게 진행되었습니다. 다양한 이점들과 제한들이있는 웹에 modular Javascript를 지원하는 다양한 도구들이 존재합니다. webpack은 이러한 시스템으로부터 학습된 교훈들을 기반으로 하고, 당신의 프로젝트의 모든 파일에 모듈의 개념을 적용합니다.


## [What is a webpack Module?](https://webpack.js.org/concepts/modules/#what-is-a-webpack-module) 

Node.js 모듈들과 대조되게, webpack 모듈들은 다양한 방법으로 그들의 의존성(dependencies)을 표현할 수 있습니다. 예: 

- ES2015 `import` 문
- CommonJS `require()` 문
- AMD `define` and `require` 문
- css/sass/less 파일 내부 `@import`문
- stylesheet url(...) 또는 HTML <img src=...> 파일 내부 이미지 url


## [Supported Module Types](https://webpack.js.org/concepts/modules/#supported-module-types)
webpack는 다음 모듈 타입들을 기본적으로 지원합니다: 

- ECMAScript modules
- CommonJS modules
- AMD modules
- Assets
- WebAssembly modules

게다가 웹팩은 다양한 언어와 로더(loader)를 통한 여러 전처리기로 작성된 모듈들을 지원합니다. 로더는 non-native 모듈들을 어떻게 처리하는지를 webpack에게 알려주고, 이러한 의존성들을 당신의 번들에 포함합니다.
webpack 커뮤니티는 널리 사용되는 다양한 언어와 언어 전처리기용 로더를 구축했습니다: 

- CoffeeScript
- TypeScript
- ESNext (Babel)
- Sass
- Less
- Stylus
- Elm

그리고 다른 것들도 많이 있습니다! 전반적으로 webpack는 사용자 정의(customization)에 대해서 강력하고 풍부한 API를 제공하며, 당신의 개발, 테스팅 그리고 production workflows에 대해서 아무런 의견 없이 모든 스택에 대해서 webpack을 사용할 수 있게합니다.

전체 리스트를 보고싶다면 [로더 리스트](https://webpack.js.org/loaders/)를 보거나 [직접 작성하세요.](https://webpack.js.org/api/loaders/) 



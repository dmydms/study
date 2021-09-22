# todo:
# - [ ] input, sys.stdin.read, sys.stdin.readline 차이점
# - [ ] * (asterisk)가 무엇인가?

import sys
_, *m = map(int, sys.stdin.read().split())
print(min(m), max(m))
import sys
n, *rest = map(int, sys.stdin.buffer.read().split()) # 첫 숫자는 n, 나머지는 rest 리스트에 담기
if n == 0:
    print(0)
    raise SystemExit
b = rest[:n]

k = ((n * 15 + 50) // 100)  # 0~50% 사이 정수 반올림
j = n - 2*k                 # 50~100% 사이 정수 반올림


b = sorted(b)
b = b[k:n-k]            # 슬라이싱 기법

res = sum(b) / j

if (res - int(res))*10 >= 5:
    res = res + 1

print(int(res))

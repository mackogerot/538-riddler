fibonacci_list = []
target_num = 216

def fib(n,j,k):
    if n == 1:
        return [j]
    if n == 2:
        return [j, k]
    fibseq = [j, k]
    for _ in range(2, n):
        fibseq.append(fibseq[-1] + fibseq[-2])
    return fibseq

for j in range(round(target_num/2)):
  for k in range(round(target_num/2)):
    if j>k:
      continue
    else:
      fib_temp = fib(15,j,k)
      if target_num in fib_temp:
        fibonacci_list.append(fib_temp)
      else:
        continue

best_combination = (0,0,0)
for item in fibonacci_list:
  fib_tuple = (item[0],item[1],item.index(target_num)+1)
  if fib_tuple[2]>best_combination[2]:
    best_combination = fib_tuple

print(best_combination)

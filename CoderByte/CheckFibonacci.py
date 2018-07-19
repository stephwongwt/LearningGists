def foo(num): 
  a, b = 1, 1
  while b < num:
    a, b = b, a + b
  return b == num

print foo(13)

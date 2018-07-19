#CoderByte Challenge. Quick function to check if num is in the Fibonacci.

def foo(num): 
  a, b = 1, 1
  while b < num:
    a, b = b, a + b
  return b == num

print foo(13)

# We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

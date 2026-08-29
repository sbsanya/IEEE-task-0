def process_list(numbers):
    result = numbers.copy()   
    for num in result:
        if num < 0:
            result.remove(num)
    result.append(0)
    result.sort()
    return result
n=int(input('How many integers do you want in the list?'))
numbers=[]
for x in range(0,n):
  y=int(input('Enter a number:'))
  numbers.append(y)
result=process_list(numbers)
print("Original:", numbers)
print("Result:", result)

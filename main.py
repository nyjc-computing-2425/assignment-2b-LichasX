num = input('Enter a number (decimal only): ')
for x, y in enumerate(num):
  if y == ".":
    dp = len(num[x+1::])
# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')

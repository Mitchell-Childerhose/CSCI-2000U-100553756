def has_no_e(input):
 if(input == 'e'):
  return true
 else:
  return false

reader = open('gadsby_stripped.txt', 'r')
for line in reader:
 print(has_no_e(line))

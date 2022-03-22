print(" ")
print("Type the first number to calculate:")
try: 
    input1 = int(input())
except:
    print('Input not valid! Value must be a number.')
    exit()

print(" ")
print("Type a calculating action:")
print("Hint: + for addition, - for subtraction, * for multiplication, / for division")
input2 = input()
print(" ")
print("Type the second number to calculate:")
try: 
    input3 = int(input())
except:
    print('Input not valid! Value must be a number.')
    exit()
print(" ")
print("Result:")
if input2 == "+":
   print(input1 + input3)
if input2 == "-":
    print(input1 - input3)
if input2 == "*":
    print(input1 * input3)
if input2 == "/":
    print(input1 / input3)

# Code from https://github.com/DaneeSkripter/MeLearningPython/ 

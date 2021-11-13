print("Type the first number to calculate:")
input1 = int(input())
print(" ")
print("Type a calculating action:")
print("Hint: + for addition, - for subtraction, * for multiplication, / for division")
input2 = input()
print(" ")
print("Type the second number to calculate:")
input3 = int(input())
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
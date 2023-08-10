firstNumber=int(input("Enter your First Number : "))
function=str(input("Enter the sum(+,/,*,-) : "))
secondNumber=int(input("Enter your Second Number : "))

if function =='+':
    output=firstNumber+secondNumber
elif function == '/':
    output=firstNumber/secondNumber
elif function == '*':
    output=firstNumber*secondNumber
elif function == '-':
    output=firstNumber-secondNumber

print("Answer is : ",output)
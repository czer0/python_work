prompt = "Enter a number, and I'll tell you if it's "
prompt += "a multiple of ten: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of ten")
else:
    print(str(number) + " is not a multiple of ten")


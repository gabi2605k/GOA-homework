#   3) შექმენით სია რომელშიც მოათავსებთ 1-დან 20მდე რიცხვებს შემდ
# ეგ კი ამ სიიდან დაბეჭდავთ მხოლოდ ლუწ რიცხვებს გამოიყენეთ for loop
number= list(range(1, 21))
for num in number:
    if num % 2 == 0:
        print(num)
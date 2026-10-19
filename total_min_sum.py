# თუ მომხმარებელი ჩაწერს სიტყვას "stop", ციკლი უნდა შეწყდეს (break).  ნაწილი  1 

total = 0
count = 0
min_num = None
max_num = None

while True:
    user_input = input("შეიყვანე რიცხვი ან 'stop': ")

    if user_input.lower() == "stop":
        break

    try:
        number = float(user_input)

        total += number
        count += 1

        if min_num is None or number < min_num:
            min_num = number

        if max_num is None or number > max_num:
            max_num = number

    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'")

print(f"რიცხვების ჯამი: {total}")
print(f"რიცხვების რაოდენობა: {count}")

if count > 0:
    print(f"მაქსიმალური რიცხვი: {max_num}")
    print(f"მინიმალური რიცხვი: {min_num}")
else:
    print("რიცხვები არ შეგიყვანიათ.")

    # მეორე ნაწილი 


while True:
    try:
        height = int(input("შეიყვანეთ პირამიდის სიმაღლე (1-8): "))

        if height < 1 or height > 8:
            print("შეიყვანეთ რიცხვი 1-დან 8-ის ჩათვლით!")
            continue

        break

    except ValueError:
        print("შეცდომა! შეიყვანეთ მთელი რიცხვი.")

for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")

    for k in range(i):
        print("#", end="")

    print()

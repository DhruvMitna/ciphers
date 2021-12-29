action = input("Do you want to encode or decode?: ")
num = input("Enter the numbers: ")

try:

    if action == "encode":

        print(bin(num).replace("0b",""))

    elif action == "decode":

        print(int(num,2))

    else:

        print("Invalid action.")

except ValueError:

    print("Please enter a valid number.")
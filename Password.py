import random


def password_generator(n):
    password = ""
    for i in range(n):
        password += random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*")
    return password


def main():
    n = int(input("Enter the length of the password: "))
    print(password_generator(n))


if __name__ == "__main__":
    main()

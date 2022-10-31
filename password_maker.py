import random
import string


def make_password(user_input):
    count = 0
    password = []
    full_list = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    for x in range(0, user_input):
        choice = random.choice(full_list[count])
        password.append(random.choice(choice))
        count += 1
        if count == 4:
            count = 0
    random.shuffle(password)
    password = ''.join(password)
    print(f'Your new {user_input} character password is: {password}')


def main():
    while True:
        try:
            user_input = int(input('Please enter your desired password size: '))
            if user_input < 0:
                user_input = user_input * -1
        except ValueError:
            print('Please be sure to input a numeric value')
        else:
            break
    make_password(user_input)


if __name__ == '__main__':
    main()

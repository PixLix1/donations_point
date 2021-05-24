import random

cheer_up_list = ['You can do this!',
                 'Hai, hai, trage tare!',
                 ' :) :) :) ',
                 ]


def print_hi():
    print(cheer_up_list[random.randint(0, len(cheer_up_list) - 1)])


if __name__ == '__main__':
    print_hi()

# TO DO LIST:
# if user has products, then is_staff = 1

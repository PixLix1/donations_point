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
# check duplicated products
# donations page: categories >> list of products >> product page
# categories, filters, search, pagination
# homepage contains last 10 products added
# add to cart transform into add to favorites

# product request system (ordering)
# send email to donor > donor approves request > product removed from db or inactive?


# nice to have: number of views and number of add to fav


# QUESTIONS:
# views - products: category_list - request.get queryset is empty;
# Category.objects.all() returns <QuerySet [<Category: Category object (1)>, <Category: Category object (2)
#   .. because of .objects query?
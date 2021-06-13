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
# if user has items, then is_staff = 1
# check duplicated items
# donations page: categories >> list of items >> product page
# categories, filters, search, pagination
# homepage contains last 10 items added
# add to cart transform into add to favorites

# product request system (ordering)
# send email to donor > donor approves request > product removed from db or inactive?


# nice to have: number of views and number of add to fav


# QUESTIONS:
# views - items: category_list - request.get queryset is empty;
#       >> nu e empty. doar daca nu este parametru vine empty
# Category.objects.all() returns <QuerySet [<Category: Category object (1)>, <Category: Category object (2)
#   .. because of .objects query?
# middleware return?
#       >> se transfera actiunea la functia care este decorata cu middleware
# de ce in db model activation, id incepe cu 105? de la faked models? e ok?
# de unde stie clasa UserActivation care mosteneste class form de metoda self.user.set_password?
#       in view initiez form UserActivation cu user luat din model Activation pe baza token
#       set_pass e posibil pt ca lucrez cu record de user?

# https://dj-rest-auth.readthedocs.io/en/latest/faq.html
# password reset urls only work if declared in main app urls, not if in users app urls

# la view add_to_favorites e ok sa interoghez db pt fiecare sesiune?
# de ce page_obj.paginator? ma asteptam la paginator.page_obj
# de unde vine page_obj?
#       >> tine de ListView

# !!! in list view return to same page
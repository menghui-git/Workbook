from django.contrib.auth.models import (User as DjangoUser,
                                        Group as DjangoGroup)


class User(DjangoUser):
    pass


class Group(DjangoGroup):
    pass

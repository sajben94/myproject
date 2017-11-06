import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')

import django
django.setup()

# FAKE POP SCRIPT

import random
from myapp.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.free_email()
        user = Users.objects.get_or_create(first_name=first_name, last_name=last_name,email=email)[0]

if __name__ == '__main__':
    print('start popopo')
    populate(10)
    print('end popopo')

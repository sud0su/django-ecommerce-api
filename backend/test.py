import os

with open(os.path.abspath(os.path.join('/Users/immap/Documents/Docker/Python/Django/django-ecommerce-api/backend', '..', '.env'))) as f:
    mylist = [line.rstrip('\n') for line in f]
    print(mylist)
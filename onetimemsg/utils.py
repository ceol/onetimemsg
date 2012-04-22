import string
import random

# @see: http://stackoverflow.com/a/2257449
def uid_generator(size=8, chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
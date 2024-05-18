import random
import string

import clipboard

params_mapping = (
    string.digits,
    string.digits + string.ascii_letters,
    string.digits + string.ascii_letters + string.punctuation
)


def password_generator(parameters):
    length = parameters['length']
    complication = parameters['complication']
    save = parameters['save']

    password = ''.join(random.choice(params_mapping[complication - 1]) for _ in range(length))

    if save:
        clipboard.copy(password)

    print(f"Your password:  {password}")

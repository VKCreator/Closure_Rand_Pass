from random import randint, choices


def set_generator_random_password(psw_chars, min_length, max_length):
    def generate_random_password():
        length_current_pass = randint(min_length, max_length)
        return ''.join(choices(psw_chars, k=length_current_pass))

    return generate_random_password


if __name__ == '__main__':
    rnd = set_generator_random_password("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
    print(rnd())


def is_prime(number):
    if number < 2:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True

def run():
    number = int(input('Escribe un número: '))
    result = is_prime(number)

    if result is True:
        print('Tu número es primo')
    else:
        print('Tu número NO es primo')

if __name__ == '__main__':
    run()

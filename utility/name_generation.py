import random

# Базові компоненти для генерації імен
prefixes = ['Var', 'Mal', 'Cae', 'Ulrik', 'Ragnar', 'Bel', 'Lucius', 'Mortarion', 'Typhus', 'Horus']
suffixes = ['ion', 'tor', 'nus', 'gar', 'kan', 'rax', 'ius', 'dor', 'mar', 'con']

def gen_name():
    return random.choice(prefixes) + random.choice(suffixes)


if __name__ == "__main__":
    # Генеруємо 64 унікальних імені
    unique_names = set()
    while len(unique_names) < 64:
        unique_names.add(gen_name())

    # Виводимо згенеровані імені
    for name in unique_names:
        print(name)

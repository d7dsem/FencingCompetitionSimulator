import random

# Базові компоненти для генерації імен
prefixes = ['Var', 'Mal', 'Cae', 'Ulrik', 'Ragnar', 'Bel', 'Lucius', 'Mortarion', 'Typhus', 'Horus']
suffixes = ['ion', 'tor', 'nus', 'gar', 'kan', 'rax', 'ius', 'dor', 'mar', 'con']

def get_rand_name():
    return f"{random.choice(prefixes) + random.choice(suffixes)}"

primarchs = [
    "Lion El'Jonson",
    "Fulgrim",
    "Perturabo",
    "Jaghatai Khan",
    "Leman Russ",
    "Rogal Dorn",
    "Konrad Curze",
    "Sanguinius",
    "Ferrus Manus",
    "Roboute Guilliman",
    "Mortarion",
    "Magnus the Red",
    "Horus Lupercal",
    "Lorgar Aurelian",
    "Vulkan",
    "Corvus Corax",
    "Alpharius Omegon"
]

name_queue = primarchs[:]

random.shuffle(name_queue)

def shuffle_names():
    random.shuffle(name_queue)

def gen_name():
    if name_queue:
        return name_queue.pop()
    else:
        return get_rand_name()
    
    



if __name__ == "__main__":
    # Генеруємо 64 унікальних імені
    unique_names = set()
    while len(unique_names) < 64:
        unique_names.add(get_rand_name())

    # Виводимо згенеровані імені
    for name in unique_names:
        print(name)

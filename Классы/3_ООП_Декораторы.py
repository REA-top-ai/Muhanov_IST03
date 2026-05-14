from random import randint


def is_alive(func):
    def wrapper(*args, **kwargs):
        hero = args[0]

        if hero.health <= 0:
            print(f'{hero.name} мертв и не может действовать!')
            return None

        return func(*args, **kwargs)

    return wrapper


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f'[LOG] Начало действия: {func.__name__}')

        result = func(*args, **kwargs)

        print('[LOG] Действие завершено')

        return result

    return wrapper


# Декоратор пасхального ивента:
# увеличивает здоровье в 2 раза и ману в 1.5 раза
def easter_event(func):
    def wrapper(*args, **kwargs):
        hero = args[0]

        hero.health *= 2
        hero.mana = int(hero.mana * 1.5)

        print('Пасхальный ивент активирован!')

        return func(*args, **kwargs)

    return wrapper


# Декоратор священного посоха:
# добавляет волшебнику +5 маны
def holy_staff(func):
    def wrapper(*args, **kwargs):
        hero = args[0]

        if hero.hero_class == 'волшебник':
            hero.mana += 5
            print('Священный посох добавил +5 к мане')

        return func(*args, **kwargs)

    return wrapper


# Декоратор "удачный удар"
# С шансом 20% герой наносит критический удар
def critical_hit(func):
    def wrapper(*args, **kwargs):
        damage = args[1]

        if randint(1, 5) == 3:
            damage *= 2
            print('Критический удар! Урон увеличен вдвое')

        return func(args[0], damage)

    return wrapper


class Hero:

    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class

        if self.hero_class == 'волшебник':
            self.health = 60
            self.mana = 50

        elif self.hero_class == 'воин':
            self.health = 100
            self.mana = 10

        else:
            raise ValueError('Такого класса героя не существует')

        self.spells_names = {}
        self.items = {}

    @is_alive
    @critical_hit
    def attack(self, damage):
        print(f'Герой нанес урон: {damage}')

    @log_action
    def heal(self, amount):
        self.health += amount
        print(f'{self.name} восстановил {amount} здоровья')

    @is_alive
    def cast_spell(self, spell_name):

        if spell_name not in self.spells_names:
            print(f'Заклинание {spell_name} не изучено')

        else:
            mana_cost = self.spells_names[spell_name]['mana_cost']

            if self.mana >= mana_cost:
                self.mana -= mana_cost
                print(f'Применено заклинание {spell_name}')

            else:
                print('Недостаточно маны')

    def add_spell(
        self,
        spell_name,
        mana_cost=0,
        attack_damage=0,
        health_increase=0
    ):

        self.spells_names[spell_name] = {
            'mana_cost': mana_cost,
            'attack_damage': attack_damage,
            'health_increase': health_increase
        }

    def add_item(self, item_name, param, value):

        if len(self.items) >= 6:
            print('Нельзя надеть больше шести предметов')
            return

        self.items[item_name] = {
            param: value
        }

        if param == 'здоровье':
            self.health += value

        elif param == 'мана':
            self.mana += value


@easter_event
def start_event(hero):
    print(f'Праздничный бонус применен для {hero.name}')


@holy_staff
def activate_staff(hero):
    print(f'Священный посох активирован для {hero.name}')


wizard = Hero('Гэндальф', 'волшебник')
warrior = Hero('Шрек', 'воин')

print(wizard.health, wizard.mana)

start_event(wizard)

print(wizard.health, wizard.mana)

activate_staff(wizard)

print(wizard.health, wizard.mana)

wizard.add_spell('Огненный шар', 10, 30, 0)

print(wizard.spells_names)

wizard.cast_spell('Огненный шар')

warrior.attack(15)
warrior.attack(15)
warrior.attack(15)
warrior.attack(15)

warrior.heal(20)

warrior.add_item('Шлем', 'здоровье', 15)

print(warrior.health)
print(warrior.items)
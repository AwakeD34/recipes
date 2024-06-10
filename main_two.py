cook_book = {}

with open('recipes.txt', 'r') as file:
    lines = file.readlines()
    dish = ''
    ingredients = []
    count = 0

    for line in lines:
        line = line.strip()
        if line.isdigit():
            count = int(line)
        elif line:
            if count > 0:
                ingredient, quantity, measure = line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient,
                    'quantity': int(quantity),
                    'measure': measure
                })
                count -= 1
            else:
                if dish:
                    cook_book[dish] = ingredients
                dish = line
                ingredients = []

    if dish:
        cook_book[dish] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
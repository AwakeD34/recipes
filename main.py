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

print(cook_book)
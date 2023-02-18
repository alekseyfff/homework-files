file_name = 'recipes.txt'

cook_book = {}
with open(file_name, 'r', encoding='utf-8') as f:
    for recipe in f:
        name = recipe.strip()
        cook_book[name] = []
        count_ingridients = f.readline()
        for i in range(int(count_ingridients)):
            ingridient_name, quantity, measure = f.readline().strip().split(' | ')
            cook_book[name].append({'ingredient_name': ingridient_name, 'quantity': quantity, 'measure': measure})
        blank_line = f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    get_shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingridient in cook_book[dish]:
                    if ingridient['ingredient_name'] not in get_shop_list.keys():
                        get_shop_list[ingridient['ingredient_name']] = {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * person_count}
                    else:
                        get_shop_list[ingridient['ingredient_name']]['quantity'] = str(int(get_shop_list[ingridient['ingredient_name']]['quantity']) + int(ingridient['quantity']) * person_count)
    return get_shop_list

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

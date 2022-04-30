
def get_shop_list_by_dishes(cook_book: dict, dishes: list, person_count: int):
    result = {}

    for dish_name in dishes:
        for ingridient in cook_book[dish_name]:

            ingredient_name = ingridient['ingredient_name']
            if ingredient_name in result.keys():
                result[ingredient_name]['quantity'] += ingridient['quantity'] * person_count
            else:
                result[ingredient_name] = {'measure': ingridient['measure'], 'quantity': ingridient['quantity'] * person_count}

    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cook_book = {}
    with open("./files/recipes.txt") as file:
        while True:
            dish_name = file.readline()
            if dish_name == "":
                break

            dish_name = dish_name.rstrip()
            if dish_name == "":
                continue

            cook_book[dish_name] = []
            ingridients_amount = int(file.readline().rstrip())
            for i in range(ingridients_amount):
                ingridient = dict(zip(['ingredient_name', 'quantity', 'measure'], file.readline().rstrip().split(" | ")))
                ingridient['quantity'] = int(ingridient['quantity'])
                cook_book[dish_name].append(ingridient)

    print('Задача №1:')
    print(cook_book)

    print()
    print('Задача №2')
    print(get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 3))

    print()
    print('Задача №3')

    # читаем
    names = ['./files/1.txt', './files/2.txt', './files/3.txt']
    files = []
    for file_name in names:
        with open(file_name) as f:
            text = f.read()
            files.append({"lines_amount": len(text.splitlines()), "text": text})
            print(f'Прочитан файл: {file_name}')

    # сортируем
    sorted_files = sorted(files, key=lambda d: d['lines_amount'])

    # пишем
    file_name = './files/result.txt'
    f = open(file_name, 'w')
    for file in sorted_files:
        f.write(file['text'] + '\n')
    f.close()

    print(f'Записан файл: {file_name}')


from pprint import pprint
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        cook_book_name = line.strip()
        emp_count = int(file.readline())
        employees = []
        for _ in range(emp_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            employees.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[cook_book_name] = employees
    pprint(cook_book, sort_dicts=False)

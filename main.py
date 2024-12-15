with open("Recipes.txt") as f:
    cook_book = {}
    for line in f:
        dish = line.split()
        if "|" not in dish:
            ingredients = []
            meal = " ".join(dish)
            num = int(f.readline().strip())
            for i in range(num):
                element = f.readline().strip()
                element = element.split(" | ")
                ingredients.append({'ingredient_name': element[0], 'quantity': element[1], 'measure': element[2]})
            cook_book[meal] = ingredients        
            f.readline().strip()
    
    def get_shop_list_by_dishes(dishes, person_count):
        result = {}
        for dish in dishes:
            if dish in cook_book:
                ingredients = cook_book[dish]
                num = len(ingredients)
                for j in range(num):
                    ingredient_name = ingredients[j]['ingredient_name']
                    quantity = int(ingredients[j]['quantity']) * person_count
                    measure = ingredients[j]['measure']
                    result[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                print(f"Dish '{dish}' not found in cook_book.")
        return result

#print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

counts = []
files = []

with open('1.txt', 'r') as f1:
    count_1 = 0
    write_1 = []
    for line in f1:
        count_1 += 1
        write_1.append(line)
    counts.append(count_1)
    files.append(('1.txt', write_1))

with open('2.txt', 'r') as f2:
    count_2 = 0
    write_2 = []
    for line in f2:
        count_2 += 1
        write_2.append(line)
    counts.append(count_2)
    files.append(('2.txt', write_2))

with open('3.txt', 'r') as f3:
    count_3 = 0
    write_3 = []
    for line in f3:
        count_3 += 1
        write_3.append(line)
    counts.append(count_3)
    files.append(('3.txt', write_3))

counts, files = zip(*sorted(zip(counts, files)))

with open("result.txt", "w") as f4:
    for file_name, write in files:
        f4.write(f"{file_name}\n")
        f4.write(f"{len(write)}\n")
        f4.writelines(write)
        f4.write("\n")
    
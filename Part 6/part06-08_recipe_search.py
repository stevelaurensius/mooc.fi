def search_by_name(filename, search_string):
    result = []
    with open(filename) as recipe:
        for line in recipe:
            line = line.replace('\n', '')
            if line == line.capitalize():
                if search_string in line.lower():
                    result.append(line)
    return result


def search_by_time(filename: str, prep_time: int):
    result = []
    with open(filename) as recipe:
        for line in recipe:
            line = line.replace('\n', '')
            if line == line.capitalize():
                result.append(line)
    result = [x for x in result if x != '']
    result_list = [f"{result[i]}, preparation time {result[i + 1]} min" for i in range(0, len(result), 2) if
                   int(result[i + 1]) <= prep_time]
    # result = [[result[i], int(result[i+1])] for i in range(0, len(result), 2) if int(result[i+1]) <= prep_time]
    return result_list


def search_by_ingredient(filename: str, ingredient: str):
    recipes = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    current_recipe = {}
    for line in lines:
        line = line.strip()
        if line.isdigit():
            current_recipe['cooking_time'] = int(line)
        elif not line:
            if current_recipe:
                recipes.append(current_recipe)
                current_recipe = {}
        else:
            if 'name' not in current_recipe:
                current_recipe['name'] = line
                current_recipe['ingredients'] = []
            elif 'cooking_time' in current_recipe:
                current_recipe['ingredients'].append(line)

    if current_recipe:
        recipes.append(current_recipe)

    result = []
    for recipe in recipes:
        if ingredient in recipe['ingredients']:
            str_result = recipe['name'] + ', ' 'preparation time ' + str(recipe['cooking_time']) + ' min'
            result.append(str_result)
    return result


if __name__ == '__main__':
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet_page(request, servings):
    omlets = {
        'omlet': {
            'яйца, шт': 2 * int(servings),
            'молоко, л': 0.1 * float(servings),
            'соль, ч.л.': 0.5 * float(servings),
        }
    }
    return render(request, 'index.html', omlets)

def pasta_page(request, servings):
    pastas = {
        'pasta': {
            'макароны, г': 0.3 * float(servings),
            'сыр, г': 0.05 * float(servings),
        }
    }
    return render(request, 'index.html', pastas)

def buter_page(request, servings):
    buters = {
        'buter': {
            'хлеб, ломтик': 1 * int(servings),
            'колбаса, ломтик': 1 * int(servings),
            'сыр, ломтик': 1 * int(servings),
            'помидор, ломтик': 1 * int(servings),
        }
    }
    return render(request, 'index.html', buters)

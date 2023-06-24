pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input("Provide an ingredient: ")

if ingredient in pasta:
    print("Pasta Time!")

if ingredient in apple_pie:
    print("Apple Pie Time!")

if ingredient in ratatouille:
    print("Ratatouille Time!")

if ingredient in chocolate_cake:
    print("Chocolate Cake Time!")

if ingredient in omelette:
    print("Omelette Time!")



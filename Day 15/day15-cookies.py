##--- Day 15: Science for Hungry People ---
##
##Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.
##
##Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:
##
##capacity (how well it helps the cookie absorb milk)
##durability (how well it keeps the cookie intact when full of milk)
##flavor (how tasty it makes the cookie)
##texture (how it improves the feel of the cookie)
##calories (how many calories it adds to the cookie)
##You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.
##
##For instance, suppose you have these two ingredients:
##
##Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
##Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
##Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:
##
##A capacity of 44*-1 + 56*2 = 68
##A durability of 44*-2 + 56*3 = 80
##A flavor of 44*6 + 56*-2 = 152
##A texture of 44*3 + 56*-1 = 76
##Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.
##
##Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
##
##--- Part Two ---
##
##Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).
##
##For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.
##
##Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
from itertools import product
from functools import reduce
import operator

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.scores = {"capacity": int(capacity), "durability": int(durability),"flavor": int(flavor),"texture": int(texture)}
        self.calories = int(calories)


# Returns the score of the given recipe (a tuple designating the distribution of tablspoons), for the given ingredients.
def recipeScore(ingredients, recipe):
    recipeMap = list(zip(ingredients, recipe))
    return reduce(operator.mul, [max(0,
                                     sum([amount * ingredient.scores.get(ingredientName)
                                          for ingredient, amount in recipeMap]))
                                         for ingredientName in ingredients[0].scores.keys()])

# Get the highest score of any ingredient combination. Optionally limit to only recipes that reach a
# certain number of calories.
def bestRecipeScore(ingredients, recipes, calorieAmount=None):
    bestScore = 0
    for recipe in recipes:
        recipeMap = list(zip(ingredients, recipe))
        currentScore = recipeScore(ingredients, recipe)
        calories = sum([ing.calories * amount for ing, amount in recipeMap])
        if (calorieAmount == None or calorieAmount == calories):
            bestScore = max(bestScore, currentScore)
    return bestScore

# Returns an iterable containing the mix of amounts of ingredients to use.
def getRecipes(ingredients, numTablespoons):
    recipes = []
    for recipeAmounts in product(range(numTablespoons + 1), repeat=len(ingredients)):
        if (sum(map(int,recipeAmounts)) == numTablespoons):
            recipes.append(recipeAmounts)
    return recipes

def getIngredientsFromFile(file):
    ingredients = []
    for line in file:
        line = [part.strip(",").strip(":") for part in line.split()]
        ingredients.append(Ingredient(line[0],int(line[2]),int(line[4]),int(line[6]),int(line[8]),int(line[10])))
    return ingredients

f = open('day15-input.txt','r')
ingredients = getIngredientsFromFile(f)
recipes = getRecipes(ingredients, 100)

#print("Part One:", bestRecipeScore(ingredients, recipes))
print("Part Two:", bestRecipeScore(ingredients, recipes, 500))

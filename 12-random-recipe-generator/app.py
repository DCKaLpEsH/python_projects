print("👨🍳 Random Recipe Generator 🍳👩")

import random

flavor = ["lemon", "mint", "vanilla", "chocolate", "strawberry"]
method = ["baked", "fried", "grilled", "roasted", "boiled"]
protein = ["chicken", "beef", "fish", "tofu", "shrimp", "paneer"]
veggie = ["carrot", "potato", "onion", "garlic", "ginger"]
carb = ["rice", "pasta", "bread", "potato", "quinoa"]

def generate_recipe():
    print("🍴 Today's Recipe:")
    print(f"{random.choice(flavor)} {random.choice(method)} {random.choice(protein)} {random.choice(veggie)} {random.choice(carb)}")

generate_recipe()

RECIPES_NUTRITION = {
    "Poha": {"ingredients": ["flattened rice", "turmeric", "mustard seeds", "onion", "potato", "lemon", "curry leaves", "peanuts"], "calories": 270, "protein": 6, "cost_in_inr": 35},
    "Idli Sambar": {"ingredients": ["rice batter", "lentils", "tamarind", "tomato", "bottle gourd", "sambar powder", "mustard seeds"], "calories": 200, "protein": 6, "cost_in_inr": 45},
    "Aloo Paratha": {"ingredients": ["whole wheat flour", "potatoes", "ghee", "cumin powder", "coriander", "green chili", "yogurt"], "calories": 300, "protein": 8, "cost_in_inr": 50},
    "Chole Bhature": {"ingredients": ["chickpeas", "all purpose flour", "yogurt", "soda", "garam masala", "tomato puree", "onion"], "calories": 450, "protein": 11, "cost_in_inr": 65},
    "Palak Paneer": {"ingredients": ["spinach", "paneer cheese", "cream", "garlic", "ginger", "garam masala", "onion", "oil"], "calories": 180, "protein": 10, "cost_in_inr": 80},
    "Dal Makhani": {"ingredients": ["black lentils", "kidney beans", "butter", "cream", "garam masala", "tomato puree", "garlic"], "calories": 165, "protein": 9, "cost_in_inr": 70},
    "Chicken Curry": {"ingredients": ["chicken pieces", "curry powder", "coconut milk", "onion", "tomato", "ginger", "garlic"], "calories": 180, "protein": 16, "cost_in_inr": 110},
    "Vegetable Biryani": {"ingredients": ["basmati rice", "mixed vegetables", "biryani masala", "yogurt", "mint leaves", "saffron"], "calories": 150, "protein": 4, "cost_in_inr": 75},
    "Masala Dosa": {"ingredients": ["rice batter", "potatoes", "onion", "mustard seeds", "coconut chutney", "sambar"], "calories": 387, "protein": 7, "cost_in_inr": 60},
    "Baingan Bharta": {"ingredients": ["eggplant", "onion", "tomato", "green chili", "mustard oil", "garlic", "coriander"], "calories": 110, "protein": 3, "cost_in_inr": 55}
}

def display_recipes():
    print("\n-------------------------------- MENU --------------------------------")
    print(f"{'Meal Name':<20} | {'Calories (kcal)':<15} | {'Protein (g)':<12} | {'Est. Cost (₹)':<12}")
    print("-" * 70)
    for i, (meal, data) in enumerate(RECIPES_NUTRITION.items(), 1):
        print(f"{i}. {meal:<17} | {data['calories']:<15} | {data['protein']:<10.1f} | {data['cost_in_inr']:<10.2f}")
    print("----------------------------------------------------------------------")

def plan_daily_meals():
    meal_plan = {}
    meal_types = ["Breakfast", "Lunch", "Dinner"]

    display_recipes()

    for meal_type in meal_types:
        while True:
            choice = input(f"Enter the number for today's {meal_type} meal: ").strip().lower()

            try:
                meal_name = list(RECIPES_NUTRITION.keys())[int(choice) - 1]
                meal_plan[meal_type] = meal_name
                break
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid number.")

    return meal_plan

def generate_grocery_list_and_summary(meal_plan):
    all_ingredients = []
    total_calories = 0
    total_protein = 0
    total_cost = 0

    for meal in meal_plan.values():
        all_ingredients.extend(RECIPES_NUTRITION[meal]["ingredients"])
        total_calories += RECIPES_NUTRITION[meal]["calories"]
        total_protein += RECIPES_NUTRITION[meal]["protein"]
        total_cost += RECIPES_NUTRITION[meal]["cost_in_inr"]

    grocery_counts = {}
    for item in all_ingredients:
        if item in grocery_counts:
            grocery_counts[item] += 1
        else:
            grocery_counts[item] = 1

    print("\n--- Consolidated Daily Grocery List ---")
    for item, count in sorted(grocery_counts.items()):
        if count > 1:
            print(f"* {item.capitalize()} (x{count})")
        else:
            print(f"* {item.capitalize()}")
    print("-------------------------------------")

    print("\n--- Daily Summary ---")
    print(f"Total Estimated Calories: {total_calories} kcal")
    print(f"Total Estimated Protein: {total_protein:.1f} g")
    print(f"Total Estimated Cost: ₹{total_cost:.2f}")
    print("---------------------")

def main():
    print("Welcome to the Daily Indian Meal Planner and Grocery List Generator!")
    
    daily_plan = plan_daily_meals()

    print("\n--- Your Daily Meal Plan ---")
    print(f"{'Meal Type':<12} | {'Meal Name':<20} | {'Cal':<5} | {'Prt (g)':<7} | {'Cost (₹)':<7}")
    print("-" * 65)
    for meal_type, meal_name in daily_plan.items():
        nutrition = RECIPES_NUTRITION[meal_name]
        print(f"{meal_type:<12} | {meal_name:<20} | {nutrition['calories']:<5} | {nutrition['protein']:<7.1f} | {nutrition['cost_in_inr']:<7.2f}")
    print("-----------------------------------------------------------------")

    generate_grocery_list_and_summary(daily_plan)

if __name__ == "__main__":
    main()


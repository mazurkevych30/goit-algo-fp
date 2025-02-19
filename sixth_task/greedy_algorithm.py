
def greedy_algorithm (items: dict, budget: int) -> int:
    sorted_items = dict(sorted(items.items(),
                key=lambda item: item[1]["calories"] / item[1]["cost"],
                reverse=True)
    )
    total_calories = 0

    for item in sorted_items.items():
        if budget >= item[1]["cost"]:
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]

    return total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, 35))

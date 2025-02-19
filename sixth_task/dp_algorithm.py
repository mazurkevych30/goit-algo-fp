
def dynamic_programming(foods: dict, budget: int) -> int:
    K = [[0 for _ in range(budget + 1)] for _ in range(len(foods) + 1)]

    for idx, (_, val) in enumerate(foods, start=1):
        for bg in range(budget + 1):
            if idx == 0 or bg == 0:
                K[idx][bg] = 0
            elif val["cost"] <= bg:
                K[idx][bg] = max(val["calories"] + K[idx - 1][bg - val["cost"]], K[idx - 1][bg])
            else:
                K[idx][bg] = K[idx - 1][bg]

    return K[len(foods)][budget]



items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(dynamic_programming(list(items.items()), 35))

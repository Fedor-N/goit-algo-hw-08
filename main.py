import heapq


def min_cost_to_connect_cables(cables):
    # Ініціалізуємо купу
    heapq.heapify(cables)

    total_cost = 0

    # Поки у купі є більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # Об'єднуємо їх і додаємо в купу
        combined_cable = cable1 + cable2
        total_cost += combined_cable
        heapq.heappush(cables, combined_cable)

    return total_cost


# Приклад використання:
cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print("Мінімальні витрати на з'єднання кабелів:", result)

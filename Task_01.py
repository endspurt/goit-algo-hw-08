import heapq

def min_cost_to_connect_cables(lengths):
    """
    Функція для мінімізації вартості з'єднання кабелів.
    
    Аргументи:
    lengths (List[int]): Список довжин кабелів.
    
    Повертає:
    int: Мінімальна вартість з'єднання всіх кабелів.
    """
    # Перетворення списку довжин кабелів у мінімальну купу
    heapq.heapify(lengths)
    
    total_cost = 0
    
    # Продовжуємо з'єднувати кабелі, поки не залишиться один кабель
    while len(lengths) > 1:
        # Витягуємо два найменших кабелі з купи
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        
        # Вартість з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(lengths, cost)
    
    return total_cost

# Приклад використання функції
lengths = [4, 3, 2, 6]
print("Мінімальна вартість з'єднання кабелів:", min_cost_to_connect_cables(lengths))

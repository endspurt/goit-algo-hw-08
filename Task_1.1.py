import heapq

def merge_k_lists(lists):
    """
    Функція для злиття k відсортованих списків в один відсортований список.
    
    Аргументи:
    lists (List[List[int]]): Список відсортованих списків.
    
    Повертає:
    List[int]: Відсортований список.
    """
    min_heap = []
    
    # Додаємо перші елементи всіх списків до купи
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    
    result = []
    
    # Продовжуємо витягати найменші елементи з купи і додавати наступні елементи відповідних списків
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
    
    return result

# Приклад використання функції
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

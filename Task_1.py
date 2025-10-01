import timeit
import functools

denominations = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum):
    coins_count = {}
    for coin in denominations:
        if sum == 0:
            break
        count = sum//coin
        if count > 0:
            coins_count[coin] = count
            sum -= coin * count
    return coins_count  

# result1 = find_coins_greedy(103)
# print(result1)

def find_min_coins(amount, memo=None):
    if memo is None:
        memo = {}
    
    # Базовий випадок
    if amount == 0:
        return {}
    
    # Якщо результат вже обчислений
    if amount in memo:
        return memo[amount]
    
    # Якщо сума менша за найменшу монету
    if amount < min(denominations):
        memo[amount] = None
        return None
    
    best_result = None
    min_coins = float('inf')
    
    # Перебираємо всі можливі монети
    for coin in denominations:
        if coin <= amount:
            # Рекурсивно знаходимо оптимальний розклад для залишку
            remainder_result = find_min_coins(amount - coin, memo)
            
            if remainder_result is not None:
                # Рахуємо загальну кількість монет
                total_coins = sum(remainder_result.values()) + 1
                
                if total_coins < min_coins:
                    min_coins = total_coins
                    # Створюємо новий результат
                    best_result = remainder_result.copy()
                    if coin in best_result:
                        best_result[coin] += 1
                    else:
                        best_result[coin] = 1
    
    # Зберігаємо результат у мемо
    memo[amount] = best_result
    return best_result

# Тестування
# result2 = find_min_coins(103)
# print(result2)


# Тестові суми
small_amounts = [13, 47, 83]
large_amounts = [1987, 5432, 9876]

print("ПОРІВНЯННЯ ЧАСУ ВИКОНАННЯ")
print("=" * 50)

# Тестування маленьких сум
print("\nМАЛЕНЬКІ СУМИ:")
print("-" * 30)
for amount in small_amounts:
    print(f"\nСума: {amount}")
    
    # Жадібний алгоритм
    greedy_time = timeit.timeit(functools.partial(find_coins_greedy, amount), number=10000)
    print(f"Жадібний:     {greedy_time:.6f} сек")
    
    # Динамічне програмування
    dp_time = timeit.timeit(functools.partial(find_min_coins, amount), number=10000)
    print(f"Динамічне:    {dp_time:.6f} сек")

# Тестування великих сум
print("\nВЕЛИКІ СУМИ:")
print("-" * 30)
for amount in large_amounts:
    print(f"\nСума: {amount}")
    
    # Жадібний алгоритм
    greedy_time = timeit.timeit(functools.partial(find_coins_greedy, amount), number=1000)
    print(f"Жадібний:     {greedy_time:.6f} сек")
    
    # Динамічне програмування (менше запусків через повільність)
    dp_time = timeit.timeit(functools.partial(find_min_coins, amount), number=100)
    print(f"Динамічне:    {dp_time:.6f} сек")
M = 13

WORDS = ["БІЛЬШЕ", "ДІЛА", "МЕНШЕ", "СЛІВ", "ОТАК", "ДОБУДЕШ", "ХЛІБ"]

LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7,
    'Є': 8, 'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14,
    'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21,
    'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def simple_hash_from_map(key: str) -> int:
    sum_of_positions = 0
    print(f"Сума позицій літер:", end="")
    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        print(f" {position}", end=" +")
        sum_of_positions += position
        hash_address = sum_of_positions % M
    print(f"\b= {sum_of_positions}")
    print(f"Визначення хеш-адреси: {sum_of_positions} % {M} = {hash_address}")
    return hash_address


def build_open_hash_table(words: list, m: int) -> list:
    hash_table = [[] for _ in range(m)]
    print(f"\nСтворення порожньої хеш-таблиці:")
    print(hash_table)
    for word in words:
        print("\n----------------------------------------------------")
        print(f"Поточне слово: {word}")
        address = simple_hash_from_map(word)
        print(f"Вміст комірки {address}: {hash_table[address]}")
        if hash_table[address]:
            print("Виявлено колізію!")
            print(f"У комірці {address} вже знаходяться слова: {hash_table[address]}")
            print("Нове слово буде додано до існуючого списку.")
        else:
            print(f"Комірка {address} порожня. Колізії немає.")
        hash_table[address].append(word)
        print(f"Слово '{word}' додано до комірки {address}.")
        print(f"Новий вміст комірки {address}: {hash_table[address]}")
    return hash_table


def display_hash_table(table: list):
    print("\n--- Результат хешування (Таблиця M=13) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")
        
print(f"Розмір хеш-таблиці M = {M}")
print(f"Список слів: {WORDS}")
hash_table = build_open_hash_table(WORDS, M)
print("\n----------------------------------------------------")

display_hash_table(hash_table)

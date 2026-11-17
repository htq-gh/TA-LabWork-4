M = 13

WORDS = ["БІЛЬШЕ", "ДІЛА", "МЕНШЕ", "СЛІВ", "ОТАК", "ДОБУДЕШ", "ХЛІБ"]

LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7,
    'Є': 8, 'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14,
    'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21,
    'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

def primary_hash(key: str) -> int:
    sum_of_positions = 0
    print(f"Сума позицій літер:", end="")
    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        print(f"{position}", end=" + ")
        sum_of_positions += position
    print(f"\b\b= {sum_of_positions}")
    print(f"Визначення хеш-адреси: {sum_of_positions} % {M} = {sum_of_positions % M}")
    return sum_of_positions % M

def build_closed_hash_table(words: list, m: int) -> list:
    hash_table = [None] * m
    inserted_count = 0
    print("\nСтворення порожньої хеш-таблиці:")
    print(hash_table)
    for word in words:
        print("\n----------------------------------------------------")
        print(f"Поточне слово: {word}")
        start_address = primary_hash(word)
        address = start_address
        print("\n> Пошук вільної комірки.")
        for i in range(m):
            address = (start_address + i) % m
            if hash_table[address] is None:
                print(f"Комірка {address} вільна.")
                hash_table[address] = word
                inserted_count += 1
                print(f"Слово '{word}' додано до комірки {address}.")
                print(f"Кількість доданих слів: {inserted_count}")
                print(f"Поточна хеш-таблиця: {hash_table}")
                break
            else:
                print(f"Комірка {address} зайнята словом '{hash_table[address]}'.")
                print("Переходимо до наступної комірки.\n")
        else:
            print(f"Помилка: Таблиця заповнена. Не вдалося додати слово: {word}")
    return hash_table

def display_hash_table(table: list):
    print("\n--- Хеш-таблиця (Відкрита адресація, M=13) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d} | {value}")

print(f"Розмір хеш-таблиці M = {M}")
print(f"Список слів: {WORDS}")
hash_table = build_closed_hash_table(WORDS, M)
print("\n----------------------------------------------------")

display_hash_table(hash_table)

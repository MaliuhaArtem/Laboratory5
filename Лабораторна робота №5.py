file1 = open("prices.txt", 'a')
total_cost = 0  
while True:
    name = input("Введіть назву продукту або 'q' якщо хочете припинити: ")
    if name == 'q':
        break
    try:
        price = float(input("Введіть ціну продукту: "))
    except ValueError:
        print("Будь ласка, введіть коректну ціну.")
        continue
    new_line = f"{name} -- {price}\n"
    file1.write(new_line)
    total_cost += price
file1.close()
with open("prices.txt", 'r') as file1:
    content = file1.read()
    print(content)
print(f"Загальна вартість товарів: {total_cost:.2f}")
open("prices.txt", 'w').close()
print("Файл очищено.")

product = int(input("Введите колличество товаров: "))
m_list = []
m_dict = []
m_anlys = {}
num = 1

while num != product:
    m_dict = dict(
        {"Наименование": input("Введите название товара"), "Цена на продукт": input("Введите ценну на продукт"),
         "Количестов товаров": input("Введите количестов товаров"),
         "Единица измерения": input("Введите единицу измерения")})
    m_list.append((num, m_dict))
    num += 1
    m_anlys = dict(
        {"Название": m_dict.get("Наименование"), "цена": m_dict.get("Цена на продукт"),
         "Кол-во товаров": m_dict.get("Количестов товаров"), "Единица измерения": m_dict.get("Единица измерения")}
    )

    print(m_list)
    print(m_anlys)

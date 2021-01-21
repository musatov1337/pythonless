score = int(input("Рейтинг"))
rate_list = [7, 5, 3, 3, 2]

for el in range(len(rate_list)):
    if score == rate_list[el]:
        rate_list.insert(el + 1, score)
        break
    if rate_list[0] < score:
        rate_list.insert(0, score)
        break
    elif rate_list[-1] > score:
        rate_list.append(score)
        break
    elif rate_list[el] > score and rate_list[el + 1] < score:
        rate_list.insert(el + 1, score)
        break
print(f"После добавления рейтинга {score}, список стал следующим {rate_list}.")

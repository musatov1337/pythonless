a = int(input("Длина первого забега в киллометрах: "))
b = int(input("Цель которую хотите пробежать в киллометрах: "))
r_days = 1
r_km = a
while r_km < b:
        a = a + 0.1 * a
        r_days += 1
        r_km = r_km + a
print(f"Вы достигли цели на на %.d день" % r_days)
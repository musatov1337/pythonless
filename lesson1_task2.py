time = int(input("Write time in seconds: "))
hours = time // 3600
minute = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minute * 60)

print("Полученое время: %d:%d:%d" %(hours, minute, seconds))

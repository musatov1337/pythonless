import re

with open("study_time.txt", "r", encoding="utf=8") as content:
    sub_info = {}
    for el in content:
        a = 0
        subject, lecture, practice, test = el.split()
        lecture = re.findall("(\d+)", lecture)
        practice = re.findall("(\d+)", practice)
        test = re.findall("(\d+)", test)
        s_obj = lecture + practice + test
        for el_n in s_obj:
            el_n = int(el_n)
            a += el_n
            sub_info[subject] = a
print(f"Предметы {sub_info}")

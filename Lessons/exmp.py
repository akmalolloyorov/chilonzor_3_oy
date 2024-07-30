import datetime, time

# Hozirgi sana va vaqtni olish
hozirgi_vaqt = datetime.datetime.now()

# Faqat soat va daqiqani olish
faqat_soat_va_daqiqa = hozirgi_vaqt.strftime("%H:%M")
print("Hozirgi soat va daqiqa:", faqat_soat_va_daqiqa)

# Faqat sanani olish (kun, oy, yil)
faqat_sana = hozirgi_vaqt.strftime("%d-%m-%Y")
print("Hozirgi sana:", faqat_sana)

year = time.strftime('%Y')
month = time.strftime("%m")
minute = time.strftime("%M")
hour = time.strftime("%H")
century = time.strftime("%C")
second = time.strftime("%S")
# print(hour, ":", minute)
# print(year)
# print(month)
print(century)
print(second)

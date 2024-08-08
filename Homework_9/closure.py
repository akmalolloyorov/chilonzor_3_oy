"""
   3. Bir son qabul qiladigan closure yozing va uni ichidagi funksiya ikki son qabul qilsin,
   agar ichki funksiyadagi sonlarni yig'indisi tashqari funksiyadagi sondan kichik bo'lsa
   ularni qo'shib tepadagi funksiyaning soniga ko'paytirib natijani qaytaring,
   agar katta bo'lsa bo'lib, agar teng bo'lsa shuncha ichki funksiyada sonlarni qo'shib qaytarib bering

"""
from context_manager import int_input


def autor(num):
    def inner(num1, num2):
        if num1 + num2 < num:
            return (num1 + num2) * num
        elif num1 + num2 > num:
            return (num1 + num2) / num
        else:
            return num

    return inner


n = int_input("previous number: ")
n1 = int_input("num1: ")
n2 = int_input("num2: ")
t = autor(n)
print(t(n1, n2))

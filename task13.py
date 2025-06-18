ism = input("Ismingizni kiriting: ")

# Chap tomondan bo‘sh joylarni olib tashlash
start = 0
while start < len(ism) and ism[start] == ' ':
    start += 1

# O‘ng tomondan bo‘sh joylarni olib tashlash
end = len(ism) - 1
while end >= 0 and ism[end] == ' ':
    end -= 1

# Tozalangan ism
tozalangan_ism = ism[start:end+1]
print("Tozalangan ism:", tozalangan_ism)

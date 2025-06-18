text = input("Textni kiriting: ")
unli_harflar = "aeiouAEIOU"
hisob = 0

for harf in text:
    if harf in unli_harflar:
        hisob += 1

print("Unli harflar soni:", hisob)

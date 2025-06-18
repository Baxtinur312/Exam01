text = input("Enter text: ")
if text.endswith((".pdf", ".docx", ".txt")):
    print("True")
else:
    print("False")    
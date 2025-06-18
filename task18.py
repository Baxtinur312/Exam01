vazn = int(input("Enter your weight: "))
hieght = float(input("Enter your height: "))
BMI = vazn // hieght ** 2
if 0 < vazn > 500:
    print("Vazn 1-500 kg oralig'ida bo'lishi kerak")
    if 0.5 <= hieght <= 3.0:
        print("Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak")
        if vazn and hieght < 0:
            print("Vazn va bo'y musbat bo'lishi kerak")
print(BMI) 
if BMI < 18.5:
 print("Kam vazn") 
elif 18.5 <= BMI <= 25:
   print("Normal vazn")   
elif 25 <= BMI <=30:
   print("Ortiqcha vazn") 
elif BMI >= 30:
   print("Semizlik")  




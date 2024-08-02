print("Measure Convertor!")
Unit = input("CM or Inches")
if Unit == "Centimetre" or "Cm" or "cm" or "CM":
     CM = int(input("How much Cm?"))
     print(CM / 2.54 )
elif Unit == "inch" or "INCH" or "in" or "IN" or "Inches":
     inch = int(input("How much inches?"))
     print(inch * 2.54 )
else:
     print("Sorry thats not a proper unit!")
     
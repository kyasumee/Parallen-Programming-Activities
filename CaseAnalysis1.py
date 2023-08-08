print("Billing Statement")

previousbill = input("Enter Previous Billing ")
presentbill = input("Enter Present Billing ")

if previousbill > presentbill:
    print("Invalid Billing")
    
consum = int(presentbill) - int(previousbill)
print(consum)

    
X = "Residential"
Y = "Commercial"
Z = "Industrial"

print("  Residential")
print("  Commercial")
print("  Industial")

typeConsum = input("Type of Consumption ")

rateR1 = 18.75
rateR2 = 17.50
rateC1 = 20.25
rateC2 = 19.75
rateI2 = 22.75
rateI1 = 22.55


addedcostR1 = 0
addedcostR2 = 0
addedcostC1 = 200
addedcostC2 = 100
addedcostI1 = 500
addedcostI2 = 300

if typeConsum == "X" or typeConsum == "x":
    print("Residential Billing")
    
    if consum >= 100:
        GMonthbill = int(consum) * int(rateR1)
        print("Gross Monthly Bill " + str(GMonthbill))
        tax = float(GMonthbill) * .05
        print("Tax: " + str(tax))
        Finalbill = int(GMonthbill) + int(addedcostR1) + int(tax)
        print("Final Monthly Bill: " + str(Finalbill))
    else:
        consum < 100
        GMonthbill = int(consum) * int(rateR2)
        print("Gross Monthly Bill " + str(GMonthbill))
        tax = float(GMonthbill) * 0
        print("Tax: " + str(tax))
        Finalbill = int(GMonthbill) + int(addedcostR2) + int(tax)
        print("Final Monthly Bill: " + str(Finalbill))
        
elif typeConsum == "Y" or typeConsum == "y":
    print("Commercial Billing")
    
    if consum >= 100:
        GMonthbill = int(consum) * int(rateC1)
        print("Gross Monthly Bill " + str(GMonthbill))
        tax = float(GMonthbill) * .10
        print("Tax: " + str(tax))
        Finalbill = int(GMonthbill) + int(addedcostC1) + int(tax)
        print("Final Monthly Bill: " + str(Finalbill))
    else:
        consum < 100
        GMonthbill = int(consum) * int(rateC2)
        print("Gross Monthly Bill " + str(GMonthbill))
        tax = float(GMonthbill) * .02
        print("Tax: " + str(tax))
        Finalbill = int(GMonthbill) + int(addedcostC2) + int(tax)
        print("Final Monthly Bill: " + str(Finalbill))
        
elif typeConsum == "Z" or typeConsum == "z":
    print("Industrial Billing")
    
    if consum >= 100:
        GMonthbill = int(consum) * int(rateI1)
        print("Gross Monthly Bill " + str(GMonthbill))
        tax = float(GMonthbill) * .10
        print("Tax: " + str(tax))
        Finalbill = int(GMonthbill) + int(addedcostI1) + int(tax)
        print("Final Monthly Bill: " + str(Finalbill))
    else:
        consum < 100
        GMonthbill = int(consum) * int(rateI2)
        print("Gross Monthly Bill " + str(GMonthbill))
        tax = float(GMonthbill) * .05
        print("Tax: " + str(tax))
        Finalbill = int(GMonthbill) + int(addedcostI1) + int(tax)
        print("Final Monthly Bill: " + str(Finalbill))
        
        
    
    
    

#marginal tax calculation

income=float(input("what is your 2019 taxable income?"))
x=9700*0.10
y=29775*0.12
z=44724*0.22
w=76524*0.24
k=43374*0.32
m=306199 * 0.35
n=9489700*0.37



if income >=0 and income <=9700:
    tax1=income * 0.10
    print(f"Your tax liability is ${tax1:,.2f}")
    tax_rate1=tax1/income*100
    print(f"Your effective tax rate is {tax_rate1:.1f}%")
    
elif income >=9701 and income <=39475:
    
    tax2=((income-9700) * 0.12) + x
    print(f"Your tax liability is ${tax2:,.2f}")
    tax_rate2=tax2/income*100
    print(f"Your effective tax rate is {tax_rate2:.1f}%")

elif income >=39476 and income <=84200:
    
    tax3=((income-39475) * 0.22) + y + x
    print(f"Your tax liability is ${tax3:,.2f}")
    tax_rate3=tax3/income*100
    print(f"Your effective tax rate is {tax_rate3:.1f}%")

elif income >=84201 and income <=160725:
   
    tax4=((income-84200)) * 0.24 + z + x + y
    print(f"Your tax liability is ${tax4:,.2f}")
    tax_rate4=tax4/income*100
    print(f"Your effective tax rate is {tax_rate4:.1f}%")
    
elif income >=160726 and income <=204100:
    
    tax5=((income-160725)) * 0.32 + w + x + y + z
    print(f"Your tax liability is ${tax5:,.2f}")
    tax_rate5=tax5/income*100
    print(f"Your effective tax rate is {tax_rate5:.1f}%")

elif income >=204101 and income <=510300:
   
    tax6=((income-204100)) * 0.35 + k + w + x + y + z
    print(f"Your tax liability is ${tax6:,.2f}")
    tax_rate6=tax6/income*100
    print(f"Your effective tax rate is {tax_rate6:.1f}%")

else:
   
    tax7=((income-510300)) * 0.37 + m + k + w + x + y + z
    print(f"Your tax liability is ${tax7:,.2f}")
    tax_rate7=tax7/income*100
    print(f"Your effective tax rate is {tax_rate7:.1f}%")


if income>=10000000:
  
    tax8=3664987+0.7*(income-10000000)
    print(f"With a new 70% bracket, your tax liability would be ${tax8:,.2f}") 
    tax_rate8=tax8/income*100
    print(f"Your effective tax rate with the new bracket would be {tax_rate8:.1f}%")
    





    

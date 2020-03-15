import math

hwy_type=""
hwy_dist=""

while True:
   try:
       hwy=int(input("Please enter a US Interstate Highway route number: "))
       hwy_dire=""
       if hwy > 0 and hwy / 10 <10:
           hwy_type = "Primary"
           if hwy%2==0:
               hwy_dire = "east-west"
           elif hwy%2!=0:
               hwy_dire = "north-south"
           if hwy%5==0:
               print(f"Interstate {hwy} is a long-distance arterial highway oriented {hwy_dire}.")
           else:
               print(f"Interstate {hwy} is oriented {hwy_dire}.")
       elif hwy>0 and hwy/10>=10:
           hwy_type = "Auxiliary"
           if int(hwy/100)%2==0:
               hwy_dire="loop highway"
           elif int(hwy/100)%2!=0:
               hwy_dire="spur highway"
           print(f"Interstate {hwy} is a {hwy_dire} of Interstate {(hwy%100):.0f}.")
       if hwy==0:

           break
   except ValueError:
       False

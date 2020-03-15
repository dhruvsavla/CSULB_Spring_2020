import math
print("Air Quality Index Calculator")
i=1
ip2=0
apm_25=0
total=0
f_AQI = 0
sumPM_25=0
validLocation=0
avg_PM25=0.0
final_aqi_location=""
air_quality=""

number_locations=int(input("How many locations for this report?"))
while number_locations<=0:             #this while loop is used if userr enterrs a negative value the program will ask for the positive input.
    number_locations=int(input("How many locations for this report?"))

for i in range(number_locations):
    AQI=0
    name_location=input(f"What is the name of Location{i+1}?")
    
    pm_25=float(input(" ->Enter PM-2.5 concentration:"))
    pm_25=int(pm_25*10)/10
    
    if pm_25>=0:
        validLocation+=1
        if pm_25>=0 and pm_25<=12:
            ip1=(50-0)/(12-0)*(pm_25-0)+0
        
        
        if pm_25>=12.1 and pm_25<=35.4:
            ip1=(100-51)/(35.4-12.1)*(pm_25-12.1)+51
        
        
        if pm_25>=35.5 and pm_25<=55.4:
            ip1=(150-101)/(55.4-35.5)*(pm_25-35.5)+101
        
        
        if pm_25>=55.5 and pm_25<=150.4:
            ip1=(200-151)/(150.4-55.5)*(pm_25-55.5)+151
        
        
        if pm_25>=150.5 and pm_25<=250.4:
            ip1=(300-201)/(250.4-150.5)*(pm_25-150.5)+300
        
        
        if pm_25>=250.5 and pm_25<=500.4:
            ip1=(500-301)/(500.4-250.5)*(pm_25-250.5)+500

        print("  PM-2.5 concentration of",round(pm_25,1),"is index level",round(ip1))

        
        if ip1 > AQI :        #this part of code is used to find the maximum index value of a location and is present for every pollutant.
            
            AQI = ip1

        sumPM_25+=pm_25

        avg_PM25=sumPM_25/validLocation

    
    
      

    pm_10=int(float(input(" ->Enter PM-10 concentration:")))

    if pm_10>=0:
        
    
    
        if pm_10>=0 and pm_10<=54:
        
            i_high=50
            i_low=0
            c_high=54
            c_low=0
            ip2=(i_high-i_low)/(c_high-c_low)*(pm_10-c_low)+i_low
        
        
        if pm_10>=55 and pm_10<=154:
            i_high=100
            i_low=51
            c_high=154
            c_low=55
            ip2=(i_high-i_low)/(c_high-c_low)*(pm_10-c_low)+i_low
        

        if pm_10>=155 and pm_10<=254:
            i_high=150
            i_low=101
            c_high=254
            c_low=155
            ip2=(i_high-i_low)/(c_high-c_low)*(pm_10-c_low)+i_low
            

        if pm_10>=255 and pm_10<=354:
            i_high=200
            i_low=151
            c_high=354
            c_low=255
            ip2=(i_high-i_low)/(c_high-c_low)*(pm_10-c_low)+i_low
            

        if pm_10>=355 and pm_10<=424:
            i_high=300
            i_low=201
            c_high=424
            c_low=355
            ip2=(i_high-i_low)/(c_high-c_low)*(pm_10-c_low)+i_low
            

        if pm_10>=425 and pm_10<=604:
            i_high=500
            i_low=301
            c_high=604
            c_low=425
            ip2=(i_high-i_low)/(c_high-c_low)*(pm_10-c_low)+i_low
        print("  PM-10 concentration of",int(pm_10),"is index level",round(ip2))

        

        if ip2 > AQI :
            
            AQI = ip2


    NO2 = int(float(input(" ->Enter NO-2 concentration:")))

    if NO2>=0:
        
    
        if NO2 >= 0 and NO2 <= 53:
            IPN = (50-0)/(53 - 0 ) * (NO2 - 0) + 0
            
        if NO2 >= 54 and NO2 <=100:
             IPN = (100-51)/(100-54) * (NO2 - 54) + 51
             
        if NO2 >= 101 and NO2 <= 360:
            IPN = (150 - 101)/(360 - 101) * (NO2 - 101) + 101
            
        if NO2 >= 361 and NO2 <= 649:
            IPN = (200 - 151)/(649 - 361 ) * (NO2 - 361) + 151
            
        if NO2 >= 650 and NO2 <= 1249:
            IPN = (300-201)/(1249 - 650) * (NO2 - 650) + 201
            
        if NO2 >= 1250 and NO2 <= 2049:
            IPN = (500 - 301)/(2049 -1250) * (NO2 - 1250) + 301
           
        print("  NO-2 concentration of", NO2 ,"is index Level", round(IPN))
        

        if IPN > AQI :
            
            AQI = IPN

    SO2 = int(float(input(" ->Enter SO-2 concentration:")))

    if SO2>=0:
            
        
        if SO2 >= 0 and SO2 < 35:
            so =(50-0)/(35-0) * (SO2 - 0) +0
            
        if SO2 >= 36 and SO2 < 75:
            so =(100-51)/(75-36) * (SO2 -36 ) + 51
            
        if SO2 >= 76 and SO2 < 185:
            so =(150 - 101)/(185 - 76) * (SO2 - 76) +101
            
        if SO2 >= 186 and SO2 < 304:
            so =(200-151)/(304 - 186) * (SO2 -186 ) +186
            
        if SO2 >= 305 and SO2 < 604:
            so =(300-201)/(604 - 305) * (SO2 - 305) +201
            
        if SO2 >= 605 and SO2 < 1004:
            so =(500 - 301)/(1004 - 605) * (SO2 - 605) +301
            
        print("  SO-2 concentration of",SO2,"is index level" ,round(so))
        

        if so > AQI :
            
            AQI = so

    CO = float(input(" ->Enter CO Concentration:"))

    if CO >=0:
        
        
        if CO >=0 and CO<=4.4:
            i_high=50
            i_low=0
            c_high=4.4
            c_low=0
            ICO=(i_high-i_low)/(c_high-c_low)*(CO-c_low)+i_low
            

        if CO >=4.5 and CO<=9.4:
            i_high=100
            i_low=51
            c_high=9.4
            c_low=4.5
            ICO=(i_high-i_low)/(c_high-c_low)*(CO-c_low)+i_low
            

        if CO >=9.5 and CO<=12.4:
            i_high=150
            i_low=101
            c_high=12.4
            c_low=9.5
            ICO=(i_high-i_low)/(c_high-c_low)*(CO-c_low)+i_low
            

        if CO >=12.5 and CO<=15.4:
            i_high=200
            i_low=150
            c_high=15.4
            c_low=12.5
            ICO=(i_high-i_low)/(c_high-c_low)*(CO-c_low)+i_low
            

        if CO >=15.5 and CO<=30.4:
            i_high=300
            i_low=201
            c_high=30.4
            c_low=15.5
            ICO=(i_high-i_low)/(c_high-c_low)*(CO-c_low)+i_low
            

        if CO >=30.4 and CO<=50.4:
            i_high=500
            i_low=301
            c_high=50.4
            c_low=30.4
            ICO=(i_high-i_low)/(c_high-c_low)*(CO-c_low)+i_low

        print(" CO Concentration of",CO,"is index level",round(ICO))
        

        if ICO > AQI:
            
            AQI = ICO


    O3 = int(float(input(" ->Enter O3 Concentration:")))

    
    
    if O3>124:
        if(O3 >=125 and O3<=164):
            i_high=150
            i_low=101
            c_high=164
            c_low=125
            IO3=(i_high-i_low)/(c_high-c_low)*(O3-c_low)+i_low
        
        if(O3 >=165 and O3<=204):
            i_high=200
            i_low=151
            c_high=204
            c_low=165
            IO3=(i_high-i_low)/(c_high-c_low)*(O3-c_low)+i_low
        
        if(O3 >=205 and O3<=404):
            i_high=300
            i_low=201
            c_high=404
            c_low=205
            IO3=(i_high-i_low)/(c_high-c_low)*(O3-c_low)+i_low
        
        if(O3 >=405 and O3<=604):
            i_high=500
            i_low=301
            c_high=604
            c_low=405
            IO3=(i_high-i_low)/(c_high-c_low)*(O3-c_low)+i_low
        print(" O3 Concentration of",int(O3),"is index level",round(IO3))
        

        if IO3 > AQI :
            
            AQI = IO3
        
        
       

    
    
    
    
    print ("AQI for " , name_location ,"is",round(AQI))

    if AQI >= 0 and AQI <= 50:
        air_quality="Good"
    elif AQI >= 51 and AQI <=100:
        air_quality="moderate"
    elif AQI >=101 and AQI <= 150:
        air_quality="Unhealthy for sensitive groups"
    elif AQI >= 151 and AQI <= 200:
        air_quality="Unhealthy"
    elif AQI >= 201 and AQI <= 300:
        air_quality="very unhealthy"
    elif AQI >= 301 and AQI <= 500:
        air_quality="Hazardous"

    print("Air Quality:",air_quality)

    
    

 
    if AQI >= f_AQI:                                     
        final_aqi_location=name_location          #this line of code is used to find the location name with maximum index value, i have initialized final_aqi_location at the start of the program
        f_AQI = AQI
        

print("Summary :\nLocation with highest AQI is ",final_aqi_location,"(",round(f_AQI),")")
if pm_25>=0: 
    print("Average PM-2.5 concentration:",math.floor(avg_PM25*10)/10)
    
        
#this is neel savla's change.




        






























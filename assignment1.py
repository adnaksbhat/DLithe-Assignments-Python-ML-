#A dam reservoir's capacity is 250e100 cubic metre where it holds 199.5e85 cu.m water.
#A rain occured in the area which gave 25e8 cu.m water but 25% amount of this rain water ran-off useless. The remaining water from this rainfall flowed to the reservoir and there it was collected. On another day, a heavy storm increased the water level of this dam to its 15% of the current water level. Ground water sources contributed 5% to reservoir's current level. 5% of the present level of reservoir evaporated and later 15% amount of water was passed for irrigation to arid regions. 

#Write a program to find the current water level of the reservoir?










import math
capacity=(250*math.exp(100))
holds=(199.5*math.exp(85))

totalrain=(25*math.exp(8))
usefulrain=totalrain*0.75
indam=holds+usefulrain+(0.20*usefulrain)         #5% and 15% increase on current level. So 20% increase
indamlater=indam-(0.05*indam)
indamlater2=indamlater-(0.15*indamlater)


if(indamlater>holds):
    print("Not possible")
else:
    print("Current Water level = "+str(round(indamlater2,2))+" cu.m") 
    






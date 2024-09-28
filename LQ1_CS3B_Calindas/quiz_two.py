#Quiz 2

#Groupmates Full Names
GroupmateNamel = "Adrian Cedric 0. Calindas"
GroupmateName2 = "Chryson M. Valdez"
GroupmateName3 = "Sharmaine N. Gasatan"

#Groupmates Ages
GroupmateAgel = "20"
GroupmateAge2 = "20"
GroupmateAge3 = "19"
#Groupmates Allowances
GroupmateAllowancel = float(500)
GroupmateAllowance2 = float(500)
GroupmateAllowance3 = float(500)

#Calculate all our Ages and Allowances
Mem1AgeAllowanceTotal = (int(GroupmateAgel) + GroupmateAllowancel)
print(Mem1AgeAllowanceTotal)
Mem2AgeAllowanceTotal = (int(GroupmateAge2) + GroupmateAllowance3)
print(Mem2AgeAllowanceTotal)
Mem3AgeAllowanceTotal = (int(GroupmateAge3) + GroupmateAllowance3)
print(Mem3AgeAllowanceTotal)

Mem1AgeAllowanceSub = (int(GroupmateAgel) - GroupmateAllowancel)
print(Mem1AgeAllowanceSub)
Mem2AgeAllowanceSub = (int(GroupmateAge2) - GroupmateAllowance3)
print(Mem2AgeAllowanceSub)
Mem3AgeAllowanceSub = (int(GroupmateAge3) - GroupmateAllowance3)
print(Mem3AgeAllowanceSub)

Mem1AgeAllowanceMul = (int(GroupmateAgel) * GroupmateAllowancel)
print(Mem1AgeAllowanceMul)
Mem2AgeAllowanceMul = (int(GroupmateAge2) * GroupmateAllowance3)
print(Mem2AgeAllowanceMul)
Mem3AgeAllowanceMul = (int(GroupmateAge3) * GroupmateAllowance3)
print(Mem3AgeAllowanceMul)


#Shows the length of our Names 
MemberlNameLength = (len(GroupmateNamel)) 
Member2NameLength = (len(GroupmateName2))
Member3NameLength = (len(GroupmateName3))

#Compare all our Ages and Full Names' Length
print((GroupmateAgel == GroupmateAge2), (GroupmateAge2 == GroupmateAge3))
print((MemberlNameLength == Member2NameLength), (Member2NameLength == Member3NameLength))
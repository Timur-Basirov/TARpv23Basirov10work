#1
#for
#r=0
#for i in range(0,15,1):
#    arv=float(input("Sisesta {0} .arv".format(i+1)))
#    if arv==int(arv):
#        r+=1
#print("Täisarvude arv on "+str(r))
##while true
#r=0
#i=0
#while True:
#    i+=1
#    arv=float(input("Sisesta {0}.arv ".format(i)))
#    if arv==int(arv):
#        r+=1
#    if i==15: break
#print("Täisarvude arv on "+str(r))

##while tingimusega
#r=0
#i=0
#while i<15:
#    i+=1
#    arv=float(input("Sisesta {0}.arv ".format(i)))
#    if arv==int(arv):
#        r+=1
    
#print("Täisarvude arv on "+str(r))

#print()
#6.    С клавиатуры вводятся N чисел.

#Составьте программу, которая определяет количество отрицательных,

 #количество положительных и количество нулей среди введенных чисел.  

#Значение N вводится с клавиатуры.
print("Sisesta 10 numbrid, mis teile meeldivad.")
plus=0
minus=0
null=0
i=0
while i<10:
    i+=1
    num=float(input("Sisesta {0}.arv ".format(i)))
    if num>0:
        plus+=1
    if num<0:
        minus+=1
    if num==0:
        null+=1
print("positiivsed numbrid: ",plus)
print("negatiivsed numbrid: ",minus)
print("nullinumbrid: ",null)
#TARpv23 Timur Basirov
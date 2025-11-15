annee=int(input("Veuillez entrer l\'annee : "))
if (annee%4==0 and annee%100!=0 )or annee%400==0:
    print("L\'annee est bissextile✅")
else:
    print("L\'anne n'est pas bissextile❌")
print("\n")    
print("\tMerci bien 😁")  
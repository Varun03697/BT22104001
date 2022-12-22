grossincome=int(input("Gross Income:"))
noofdependents=int(input("No. of dependents:"))

taxableincome=(grossincome-10000-(noofdependents * 3000))
print("Tax:",taxableincome*(20/100))








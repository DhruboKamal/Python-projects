#if the numer is even
# NOTE: cd E:\Codes\Python projects
hrs=input("Enter Hours:")
rate=input("Enter Rate:")
hrs=float(hrs)
rate=float(rate)
if hrs>40:
    print(40*rate+(hrs-40)*rate*1.5)
else:
    print(hrs*rate)

print (" Hello Galaxy")

# using git  via PyCharm

# Payment

def computepay(h,r):
    if h>45:
        return (40*r) + (h-40)*(r*1.5)
    else :
        return (h*r)*g

hrs = input("Enter Hours-Gunluk Çalışma Saati:")
h=float(hrs)
rate=input("Enter Rate-Saatlik Ücret:")
r=float(rate)
gun=input("Calısılan toplam gun:")
g=float(gun)

p = computepay(h,r)
print("Pay-Brut Ucret",p)

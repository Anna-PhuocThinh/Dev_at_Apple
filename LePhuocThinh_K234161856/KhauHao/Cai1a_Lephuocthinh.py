#Cau 1A
C0 = float(input("Chi phi dau tu ban dau la: "))
Ct = float(input("So tien du kien nhan duoc moi nam: "))
t =  float(input("Thoi gian thuc hien du an: "))
r = float(input("Lai suat chiet khau: "))

i=1
S = 0

while i <= t:
    C = Ct/((1+r)**i)
    S = S + C
    i = i+1

NPV = S - C0
print("NPV= ",NPV)

#Cau 1B

if NPV > 0:
    print("Dự án sinh lời, nên đầu tư.")
elif NPV < 0:
    print("Dự án không sinh lời, không nên đầu tư.")
else:
    print("Dự án hòa vốn.")

import math as mt
def calculateN(delta_p, delta_s, ws, wp):
    p = 1/(delta_p**2)
    q = 1/(delta_s**2)
    k1, k2  = (q - 1) / (p - 1), ws / wp
    
    num = k1**(0.5)
    denom = k2 
    
    return mt.log10(num) / mt.log10(denom)

def calculateCutoff(delta_p, wp, N):
    p = 1/(delta_p**2)
    denom = (p - 1) ** (1/(2*N))
    num = wp
    return num / denom

def calulateCoef(N):
    for i in range(1, N // 2 + 1):
        omega = ((2*i - 1)/(2*N))*mt.pi
        bk = 2*mt.sin(omega) 
        bk_formatted = "{0:.5g}".format(bk)
        print(f"Here is b{i} : {bk_formatted}")
        
print("Input User Specification (1 - dp, ds, ws, wp) below: \n(pls note that every specification is seperated by a SPACE)\nEX : 1 1 1 1")
(dp, ds, ws, wp) = map(lambda x: float(x) , input(">").split())

n = mt.ceil(calculateN(dp, ds, ws, wp))
print(f"N is {n}")
wc = calculateCutoff(dp, wp, n)
wc_formatted = "{0:.5g}".format(wc)
print(f"cutoff is {wc_formatted}")


calulateCoef(n)
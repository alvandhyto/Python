import math as mt
def calculateE(delta_s, delta_p, ws, wp):
    p = 1/(delta_p ** 2)
    return (p - 1) ** 0.5

def calculateN(delta_s, delta_p, ws, wp):
    p = 1/(delta_p**2)
    q = 1/(delta_s**2)
    k1, k2  = (q - 1) / (p - 1), ws / wp
    
    num = k1**(0.5)
    denom = k2 
    
    return mt.acosh(num) / mt.acosh(denom)

def calculateCoef(e, N):
    p = 1/e 
    q = 1 + p**2
    k = (q ** 0.5 + p)
    dn = 0.5 * (k ** (1/N) - k ** (-1/N))
    dn_formatted = "{0:.5g}".format(dn)
    
    print(f"Here is Co : {dn_formatted}")
    for i in range(1, N // 2 + 1):
        omega = ((2*i - 1)/(2*N))*mt.pi
        ck = dn**2 + (mt.cos(omega))**2
        ck = "{0:.5g}".format(ck)
        bk = 2 * dn*mt.sin(omega)
        bk = "{0:.5g}".format(bk)
        
        print(f"Here is c{i} : {ck}")
        print(f"Here is b{i} : {bk}")
        
print("Input User Specification (1 - dp, ds, ws, wp) below: \n(pls note that every specification is seperated by a SPACE)\nEX : 1 1 1 1")
(dp, ds, ws, wp) = map(lambda x: float(x) , input(">").split())
e = calculateE(ds, dp, ws, wp)
e_formatted = "{0:.5g}".format(e)
print(f"E is {e_formatted}")
n = mt.ceil(calculateN(ds, dp, ws, wp))
print(f"N is {n}")
calculateCoef(e, n)
        
    
    
    
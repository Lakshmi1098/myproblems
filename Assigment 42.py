def find_factors(num):
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    max=0
    for i in range(0,len(list_of_factors)):
        if(max<list_of_factors[i]and is_prime(list_of_factors[i],list_of_factors[i]-1)):
            max=list_of_factors[i]
    return max

def find_f(num):
    list_of_factors=find_factors(num)
    return find_largest_prime_factor(list_of_factors)

def find_g(num):
    g=find_f(num)+find_f(num+1)+find_f(num+2)+find_f(num+3)+find_f(num+4)+find_f(num+5)+find_f(num+6)+find_f(num+7)+find_f(num+8)
    return g

print(find_g(10))

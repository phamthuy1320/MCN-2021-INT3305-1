# -*- coding: utf-8 -*-
# N: tổng số lần
# n: số lần sai
# r: số lần đúng
# p:xác suất đúng
import math
def factorial(n):
    fact = 1
    if(n==0 or n ==1):
        return fact
    else:
        for i in range(2,n+1):
            fact = fact*i
        return fact
def combination(N,n):
    fact_N = factorial(N)
    fact_n = factorial(n)
    fact_N_n = factorial(N-n)
    comb = fact_N/(fact_n*fact_N_n)
    return comb


def propb(n,p,r):
	Pr = combination((n+r-1),n)*(p**r)*(1-p)**(n)
	return Pr

def infoMeasure(n,p,r):
	Pr = propb(n,p,r)
	Ix = -(math.log(Pr,2))
	return Ix

def sumProb(N,p, r):
	sum = 0
	for n in range(1,N-r+1):
		# print(n)
		pr = propb(n,p,r)
		sum+=pr
	return sum

def approxEntropy(N,p, r):
	En = 0
	for n in range(1,N-r+1):
		Hx = propb(n,p,r)*infoMeasure(n,p,r)
		En+=Hx
	return En/N

print('1c) NegBinomial')
print('+ propability (6,0.3,4):',propb(6,0.3,4))
print('+ Information source (6,0.3,4):',infoMeasure(6,0.3,4))

print('+ Sum propabilities (N,p,r) = (6,0.3,4):',sumProb(6,0.3,4))
print('+ Approximate Entropy (N,p,r)= (6,0.3,4):', approxEntropy(6,0.3,4))
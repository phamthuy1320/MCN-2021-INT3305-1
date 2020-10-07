# -*- coding: utf-8 -*-
# N: tổng số lần
# n: số lần sai cho đến khi đúng 
# p: xác suất sai
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


def propb(n,p,N):
	Pr = combination(N,n)*(p**n)*(1-p)**(N-n)
	return Pr

def infoMeasure(n,p, N):
	Pr = propb(n,p, N)
	Ix = -(math.log(Pr,2))
	return Ix

def sumProb(N, p):
	sum = 0
	for n in range(1,N+1):
		# print(n)
		pr = propb(n,p, N)
		sum+=pr
	return sum

def approxEntropy(N,p):
	En = 0
	for n in range(1,N+1):
		Hx = propb(n,p,N)*infoMeasure(n,p,N)
		En+=Hx
	return En/N

print('1b) Binomial')
print('+ propability (4,0.3,6):',propb(4,0.3,6))
print('+ Information source (4,0.3,6):',infoMeasure(4,0.3,6))

print('+ Sum propabilities (N,p) = (6,0.3):',sumProb(6,0.3))

print('Gỉa sử N=200, p=0.3=>sum propabilities:',sumProb(200,0.3))
print('Sấp xỉ 1')
print('+ Approximate Entropy (N,p) = (6,0.3):', approxEntropy(6,0.3))
print('Với x=1/2, sử dụng approxEntropy*N:lấy N=200 ', approxEntropy(500,0.5)*500)
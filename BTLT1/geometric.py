# -*- coding: utf-8 -*-
# N: tổng số lần tung
# p: xác suất sai
import math
def propb(n, p):
	Pr = ((1-p)**(n-1))*p
	return Pr

def infoMeasure(n, p):
	Pr = propb(n,p)
	Ix = -(math.log(Pr,2))
	return Ix

def sumProb(N, p):
	'''
	Khi N tiến đến vô cùng thì tổng xác suất tiến tới 1
	Vì:
		\sum_{n=0}^{\infty}P\left ( X \right ) = \sum_{n=0}^{\infty}\left ( 1-p \right )^{n}p = p\sum_{n=0}^{\infty}\left ( 1-p \right )^{n},\break
	(1-p)<1
	=>\sum_{n=0}^{\infty}P\left ( X \right ) =\frac{p}{1-(1-p))}=\frac{p}{p}=1
    	
	Ảnh ./1a_4.png
	'''
	sum = 0
	for n in range(1,N+1):
		# print(n)
		pr = propb(n,p)
		sum+=pr
	return sum

def approxEntropy(N,p):
	'''
	Với p=1/2=>
		H\left ( X \right ) = \sum_{n=1}^{\infty}\frac{n}{2^n} = \sum_{n=1}^{\infty}(\frac{n+1}{2^n} - \frac{1}{2^n}) = 2\sum_{n=2}^{\infty}\frac{n}{2^n} - 1
\break
H\left ( X \right ) = 2\times\left (H\left ( X \right )-\frac{1}{2}   \right ) -1=2
Ảnh (./1a_5.png)

	'''
	En = 0
	for n in range(1,N):
		Hx = propb(n,p)*infoMeasure(n,p)
		En+=Hx
	return En/N

print('1a) GeoMetric')
print('+ propability (15,0.03):',propb(15,0.03))

print('+ Information source (15,0.03):',infoMeasure(15,0.03))

print('+ Sum propabilities (N,p) = (15,0.03):',sumProb(15,0.03))
print(sumProb.__doc__)
print('Gỉa sử N=200, p=0.03=>sum propabilities:',sumProb(200,0.03))
print('Sấp xỉ 1')

print('+ Approximate Entropy (N,p) = (15,0.03):', approxEntropy(15,0.03))
print(approxEntropy.__doc__)
print('Với x=1/2, sử dụng approxEntropy*N:lấy N=200 ', approxEntropy(200,0.5)*200)

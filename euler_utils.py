from math import sqrt

phi = (sqrt(5)+1)/2

"""
	Returns the Collatz sequence for n
"""
def collatz(n):
	if n <= 0:
		return None
	else:
		seq = []
		while n > 1:
			seq.append(n)
			if (n%2):	n = 3*n+1
			else:		n /= 2
		return seq

"""
	Checks if input integer or string is a palindrome, code pulled from http://stackoverflow.com/a/18959976/760318
"""
def isPalindrome(n):
	string = str(n)
	for i,char in enumerate(string):
		if char != string[-i-1]:
			return False
	return True

"""
	Finds all proper divisors of n, where a proper divisor of n is k such that n % k == 0
	
	Restricted to positive n for now
"""
def findAllDivisors(n):

	if not (n > 1):
		return None

	divs = [1]
	
	if n > 2:
		for k in range(2,n):
			if n % k == 0:
				if k not in divs:
					divs.append(k)
		
	
	return sorted(divs)

"""
	Returns true if and only if the input number's divisors sum to a value larger than itself
	
	Tested only on positive integers
"""
def isAbundant(num):
	if num <= 0:	return None
	divisors = findAllDivisors(num)
	return sum(divisors) > num

"""
	Pulled from http://stackoverflow.com/a/16996439/760318
	
	Returns all prime factors for n
"""
def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

"""
	Returns the n-th Fibonacci number as computed by Binet's formula: 
		Fib(n) = ( (phi)^n - (-phi)^-n ) / sqrt(5)
	Where phi = (1 + sqrt(5))/2
"""
def fib(n):
	global phi
	return int( ( phi ** n - (-phi) ** -n ) / sqrt(5) )
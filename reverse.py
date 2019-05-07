n=-123
rev=0
if n<0:
	num=n
	while(num!=0):
	 rem=num%10
	 rev=(rev*10)+rem
	 num=num//10
print(rev)
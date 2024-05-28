# Finding the 3N+1 Sequence
# Given a positive integer, N, define the 3N+1 sequence starting from N as follows:

# If N is an even number, then divide N by two.
# If N is an odd number, then multiply N by 3 and add 1.
# Continue to generate numbers in this way until N becomes equal to 1.

n=int(input("value :"))
while n !=1:
    if n%2==0:
        n=n//2
        print(f" even {n}")
    else:
        n=n*3+1
        print(n)


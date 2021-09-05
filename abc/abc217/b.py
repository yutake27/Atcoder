s1 = input()
s2 = input()
s3 = input()

contests = set(['ABC', 'ARC', 'AGC', 'AHC'])
contests.remove(s1)
contests.remove(s2)
contests.remove(s3)
print(contests.pop())

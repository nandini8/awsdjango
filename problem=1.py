n=1000
mulof3 = [x for x in range(0,n,3)]
mulof5 = [x for x in range(0,n,5)]
print(sum(set(mulof5),set(mulof3)))
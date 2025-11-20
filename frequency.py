test_dic={
    "codingal":2,
    "for":2,
    "coding":1,
    "is":2,
    "best":2
}
k=2
res=0
for key in test_dic:
    if test_dic[key]==k:
        res=res+1
print("The frequency is",res,"times of", k)
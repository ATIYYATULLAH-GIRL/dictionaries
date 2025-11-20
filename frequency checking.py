dic={
    "atiyyatullah":2,
    "sana":5,
    "lindani":1,
    "iranzi":9,
    "aparna":2,
    "gungun":9
}
a=9
ans=0
for key in dic:
    if dic[key]==a:
        ans=ans+1
print("The frequency is",ans,"times of",a)
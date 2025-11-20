dict={
    "classmate1":{
        "name":"Sana",
        "grade":"12"
    },
    "classmate2":{
        "name":"Lindani",
        "grade":"7"
    },
    "classmate3":{
        "name":"Atiyyatullah",
        "grade":"7"
    },
    "classmate4":{
        "name":"Lindani",
        "grade":"7"
    }
}
result={}
for key,value in dict.items():
    if value not in result.values():
        result[key]=value
print(result)
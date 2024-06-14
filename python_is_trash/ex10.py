# # 4. Есть src = 'www.google.com'
# a. заслайсить src так что-бы осталось только google
# b. заслайсить src так что-бы осталось только www
# c. заслайсить src так что-бы осталось только .com

src = 'www.google.com'
print(src[src.find("g"):src.find("e") + 1])
print(src[0:3])
print(src[-4:])
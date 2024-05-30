# Есть `src = 'www.google.com'`
#  - Заслайсить `src`, чтобы осталось только `google`.
#  - Заслайсить `src`, чтобы осталось только `www`.
#  - Заслайсить `src`, чтобы осталось только `.com`.

src = "www.google.com"
print(src[4:-4])
print(src[0:4])
print(src[-4:])
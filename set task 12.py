a="suruthika"
same=set()
for ch in a:
    if ch in same:
        print("false")
        break
    same.add(ch)
else:
     print("false")


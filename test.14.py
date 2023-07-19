num=int(input("구입음악개수:"))
price=400*num
discount=price * 30 / 100
total = price-discount

print("총가격:%s"%price)
print("할인금액:%s"%discount)
print("구입가격:%s"%total)
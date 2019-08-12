cc = input("Swipe the card")
cc_number = cc.split('^')[0]
cc_name = cc.split('^')[1]
cc_exp = cc.split('^')[2]
cc_date = cc_exp[:4]

print("Card Number: " + cc_number)
print("Card Holder: " + cc_name)
print("Expiration Date: " + cc_date)

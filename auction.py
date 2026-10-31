Blind_auction={}
a=True

while a==True:
    name = input("Enter your Name")
    Blind_auction[name] = int(input("Enter your Bidding amount"))

    h=input("Are there any other Bidders Type yes or no").lower()

    if h=="no":
        a=False
    else:
        print("\n"*1000)
bid=0
nam=""
for key in Blind_auction:
    if Blind_auction[key]>bid:
        bid=Blind_auction[key]
        nam=key
print(nam+f":{bid}")

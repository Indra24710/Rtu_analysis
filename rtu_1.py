for j in range(4):
    i=0
    social=0.00
    shop=0.00
    games=0.00 
    stream=0.00
    print("enter the string")
    string=input()
    new=string.split(" ")
    while(i<len(new)):
        if((new[i]=="Instagram")or(new[i]=="Pro")or(new[i]=="WhatsApp")or(new[i]=="Snapchat")or(new[i]=="Messenger")or(new[i]=="Twitter")or(new[i]=="Lite")or(new[i]=="Facebook")or(new[i]=="Pinterest")):
            i=i+1
            
            

            social=social+ float((new[i]))
        else:
            if((new[i]=="Shopping")or(new[i]=="Pro")or(new[i]=="Flipkart")or(new[i]=="eBay")or(new[i]=="Paytm")or(new[i]=="Uber")or(new[i]=="OlaCabs")or(new[i]=="BookMyShow")or(new[i]=="Walmart")or(new[i]=="Snapdeal")or(new[i]=="Zomato")or(new[i]=="BookMyShow")or(new[i]=="Swiggy")):
                i=i+1
                shop=shop+float((new[i]))
            else:
                if((new[i]=="Netflix")or(new[i]=="Pro")or(new[i]=="Video")or(new[i]=="Music")or(new[i]=="Store")or(new[i]=="Spotify")or(new[i]=="YouTube")or(new[i]=="Hotstar")or(new[i]=="Netflix")or(new[i]=="TV")or(new[i]=="Hotstar")):
                    i=i+1
                    stream=stream+float((new[i]))
                else:
                    if((new[i]=="Mobile")or(new[i]=="Pro")or(new[i]=="Space")or(new[i]=="Cars")or(new[i]=="Royale")or(new[i]=="Clans")or(new[i]=="Games")or(new[i]=="Walmart")):
                       i=i+1
                       games=games+float((new[i]))
        i=i+1
    social_daily.append(social)
    shop_daily.append(shop)
    games_daily.append(games)
    stream_daily.append(stream)
import matplotlib.pyplot as plt
import numpy as np
objects = ['social_daily','shop_daily','stream_daily','games']

y_pos = np.arange(len(objects))
performance = [sum(social_daily)/11,sum(shop_daily)/11,sum(stream_daily)/11,sum(games_daily)/11]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage hrs per week')
plt.title('Phone Usage analysis')

plt.show()

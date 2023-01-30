import bitcoin_price
import abc_pattern_methods
import time

print("This app is recommendedly used by traders who are familiar with Eliot's wave theory and have no self-control.")
print("It's a work in progress.")
print("Current version only supports 5 min timescale.")

# selectedCrypto = input("Please enter the cryto you wanna analyse(1 = BTC, 2 = ETH")
# direction = input("Select your trading mode(1 = long, 2 = short")

currentWave = input("Enter the current wave you analyzed(1 = B, 2 = C)  :  ")
startPointOfA = float(input("Enter the start point of your analysed A wave  :  "))
endPointOfA = float(input("Enter the end point of your analysed A wave  :  "))


flag = True

while flag:
    price = bitcoin_price.coins[0]['quote']['USD']['price']

    print(price)

    print(abc_pattern_methods.Get_382_In_B_Wave(startPointOfA, endPointOfA))
    print(abc_pattern_methods.Get_5_In_B_Wave(startPointOfA, endPointOfA))
    print(abc_pattern_methods.Get_618_In_B_Wave(startPointOfA, endPointOfA))

    if(price <= abc_pattern_methods.Get_382_In_B_Wave(startPointOfA, endPointOfA) * 1.001 
    and price >= abc_pattern_methods.Get_382_In_B_Wave(startPointOfA, endPointOfA) * 0.999):
        print("We mildly suggest you to buy/sell now")

    if(price <= (abc_pattern_methods.Get_5_In_B_Wave(startPointOfA, endPointOfA) * 1.001) 
    and price >= (abc_pattern_methods.Get_5_In_B_Wave(startPointOfA, endPointOfA) * 0.999)):
        print("We moderately suggest you to buy/sell now")

    if(price <= abc_pattern_methods.Get_618_In_B_Wave(startPointOfA, endPointOfA) * 1.001 
    and price >= (abc_pattern_methods.Get_618_In_B_Wave(startPointOfA, endPointOfA) * 0.999)):
        print("We strongly suggest you to buy/sell now")

    # Sleep for 5 minutes (5 * 60 seconds)
    time.sleep(5 * 60)
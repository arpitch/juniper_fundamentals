# # Let's shop'
#
# The dictionary will contain mappings of items for an online store
# The items will have the item name as the key and then the corresponding quantity and price as value. I.e, sneakers is the name of the item, and 1, 120 as the corresponding quantity and price
# The dictionary should have at least 5 items. More is fine.
# Display all the keys in the dictionary
# Display all the values in the dictionary
# Iterate over the dictionary and display the key/ value pairs
# Create a new dictionary called sale and only add items from the sopping_cart dictionary that are <= $10. If there's no items that's less than $10, then update the dictionary with two items that are <= $10 :wink:
# .

sale = {}
shop_cart = {
             'milk':[100, 12],
             'butter':[50, 3],
             'chips':[75, 4],
             'bread':[45, 4],
             'pasta':[50, 15]
            }
print('here are the keys ')
for key in shop_cart:
        print(key)

print('here are the values ')
for value in shop_cart:
     print(shop_cart[value])

print('here are the key/value pairs ')
for key, value in shop_cart.items():
    print('item :',key, "=>", 'quantity :',value[0] ,'price :',value[1] )
    if (value[1]) <= 10:
         sale.update({key:value})
 # this can also work instead of sale.update -   sale[key] = value

print('here are the sale items less than $10 ')
for key, value in sale.items():
    print('sale item :', key, "=>", 'quantity :', value[0], 'price :', value[1])

# Travel Packing List and Selection
packing_list = ['clothes', 'toothbrush', 'passport', 'camera']
item_to_check = 'passport'

# TODO: Write a line of code to check if the item_to_check is in the packing_list
is_item_packed = item_to_check in packing_list


# TODO: Find the index of item_to_check in the list if it is packed, otherwise set it to -1
if is_item_packed is True:
  item_index = packing_list.index(item_to_check) if is_item_packed else -1
print(item_index)


# Print out the results
print("Is the item packed?", is_item_packed)
print("Item index:", item_index)
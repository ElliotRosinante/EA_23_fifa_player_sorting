import unicodedata
def check_how_unicode_is_affected_in_string_matching():
    
    if "jose" in "Diogo José".lower():
        print("unicode doesn't matter")
        print(True)

    elif "josé" in "Diogo José".lower():
        print("yh, unicode matters")
        print(True)


# check_how_unicode_is_affected_in_string_matching()
# yh, unicode matters
# True

def check_how_unicode_is_affected_in_string_matching_after_we_normalize_the_unicode():
    print(unicodedata.normalize('NFC',"Diogo José".lower()))
    # diogo josé
   
    if "jose" in unicodedata.normalize('NFC',"Diogo José".lower()):
        print("unicode doesn't matter after we have normalized it")
        print(True)

    # elif "josé" in "Diogo José".lower():
    #     print("yh, unicode matters")
    #     print(True)
    

# check_how_unicode_is_affected_in_string_matching_after_we_normalize_the_unicode()

def the_right_way_to_approach_the_ignoring_of_ascciCode():
    player_name = unicodedata.normalize('NFD', "Diogo José").encode('ascii', 'ignore').decode('utf-8').lower()
    if "jose" in player_name:
        print("Yes! This really did work")
the_right_way_to_approach_the_ignoring_of_ascciCode()

# playing with code to see and understand how it truly works 
num_keys = 5
indices = [0] * num_keys

print(indices)
# [0, 0, 0, 0, 0]

fruits = ["watermelon","pineapple","mango","apple"]
num_fruits = len(fruits)

# to print the members of a list that starts printing form the last member down to the last one in reverse order.
for i in range(num_fruits-1,-1,-1):
    print(fruits[i])
    
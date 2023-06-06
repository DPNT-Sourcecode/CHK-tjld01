

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sum = 0
    item_dict = {}
    for item in skus:
        if item not in "ABCD":
            return -1
        if item == "A" and not in item_dict:
            item_dict["A"] = 1
        if item == "B":
            ret


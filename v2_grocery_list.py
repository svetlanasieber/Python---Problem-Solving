def shop_from_grocery_list(*args):
    budget, grocery_list, *data = args
    my_budget = float(budget)
    missing_product = []
    dic = {}
    buy_product = []
    flag = False

    for product, price in data:
        if product not in dic.keys():
            dic[product] = float(price)

    for product, price in dic.items():
        if product in grocery_list:
            if (my_budget - price) < 0:
                missing_product.append(product)
                buy_product.append(product)
                flag = True
                break
            else:
                my_budget -= price
                buy_product.append(product)

    for product in grocery_list:
        if product not in dic.keys():
            missing_product.append(product)

    if flag:
        for product in dic.keys():
            if product not in buy_product:
                missing_product.append(product)

    if missing_product:
        return f"You did not buy all the products. Missing products: {', '.join(missing_product)}."
    else:
        return f"Shopping is successful. Remaining budget: {my_budget:.2f}."


print(shop_from_grocery_list(
    0,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
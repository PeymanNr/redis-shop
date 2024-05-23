from redis_client import (
    get_product,
    add_product,
    add_to_cart,
    remove_from_cart,
    get_cart_items
)

while True:
    commands = ['add_product', "get_product", 'add_to_card',
                'remove_from_cart', 'cart_items']
    command = input("what are you command: ")
    if command not in commands:
        print('command you entered is wrong')

    if command == 'add_product':
        get_product_input = input("send product id")
        add_product_title_input = input("send product title")
        add_product(product_id=get_product_input,
                    title=add_product_title_input)

    elif command == 'get_product':
        get_product_input = input("send product id for get product: ")
        get_product(product_id=get_product_input)

    elif command == 'add_to_cart':
        get_product_input = input("send product id for add to cart: ")
        get_product_quantity = input("enter quantity product :")
        add_to_cart(product_id=get_product_input,
                    quantity=get_product_quantity)

    elif command == 'remove_from_cart':
        get_product_input = input('enter product id for remove from cart:')
        remove_from_cart(product_id=get_product_input)

    elif command == 'cart_items':
        get_cart_items()

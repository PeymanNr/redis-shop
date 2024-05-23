import redis


def connect():
    try:
        client = redis.Redis(host="localhost", port=6379)

        return client

    except Exception as e:
        print("Error connecting to Redis server:", e)


def add_product(product_id, title):
    client = connect()
    client.set(product_id, title)


def get_product(product_id):
    client = connect()
    product_data = client.get(product_id)
    print(product_data)


def add_to_cart(product_id, quantity):
    client = connect()
    client.zadd("cart", {product_id: quantity})


def remove_from_cart(product_id):
    client = connect()
    client.zrem("cart", product_id)


def get_cart_items():
    client = connect()
    items = client.zrange('cart', 0, -1, withscores=True)
    print(items)


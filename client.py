import requests

# Base URL of the API
BASE_URL = "http://127.0.0.1:8000/products"

# Function to add a new product
def add_product(name: str, description: str, price: float):
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=data)
    
    if response.status_code == 201:
        print(f"Product created successfully: {response.json()}")
    else:
        print(f"Failed to create product: {response.status_code}, {response.text}")

# Function to get all products
def get_products():
    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        products = response.json()
        print("List of products:")
        for product in products:
            print(f"Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    else:
        print(f"Failed to retrieve products: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Adding products
    add_product("Laptop", "A high-end gaming laptop", 1500.00)
    add_product("Smartphone", "Iphone 16", 800.00)

    # Retrieve and print all products
    get_products()

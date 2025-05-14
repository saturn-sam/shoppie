
import os
import requests
import json
import time

# Configuration
AUTH_SERVICE_URL = os.environ.get('AUTH_SERVICE_URL', 'http://auth-service:8000')
ADMIN_SERVICE_URL = os.environ.get('ADMIN_SERVICE_URL', 'http://admin-service:5000')
CLIENT_SERVICE_URL = os.environ.get('CLIENT_SERVICE_URL', 'http://client-service:5000')

# Sample data
ADMIN_USER = {
    'username': 'admin',
    'email': 'admin@example.com',
    'password': 'adminpassword',
    'is_staff': True
}

REGULAR_USER = {
    'username': 'user',
    'email': 'user@example.com',
    'password': 'userpassword',
    'is_staff': False
}

SAMPLE_PRODUCTS = [
    {
        'name': 'Wireless Headphones',
        'description': 'High-quality wireless headphones with noise cancellation.',
        'price': 99.99,
        'quantity': 50,
        'image': 'https://images.unsplash.com/photo-1618160702438-9b02ab6515c9'
    },
    {
        'name': 'Smartphone',
        'description': 'Latest model smartphone with advanced camera and long battery life.',
        'price': 699.99,
        'quantity': 25,
        'image': 'https://images.unsplash.com/photo-1582562124811-c09040d0a901'
    },
    {
        'name': 'Laptop',
        'description': 'Powerful laptop perfect for work and gaming.',
        'price': 1299.99,
        'quantity': 15,
        'image': 'https://images.unsplash.com/photo-1721322800607-8c38375eef04'
    },
    {
        'name': 'Smart Watch',
        'description': 'Track your fitness and stay connected with this stylish smart watch.',
        'price': 199.99,
        'quantity': 30,
        'image': 'https://images.unsplash.com/photo-1618160702438-9b02ab6515c9'
    }
]

def wait_for_services():
    """Wait for all services to be ready"""
    services = [
        (AUTH_SERVICE_URL, 'auth'),
        (ADMIN_SERVICE_URL, 'admin'),
        (CLIENT_SERVICE_URL, 'client')
    ]
    
    for url, name in services:
        print(f"Waiting for {name} service...")
        health_url = f"{url}/health"
        max_retries = 10
        retries = 0
        
        while retries < max_retries:
            try:
                response = requests.get(health_url, timeout=5)
                if response.status_code == 200:
                    print(f"{name.capitalize()} service is ready!")
                    break
            except requests.RequestException:
                pass
            
            retries += 1
            print(f"Waiting for {name} service... Attempt {retries}/{max_retries}")
            time.sleep(5)
            
        if retries == max_retries:
            print(f"Error: {name} service not available after {max_retries} attempts")
            return False
    
    return True

def create_user(user_data):
    """Create a user in the auth service"""
    try:
        url = f"{AUTH_SERVICE_URL}/api/auth/register/"
        response = requests.post(url, json=user_data)
        
        if response.status_code == 201:
            user_info = response.json()
            print(f"Created user: {user_data['username']}")
            return user_info
        else:
            print(f"Failed to create user {user_data['username']}: {response.text}")
            return None
    except Exception as e:
        print(f"Error creating user: {str(e)}")
        return None

def login_user(username, password):
    """Login and get JWT token"""
    try:
        url = f"{AUTH_SERVICE_URL}/api/auth/login/"
        response = requests.post(url, json={
            'username': username,
            'password': password
        })
        
        if response.status_code == 200:
            auth_data = response.json()
            print(f"Logged in as: {username}")
            return auth_data['token']
        else:
            print(f"Failed to login as {username}: {response.text}")
            return None
    except Exception as e:
        print(f"Error logging in: {str(e)}")
        return None

def create_products(token):
    """Create sample products using admin token"""
    if not token:
        print("No admin token available, skipping product creation")
        return False
        
    headers = {'Authorization': f'Bearer {token}'}
    products_created = 0
    
    for product in SAMPLE_PRODUCTS:
        try:
            url = f"{ADMIN_SERVICE_URL}/api/products"
            response = requests.post(url, json=product, headers=headers)
            
            if response.status_code == 201:
                product_data = response.json()
                print(f"Created product: {product['name']}")
                products_created += 1
            else:
                print(f"Failed to create product {product['name']}: {response.text}")
        except Exception as e:
            print(f"Error creating product: {str(e)}")
    
    print(f"Created {products_created} out of {len(SAMPLE_PRODUCTS)} products")
    return products_created > 0

def main():
    """Initialize sample data for all services"""
    print("Starting initialization...")
    
    # Wait for services to be ready
    if not wait_for_services():
        print("Services not ready, aborting initialization")
        return
    
    # Create admin user
    admin_info = create_user(ADMIN_USER)
    
    # Create regular user
    user_info = create_user(REGULAR_USER)
    
    # Get admin token for creating products
    admin_token = login_user(ADMIN_USER['username'], ADMIN_USER['password'])
    
    # Create sample products
    if admin_token:
        create_products(admin_token)
    
    print("Initialization complete!")

if __name__ == "__main__":
    main()

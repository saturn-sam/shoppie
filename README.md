
# Shoppie - Microservices E-Commerce Application

This is a microservices-based e-commerce application demo built with React, Django, Flask, redis and RabbitMQ.
This project is only for test and understanding of microservice architecture. This was developped for seamless test of microservice and deployment of the services on a kubernetes cluster as well as on docker compose. 

## Architecture

The application consists of:

1. **React Frontend** - Single frontend application with role-based UI
2. **Auth Service (Django/DRF)** - Handles user authentication
3. **Inventory Management Service (Flask)** - Product and inventory management
4. **Product Catalog Service (Flask)** - Product display for customers
5. **Cart Service (Flask)** - Shopping cart management
6. **Order Service (Flask)** - Order processing and management
7. **Payment Service (Flask)** - Payment processing
8. **Shipping Service (Flask)** - Shipping and fulfillment
9. **Analytics Service (Flask)** - Business analytics and reporting
10. **RabbitMQ** - Message queue for inter-service communication

## Repositories of all services:
1. **React Frontend** - [https://github.com/saturn-sam/shoppie-frontend]
2. **Auth Service (Django/DRF)** - [https://github.com/saturn-sam/shoppie-auth]
3. **Inventory Management Service (Flask)** -[https://github.com/saturn-sam/shoppie-inventory-service]
4. **Product Catalog Service (Flask)** - [https://github.com/saturn-sam/shoppie-product-catalog-service]
5. **Cart Service (Flask)** - [https://github.com/saturn-sam/shoppie-cart-service]
6. **Order Service (Flask)** - [https://github.com/saturn-sam/shoppie-order-service]
7. **Payment Service (Flask)** - [https://github.com/saturn-sam/shoppie-payment-service]
8. **Shipping Service (Flask)** - [https://github.com/saturn-sam/shoppie-shipping-service]
9. **Analytics Service (Flask)** - [https://github.com/saturn-sam/shoppie-analytics-service]

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Node.js (for local development)
- python

### Running with Docker Compose

1. Clone the repository
2. Start the services:

```bash
chmod u+x setup.sh
```

```bash
sh setup.sh
```

```bash
docker-compose up -d
```

3. Initialize the services (create admin user and sample data):

```bash
chmod +x scripts/init-services.sh
./scripts/init-services.sh
```

4. Access the application:
   - Frontend: http://localhost:3000
   - RabbitMQ Management: http://localhost:15672 (guest/guest)

### Development Setup

For development with hot reloading:

```bash
docker-compose -f docker-compose.dev.yml up -d
```

## Service Endpoints

### Auth Service (Port: 8000)

Authentication endpoints:
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `POST /api/auth/validate-token/` - Validate JWT token
- `GET /api/auth/user/` - Get current user details

### Inventory Management Service (Port: 5001)

Product management endpoints (staff only):
- `GET /api/products` - List all products
- `GET /api/products/<id>` - Get product details
- `POST /api/products` - Create new product
- `PUT /api/products/<id>` - Update product
- `DELETE /api/products/<id>` - Delete product

### Product Catalog Service (Port: 5002)

Customer-facing product endpoints:
- `GET /client-api/products` - List available products
- `GET /client-api/products/<id>` - Get product details
- `POST /client-api/products/<id>/like` - Like a product
- `GET /client-api/purchases` - Get user's purchase history

### Cart Service (Port: 5003)

Shopping cart endpoints:
- `GET /cart-api/cart` - Get user's cart
- `POST /cart-api/cart` - Add item to cart
- `PUT /cart-api/cart/<id>` - Update cart item quantity
- `DELETE /cart-api/cart/<id>` - Remove item from cart

### Order Service (Port: 5004)

Order management endpoints:
- `GET /order-api/orders` - List user's orders
- `POST /order-api/orders` - Create new order
- `GET /order-api/orders/<id>` - Get order details
- `POST /order-api/orders/<id>/cancel` - Cancel order
- `PUT /order-api/internal/orders/<id>/status` - Update order status (internal)

### Payment Service (Port: 5005)

Payment processing endpoints:
- `POST /payment-api/payments` - Process payment
- `GET /payment-api/payments/order/<orderId>` - Get payment status
- `GET /payment-api/payment-methods` - List saved payment methods
- `POST /payment-api/payment-methods` - Add payment method
- `POST /payment-api/payments/<id>/refund` - Process refund

### Shipping Service (Port: 5006)

Shipping and fulfillment endpoints:
- `GET /shipping-api/shipping/rates` - Get shipping rates
- `POST /shipping-api/shipments` - Create shipment
- `GET /shipping-api/shipments/tracking/<number>` - Get tracking details
- `GET /shipping-api/shipments/order/<orderId>` - Get order shipments

### Analytics Service (Port: 5007)

Analytics and reporting endpoints:
- `GET /analytics-api/analytics/sales` - Get sales data
- `GET /analytics-api/analytics/products` - Get product analytics
- `GET /analytics-api/analytics/users` - Get user analytics
- `GET /analytics-api/analytics/dashboard` - Get dashboard metrics
- `POST /analytics-api/analytics/activity` - Log user activity

## Message Queue Architecture

The application uses RabbitMQ with topic exchanges:

- Exchanges:
  - `product_events` - Product-related events
  - `order_events` - Order-related events
  - `payment_events` - Payment-related events
  - `shipping_events` - Shipping-related events

- Routing keys:
  - `product.created`
  - `product.updated`
  - `product.deleted`
  - `order.created`
  - `order.cancelled`
  - `payment.processed`
  - `payment.failed`
  - `shipment.created`
  - `shipment.updated`

## Service Communication

Services communicate through:
1. REST APIs for synchronous operations
2. RabbitMQ for asynchronous events
3. Consul for service discovery

## Default Admin User

- Username: admin
- Email: admin@example.com
- Password: admin

## Environment Variables

Each service requires specific environment variables. Check the `.env.example` file in each service directory for required variables.

## Monitoring and Logging

- RabbitMQ Management UI: http://localhost:15672
- Consul UI: http://localhost:8500

## License

This project is licensed under the MIT License.


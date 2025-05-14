# API Documentation

This document provides a comprehensive overview of the API endpoints for all services in the Shoppie Multi-Service application. Each service is described with its endpoints, HTTP methods, descriptions, and return data formats.

---

## Analytics Service

1. **GET** `/analytics-api/health`
   - Description: Health check for the analytics service.
   - Returns: `{ "status": "healthy", "service": "analytics-service" }`

2. **GET** `/analytics-api/analytics/sales`
   - Description: Retrieve sales analytics.
   - Returns: `{ "sales": [ { "date": "<string>", "total": <float>, ... } ] }`

3. **GET** `/analytics-api/analytics/products`
   - Description: Retrieve analytics for all products.
   - Returns: `[ { "productId": <int>, "views": <int>, "sales": <int>, ... } ]`

4. **GET** `/analytics-api/analytics/products/<int:product_id>`
   - Description: Retrieve analytics for a specific product.
   - Returns: `{ "productId": <int>, "views": <int>, "sales": <int>, ... }`

5. **GET** `/analytics-api/analytics/users`
   - Description: Retrieve user analytics.
   - Returns: `[ { "userId": <int>, "activity": [ { "type": "<string>", "timestamp": "<string>" } ], ... } ]`

6. **GET** `/analytics-api/analytics/dashboard`
   - Description: Retrieve dashboard analytics.
   - Returns: `{ "metrics": { "totalSales": <float>, "activeUsers": <int>, ... } }`

7. **POST** `/analytics-api/analytics/activity`
   - Description: Submit user activity analytics.
   - Returns: `{ "message": "Activity recorded successfully" }`

---

## Auth Service

1. **GET** `/auth/users/`
   - Description: Retrieve user-related data.
   - Returns: `{ "id": <int>, "username": "<string>", ... }`

2. **POST** `/auth/users/`
   - Description: Create a new user.
   - Returns: `{ "id": <int>, "username": "<string>", "message": "User created successfully" }`

3. **POST** `/auth/token/`
   - Description: Obtain authentication token.
   - Returns: `{ "token": "<string>", "refresh": "<string>" }`

4. **POST** `/auth/token/refresh/`
   - Description: Refresh authentication token.
   - Returns: `{ "token": "<string>" }`

---

## Cart Service

1. **GET** `/cart-api/health`
   - Description: Health check for the cart service.
   - Returns: `{ "status": "healthy", "service": "cart-service" }`

2. **GET** `/cart-api/cart`
   - Description: Retrieve the current user's cart.
   - Returns: `{ "items": [ { "productId": <int>, "quantity": <int>, ... } ] }`

3. **POST** `/cart-api/cart`
   - Description: Add an item to the cart.
   - Returns: `{ "message": "Item added to cart successfully" }`

4. **DELETE** `/cart-api/cart/<int:item_id>`
   - Description: Remove an item from the cart.
   - Returns: `{ "message": "Item removed from cart successfully" }`

---

## Inventory Service

1. **GET** `/inventory-api/health`
   - Description: Health check for the inventory service.
   - Returns: `{ "status": "healthy", "service": "inventory-service" }`

2. **GET** `/inventory-api/products`
   - Description: Retrieve all products in inventory.
   - Returns: `[ { "id": <int>, "name": "<string>", "stock": <int>, ... } ]`

3. **PUT** `/inventory-api/products/<int:product_id>`
   - Description: Update stock for a specific product.
   - Returns: `{ "message": "Stock updated successfully" }`

---

## Order Service

1. **GET** `/order-api/health`
   - Description: Health check for the order service.
   - Returns: `{ "status": "healthy", "service": "order-service" }`

2. **POST** `/order-api/orders`
   - Description: Create a new order.
   - Returns: `{ "orderId": <int>, "message": "Order created successfully" }`

3. **GET** `/order-api/orders`
   - Description: Retrieve all orders.
   - Returns: `[ { "id": <int>, "status": "<string>", ... } ]`

4. **GET** `/order-api/my-orders`
   - Description: Retrieve orders for the authenticated user.
   - Returns: `[ { "id": <int>, "items": [ { "name": "<string>", "quantity": <int>, ... } ], ... } ]`

5. **GET** `/order-api/orders/<int:order_id>`
   - Description: Retrieve details of a specific order.
   - Returns: `{ "id": <int>, "items": [ { "name": "<string>", "quantity": <int>, ... } ], ... }`

6. **POST** `/order-api/orders/<int:order_id>/cancel`
   - Description: Cancel a specific order.
   - Returns: `{ "message": "Order cancelled successfully" }`

7. **PUT** `/order-api/internal/orders/<int:order_id>/status`
   - Description: Update the status of an order (internal use).
   - Returns: `{ "message": "Order status updated successfully" }`

---

## Payment Service

1. **GET** `/payment-api/health`
   - Description: Health check for the payment service.
   - Returns: `{ "status": "healthy", "service": "payment-service" }`

2. **POST** `/payment-api/payments`
   - Description: Create a new payment.
   - Returns: `{ "paymentId": <int>, "message": "Payment processed successfully" }`

3. **GET** `/payment-api/payments/order/<int:order_id>`
   - Description: Retrieve payment details for a specific order.
   - Returns: `{ "orderId": <int>, "paymentDetails": { ... } }`

---

## Product Catalog Service

1. **GET** `/catalog-api/products`
   - Description: Retrieve all products.
   - Returns: `[ { "id": <int>, "name": "<string>", "price": <float>, ... } ]`

2. **GET** `/catalog-api/products/<int:product_id>`
   - Description: Retrieve details of a specific product.
   - Returns: `{ "id": <int>, "name": "<string>", "price": <float>, ... }`

3. **POST** `/catalog-api/products/<int:product_id>/like`
   - Description: Like a specific product.
   - Returns: `{ "message": "Product liked successfully" }`

4. **POST** `/catalog-api/products/<int:product_id>/purchase`
   - Description: Purchase a specific product.
   - Returns: `{ "purchaseId": <int>, "message": "Purchase successful" }`

5. **GET** `/catalog-api/purchases`
   - Description: Retrieve purchase history.
   - Returns: `[ { "id": <int>, "items": [ { "name": "<string>", "quantity": <int>, ... } ], ... } ]`

---

## Shipping Service

1. **GET** `/shipping-api/health`
   - Description: Health check for the shipping service.
   - Returns: `{ "status": "healthy", "service": "shipping-service" }`

2. **GET** `/shipping-api/shipping/rates`
   - Description: Retrieve shipping rates.
   - Returns: `[ { "rateId": <string>, "price": <float>, ... } ]`

3. **POST** `/shipping-api/shipments`
   - Description: Create a new shipment.
   - Returns: `{ "shipmentId": <int>, "message": "Shipment created successfully" }`

4. **GET** `/shipping-api/shipments/tracking/<tracking_number>`
   - Description: Track a shipment by tracking number.
   - Returns: `{ "trackingNumber": "<string>", "status": "<string>", ... }`

5. **GET** `/shipping-api/shipments/order/<int:order_id>`
   - Description: Retrieve shipment details for a specific order.
   - Returns: `{ "orderId": <int>, "shipmentDetails": { ... } }`

6. **POST** `/shipping-api/internal/shipments/<int:shipment_id>/update`
   - Description: Update shipment details (internal use).
   - Returns: `{ "message": "Shipment updated successfully" }`
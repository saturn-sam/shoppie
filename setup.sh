
#!/bin/bash
set -e
echo "Cloning all services..."
cd ..
git clone https://github.com/saturn-sam/shoppie-shipping-service.git
git clone https://github.com/saturn-sam/shoppie-product-catalog-service.git
git clone https://github.com/saturn-sam/shoppie-payment-service.git
git clone https://github.com/saturn-sam/shoppie-order-service.git
git clone https://github.com/saturn-sam/shoppie-inventory-service.git
git clone https://github.com/saturn-sam/shoppie-frontend.git
git clone https://github.com/saturn-sam/shoppie-cart-service
git clone https://github.com/saturn-sam/shoppie-analytics-service.git
git clone https://github.com/saturn-sam/shoppie-auth.git

cd shoppie


# Start services
echo "Starting services with Docker Compose..."
docker-compose up -d

# echo "Setup complete! The application is now running."
# echo "- Frontend: http://localhost:3000"
# echo "- Auth Service API: http://localhost:8000"
# echo "- Inventory Management Service API: http://localhost:5001"
# echo "- Product Catalog Service API: http://localhost:5002"
# echo "- Order Service API: http://localhost:5003"
# echo "- Payment Service API: http://localhost:5004"
# echo "- Shipping Service API: http://localhost:5005"
# echo "- Analytics Service API: http://localhost:5006"
# echo "- RabbitMQ Management: http://localhost:15672 (guest/guest)"
# echo ""
# echo "Default users:"
# echo "- Admin: username=admin, password=adminpassword"
# echo "- User: username=user, password=userpassword"


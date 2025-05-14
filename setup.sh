
#!/bin/bash
set -e

# Create directory structure
# echo "Creating directory structure..."
# mkdir -p frontend/src
# mkdir -p auth-service/users/migrations
# mkdir -p inventory-service
# mkdir -p product-catalog-service
# mkdir -p order-service
# mkdir -p payment-service
# mkdir -p shipping-service
# mkdir -p analytics-service

# Copy frontend files
# echo "Copying frontend files..."
# cp -r src/* frontend/src/
# cp package.json frontend/
# cp package-lock.json frontend/ 2>/dev/null || true
# cp tsconfig.json frontend/
# cp tsconfig.app.json frontend/ 2>/dev/null || true
# cp tsconfig.node.json frontend/ 2>/dev/null || true
# cp tailwind.config.ts frontend/
# cp postcss.config.js frontend/
# cp index.html frontend/
# cp vite.config.ts frontend/

# Start services
echo "Starting services with Docker Compose..."
docker-compose up -d

echo "Setup complete! The application is now running."
echo "- Frontend: http://localhost:3000"
echo "- Auth Service API: http://localhost:8000"
echo "- Inventory Management Service API: http://localhost:5001"
echo "- Product Catalog Service API: http://localhost:5002"
echo "- Order Service API: http://localhost:5003"
echo "- Payment Service API: http://localhost:5004"
echo "- Shipping Service API: http://localhost:5005"
echo "- Analytics Service API: http://localhost:5006"
echo "- RabbitMQ Management: http://localhost:15672 (guest/guest)"
echo ""
echo "Default users:"
echo "- Admin: username=admin, password=adminpassword"
echo "- User: username=user, password=userpassword"


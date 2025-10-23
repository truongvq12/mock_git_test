# Test Data Configuration

## Sample Data Files

### users.json
```json
{
  "users": [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com"}
  ]
}
```

### products.json
```json
{
  "products": [
    {"id": 1, "name": "Product A", "price": 29.99},
    {"id": 2, "name": "Product B", "price": 49.99},
    {"id": 3, "name": "Product C", "price": 19.99}
  ]
}
```

### config.json
```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "name": "test_db"
  },
  "api": {
    "base_url": "https://api.example.com",
    "timeout": 30
  }
}
```

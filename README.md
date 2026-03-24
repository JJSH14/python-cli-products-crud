# Python CLI Products CRUD

A minimal CLI tool for CRUD operations on products using Python, SQLAlchemy ORM, and PostgreSQL.

## Features

✅ **List all products** - View all products in formatted table  
✅ **Add products** - Create new products with name, price, and optional description  
✅ **Get product** - Retrieve product details by ID  
✅ **Update product** - Modify product information  
✅ **Delete product** - Remove products with confirmation  
✅ **Database initialization** - Automatic table creation  

## Project Structure

```
python-cli-products-crud/
├── database.py      # Database configuration and session setup
├── models.py        # SQLAlchemy Product model
├── crud.py          # CRUD operations (Create, Read, Update, Delete)
├── cli.py           # Click CLI commands
├── requirements.txt # Python dependencies
├── .env.template    # Environment variables template
└── README.md        # This file
```

## Requirements

- Python 3.8+
- PostgreSQL 12+ (or SQLite for development)
- pip (Python package manager)

## Installation

### 1. Clone or Download Project

```bash
cd python-cli-products-crud
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Copy `.env.template` to `.env`:

```bash
cp .env.template .env
```

**For PostgreSQL:**
```
DATABASE_URL=postgresql://username:password@localhost:5432/products_db
```

**For SQLite (Development):**
```
DATABASE_URL=sqlite:///products.db
```

### 5. Initialize Database

```bash
python cli.py init
```

## Usage

### List All Products

```bash
python cli.py list
```

Output:
```
======================================================================
ID    Name                          Price           Description      
======================================================================
1     Laptop                        $12.99          Gaming Laptop    
2     Mouse                         $25.50          Wireless Mouse   
======================================================================
```

### Add New Product

```bash
python cli.py add "Product Name" 99.99 --desc "Product Description"
```

Examples:
```bash
python cli.py add "Laptop" 12.99 --desc "Gaming Laptop"
python cli.py add "Mouse" 25.50
python cli.py add "Keyboard" 79.99 --desc "Mechanical Keyboard"
```

### Get Product by ID

```bash
python cli.py get 1
```

Output:
```
Product Details:
==================================================
ID: 1
Name: Laptop
Price: $12.99
Description: Gaming Laptop
==================================================
```

### Update Product

```bash
python cli.py update 1 "Updated Name" 14.99 --desc "Updated Description"
```

Examples:
```bash
python cli.py update 1 "Laptop Pro" 1499.99
python cli.py update 2 --desc "New Description"
```

### Delete Product

```bash
python cli.py delete 1
```

Will prompt for confirmation:
```
Are you sure you want to delete this product? [y/N]: y
✓ Product 1 deleted successfully!
```

## Database Schema

### Products Table

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT |
| name | VARCHAR(100) | NOT NULL |
| price | FLOAT | NOT NULL |
| description | VARCHAR(500) | NULLABLE |

## Technologies Used

- **SQLAlchemy** - ORM for database operations
- **psycopg2-binary** - PostgreSQL adapter
- **Click** - CLI framework
- **python-dotenv** - Environment variables management

## Common Commands Cheatsheet

```bash
# Initialize
python cli.py init

# CRUD Operations
python cli.py list
python cli.py add "Name" 10.00 --desc "Description"
python cli.py get 1
python cli.py update 1 "New Name" 20.00
python cli.py delete 1

# Help
python cli.py --help
python cli.py add --help
```

## Error Handling

The CLI includes error handling for:
- Invalid product IDs
- Database connection errors
- Invalid input validation
- Duplicate operations

## Development Notes

- To enable SQL logging, set `echo=True` in `database.py`
- All prices are stored as FLOAT type
- Product descriptions are optional
- Database is automatically created on first `init` command

## Author

Created for CRUD Operations Assessment

## License

MIT

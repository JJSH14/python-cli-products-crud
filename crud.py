"""CRUD operations for products."""

from sqlalchemy.exc import SQLAlchemyError

from database import get_db
from models import Product


def create_product(name: str, price: float, description: str = None) -> Product:
    """Create a new product."""
    db = get_db()
    try:
        product = Product(name=name, price=price, description=description)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error creating product: {str(e)}")
    finally:
        db.close()


def get_product_by_id(product_id: int) -> Product:
    """Get product by ID."""
    db = get_db()
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        return product
    except SQLAlchemyError as e:
        raise Exception(f"Error fetching product: {str(e)}")
    finally:
        db.close()


def list_all_products():
    """List all products."""
    db = get_db()
    try:
        products = db.query(Product).all()
        return products
    except SQLAlchemyError as e:
        raise Exception(f"Error listing products: {str(e)}")
    finally:
        db.close()


def update_product(
    product_id: int, name: str = None, price: float = None, description: str = None
) -> Product:
    """Update a product."""
    db = get_db()
    try:
        product = db.query(Product).filter(Product.id == product_id).first()

        if not product:
            raise Exception(f"Product with ID {product_id} not found")

        if name:
            product.name = name
        if price:
            product.price = price
        if description is not None:
            product.description = description

        db.commit()
        db.refresh(product)
        return product
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error updating product: {str(e)}")
    finally:
        db.close()


def delete_product(product_id: int) -> bool:
    """Delete a product."""
    db = get_db()
    try:
        product = db.query(Product).filter(Product.id == product_id).first()

        if not product:
            raise Exception(f"Product with ID {product_id} not found")

        db.delete(product)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error deleting product: {str(e)}")
    finally:
        db.close()

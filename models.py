"""Product model definition."""

from sqlalchemy import Column, Float, Integer, String

from database import Base


class Product(Base):
    """Product model for database."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500), nullable=True)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"

    def to_dict(self):
        """Convert product to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
        }

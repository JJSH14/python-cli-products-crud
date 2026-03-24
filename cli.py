"""CLI commands for product management."""

import click

from crud import (
    create_product,
    delete_product,
    get_product_by_id,
    list_all_products,
    update_product,
)
from database import init_db


@click.group()
def cli():
    """Product Management CLI."""
    pass


@cli.command()
def list():
    """List all products."""
    try:
        products = list_all_products()
        if not products:
            click.echo("No products found.")
            return

        click.echo("\n" + "=" * 70)
        click.echo(f"{'ID':<5} {'Name':<30} {'Price':<15} {'Description':<20}")
        click.echo("=" * 70)

        for product in products:
            desc = product.description or "N/A"
            click.echo(
                f"{product.id:<5} {product.name:<30} ${product.price:<14.2f} "
                f"{desc:<20}"
            )

        click.echo("=" * 70 + "\n")
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red"))


@cli.command()
@click.argument("name")
@click.argument("price", type=float)
@click.option("--desc", default=None, help="Product description")
def add(name, price, desc):
    """Add a new product.

    Example: add "Laptop" 12.99 --desc "Gaming Laptop"
    """
    try:
        if len(name) > 100:
            click.echo(
                click.style("Error: Product name must be max 100 characters", fg="red")
            )
            return

        product = create_product(name, price, desc)
        click.echo(
            click.style(
                f"✓ Product created successfully!\n"
                f"  ID: {product.id}, Name: {product.name}, "
                f"Price: ${product.price:.2f}",
                fg="green",
            )
        )
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red"))


@cli.command()
@click.argument("product_id", type=int)
def get(product_id):
    """Get product by ID.

    Example: get 1
    """
    try:
        product = get_product_by_id(product_id)
        if not product:
            click.echo(
                click.style(f"Product with ID {product_id} not found", fg="yellow")
            )
            return

        click.echo(f"\nProduct Details:")
        click.echo("=" * 50)
        click.echo(f"ID: {product.id}")
        click.echo(f"Name: {product.name}")
        click.echo(f"Price: ${product.price:.2f}")
        click.echo(f"Description: {product.description or 'N/A'}")
        click.echo("=" * 50 + "\n")
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red"))


@cli.command()
@click.argument("product_id", type=int)
@click.argument("name", required=False)
@click.argument("price", type=float, required=False)
@click.option("--desc", default=None, help="Product description")
def update(product_id, name, price, desc):
    """Update a product.

    Example: update 1 "Laptop Updated" 15.99 --desc "New Description"
    """
    try:
        product = update_product(product_id, name, price, desc)
        click.echo(
            click.style(
                f"✓ Product updated successfully!\n"
                f"  ID: {product.id}, Name: {product.name}, "
                f"Price: ${product.price:.2f}",
                fg="green",
            )
        )
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red"))


@cli.command()
@click.argument("product_id", type=int)
@click.confirmation_option(prompt="Are you sure you want to delete this product?")
def delete(product_id):
    """Delete a product by ID.

    Example: delete 1
    """
    try:
        delete_product(product_id)
        click.echo(
            click.style(f"✓ Product {product_id} deleted successfully!", fg="green")
        )
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red"))


@cli.command()
def init():
    """Initialize database tables."""
    try:
        init_db()
        click.echo(click.style("✓ Database initialized successfully!", fg="green"))
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red"))


if __name__ == "__main__":
    cli()

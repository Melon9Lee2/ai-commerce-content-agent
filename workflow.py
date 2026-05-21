import asyncio
from agent import generate_script

async def main():
    products = ["Skincare Cream", "Wireless Earbuds", "Smart Watch"]
    for product in products:
        script = generate_script(product)
        print(f"Generated script for {product}:\n{script}\n")

if __name__ == "__main__":
    asyncio.run(main())

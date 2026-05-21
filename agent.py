from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_script(product_info):
    """
    Generate short-form ad scripts for e-commerce products.
    """
    prompt = f"Create a Douyin ad script for: {product_info}"
    response = client.chat_completion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
import os
openai.api_key  = os.getenv('OPENAI_API_KEY')

# Define function to generate domain names
def generate_domain_names(keywords):
    # Use OpenAI to generate domain names based on keywords
    domain_names = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a ordered list of 10 SEO-optimized domain names based on the following top keywords: " + ", ".join(keywords),
        max_tokens=60,
        n=10,
        stop=None,
        temperature=0.5
    ).choices
    # Extract domain names from OpenAI response
    domain_names = [choice.text.strip() for choice in domain_names]
    return domain_names

# Example usage of the function
# Replace this list with your top SEO-optimized keywords
top_seo_keywords = ["shopping", "ai", "gpt"]

generated_domain_names = generate_domain_names(top_seo_keywords)
print(generated_domain_names)

# namegpt; names-plugin

# Introduction
This Python script demonstrates how to use the OpenAI API to generate SEO-optimized domain names based on a list of top keywords. By utilizing the OpenAI GPT-3 model, it generates creative and relevant domain names. This can be helpful for businesses, developers, or individuals looking to create new websites with SEO-optimized domain names related to specific keywords.

## Requirements
Python 3.6 or higher
openai Python library

## Installation Instructions

1. Install Python 3.6 or higher if you haven't already. You can download the appropriate version for your operating system from the official Python website: https://www.python.org/downloads/

2. Install the openai library using pip:

   ``` 
   pip install openai
   ```
       
3. Obtain an API key for the OpenAI API. To do this, sign up for an account on the OpenAI website (https://beta.openai.com/signup/) and follow the instructions to obtain your API key.

4. Set the OPENAI_API_KEY environment variable in your terminal or script with your OpenAI API key:  
   ```
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```

5. Save the provided code in a Python file, for example, as it is namegpt.py.

   Find and Replace these keywords in the python code with your desired top SEO-optimized keywords.
   ```
   # Replace this list with your top SEO-optimized keywords
   top_seo_keywords = ["shopping", "ai", "gpt"]
   ```
6. Run the script using the command:
   ``` 
   python namegpt.py
   ```
## The script will generate and print 10 SEO-optimized domain names based on the provided top keywords using the OpenAI API.

7. If needed, make a new file containing your OpenAI API and save as .env
   ```
   OPENAI_API_KEY=Your API Here
   ```

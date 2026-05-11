import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDkx2dhNgDJ3aC8KLX3Nxexj_b7tRMvquA")

# List models that support generateContent
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error: {e}")

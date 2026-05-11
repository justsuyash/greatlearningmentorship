import os
import sys

from langchain_google_genai import ChatGoogleGenerativeAI

print("GOOGLE_API_KEY:", bool(os.getenv("GOOGLE_API_KEY")))

try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    response = llm.invoke("Hi")
    print(response.content)
except Exception as e:
    import traceback
    traceback.print_exc()


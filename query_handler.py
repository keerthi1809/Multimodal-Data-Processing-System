import google.generativeai as genai
import os, json

genai.configure(api_key="YOUR_GEMINI_API_KEY")

def get_answer(query, data):
    prompt = f"Answer this based on the following data:\n{json.dumps(data)}\n\nQuery: {query}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

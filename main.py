from typing import Optional

from fastapi import FastAPI

import os
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
import requests
from google import genai

app = FastAPI()
load_dotenv()
AI_API_KEY = os.getenv("GeminiAPI")


@app.get("/GenerateChallenge")
async def generate_challenge(location: str = None, information: str = None):
    if not AI_API_KEY:
        return {"error": "AI API key not found"}
    content = f"Generate a short and actionable challenge for improving the environment (max 20 words) for users near {location}, where {information}. Keep it fun and motivating. examples are, plant a tree, plant a hedge or a flower, etc. Be very exact, the user should know exactly what to do. if talking about a tree, be specific about the type of tree, if talking about a flower, be specific about the type of flower. Do not use any other words than the challenge itself. The locations are public areas. Also state the reason, which metric will it improve"
    client = genai.Client(api_key=AI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=content)
    # send challenge to greenAi API
    return {"message": "Challenge generated successfully", "data": response.text}
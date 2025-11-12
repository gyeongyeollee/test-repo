from fastapi import FastAPI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경변수에서 OPENAI_API_KEY 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# FastAPI 앱 생성
app = FastAPI()

@app.get("/")
def read_root():
    return {"OPENAI_API_KEY": api_key}

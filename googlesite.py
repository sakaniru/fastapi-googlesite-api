from fastapi import FastAPI

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有前端網頁連接
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {"message": "阿志是GAY"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("googlesite:app", host="127.0.0.1", port=8000, reload=True) 


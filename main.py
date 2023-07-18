from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ml import recommend

app = FastAPI()

# Enable CORS
origins = [
    # Add your frontend URL(s) here
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"],  # Add other allowed methods as needed
    allow_headers=["*"],
)

# Example endpoint for sending data
@app.post('/send-data')
async def send_data(data: dict):
    movie = data['movie']
    result_dict = {i+1: '' for i in range(5)}
    processed_data = recommend(movie)
    
    for i, result in enumerate(processed_data):
        result_dict[i+1] = result
    
    return {'processedData': result_dict}


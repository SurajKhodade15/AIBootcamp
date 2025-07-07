from fastapi import FastAPI

api = FastAPI()

tourist_points = [
    {"id": 1, "name": "Shaniwar Wada", "description": "Historic fortification in the city center."},
    {"id": 2, "name": "Aga Khan Palace", "description": "Landmark palace & memorial to Mahatma Gandhi."},
    {"id": 3, "name": "Sinhagad Fort", "description": "Hill fortress with panoramic views."},
    {"id": 4, "name": "Pataleshwar Cave Temple", "description": "Rock-cut cave temple dating to the 8th century."},
    {"id": 5, "name": "Chhatrapati Shivaji Maharaj Terminus", "description": "Historic railway station in Pune."}
]

@api.get("/")
async def root():
    return {"message": "Welcome to Pune Tourist Points API"}

@api.get("/points")
async def get_points():
    return {"tourist_points": tourist_points}

@api.get("/points/{point_id}")
async def get_point(point_id: int):
    for point in tourist_points:
        
        if point["id"] == point_id:
            return point
    return {"error": "Tourist point not found"}

@api.post("/points")
async def create_point(point: dict):
    tourist_points.append(point)
    return {"message": "Tourist point created successfully"}
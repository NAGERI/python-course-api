from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI( title="Courses API")

@app.get("/")
async def hello():
    return "Go to /api/courses"

@app.get("/api/courses", description="Get all available courses.")
async def getAllCourses():
    content = {"message": "All Courses"}
    return JSONResponse(status_code=200, content=content)

@app.get("/api/courses/{id}", description="Get all available courses.")
async def getCourse(id: int):
    try:      
      content = {"message": f"Course {id} found"}
      return JSONResponse(status_code=200, content=content)
    except:
      return JSONResponse(status_code=400, content=f"Course with id {id} not found")

@app.post("/api/courses", description="Create a course resource.")
async def createCourse():
    content = {"message": "All Courses"}
    return JSONResponse(status_code=200, content=content)

@app.patch("/api/courses/{id}", description="Update a course.")
async def updateCourse(id:int):
    content = {"message": f"Update Course id: {id} "}
    return JSONResponse(status_code=200, content=content)

@app.delete("/api/courses/{id}", description="Delete a course resource.")
async def deleteCourse(id: int):
    content = {"message": f"Delete Course : {id}"}
    return JSONResponse(status_code=200, content=content)

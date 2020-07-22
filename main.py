from fastapi import FastAPI, Request, Header
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient
from bson import json_util, ObjectId
import json

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:C2y6yDjf5%2FR%2Bob0N8A7Cgv30VRDJIWEHLM%2B4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw%2FJw%3D%3D@localhost:10255/admin?ssl=true&ssl_cert_reqs=CERT_NONE")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index():
    return {"hello": "world"}

@app.get("/list")
async def listall(request: Request):
    db = client.test

    cursor = db.todo.find({})

    l = await cursor.to_list(length=100)    

    return templates.TemplateResponse("index.html", 
    {
        "request": request,
        "a1": "active",
        "todos": l,
        "t": "TODO with FastAPI",
        "h": "ToDo Reminder"
    })

@app.get("/incomplete")
async def incomplete(request: Request):
    db = client.test
    cursor = db.todo.find({"done": "no"})

    l = await cursor.to_list(length=100)

    return templates.TemplateResponse("index.html", 
    {
        "request": request,
        "a2": "active",
        "todos": l,
        "t": "TODO with FastAPI",
        "h": "ToDo Reminder"
    })

@app.get("/complete")
async def complete(request: Request):
    db = client.test
    cursor = db.todo.find({"done": "yes"})

    l = await cursor.to_list(length=100)

    return templates.TemplateResponse("index.html", 
    {
        "request": request,
        "a3": "active",
        "todos": l,
        "t": "TODO with FastAPI",
        "h": "ToDo Reminder"
    })

@app.get("/done")
async def done(request: Request, referer: str = Header(None)):    
    id = request.query_params["_id"]

    db = client.test
    query = {"_id": ObjectId(id)}
    task = await db.todo.find_one(query)

    print(referer)


    if task["done"] == "yes":
        await db.todo.update_one(query, {"$set": {"done": "no"}})
    else:
        await db.todo.update_one(query, {"$set": {"done": "yes"}})

    return RedirectResponse(referer)

@app.post("/action")
async def action(request: Request):
    doc = {
        "name": request.query_params["name"],
        "desc": request.query_params["desc"],
        "date": request.query_params["date"],
        "pr": request.query_params["pr"],
        "done": "no"
    }

    db = client.test

    result = await db.todos.insert_one(doc)
    print(result)

    return RedirectResponse("/list")




if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
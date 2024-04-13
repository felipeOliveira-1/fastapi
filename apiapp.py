from fastapi import FastAPI

app = FastAPI()

richest_people_list = {
    "Elon Musk": "280 Billion USD", 
    "Jeff Bezos": "250 Billion USD", 
    "Bill Gates": "200 Billion USD", 
    "Mark Zukerberg": "180 Billion USD"    
}

# End Point 1
@app.get("/richest-people")
def richest_people():
    return richest_people_list


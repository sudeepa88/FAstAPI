from fastapi import FastAPI
start_app=FastAPI()



@start_app.get("/calc/{a},{b}")
def calculation(a:int,b:int):
    return{a*b}
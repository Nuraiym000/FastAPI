from path import Path
from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import uvicorn
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()


app.include_router(auth_router)
app.include_router(order_router)


# app = FastAPI(title='How to Send Email')
@app.get('/')
def index():
    return 'Hello World'

# if name == '__main__':
#     uvicorn.run('main:app', reload=True)


# @app.get('/send-email/asynchronous')
# async def send_email_asynchronous():
#     await send_email_async('Hello World','nurajymmm1@gmail.com',
#     {'title': 'Hello World', 'name': 'Nura'})
#     return 'Success'
#
# @app.get('/send-email/backgroundtasks')
# def send_email_backgroundtasks(background_tasks: BackgroundTasks):
#     send_email_background(background_tasks, 'Hello World',
#     'someemail@gmail.com', {'title': 'Hello World', 'name':       'John Doe'})
#     return 'Success'
#
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
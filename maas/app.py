from aiohttp import web
from asyncworker import App, RouteTypes

app = App("", "", "", 1)


@app.route(["/"], type=RouteTypes.HTTP, methods=["POST"])
async def operation(request: web.Request):
    data = await request.json()
    try:
        result = division(data["left"], data["right"])
        if type(result) != int:
            result = int(result)
        myjson = {"result": result}
    except:
        myjson = {}
    return web.json_response(myjson)


def division(a, b):
    if b == 0:
        raise Exception("Division by zero")
    return a / b

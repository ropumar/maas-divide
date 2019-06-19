from aiohttp import web
from asyncworker import App, RouteTypes

app = App("", "", "", 1)


@app.route(["/"], type=RouteTypes.HTTP, methods=["POST"])
async def operation(request: web.Request):
    data = await request.json()
    result = division(data["left"], data["right"])
    return web.json_response(result)


def division(a, b):
    if b == 0:
        return {"result": "Division by zero"}
    return {"result": a / b}

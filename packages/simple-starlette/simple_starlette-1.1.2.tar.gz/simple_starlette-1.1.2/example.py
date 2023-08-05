from starlette.requests import Request
from simple_starlette import SimpleStarlette, Response, ResTypeEnum

app = SimpleStarlette(__name__)

@app.route("/test")
class Test:
    async def get(self, request: Request):
        return Response(request.url, ResTypeEnum.TEXT)

    async def post(self, request: Request):
        return Response(request.url, ResTypeEnum.TEXT)

app.run()

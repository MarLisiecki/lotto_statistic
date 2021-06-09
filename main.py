from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from stat_func.implementation import Lotto

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"))

lotto = Lotto()
# lotto.download_file()
lotto.convert_file()
data = sorted(list(lotto.most_common().keys()))


@app.get('/', response_class=HTMLResponse)
def render_app(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request, 'data': data})

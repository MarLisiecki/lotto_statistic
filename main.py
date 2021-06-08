from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"))

@app.get('/', response_class=HTMLResponse)
def render_app(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

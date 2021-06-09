from time import sleep

from fastapi import FastAPI, Request, Form
from fastapi_utils.tasks import repeat_every
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from stat_func.implementation import Lotto

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"))
lotto = Lotto()
data = sorted(list(lotto.most_common().keys()))


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 12)
async def download_file_with_lotto_numbers() -> None:
    lotto.download_file()
    sleep(2)
    lotto.convert_file()


@app.post('/numbers_from_user', response_class=HTMLResponse)
async def number_get(request: Request, first_nb: int = Form(...), second_nb: int = Form(...), third_nb: int = Form(...),
                     fourth_nb: int = Form(...),
                     fifth_nb: int = Form(...), sixth_nb: int = Form(...)):
    input_list = [first_nb, second_nb, third_nb, fourth_nb, fifth_nb, sixth_nb]
    if lotto.check_my_numbers(input_list):
        answer = 'Te liczby już kiedyś padły!'
    else:
        answer = 'Te liczby nigdy nie padły!'
    return templates.TemplateResponse('index.html', context={'request': request, 'data': data, 'answer': answer})


@app.get('/', response_class=HTMLResponse)
def render_app(request: Request):
    answer = str()
    return templates.TemplateResponse('index.html', context={'request': request, 'data': data, 'answer': answer})

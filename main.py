# fastapi_app/main.py
import json
import uvicorn
from fastapi import FastAPI, Request, responses
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger

from formation.formation_of_reports import formation_of_reports
from formation.formation_of_surcharges import formation_of_surcharges, formation_of_surcharges_1
from formation.formation_the_payroll import formation_the_payroll
from formation.summary_by_types_and_categories import summary_by_types_and_categories
from formation.tabel_21012 import tabel
from formation.transfer_profession import transfer_prof
from launch_program import launch_program

app = FastAPI()

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализируем шаблоны
templates = Jinja2Templates(directory="templates")

# Загружаем данные
def get_data_from_json():
    with open('data/tab_2024.json', 'r', encoding='utf-8') as file:
        return json.load(file)

dist_list = get_data_from_json()

# Главная страница
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "buttons": [
                {"name": "КШД", "endpoint": "/transfer-prof"},
                {"name": "BZ 14", "endpoint": "/summary"},
                {"name": "Формирование рапортов", "endpoint": "/formation-reports"},
                {"name": "Формирование табеля", "endpoint": "/tabel"},
                {"name": "Доплаты", "endpoint": "/additional-payments"},
                {"name": "Доплаты 130, 410", "endpoint": "/additional-payments-1"},
                {"name": "Формирование списочного состава", "endpoint": "/payroll"},
                {"name": "Запустить программу", "endpoint": "/launch"},
            ]
        }
    )

# Формирование рапортов
@app.post("/formation-reports")
async def handle_formation_reports():
    try:
        formation_of_reports(dist_list)
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# Формирование табеля
@app.post("/tabel")
async def handle_tabel():
    try:
        tabel(dist_list)
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# Формирование доплат 124, 164
@app.post("/additional-payments")
async def handle_additional_payments():
    try:
        formation_of_surcharges()
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# Формирование доплат 130, 140
@app.post("/additional-payments-1")
async def handle_additional_payments_1():
    try:
        formation_of_surcharges_1()
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# Формирование списочного состава
@app.post("/payroll")
async def handle_payroll():
    try:
        formation_the_payroll()
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# КШД
@app.post("/transfer-prof")
async def handle_transfer_prof():
    try:
        transfer_prof()
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# BZ 14
@app.post("/summary")
async def handle_summary():
    try:
        summary_by_types_and_categories()
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# Запуск программы
@app.post("/launch")
async def handle_launch():
    try:
        launch_program()
        return responses.JSONResponse({"status": "success"})
    except Exception as e:
        logger.exception(e)
        return responses.JSONResponse({"status": "error", "error": str(e)}, status_code=500)

# 🔥 Точка входа для запуска приложения
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
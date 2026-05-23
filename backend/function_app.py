import azure.functions as func
from main import app as fastapi_app

app = func.AsqiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)

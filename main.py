from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from service.utils import get_text_from_link, remove_all_temp_files


app = FastAPI()


@app.on_event("startup")
def startup():
    remove_all_temp_files()


@app.on_event("shutdown")
def shutdown():
    remove_all_temp_files()


@app.get('/gettext')
def get_text(link: str):
    result_filename = get_text_from_link(link)
    if result_filename:
        return FileResponse(path=result_filename, filename='Text_from_link.txt', media_type='multipart/form-data')
    return {'Message': 'No text.'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

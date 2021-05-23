from fastapi import FastAPI, status, HTTPException
from . import utils

app = FastAPI()


@app.get("/cbu_calculator/{key}", status_code=status.HTTP_200_OK)
def cbu_calculator(key:str):

    if len(key) < 22:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The {key} must be 22 digits.")

    validate = utils.cbu_checked(str(key))

    return {
        "validate": validate,
        "cbu": validate and not(str(key)[:3] == "000"),
        "cvu": validate and str(key)[:3] == "000"
    }
    

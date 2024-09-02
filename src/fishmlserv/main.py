from typing import Union
from fastapi import FastAPI
import pickle
from fishmlserv.model.manager import get_model_path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id":item_id, "q":q}

@app.get("/fish")
def fish(length: float, weight: float):
    """
    물고기 종류 판별기

    Args: 
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
#    if length > 30.0:
#        prediction="도미"
#    else:
#        prediction="빙어"

#    with open("/home/esthercho/code/fishmlserv/note/model.pkl", "rb") as file:
#        fish_model=pickle.load(file)

#    prediction=fish_model.predict([[length, weight]])
    model_path=get_model_path()
    with open(model_path, 'rb') as f:
        fish_model=pickle.load(f)

    fish_class=fish_model.predict([[length, weight]])
    fish_name="몰라"

    if fish_class==0:
        fish_name="도미"
    else:
        fish_name="빙어"
#    if prediction[0]==1:
#        fish_class="도미"
#    else:
#       fish_class="빙어"


    return {
            "prediction": fish_name,
            "length":length,
            "weight":weight
            }

#@app.get("/test")
#def test():
#    from src.fishmlserv.model.manager import get_model_path
#    model_path=get_model_path()
#    return model_path

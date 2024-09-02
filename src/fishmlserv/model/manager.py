import os

def get_model_path():
    my_path=os.path.dirname(__file__)
    model_path= os.path.join(my_path, "model.pkl")

    return model_path

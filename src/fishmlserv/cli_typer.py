import typer 
#from sklearn.neighbors import KNeighborsClassifier
from fishmlserv.model.manager import get_model_path
import pickle

app=typer.Typer()

@app.command()
def prediction(length: float = typer.Option(..., "-l", "--length", help="Length of the fish"), weight: float = typer.Option(..., "-w", "--weight", help="Weight of the fish")):
    model_path=get_model_path()
    with open(model_path, 'rb') as f:
        fish_model=pickle.load(f)
    data=[[length, weight]]
    prediction=fish_model.predict(data)
    mapping={0: '빙어', 1: '도미'}
    mapped_prediction=mapping[prediction[0]]
    print(mapped_prediction)
    return mapped_prediction

@app.command()
def main():
    typer.run(prediction)

if __name__=='__main__':
    main()

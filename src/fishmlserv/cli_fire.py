import fire
from sklearn.neighbors import KNeighborsClassifier
from fishmlserv.model.manager import get_model_path
import pickle

def prediction(length: float, weight: float):
    """
    length와 weight를 이용한 물고기 예측 모델 (빙어, 도미)

    Args:
        length(float): 물고기의 길이
        weight(float): 물고기의 무게

    Return:
        예측된 물고기의 종류
    """
    model_path=get_model_path()
    with open(model_path, 'rb') as f:
        fish_model=pickle.load(f)
    data=[[length, weight]]
    prediction=fish_model.predict(data)
    mapping={0: '빙어', 1: '도미'}
    mapped_prediction=mapping[prediction[0]]
    return mapped_prediction

def main():
    fire.Fire(prediction)

if __name__=='__main__':
    main()

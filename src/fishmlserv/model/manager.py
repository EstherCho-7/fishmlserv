import os

def get_model_path():
    import pickle
    #  이 함수 파일의 절대 경로 받아오기
    # 절대 경로를 이용해 model.pkl의 경로를 조합
    # 조합된 경로를 리턴 = 끝
    # 사용 fastapi main.py에서 아래와 같이 사용
    # from sighmlserv.model.manager import get_model_path
    
#    this_file_path=os.path.abspath(__file__)
    my_path=os.path.dirname(__file__)
#    rel_path=os.path.expanduser('~/code/fishmlserv/src/fishmlserv/model')
    model_path= os.path.join(my_path, "model.pkl")
#    with open(join_path, "rb") as file:  # 추가
#        fish_model=pickle.load(file)     # 추가
#    model_path=os.path.abspath(join_path)

    return model_path

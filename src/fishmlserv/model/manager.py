def get_model_path():
    import os
    #  이 함수 파일의 절대 경로 받아오기
    # 절대 경로를 이용해 model.pkl의 경로를 조합
    # 조합된 경로를 리턴 = 끝
    # 사용 fastapi main.py에서 아래와 같이 사용
    # from sighmlserv.model.manager import get_model_path
    
    this_file_path=os.path.abspath(__file__)
    this_dir=os.path.dirname(this_file_path)
    rel_path=os.path.expanduser('~/code/fishmlserv/src/fishmlserv/model')
    join_path=os.path.join(rel_path, 'model.pkl')
    with open(join_path, "rb") as file:  # 추가
        fish_model=pickle.load(file)     # 추가
#    model_path=os.path.abspath(join_path)

    return fish_model 

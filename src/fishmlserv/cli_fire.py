import fire
from sklearn.neighbors import KNeighborsClassifier

#def predict(length: float, weight: float):
#    kn=KNeighborsClassifier()

#    fish_data=[]

def hello(name):
    return 'hello {name}!'.format(name=name)

def main():
    fire.Fire(hello)

if __name__=='__main__':
    main()

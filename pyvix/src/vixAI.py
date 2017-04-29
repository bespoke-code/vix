#Creating network using KERAS
import numpy
from keras.model import Sequential
from keras.layers import Dense

def main():
    #fix random seed for reproducibility
    seed=7
    numpy.random.seed(seed)
    #load dataset
    dataset=numpy.loadtxt("thingslike.data.txt", delimiter=",")
    #split dataset into input(X) and output(Y) variables
    x=dataset[:, 0:8]
    y=dataset[:, 8]
    #CREATE MODEL
    vix = Sequential()
    vix.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
    vix.add(Dense(8, init='uniform', activation='relu'))
    vix.add(Dense(1, init='uniform', activation='relu'))
    #compile vixAI
    vix.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    #fit vixAI
    vix.fit(X, Y, nb_epoch=150, batch_size=10, verbose=2)
    #evaluate vixAI
    scores=vix.evaluate(x,y)
    print("\n%s: %.2f%%" %(vix.metrics_names[1], scores[1]*100))
    #calculate predictions for vixAI
    predictions=vix.predict(X)
    #round predictions for vixAI
    rounded=[round(x[0]) for x in predictions]
    print(rounded)


    if __name__=='__main__':
        main()


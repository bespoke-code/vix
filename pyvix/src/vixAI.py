# Creating network using KERAS
import numpy
from keras.models import Sequential
from keras.layers import Dense


def main():
    # fix random seed for reproducibility
    seed = 7
    numpy.random.seed(seed)
    # load dataset
    dataset = numpy.loadtxt("../datasets/data-nasa-subset.csv", delimiter=",")
    # split dataset into input(X) and output(Y) variables
    x = dataset[:, 1:3]
    y = dataset[:, 4]
    # CREATE MODEL
    vix = Sequential()
    vix.add(Dense(5, input_dim=3, init='uniform', activation='relu'))
    vix.add(Dense(3, init='uniform', activation='relu'))
    vix.add(Dense(1, init='uniform', activation='relu'))
    # compile vixAI
    vix.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit vixAI
    vix.fit(x, y, nb_epoch=150, batch_size=10, verbose=2)
    # evaluate vixAI
    scores = vix.evaluate(x, y)
    print("\n%s: %.2f%%" % (vix.metrics_names[1], scores[1] * 100))
    # calculate predictions for vixAI
    predictions = vix.predict(x)
    # round predictions for vixAI
    rounded = [round(x[0]) for x in predictions]
    print(rounded)

    if __name__ == '__main__':
        main()

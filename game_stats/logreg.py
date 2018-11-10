from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from sklearn.model_selection import train_test_split
from scoreCalc import scoreCalculator

import pandas as pd
import numpy as np
import ast
import keras

league = pd.read_csv('data/leagueoflegends/LeagueofLegends.csv')

bKills = np.array(league.iloc[:, 11])
bDragons = np.array(league.iloc[:, 14])
bBarons = np.array(league.iloc[:, 15])
rKills = np.array(league.iloc[:, 18])
rDragons = np.array(league.iloc[:, 21])
rBarons = np.array(league.iloc[:, 22])
y = np.array(league.iloc[:, 5])  # blue win/loss column (0 or 1)
X = []


def size(input):
    return len(ast.literal_eval(input))


for n in range(len(bKills)):
    bAssists, rAssists = 0, 0
    for m in ast.literal_eval(bKills[n]):
        bAssists += len(m[3])
    for m in ast.literal_eval(rKills[n]):
        rAssists += len(m[3])
    X.append([
        size(bKills[n]),
        size(rKills[n]),
        bAssists,
        rAssists,
        size(bDragons[n]),
        size(rDragons[n]),
        size(bBarons[n]),
        size(rDragons[n])
    ])
X = np.array(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


def get_model():
    # Model architecture
    model = Sequential()
    model.add(Dense(20, input_dim=8,
                    kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))

    # Compile model
    model.compile(loss='mean_squared_error',
                  optimizer='adam', metrics=['accuracy'])
    return model


model = get_model()

# Train model
batch_size = 10
epochs = 100

model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs,
          validation_data=(X_test, y_test), verbose=1)
model.save('model.h5')

# Test it out!
model = load_model('model.h5')
output_labels = ['bWin', 'rWin']
test_sample = 0
test = np.expand_dims(X_train[test_sample], axis=0)
pred = model.predict(test)[0]

print('Prediction: ' + output_labels[int(np.round(pred - 1))]
      + ', ' + 'Actual: ' + output_labels[y_train[test_sample] - 1])

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, LSTM, Dropout, RepeatVector, TimeDistributed
from  keras import regularizers
from keras.models import Model
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.utils.multiclass import type_of_target
import seaborn as sns

#Read dataset
data = pd.read_excel(r'D:\Σχολή\4ο\Βαθιά Μάθηση\input2.xlsx')
data = data.sort_values('date').reset_index(drop=True)
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

train, test = data['2021-09-27':'2022-01-31'], data['2022-01-31':]

scaler = StandardScaler()
X_train = scaler.fit_transform(train)
X_test = scaler.transform(test)

X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])


####################### Model1 ##############################
model = Sequential()
model.add(LSTM(128, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))

model.add(Dropout(rate=0.5))
model.add(RepeatVector(X_train.shape[1]))

model.add(LSTM(128, activation='relu', return_sequences=True))
model.add(Dropout(rate=0.5))
model.add(TimeDistributed(Dense(X_train.shape[2])))
model.compile(optimizer= tf.keras.optimizers.Adam(), loss='mae', metrics=['mae'])
model.summary()


######################### Model2 ##############################

#model = Sequential()
#model.add(LSTM(32, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True))
#model.add(Dropout(rate=0.3))
#model.add(LSTM(16, activation='relu', return_sequences=False))

#model.add(RepeatVector(X_train.shape[1]))
#model.add(LSTM(16, activation='relu', return_sequences=True))
#model.add(Dropout(rate=0.3))
#model.add(LSTM(32, activation='relu', return_sequences=True))

#model.add(TimeDistributed(Dense(X_train.shape[2])))
#model.compile(optimizer='adam', loss='mse', metrics=['mse'])
#model.summary()


######################## Model3 #############################3

#model = Sequential()
#model.add(LSTM(32, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True))
#model.add(LSTM(16, activation='relu', return_sequences=False))
#model.add(RepeatVector(X_train.shape[1]))
#model.add(LSTM(16, activation='relu', return_sequences=True))
#model.add(LSTM(32, activation='relu', return_sequences=True))
#model.add(TimeDistributed(Dense(X_train.shape[2])))

#model.compile(optimizer='adam', loss='mae', metrics=[tf.keras.metrics.Accuracy()])
#model.summary()


# fit model
history = model.fit(X_train, X_train, epochs=10, batch_size=32, validation_split=0.3, verbose=1)

plt.plot(history.history['loss'], label='Training loss')
plt.plot(history.history['val_loss'], label='Validation loss')
plt.legend()
plt.show()

#plot the loss distribution
X_pred = model.predict(X_train)
X_pred = X_pred.reshape(X_pred.shape[0], X_pred.shape[2])
X_pred = pd.DataFrame(X_pred, columns=train.columns)
X_pred.index = train.index

scored = pd.DataFrame(index=train.index)
Xtrain = X_train.reshape(X_train.shape[0], X_train.shape[2])
scored['Loss_mae'] = np.mean(np.abs(X_pred - Xtrain), axis=1)
sns.displot(scored['Loss_mae'], bins= 20, kde= True, color='blue')
plt.show()

#calculate loss on test
X_pred = model.predict(X_test)

X_pred = X_pred.reshape(X_pred.shape[0], X_pred.shape[2])
X_pred = pd.DataFrame(X_pred, columns=test.columns)
X_pred.index = test.index

scored = pd.DataFrame(index=test.index)
Xtest = X_test.reshape(X_test.shape[0], X_test.shape[2])
scored['Loss_mae'] = np.mean(np.abs(X_pred-Xtest), axis=1)
scored['Threshold'] = 0.5
scored['Anomaly'] = scored['Loss_mae'] > scored['Threshold']

#calculate the same metrics for the training set and merge all data in a single dataframe
X_pred_train = model.predict(X_train)
X_pred_train = X_pred_train.reshape(X_pred_train.shape[0], X_pred_train.shape[2])
X_pred_train = pd.DataFrame(X_pred_train, columns=train.columns)
X_pred_train.index = train.index

scored_train = pd.DataFrame(index=train.index)
scored_train['Loss_mae'] = np.mean(np.abs(X_pred_train - Xtrain), axis=1)
scored_train['Threshold'] = 0.5
scored_train['Anomaly'] = scored_train['Loss_mae'] > scored_train['Threshold']
scored = pd.concat([scored_train, scored])

scored.plot(logy=True, figsize=(6,19), ylim=[1e-4, 1e1], color=['blue', 'red'])
plt.show()

print(model.evaluate(X_train, X_pred_train))
print(model.evaluate(X_test, X_pred))

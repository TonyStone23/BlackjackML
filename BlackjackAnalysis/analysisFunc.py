import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.metrics import mean_squared_error as mse, mean_absolute_error as mae, mean_absolute_percentage_error as mape, r2_score as r2
from sklearn.cluster import KMeans

def kmeans(adf):
    x= adf.drop(['Dealer Wins', 'Stake'], axis = 1)
    X = x.to_numpy()

    fig = plt.figure(figsize = [10, 8])
    ax = fig.add_subplot(111, projection = '3d')

    plt.scatter(X[:, 0], X[:, 1], X[:, 2], c = 'gray')

    km = KMeans(n_clusters = 5, random_state = 42)
    km.fit(X)
    C = km.cluster_centers_
    labels = km.labels_

    for i in range(5):
        ax.scatter(
            X[labels == i, 0],
            X[labels == i, 1], 
            X[labels == i, 2], 
            label=f'Cluster {i+1}'
        )
    
    # Plot centroids
    ax.scatter(C[:, 0], C[:, 1], C[:, 2], s=200, c='red', marker='X', label='Centroids')

    ax.set_xlabel('Rounds')
    ax.set_ylabel('Wins')
    ax.set_ylabel('Earnings')
    plt.show()

def regression(adf):
    y = adf['Round Earnings']
    x = adf.drop(['Dealer Wins','Round Earnings', 'Player Wins'], axis = 1)

    x_train, x_test, y_train, y_test = tts(x, y, test_size = 0.2, random_state = 42)

    rf = rfr(n_estimators = 100, random_state = 42)
    rf.fit(x_train, y_train)

    y_test_pred = rf.predict(x_test)

    rf_mae = mae(y_test, y_test_pred)
    rf_mse = mse(y_test, y_test_pred)
    rf_rmse = np.sqrt(rf_mse)
    rf_mape = rf_mae * 100
    rf_r2 = r2(y_test, y_test_pred)

    importances = rf.feature_importances_
    featNom = x.columns
    indicies = np.argsort(importances)[::-1]

    print(f"predicted profit: {round(np.average(y_test_pred), 5)}")
    print(f"MSE: {round(rf_mse, 5)}")
    print(f"RMSE: {round(rf_rmse, 5)}")
    print(f"MAE: {round(rf_mae, 5)}")
    print(f"MAPE: {round(rf_mape, 5)}%")
    print(f"R2: {round(rf_r2, 5)}")

    impPlt = plt
    impPlt.figure(figsize = [10,6])
    impPlt.bar(range(x.shape[1]),importances[indicies], align = 'center')
    impPlt.xticks(range(x.shape[1]), featNom[indicies], rotation = 90)
    impPlt.title("Feature Importances")
    impPlt.ylabel("importance Score")
    impPlt.xlabel("Features")
    plt.show()

def heatmap(adf, title, vm):
    max = vm
    min = vm * -1
    corrmat = adf.corr()
    sns.heatmap(corrmat, vmax = max, vmin = min, square = True)
    plt.title(title)
    plt.show()


import numpy as np
import matplotlib.pyplot as plt


def Draw_map(predict, observed,model_name):
    # 显示预测图
    n = predict.shape[1]
    n1 = predict.shape[2]
    lim = np.arange(0, 0.6, 0.05)
    x = np.linspace(-6, 6, n1)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)

    predictive_model_name="predicted soil moisture by "+model_name+" model"
    plt.contourf(X, Y, predict[8],lim)
    plt.colorbar(orientation='horizontal')
    plt.title(predictive_model_name)
    plt.show()


    plt.contourf(X, Y, observed[8],lim)
    plt.colorbar(orientation='horizontal')
    plt.title("observed soil moisture")
    plt.show()




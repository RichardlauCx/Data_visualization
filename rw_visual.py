import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:  # 只要程序处于活动状态，就不停的模拟随机漫步
    rw = RandomWalk(50000)  # 创建一个Random_Walk的实例，并将其包含的点都绘制出来
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))  # 绘制图像

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.scatter(0, 0, c='yellow', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # plt.axes().get_xaxis().set_visible(False)  # 隐藏坐标轴
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
plt.plot(input_values, squares, linewidth=5)  # 提供输入x和输出值y，确保准确对应
# 设置图表标题， 并且给坐标加上标签

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

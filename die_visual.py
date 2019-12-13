from die_gallery import Die
import pygal

die = Die()  # 创建一个D6
results = []  # 掷几次骰子，并将结果存储在一个列表之中
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []  # 分析结果
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)  # 记录每一个点数出现的次数

hist = pygal.Bar()  # 可视化为直方图
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)  # 一个标签以及数据列表
hist.render_to_file("die_visual_1.svg")
print(frequencies)
from die_gallery import Die
import pygal

die_1 = Die()  # 创建一个 D6骰子和 D10骰子
die_2 = Die(10)
results = []  # 掷几次骰子，并将结果存储在一个列表之中
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()  # 返回两个骰子生成的总点数
    results.append(result)

frequencies = []  # 分析结果
max_result = die_1.num_sides + die_2.num_sides
# print(max_result)
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)  # 记录每一个点数出现的次数

hist = pygal.Bar()  # 可视化为直方图
hist.title = "Results of rolling a D6 and D10 dice 50000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)  # 一个标签以及数据列表
hist.render_to_file("die_visual_2.svg")
print(frequencies)
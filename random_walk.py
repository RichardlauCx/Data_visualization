from random import choice


class RandomWalk():  # 一个生成随机漫步数据的类
    def __init__(self, num_points=5000):  # 初始化随机漫步属性 类的内置函数 便于类绑定属性，也便于类对应方法
        self.num_points = num_points
        self.x_values = [0]  # 所有随机漫步都始于（0,0）
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])  # 决定前进方向以及沿这个方向前进的距离
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):  # 计算漫步包含的所有点
        while len(self.x_values) < self.num_points:  # 不断漫步，直到列表达到指定的长度

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:  # 拒绝原地踏步
                continue

            next_x = self.x_values[-1] + x_step  # 计算下一个x和y值
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
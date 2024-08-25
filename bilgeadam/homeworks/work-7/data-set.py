import math


class DataSet:

    def __init__(self, data):
        self.data = data

    def average(self):
        if len(self.data) == 0:
            return "ortalama 0"
        else:
            total = sum(self.data)
            return total / len(self.data)

    def median(self):
        if len(self.data) % 2 == 0:
            return "liste çift elemanlıdır"
        else:
            median = len(self.data) // 2
            return median

    def std_dev(self):
        if len(self.data) == 0:
            return "Data set is empty"
        avrg = sum(self.data) / len(self.data)
        avrg_diff = list(map(lambda x: x - avrg, self.data))
        sqrd_sum = sum(map(lambda x: x ** 2, avrg_diff))
        result = math.sqrt(sqrd_sum / (len(self.data)))
        return result


my_arr = [1, 2, 3, 4, 5]
data1 = DataSet(my_arr)

print(data1.average())  # Outputs the average
print(data1.median())   # Outputs the median index or a message
print(data1.std_dev())  # Outputs the standard deviation

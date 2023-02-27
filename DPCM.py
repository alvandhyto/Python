# PR#2 Sistem Komunikasi Multimedia
import math

# Contoh Input: "5 6 5 6 5 7 4 8 3 9 2 10 1 9 2 8 6 6 6 10 1 10 1 6 1 6 1 3 5 7 9"
sample = list(map(int, input("Input Set Sampel: ").split()))


def Rxx_0(sample):
    occurence = [[x, sample.count(x)] for x in set(sample)]
    sum = 0

    for i in range(len(occurence)):
        sum += occurence[i][1] * (occurence[i][0] ** 2)

    print("Rxx(0) = {0}/{1} = {2}".format(sum, len(sample), sum/len(sample)))


def Rxx_N(sample, N):
    sum = [0 for x in range(N)]

    for i in range(N):
        for j in range(len(sample) - (i + 1)):
            sum[i] += sample[j] * sample [j + (i + 1)]

        print("Rxx({0}) = {1}/{2} = {3}".format((i + 1), sum[i], (len(sample) - (i + 1)), sum[i]/(len(sample) - (i + 1))))


def Prediction_gain(sample):
    xi_squared = 0
    xi_squared_minus = 0

    for i in range(len(sample)):
        xi_squared += sample[i] ** 2
        xi_squared_minus += (sample[i] - (0.6225 * sample[i - 1])) ** 2

    print("Prediction Gain = {0}/{1} = {2}".format(xi_squared, xi_squared_minus, 10 * math.log(xi_squared/xi_squared_minus, 10)))


# Misal Nyari Rxx(3)
Rxx_0(sample)
Rxx_N(sample, 3)
Prediction_gain(sample)
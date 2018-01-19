import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# CSCI 127, Lab 12
# November 21, 2017
# Your Name
# -----------------------------------------------------

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()

    return number_buckets, county_populations

# -----------------------------------------------------

def print_summary(averages):
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])

# -----------------------------------------------------
# Do not change anything above this line
# -----------------------------------------------------

def calculate_averages(number_buckets, county_populations):
    n = 14
    x = np.array(county_populations)
    it1 = x[0:n:]
    avg1 = int(sum(it1) / n)
    it2 =x[14:n + 14:]
    avg2 = int(sum(it2) / n)
    it3 = x[28:n + 28:]
    avg3 = int(sum(it3) / n)
    it4 = x[42:n + 42:]
    avg4 = int(sum(it4) / n)
    averages = np.array((avg1, avg2, avg3, avg4), dtype=int)
    return averages
# -----------------------------------------------------

def graph_summary(averages):
    plt.figure("CSCI 127, Lab 12")
    plt.xticks([1, 2, 3, 4])
    plt.plot([1, 2, 3, 4], averages,"c--")
    plt.plot([1, 2, 3, 4], averages, "bh")
    plt.xlabel("County Groupings")
    plt.ylabel("County Population Average")
    plt.title("Montana County Population Analysis")
    plt.show()

# -----------------------------------------------------

number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)

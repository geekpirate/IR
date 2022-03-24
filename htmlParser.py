import collections
import os
import re
import sys
import datetime
import time
import matplotlib.pyplot as plt
import html2text
from bs4 import BeautifulSoup

start_time = datetime.datetime.now()
cpu_start_time = time.process_time()

# h = html2text.HTML2Text()
# h.ignore_links = True

allTokens = []
elapsedTimeList = []

inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])

allFiles = os.listdir(inputFile)
for each in allFiles:
    startTimeIndiv = datetime.datetime.now()
    path_in = os.path.join(inputFile, each)
    with open(path_in, 'r', encoding='utf-8', errors='ignore') as HTMLFile:
        index = HTMLFile.read()
        S = BeautifulSoup(index, 'html.parser')
        rawText = S.get_text().lower()
        # removes all punctuations
        rawText = re.sub(r'[^\w\s]', '', rawText)

        # removes all numbers
        out = [each for each in rawText.split() if each.isalpha()]

        allTokens += out
        # print(outputFile, each)
        if not os.path.exists(outputFile):
            os.makedirs(outputFile)
        outPath = os.path.join(outputFile, each + '.txt')
        with open(outPath, 'w', encoding='utf-8', errors='ignore') as oFile:
            for token in out:
                word = oFile.write(str(token))
                oFile.write('\n')
    elapsedEndTime = datetime.datetime.now() - startTimeIndiv
    elapsedTimeList.append(elapsedEndTime.total_seconds())

# calculates count frequency of tokens
outCount = collections.Counter(allTokens).most_common()


# sorts by token
outCount.sort(key=lambda x: x[0])

with open(r'/Users/abhinavreddy/PycharmProjects/IR_Phase_1/sortedByToken.txt', 'w', encoding='utf-8',
          errors='ignore') as sortedByToken:
    for stkn in outCount:
        sortedByToken.write(stkn[0] + " - " + str(stkn[1]))
        sortedByToken.write('\n')

# sorts by frequency
outCount.sort(key=lambda x: x[1])

with open(r'/Users/abhinavreddy/PycharmProjects/IR_Phase_1/sortedByFreq.txt', 'w', encoding='utf-8',
          errors='ignore') as sortedByFreq:
    for stfq in outCount:
        sortedByFreq.write(stfq[0] + " - " + str(stfq[1]))
        sortedByFreq.write('\n')

# Calculating the processing time
elapsed = datetime.datetime.now() - start_time
cpu_end_time = time.process_time()

print("Elapsed time taken in seconds:", elapsed.total_seconds())
print("CPU time taken in seconds:", cpu_end_time)

approach2 = [0.007979, 0.019984, 0.004961, 0.006011, 0.009936, 0.005022, 0.027887, 0.010974, 0.009005, 0.004988,
             0.009973, 0.007946, 0.002992, 0.003992, 0.004984, 0.008976, 0.009014, 0.008939, 0.024932, 0.001995, 0.004986, 0.01895, 0.005984, 0.001994, 0.012967, 0.004986, 0.030916, 0.010974, 0.024932, 0.004986, 0.00798, 0.001994, 0.00399, 0.011004, 0.001962, 0.004986, 0.011968, 0.005983, 0.007981, 0.011966, 0.007978, 0.005026, 0.073764, 0.009974, 0.001004, 0.007971, 0.007979, 0.002992, 0.00399, 0.008975, 0.004987, 0.005985, 0.005983, 0.008976, 0.004987, 0.001994, 0.002993, 0.006001, 0.009954, 0.005986, 0.004985, 0.002992, 0.003531, 0.005988, 0.004989, 0.010968, 0.00399, 0.004003, 0.003975, 0.004987, 0.00399, 0.002991, 0.00399, 0.004986, 0.135638, 0.026927, 0.012964, 0.004988, 0.004987, 0.00399, 0.004986, 0.010971, 0.005985, 0.004986, 0.005983, 0.004988, 0.007978, 0.006981, 0.004987, 0.002006, 0.004976, 0.003989, 0.001995, 0.005982, 0.015958, 0.001995, 0.002992, 0.002992, 0.005984, 0.003989, 0.008975, 0.001, 0.00299, 0.003989, 0.005657, 0.00399, 0.00203, 0.003984, 0.003958, 0.002992, 0.001994, 0.00399, 0.002991, 0.015958, 0.014962, 0.003988, 0.00698, 0.020945, 0.010972, 0.017951, 0.009974, 0.02194, 0.004988, 0.01097, 0.005984, 0.003989, 0.004986, 0.002993, 0.012966, 0.000998, 0.004986, 0.007979, 0.038895, 0.009974, 0.006982, 0.007977, 0.072806, 0.007979, 0.004988, 0.004985, 0.017951, 0.003991, 0.006981, 0.005985, 0.009972, 0.032912, 0.095744, 0.003989, 0.006981, 0.057846, 0.003989, 0.045877, 0.001995, 0.033909, 0.003991, 0.008974, 0.004988, 0.002992, 0.01496, 0.008975, 0.011968, 0.005984, 0.00499, 0.004984, 0.004986, 0.008977, 0.012965, 0.002991, 0.003991, 0.003989, 0.003988, 0.008976, 0.021942, 0.008977, 0.003989, 0.092751, 0.019947, 0.003991, 0.020943, 0.004986, 0.031914, 0.011969, 0.126661, 0.00798, 0.018949, 0.004986, 0.007978, 0.002991, 0.01496, 0.003991, 0.004993, 0.005977, 0.061861, 0.064818, 0.006967, 0.00299, 0.00698, 0.001994, 0.004986, 0.002992, 0.005987, 0.004985, 0.071808, 0.004987, 0.00698, 0.004003, 0.006968, 0.002995, 0.007978, 0.004985, 0.002993, 0.004986, 0.20944, 0.003989, 0.006016, 0.002991, 0.001994, 0.002963, 0.003988, 0.004023, 0.002962, 0.01, 0.009979, 0.005948, 0.00602, 0.016919, 0.003028, 0.001957, 0.004988, 0.009013, 0.003951, 0.01097, 0.017953, 0.032911, 0.019947, 0.013962, 0.010972, 0.009973, 0.017984, 0.034876, 0.016011, 0.017952, 0.046874, 0.025931, 0.016953, 0.029923, 0.037897, 0.016956, 0.051859, 0.015957, 0.01496, 0.044863, 0.00898, 0.014957, 0.007979, 0.016956, 0.009972, 0.057842, 0.012972, 0.029884, 0.009973, 0.011008, 0.010965, 0.011978, 0.006941, 0.022936, 0.021975, 0.008942, 0.038929, 0.01296, 0.009986, 0.022934, 0.011969, 0.012961, 0.009974, 0.016958, 0.020948, 0.012962, 0.037898, 0.031877, 0.027926, 0.042885, 0.022941, 0.017986, 0.015961, 0.016956, 0.024894, 0.007976, 0.047873, 0.023935, 0.012009, 0.0289, 0.006967, 0.009971, 0.016954, 0.007978, 0.008977, 0.051862, 0.029956, 0.010937, 0.021976, 0.010965, 0.05183, 0.054889, 0.007942, 0.010973, 0.084802, 0.031882, 0.058845, 0.02194, 0.024933, 0.008976, 0.013963, 0.011968, 0.018949, 0.01097, 0.008977, 0.012966, 0.007978, 0.010971, 0.022938, 0.019949, 0.034904, 0.008978, 0.059838, 0.028924, 0.009975, 0.034903, 0.018951, 0.024933, 0.042886, 0.019948, 0.071808, 0.022939, 0.027922, 0.036904, 0.011968, 0.020942, 0.054855, 0.065824, 0.01795, 0.023968, 0.014928, 0.021942, 0.02593, 0.030917, 0.029921, 0.063829, 0.101728, 0.049868, 0.074798, 0.015957, 0.022941, 0.056849, 0.021938, 0.007979, 0.013963, 0.069813, 0.096741, 0.071808, 0.160571, 0.01496, 0.046874, 0.026928, 0.019947, 0.050864, 0.01496, 0.019946, 0.05685, 0.018948, 0.047872, 0.062832, 0.060837, 0.067821, 0.053853, 0.086768, 0.098739, 0.017957, 0.033902, 0.048868, 0.054854, 0.026928, 0.033909, 0.015958, 0.019946, 0.011969, 0.009983, 0.01495, 0.019946, 0.030918, 0.017953, 0.024934, 0.023936, 0.016955, 0.039893, 0.022939, 0.020942, 0.341088, 0.145612, 0.111699, 0.260305, 0.089759, 0.244347, 0.097741, 0.219411, 0.083809, 0.293183, 0.016986, 0.10973, 0.248282, 0.099731, 0.3002, 0.113696, 0.225395, 0.092751, 0.273303, 0.109673, 0.262332, 0.016922, 0.124678, 0.21842, 0.155584, 0.236368, 0.089794, 0.260274, 0.008972, 0.008977, 0.005984, 0.282246, 0.086766, 0.276262, 0.13364, 0.135639, 0.103755, 0.108712, 0.079781, 0.08175, 0.058844, 0.043883, 0.092751, 0.071808, 0.027925, 0.104723, 0.049863, 0.008016, 0.006976, 0.005984, 0.003982, 0.004002, 0.004954, 0.003025, 0.003986, 0.020909, 0.005985, 0.001995, 0.002991, 0.002992, 0.00399, 0.087767, 0.004987, 0.062831, 0.047872, 0.063831, 0.071807, 0.007978, 0.005984, 0.002993, 0.007978, 0.005984, 0.002992, 0.008976, 0.002992, 0.004987, 0.003989, 0.005984, 0.007979, 0.002992, 0.004984, 0.005986, 0.00399, 0.005983, 0.005984, 0.006982, 0.013962, 0.005984, 0.004987, 0.004987, 0.00299, 0.003991, 0.002992, 0.003989, 0.023935, 0.002992, 0.017989, 0.001992, 0.002964, 0.005014, 0.084739, 0.009973, 0.007979, 0.010973, 0.007978, 0.009009]

plt.plot(list(range(1, len(elapsedTimeList)+1)), elapsedTimeList, color='green')
plt.plot(list(range(1, len(approach2)+1)), approach2, color='blue')
plt.xlabel("Number of Files")
plt.ylabel("Time elapsed")
plt.show()
plt.savefig("Time elapsed")


# 3.681029
# 3.654225


#
#
#
# # Opening the html file
# # HTMLFile = open("002.html", "r", encoding="utf8", errors='ignore')
#
#
# # Creating a BeautifulSoup object and specifying the parser
# S = BeautifulSoup(index, 'html.parser')
#
#
# # print(S.get_text())
# rawText = S.get_text().lower()
# # Using the select-one method to find the second element from the li tag
# # Tag = S.select_one('li:nth-of-type(2)')
#
# # Using the decompose method
# # Tag.decompose()
#
# # Using the prettify method to modify the code
# # print(S.body.prettify())
#
# # print(h.handle(S.body.prettify()).lower())
#
#
# # rawText = h.handle(S.body.prettify()).lower()
# # print(rawText)
#
#
# # removes all punctuations
# rawText = re.sub(r'[^\w\s]', '', rawText)
#
# # removes all numbers
# out = [each for each in rawText.split() if each.isalpha()]

import collections
import math
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
word_counts = []
allTokens = []
elapsedTimeList = []
fileCount = os.listdir('files')


inputFile = "files"
outputFile = "out1"

fileNames = []

# inputFile = str(sys.argv[1])
# outputFile = str(sys.argv[2])
sw = open(r"stopwords.txt", "r")
stop_words = sw.read().split()
outAll = []
allFiles = os.listdir(inputFile)
for each in allFiles:
    fileNames.append(each.split(".")[0])
    # print(each.split(".")[0])
    # exit()
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

        # allTokens += out
        word_counts.append(len(out))
        # print(outputFile, each)
        # if not os.path.exists(outputFile):
        #     os.makedirs(outputFile)
        # outPath = os.path.join(outputFile, each + '.txt')
        # with open(outPath, 'w', encoding='utf-8', errors='ignore') as oFile:
        #     for token in out:
        #         word = oFile.write(str(token))
        #         oFile.write('\n')
    elapsedEndTime = datetime.datetime.now() - startTimeIndiv
    elapsedTimeList.append(elapsedEndTime.total_seconds())

# calculates count frequency of tokens
    outCount = collections.Counter(out).most_common()
    outAll.append(outCount)

# sorts by token
# outCount.sort(key=lambda x: x[0])

# with open(r'/Users/abhinavreddy/PycharmProjects/IR_Phase_1/sortedByToken.txt', 'w', encoding='utf-8',
#           errors='ignore') as sortedByToken:
#     for stkn in outCount:
#         if stkn[1] > 1:
#             sortedByToken.write(stkn[0] + " - " + str(stkn[1]))
#             sortedByToken.write('\n')
#
# # sorts by frequency
# outCount.sort(key=lambda x: x[1])
#
# with open(r'/Users/abhinavreddy/PycharmProjects/IR_Phase_1/sortedByFreq.txt', 'w', encoding='utf-8',
#           errors='ignore') as sortedByFreq:
#     for stfq in outCount:
#         if stfq[1] > 1:
#             sortedByFreq.write(stfq[0] + " - " + str(stfq[1]))
#             sortedByFreq.write('\n')

outAllList = []
# print(len(fileNames))
for each in outAll:
    outAlldict = {}
    for k, j in each:
        if j > 1 and len(k) > 1:
            outAlldict[k] = j
    outAllList.append(outAlldict)


# print(len(outAllList))
time_elapsed_v1 = []

idf = dict()
for i in outAllList:
    start_t = time.time()
    for j in i.keys():
        if j in idf:
            idf[j] += 1
        else:
            idf[j] = 1
    time_elapsed_v1.append(time.time()-start_t)

# print(idf.items())
cnt = 0

time_elapsed_v2 = []
for i in outAllList:
    start_t = time.time()
    tf = dict()
    for j in i.keys():
        tf[j] = i[j]/word_counts[cnt]*math.log(len(fileCount)/idf[j])
    time_elapsed_v2.append(time.time()-start_t)

    if not os.path.exists(outputFile):
        os.makedirs(outputFile)
    # outPath = os.path.join(outputFile, each + '.txt')

    f1 = open(r"" + outputFile + "/" + fileNames[cnt] + ".wts", "w+")  # write tokens to file
    for key, value in tf.items():
        f1.write(str([key, value]))
    f1.close()
    cnt += 1




exec_t = []
t_each = []
for i in range(len(elapsedTimeList)):
    t_each.append(elapsedTimeList[i] + time_elapsed_v1[i] + time_elapsed_v2[i])
exec_t.append(t_each[0])
for i in range(1, len(time_elapsed_v1)):
    t_each[i] = t_each[i - 1] + t_each[i]
    exec_t.append(t_each[i])

file_c = range(1, 504)

filec1 = [10, 20, 40, 80, 100, 200, 300, 400, 500]
exect1 = []
for i in filec1:
    exect1.append(exec_t[i])

# print(exect1)


plt.plot(filec1, exect1)
plt.xlabel("files")
plt.ylabel("Time (seconds)")
plt.show()


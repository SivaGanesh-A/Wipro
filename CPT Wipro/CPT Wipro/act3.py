l = [-2,-1,0,1,2]
positives = 0
negatives = 0
for i in l:
    if i >= 0:
        positives += 1
    else:
        negatives += 1
print('positive: ',positives,'negatives : ',negatives)
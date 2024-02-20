def question2(text, k):
    distanceCount = {} # 记录上次出现的距离
    alphabetCount = {} # 记录是否出现
    result = '' # 返回的结果
    for i in range(len(text)):
        if i - distanceCount.get(text[i], 0) <= k and alphabetCount.get(text[i], 0) > 0:
            result += '-' # 若满足条件，则替换
        else:
            result += text[i] # 不满足条件则不替换
        alphabetCount[text[i]] = alphabetCount.get(text[i], 0) + 1 # 更新出现的次数
        distanceCount[text[i]] = i # 更新最后一次出现的位置
    return result # 返回替换后的结果
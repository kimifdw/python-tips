def ShellSort(list):
    distance = len(list)/2
    while distance >0:
        for i in range(distance, len(list)):
            temp = input_list[i]
            j = i
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            list[j] = temp
        distance = distance//2
    return list
train_v = 10
 
def train_add(list_n):
    train_sum = 0
    for i in range(len(list_n)):
        train_sum += list_n[i]
    return train_sum
list_n = [2,3,4,5,6] 
print(train_add(list_n))

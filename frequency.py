test_Dict  = {" Codingal " : 2, "is": 2, "best": 2, "For": 2, "Coding": 1}


print("The original dictionary : " + str(test_Dict))


K = 2


res = 0

for key in test_Dict:
    if test_Dict[key] == K:
        res = res + 1


print("Frequency of K is: " + str(res))

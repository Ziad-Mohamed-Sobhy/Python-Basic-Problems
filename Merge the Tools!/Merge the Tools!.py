def merge_the_tools(string, k):
    # your code goes here
    for i in range (0,len(string) ,k) :
        term = string[i:i+k]
        check_set = set()
        output = []
        for ch in term :
            if ch not in check_set:
                check_set.add(ch)
                output.append(ch)
        print(''.join(output))


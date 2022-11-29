import sys
import re

def projectno7(first_file, sec_file):
    new_list = []

    #file_prim = str(sys.argv[1])
    f = open(first_file)
    data = f.read()
    data = re.sub(" +", " ", data)
    data = data.replace("\n", " ")
    # print(data)
    a = re.split(r'[\.\?!]]* *', data)
    # print(a)

    new_a = [i for i in a if any(c.isalpha() for c in i)]
    # print(new_a)

    f.close()

    # file_sec = str(sys.argv[2])
    f1 = open(sec_file)
    data2 = f1.read()
    # print(data2)
    data2 = re.sub(" +", " ", data2)
    data2 = data2.replace("\n", " ")
    # print(data2)
    b = re.split(r'[\.\?!]]* *', data2)
    # print(b)
    new_b = [i for i in b if any(c.isalpha() for c in i)]
    # print(new_b)
    f1.close()

    common_phrases = []
    for i in new_a:
        if i in new_b:
            common_phrases.append(i)

    for i in common_phrases:
        if i in data:
            pozitie = data.index(i)
            cuv = i
            cuv += data[pozitie + len(i)]
            new_list.append(cuv)

    print("Common Phrases from given text files: ")
    print(set(new_list))


if __name__ == '__main__':
    file_prim = str(sys.argv[1])
    file_sec = str(sys.argv[2])
    projectno7(file_prim, file_sec)



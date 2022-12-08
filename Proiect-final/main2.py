import sys
import re

def prelucrare_propozitii_file(file):
    f = open(file)
    data_file = f.read()
    data_file = re.sub(" +", " ", data_file)
    data_file = data_file.replace("\n", " ")
    # print(data)
    #phrases = re.split(r'[\.\?!]]* *', data)
    phrases = re.findall("[A-Z0-9].*?[\.?!]",data_file)
    # print(phrases)
    #in updated_phrases o sa fie adaugate doar fraze valide

    #updated_phrases = [i for i in phrases if any(c.isalpha() for c in i)]
    # print(updated_phrases)
    f.close()
    return phrases



def projectno7(first_file, sec_file):

    fraze_file_prim=prelucrare_propozitii_file(first_file)
    fraze_file_sec=prelucrare_propozitii_file(sec_file)

    common_phrases = []
    for i in fraze_file_prim:
        propozitia_fara_semn_din_prim_file=i[:-1]
        for j in fraze_file_sec:
            propozitia_fara_semn_din_sec_file = j[:-1]
            if propozitia_fara_semn_din_prim_file == propozitia_fara_semn_din_sec_file:
                common_phrases.append(i)


    print("Common Phrases from given text files: ")
    print(set(common_phrases))


if __name__ == '__main__':
    file_prim = str(sys.argv[1])
    file_sec = str(sys.argv[2])
    projectno7(file_prim, file_sec)
    #print(prelucrare_propozitii_file(file_sec))
    #print(prelucrare_propozitii_file(file_prim))





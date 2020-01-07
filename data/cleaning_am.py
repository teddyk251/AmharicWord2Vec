import re


def cleaning_am(fname):
    fin = open(fname, encoding='utf-8')
    fout = open('cleaned_' + fname, 'w', encoding="utf-8")
    for line in fin:
        line = line.rstrip()
        pattern = re.compile(r"[\u1200-\u135A \u1361 \u1363-\u1364 0-9]+")
        line = " ".join(re.findall(pattern, line))
        print(line)
        fout.write(line + "\n")
    fin.close()
    fout.close()


cleaning_am('am.csv')

import sys, os

def reformat_file(in_file, out_file):

    #'ID', 'FORM', 'LEMMA', 'CPOS', 'POS', 'FEATS', 'HEAD', 'DEPREL', 'PHEAD', 'PDEPREL'
    out = open(out_file, 'w')

    with open(in_file, 'r') as fp:
        for i, line in enumerate(fp):
            arr = line.strip()
            if len(arr) == 0:
                out.write('\n')
                continue
            arr = arr.split('\t')
            ID = arr[0]
            form = arr[1]
            lemma = '_'
            cpos = arr[2]
            cpos = '_'
            pos = arr[2]
            pos = '_'
            feats = arr[3]
            feats = '_'
            head = arr[4]
            deprel = arr[5]
            phead = '_'
            pdeprel = '_'
            out.write(ID + '\t' + form + '\t' + lemma  + '\t' +  cpos + '\t' + pos + '\t' + feats + '\t' + head + '\t' + deprel + '\t' + phead + '\t' + pdeprel + '\n')

    out.close()


if __name__=="__main__":


    reformat_file(sys.argv[1], sys.argv[2])

import time
from ast import literal_eval
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k','--k', help='K itemset', required=True)
parser.add_argument('-f','--frequency', help='Frequency', required=True)
parser.add_argument('-d','--dataset', help='Dataset name', required=True)

args = parser.parse_args()

filename = args.dataset
minimum_support = int(args.frequency)
k = int(args.k)



def utility_function():
    """
    returns : final_transaction of type list of sets
              vocab_size which is the vocabulary size
    """
    f=open("Desktop/sem_3/dmml/assignment1/docword."+str(filename)+".txt",'r')
    lines=f.read().splitlines()
    vocab_size=int(lines[1])
    transactions = [[] for i in range(int(lines[0]))]
    lines=[x.split(' ') for x in lines[3:]]
    lines=[list(map(int,x)) for x in lines]
    for x in lines:
        transactions[x[0]-1].append(x[1])
    final_transaction=[set(x) for x in transactions]

    return (final_transaction,vocab_size)



def apriori(transaction, vocab_size, minimum_support, maxk):
    word_id_file=open("Desktop/sem_3/dmml/assignment1/Result."+str(filename)+".txt",'w') 
    F1=[]    
    F=[]  

    for x in range(1,vocab_size+1):
        count=0
        for l in transaction:
            if x in l :
                count+=1
        if count>=minimum_support :
            F1.append([x])
    F_prev = F1   
    k=1
    F.append(F_prev)

    while len(F_prev)!=0 and k<maxk:
        F_next = []
        candidate_list = candidate_gen(F_prev,k)
        candidate = [set(x) for x in candidate_list]
        for c in candidate:
            count = 0
            for t in transaction:
                if c.issubset(t):
                    count+=1
            if count>=minimum_support :
                F_next.append(list(c))
        F_prev = F_next
        F.append(F_prev)
        k+=1
    word_id_file.write(str(F))



def candidate_gen(F,K):
    C=[]
    n=len(F)
    if(K==1):
            for i in range(n):
                for j in range (i+1,n):
                    C = C+[[F[i][0],F[j][0]]]
            return C
    for itemset in F:
        itemset.sort()
    for i in range(n):
        for j in range(i+1,n):
            temp = 0
            for k in range (K-1):
                if F[i][k] == F[j][k]:
                    continue
                else:
                    temp = 1
                    break
            if temp==0:
                c=F[i][:]
                c.append(F[j][K-1])
                count=0
                for l in range(K):
                    for itemset in F:
                        if itemset==(c[:l]+c[(l+1):]) :
                            count += 1
                            break
                if count==K :
                    C = C+[c]
            else:
                break
    return C



if __name__=='__main__':

    start=time.time()  
    
    transactions, vocab_size = utility_function()
    apriori(transactions,vocab_size,minimum_support,k)

    vocab_file=open("Desktop/sem_3/dmml/assignment1/vocab."+str(filename)+".txt")
    vocab=vocab_file.read().splitlines()
    result=open("Desktop/sem_3/dmml/assignment1/Result."+str(filename)+".txt")
    temp=result.read().splitlines()
    temp=literal_eval(temp[0])

    Frequent_itemset=[]
    if(k<=len(temp)):
        for tmp in temp:
            for y in tmp:
                Frequent_itemset.append(list(map(lambda x: vocab[x-1], y)))
        file_out=open("Desktop/sem_3/dmml/assignment1/Final_Result-"+str(filename)+".txt",'w')
        file_out.write(str(Frequent_itemset))
        file_out.close()
    else:
        print("No itemset for k")

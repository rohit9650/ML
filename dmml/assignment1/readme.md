This is the first DMML assignment submission by Rohit Singh(MCS201812) & Shrisha Rao(MCS201916)

A K-itemset of words is a collection of words of size K that occur together in the same document.
(We interpret that K is the K length collection of words, hence, our code output all frequent itemsets of 
length atmost k.)

The input will be of the form -k=(value of K) -f=(value of F) -d=(name of the dataset)

Our code runs as follows:

In lines 5-14, we decode the value of F, K, and the dataset.

In lines 18-33, the utility function outputs the list of documents as sets containing the id's of the words
present in them. It also returns the length of the vocabulary.

In lines 37-67, we define the apriory function, which, after each iteration, adds the frequent itemsets (of words)
that it outputted to a big list that will contain all the frequent wordsets's id's.

In lines 71-103, we implement the cabdidate generation function.
    81-89: we check if the two itemsets differ only at the last position.
    90-92: append the last element of the second itemset to the first itemset.
    93-100: check if every k-subset is in F_k

In the later lines, we run the code on the input and then decode each word id to it's corresponding word.
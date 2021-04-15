DNA = input('DNA sequence is:')
def reverse(DNA):
    another_DNA_1=''
    complement = {'A':'T','a':'t','T':'A','t':'a','C':'G','G':'C','c':'g','g':'c'}
    for i in DNA:
        another_DNA_1 += complement[i]
    another_DNA = another_DNA_1[::-1]
    print(another_DNA)
    return another_DNA
reverse(DNA)

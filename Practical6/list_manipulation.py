gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
average_axon_length=[a/b for a,b in zip(gene_lengths,exon_counts)]#each value in exon_counts is divided by corresponding value in gene_lengths
print(sorted(average_axon_length))#show the sorted list, or it won't be shown when running
import matplotlib.pyplot as plt
plt.boxplot(average_axon_length)
plt.show()

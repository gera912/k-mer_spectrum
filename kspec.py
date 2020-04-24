#!/usr/bin/env python

# Program Header
# Course: Bi621
# Name:   Gerardo Perez
# Description: Python script that k-merize our data
# set at different sizes for k and plot the result.
#
# ps6: Part 1: k-mer Spectrum
#
#
# Development Environment: Atom 1.38.2
# Version: Python 3.7.3
# Date:  06/19/2019
#################################################


# Stores a file path to a variable
#file = "../lane1_NoIndex_L001_R1_003.fastq"
#file = "../test20190703.txt"

# Imports module
import matplotlib.pyplot as plt
import argparse



# Creates arguementparser object by using the argparse
parser = argparse.ArgumentParser(description="A program for K-mers")

# Adds arguemets by calling the arguement passer
parser.add_argument("-k", "--kmer_size", type = int, help="specify the k-mer size", required=True)

# Adds arguemets by calling the arguement passer
parser.add_argument("-f", "--filename", help="specify the filename", required=True)

# Parses arguemets through using the parse args method.
args = parser.parse_args()


# Creates a variable
LN =0


#KMER_LENGTH = 15

# Creates a dictionary. keys for k-mers, values os number of occurences
kmer_dict = {}

# creates a global variablethe to store the number of k-mers per record.
kcnt= 101 - args.kmer_size +1

# opens a text file to read and stores the text file as a variable.
with open(args.filename, 'r') as fh:

#with open(file, 'r') as fh:

    # A for loop that goes through each line in the text file.
    for line in fh:

        # updates the variable by an addition of one after each loop.
        LN = LN +1

        # If statemnt to get the second line from each record in text file.
        if LN%4 == 2:

            # Creates a variable
            i = 0

            # A for loop that goes through the range of a list
            for i in range(kcnt):

                # It slices a specific part in the list.
                kmer= line[0+i:args.kmer_size+i]

                # If statement to check if kmer is in the dictionary.
                if kmer in kmer_dict:

                    # If true, it add a 1 to the value of the key, the kmer.
                    kmer_dict[kmer]+=1


                else:

                    # If false, it sets 1 as a value of the key, the kmer
                    kmer_dict[kmer]=1

# Creates a dictionary that will store keys as the kmer frequency and store values
# as the number of kmers in that frequency.
k_count_dict = {}

# A for loop that goes through the items in the dictionary.
for key, value in kmer_dict.items():

    # If statement that checks if the value is in the dictionary
    if value in k_count_dict:

        # If true then add a 1 to the value of the key.
        k_count_dict[value]+= 1

    else:

        # If false, then store 1 as a value for the key.
        k_count_dict[value]=1


# Prints a statement
print("#k-mer frequency\t", "Number of K-mers in this category")

# A for loop that goes through the items in the dictionary.
for key, value in k_count_dict.items():

    # Prints a statement in a specific format
    print("{0}\t{1}\n".format(key,value))

# Plots a bar chart, “k-mer frequency” on on the X-axis and the “Number of k-mers
# in this category” on the Y-axis. Plots a log scale for the y axis.
plt.bar(k_count_dict.keys(), k_count_dict.values(), log = True)

# Limits the x-axis in plot
plt.xlim((0, 10000))

# Labels a title
plt.title('KMER_LENGTH = %i' %args.kmer_size)

# Labels X axis
plt.xlabel('k-mer frequency')

# Labels Y axis
plt.ylabel('Number of k-mers ')

# Outputs the plot.
plt.show()

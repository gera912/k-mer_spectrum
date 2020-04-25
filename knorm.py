#!/usr/bin/env python


# Program Header
# Course: Bi621
# Name:   Gerardo Perez
# Description: Python script that normalizes the
# k-mer coverage of your input reads and save those reads
# to a new FASTQ file
#
# ps6: Part 2: k-mer Normalization
#
# Development Environment: Atom 1.38.2
# Version: Python 3.7.3
# Date:  06/19/2019
#################################################

# Stores a file path to a variable
#file = "../lane1_NoIndex_L001_R1_003.fastq"
#file = "../test20190703.txt"

# Imports a module
import argparse

# Creates an arguement passer
parser = argparse.ArgumentParser(description="A program for K-mers")

# Adds arguemets by calling the arguement passer
parser.add_argument("-c", "--kmer_coverage", type = int, help="specify the coverage limit", required=True)

# Adds arguemets by calling the arguement passer
parser.add_argument("-f", "--filename", help="specify the filename", required=True)

# Adds arguemets by calling the arguement passer
parser.add_argument("-o", "--output_file", help="specify the filename", required=True)

# Parses arguemets through using the parse args method.
args = parser.parse_args()


# Creates a variable
KMER_LENGTH = 11

# Creates a variable
kcnt= 101 - KMER_LENGTH +1

# Creates a variable
cutoff = 5

# Creates a variable
LN =0


# Creates a dictionary. keys for k-mers, values os number of occurences
kmer_dict = {}

# Opens a text file to read and write. stores the text file as a variable.
with open(args.filename, 'r') as fh, open('lane1_NoIndex_L001_R1_003_%sX.fastq' % args.output_file, 'w') as f:

    # A while loop.
    while True:

        # Reads the line and strips the new line character.
        # Stores the result to a variable. Moves to next line.
        L1 = fh.readline().strip()

        # if statemnt to break for loop.
        if L1 == "":
            break

        # updates the variable by an addition of one after each line has been read.
        LN = 1 + LN

        # Reads the line and strips the new line character.
        # Stores the result to a variable. Moves to next line.
        L2 = fh.readline().strip()

        # updates the variable by an addition of one after each line has been read.
        LN = 1 + LN

        # Reads the line and strips the new line character.
        # Stores the result to a variable. Moves to next line.
        L3 = fh.readline().strip()

        # updates the variable by an addition of one after each line has been read.
        LN = 1 + LN

        # Reads the line and strips the new line character.
        # Stores the result to a variable. Moves to next line.
        L4 = fh.readline().strip()

        # updates the variable by an addition of one after each line has been read.
        LN = 1 + LN

        # A for loop that goes through the range of a list
        for i in range(kcnt):

            # It slices a specific part in the list.
            kmer = L2[0+i:KMER_LENGTH+i]

            # If statement to check if kmer is in the dictionary.
            if kmer in kmer_dict:

                # If true, it add a 1 to the value of the key, the kmer.
                kmer_dict[kmer]+=1

            else:

                # If false, it sets 1 as a value of the key, the kmer
                kmer_dict[kmer]=1

        # Creates a list.
        coverage=[]


        # A for loop that goes through the range of a list
        for i in range(kcnt):

            # It slices a specific part in the list.
            kmer= L2[0+i:KMER_LENGTH+i]

            # Adds a k-mer coverages to the list.
            coverage.append(kmer_dict[kmer])

        # Sorts list.
        coverage.sort()

        #computates the mid point of the list into a varaible.
        # lenght of the list divided by 2.
        med = int(len(coverage)/2)

        ##If statement that checks if the length of the list
        #is divisible by two
        if len(coverage) % 2 == 0:


            # If true then stores the index value that is in the position
            # before the mid way point into a variable.
            medL = coverage[med -1]

            # If true then stores the index value that is in the position
            # after the mid way point into a variable.
            medR = coverage[med]

            # Stores and computes the average of the two mid points value of a
            # even length list into a variable.
            median = (medL +medR)/2

            # If statement that checks if the median k-mer coverage is less or equal
            # to the cutoff.
            if median <= args.kmer_coverage:

                # if true, writes the formatted output to the fastq file
                f.write("{0}\n{1}\n{2}\n{3}\n".format(L1,L2,L3,L4))



        else:
            ##If false then stores the computated half way point of the list into a variable.
            # lenght of the list divided by 2 into a variable
            median=coverage[med]

            # If statement that checks if the median k-mer coverage is less or equal
            # to the cutoff.
            if median <= args.kmer_coverage:

                # if false, writes the formatted output to the fastq file
                f.write("{0}\n{1}\n{2}\n{3}\n".format(L1,L2,L3,L4))

Part 1: k-mer Spectrum
Our goal with this assignment is to understand k-mers and what they can tell us about the underlying nature of our genomic data. We will be working with (part of) a lane of 101bp Illumina sequence data. Our goal is to k-merize our data set at different sizes for k and plot the result. Call this script kspec.py and be sure to put in in your PS5 repo.
1. We will once again be working with this file, which you may have already downloaded (but get a fresh copy from Talapas if necessary):
  lane1_NoIndex_L001_R1_003.fastq.gz
This file contains 4 million Illumina reads from one of our stickleback experiments.
2. Set a global variable at the top of your program to hold the k-mer size and a second global variable to hold the file name to process (HINT: This does NOT require the use of the python keyword “global”). Write code to set these variables using the command line option -k to specify the k-mer size and the option -f to specify the filename (HINT: argparse).
3. Initialize a dictionary. In this dictionary, the k-mers themselves will act as the keys. This data structure will hold the number of occurrences of each k-mer. What are your keys? What are your values? Document each as a descriptive comment when you initialize your dictionary!
4. Given the k-mer size (-k) and read length above, calculate the number of k-mers per record and store it as global variable (HINT: The lecture tells you how to calculate this number). This may be useful during #5 below.
5. Open the FASTQ file and loop through every record. k-merize each read and either initialize or increment the counter in the dictionary for each k-mer you encounter. To do this, construct a loop that will extract the correct k-mer substring as you iterate over a given sequence (HINT: String splicing).
6. Create a second dictionary to hold a summary of your k-mer counts. Iterate over your dictionary of k-mers and record the number of k-mers that occur one time, the number of k- mers that occur twice, the number that occur three times... the number that occur 1000 times, and so on. What are your keys? What are your values? Document! Later you will use this dictionary to make a histogram plot.
7. Print to the terminal the k-mer frequency, like this (tab separated):
# k-mer frequency Number of k-mers in this category
 
1 100000 2 99999 3 89998 ...
8. Run your k-mer spectrum script twice, first with a k-mer length of 11, and then with a k-mer length of 15.
9. Plot these results as a histogram any way you know how: using Excel, R, gnuplot, matplotlib, etc. Plot the “k-mer frequency” on on the X-axis and the “Number of k-mers in this category” on the Y-axis. Use a logscale on the Y-axis so the data are more visible. You only need to plot values along the X-axis up to 10,000.
Part 2: k-mer Normalization
In the second part of this assignment your goal is to write a second Python script to normalize the k-mer coverage of your input reads and save those reads to a new FASTQ file. Call this program knorm.py.
1. Set a global variable at the top of your program to hold the k-mer coverage limit and a second variable to hold the input filename. Write code to set these variables using the command line option -c to specify the coverage limit and the option -f to specify the filename.
2. Initialize an empty dictionary. In this dictionary, the k-mers themselves will act as the keys, and the values will be the number of occurrences of each k-mer. DO NOT fill this dictionary now, wait until #5.2 below. (If we filled this dictionary here, we would be writing a k-mer filter; think about why that would be).
3. Open an output file to place reads that we wish to keep. You can specify this second file with another command line option or by modifying the input file name from the -f option (say, by adding a suffix to it).
4. Initialize an integer and set it to 0. Use this integer to keep track of what line number you are on when looping through the input FASTQ file.
5. Open the FASTQ file and loop through every record.
1. Store all four lines of the first FASTQ record in memory (HINT: Think about using modulus. How do you know you’ve gotten a full FASTQ record?). You may store the FASTQ record in whatever data structure(s) you feel is/are appropriate.
2. Now that you have a full FASTQ record, k-merize the current read and increment the counter in the dictionary (from #2 above) for each k-mer you encounter. What are your keys? What are your values? This dictionary acts as of tally of the k-mers we’ve observed so far.
 
3. Initialize an empty array. This array will store the k-mer coverages for this read.
4. Re-k-merize the same, current read, looking up each k-mer’s coverage in the dictionary, and append those coverage values to the array from #5.3.
5. Calculate the median k-mer coverage for this read from the coverage array (still no numpy allowed).
6. If the median k-mer coverage of the read is above the k-mer coverage limit do not output this read, otherwise retain the read by writing it to the output FASTQ file.
7. Continue looping through the input file.
6. Once your program is complete, normalize the input file at 5x and 10x coverage limits.
7. Use your kspec.py program to compute and plot the k-mer spectrum for the 5x and 10x normalized input files produced in #6.
To turn in your work for this assignment, do the following:
1. Upload your 2 scripts to GitHub. They must be well commented and readable.
2. You will also need to turn in four k-mer spectrum plots, two from Part 1, and two from
Part 2.
3. DO NOT add the FASTQ files to your git repo.

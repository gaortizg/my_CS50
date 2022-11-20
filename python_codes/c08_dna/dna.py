import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage:python dna.py data.csv sequence.txt")

    # Read database file into a variable
    my_database = sys.argv[1]
    with open(my_database) as file1:
        reader = csv.DictReader(file1)
        people = list(reader)
    
    # Read DNA sequence file into a variable
    my_sequence = sys.argv[2]
    with open(my_sequence) as file2:
        dna_seq = file2.readline().rstrip()

    # Find longest match of each STR in DNA sequence
    long_count = {}
    for sub_seq in people[0]:
        if sub_seq != "name":
            long_count[sub_seq] = longest_match(dna_seq, sub_seq)

    # Check database for matching profiles
    check_match = 0
    n_str = len(long_count)
    name = "none"
    for data in people:
        for sub_seq in data:
            if sub_seq != "name":
                if int(data[sub_seq]) == long_count[sub_seq]:
                    check_match += 1
            
        
        if check_match == n_str:
            name = data["name"]
            break
        else:
            check_match = 0
    
    # Print result
    if name == "none":
        print("No match")
    else:
        print(name)
    
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

main()
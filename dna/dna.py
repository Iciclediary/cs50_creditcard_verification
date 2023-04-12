import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print("Not enough arguments")

    # TODO: Read database file into a variable
    database_file_name = sys.argv[1]
    database = []
    with open(database_file_name) as file:
        reader = csv.DictReader(file)
        database = list(reader)
        # print(database)

    # TODO: Read DNA sequence file into a variable
    sequence = ""
    sequence_file_name = sys.argv[2]
    with open(sequence_file_name) as file:
        sequence = file.read()
        # print(sequence)

    # TODO: Find longest match of each STR in DNA sequence
    # get the STRs from the first row of the database
    str_list = list(database[0].keys())
    str_list.remove("name")
    # print(str_list)
    current_profile = {}
    for str in str_list:
        current_profile[str] = longest_match(sequence, str)
    # print(current_profile)

    # TODO: Check database for matching profiles
    # iterate through the database to find a match
    match_name = None
    for db_profile in database:
        # print(db_profile)
        str_match_count = 0
        for str in str_list:
            if int(db_profile[str]) == current_profile[str]:
                str_match_count += 1
        if str_match_count == len(str_list):
            match_name = (db_profile["name"])

    if match_name:
        print(f"{match_name}")
    else:
        print("No match")


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

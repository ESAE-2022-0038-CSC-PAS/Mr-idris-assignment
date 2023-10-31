import re

def find_and_match_pattern(input_string, pattern):
    # Use the findall method of the re module to find all matches of the pattern in the input_string
    matches = re.findall(pattern, input_string)
    
    # The findall method returns a list of all matches, so we iterate over each match
    for match in matches:
        # If the match is a string (and not a tuple, which would indicate a match with groups),
        # we print it as the result of the pattern match
        if isinstance(match, str):
            print(f"Pattern match found: {match}")
        # If the match is a tuple, we assume that the pattern contained groups,
        # so we print each element of the tuple as the result of a group match
        elif isinstance(match, tuple):
            for i, group_match in enumerate(match):
                print(f"Group match {i+1} found: {group_match}")

# Example usage:
input_string = "I have 2 apples, 3 oranges, and 5 bananas."
pattern = r"\d+ (\w+)"
find_and_match_pattern(input_string, pattern)

import re

def replace_pattern(input_string, pattern, replace_with):
    """
    Replaces all occurrences of a pattern in the input string with the replace_with string.
    :param input_string: string in which the pattern needs to be searched.
    :param pattern: string representing the pattern to be searched.
    :param replace_with: string that would replace the pattern found.
    :return: string with all occurrences of the pattern replaced.
    """
    # Create a pattern object
    p = re.compile(pattern)

    # Replace all occurrences of the pattern in the input string
    return p.sub(replace_with, input_string)

# Example usage:
input_string = "The cat is playing with the ball. The ball is blue. The cat is white."
pattern = r"\b(cat|ball)\b"
replace_with = "ANIMAL"

print(replace_pattern(input_string, pattern, replace_with))
    
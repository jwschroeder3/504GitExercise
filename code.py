def calculate_character_frequency(input_string):
    """
    Computes the frequency of each character in the input string.

    Parameters:
    input_string (str): The string for which character frequency is calculated.

    Returns:
    dict: A dictionary where keys are characters and values are their corresponding counts in the input string.
    """
    frequency_dict = dict()
    for char in input_string:
        if char not in frequency_dict:
            frequency_dict[char] = 1  # Initialize the count if the character is not in the dictionary.
        else:
            frequency_dict[char] += 1  # Increment the count if the character is already in the dictionary.
    return frequency_dict

def normalize_character_frequencies(frequency_dict):
    """
    Prints the normalized frequency of each character based on their counts from the input dictionary.

    Parameters:
    frequency_dict (dict): A dictionary where keys are characters and values are their corresponding counts.

    Returns:
    None: This function prints the frequencies directly to the console.
    """
    print('Frequencies:')
    total_count = sum(frequency_dict.values())  # Calculate the total count of all characters.
    
    for char, count in frequency_dict.items():
        frequency = count / total_count  # Calculate the frequency of each character.
        print(f'{char}: {frequency:.4f}')  # Print each character and its frequency, formatted to 4 decimal places.

# Example usage: calculate fraction of nucleobases in a given string.
input_string = 'ATCTGACGCGCGCCGC'
frequency_dict = calculate_character_frequency(input_string)
normalize_character_frequencies(frequency_dict)
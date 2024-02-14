#! python3
# mclip.py - A multi-clipboard program.

# Dictionary containing keyphrases and corresponding text
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip

# Check if the correct number of command-line arguments is provided
if len(sys.argv) < 2:
    # Display usage information and exit if not enough arguments are provided
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

# Extract the keyphrase from command-line arguments
keyphrase = sys.argv[1]    # first command line arg is the keyphrase

# Check if the keyphrase exists in the TEXT dictionary
if keyphrase in TEXT:
    # Copy the corresponding text to the clipboard
    pyperclip.copy(TEXT[keyphrase])
    # Display a message indicating successful copying
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    # Display a message indicating that the keyphrase is not recognized
    print('There is no text for ' + keyphrase)

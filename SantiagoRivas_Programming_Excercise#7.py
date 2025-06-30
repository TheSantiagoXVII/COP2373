import re


# Function made to split paragraphs into sentences.
def sentences_split(text):
    sentences = re.split(r'(?<=[.?!])\s+(?=[A-Z0-9])', text)
    return [s.strip() for s in sentences if s.strip()]


# Main function made to request the user for information.
def main():
    # Now we request for a paragraph to split.
    paragraph = input('Enter the paragraph: ')

    # Split the input into sentences
    sentences = sentences_split(paragraph)

    # Print the sentences along the number
    print('\nSentences:')
    for i, s in enumerate(sentences, 1):
        print(f'{i}: {s}')

    # Print the total of sentences.
    print(f'\nTotal number of sentences: {len(sentences)}')


# Closing the main function.
if __name__ == "__main__":
    main()

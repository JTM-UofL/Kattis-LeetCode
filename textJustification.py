class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # Loop through the list of words
        # if the word length + next word length is smaller, only
        # put the word and left justify, else
        # keep adding words until you cant anymore.
        # once this happens, then pass the string into a function that
        # will format based on criteria and add it to the output list

        output_list = []
        sentence = []
        i = 0

        for word in words:
            if len(word) + len(sentence) + i < maxWidth:
                sentence.append(word)
                i += 1
            else:
                output_list.append(justify(sentence))
                i = 0

        output_list.append(justify(sentence, 'left'))
        return output_list

    def justify(self, sentence : list, width : int, side : str) -> str:

            spaces = width - len(sentence)

            while spaces < 0:
                 
            return sentence
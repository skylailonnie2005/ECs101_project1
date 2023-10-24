import pandas as pd


table = pd.read_csv("comp_table.csv", dtype = str)

letters = table['character']

numbers = table['binary']

getBinary_dictionary = dict(zip(letters,numbers))

getChar_dictionary = dict(zip(numbers,letters))

#getBinary function:
def getBinary(input_file,output_file):
    with (open(input_file, 'r') as example):
        file1 = example.read()
        compressed = ""
        for x in file1:

            if x in getBinary_dictionary:
                compressed = compressed + getBinary_dictionary[x]
                file1 = file1[len(compressed):]


            else:
                if x == '\n':
                    compressed = compressed + "96"
                    file1 = file1[len(compressed):]
                else:
                    compressed = compressed + "95"
                    file1 = file1[len(compressed):]



    num_of_bits = len(compressed)
    with open(output_file,'w') as new:
        file2 = new.write(str(num_of_bits) + '. ' + compressed)

    return compressed, file1

# end of compression function


# return to text function
def back(output_file, final_output):
    with open(output_file,'r') as convert:
        file = convert.read()

        input = file

        new_input = input.split(". ")

        new_input = new_input[1]

        split = 2

        out =[(new_input[i:i+split]) for i in range(0,len(new_input),split)]
        # lines 34-38 split each of the binary, which will make it easier to turn each of them back into strings.

        uncompressed = ""
        for x in out:

            if x in getChar_dictionary:
                if x == "96":
                    uncompressed = uncompressed + "\n"
                else:
                    uncompressed = uncompressed + getChar_dictionary[x]

            else:
                uncompressed = uncompressed + "#"





    # writes the final uncompressed document
    with open(final_output,'w') as result:
        file = result.write(uncompressed)

    return

# Comparisson function needs to be added later!!!!!!!!!!!!!!



getBinary('input.txt','BinOutput.txt')

back('BinOutput.txt','TextOutput.txt')
















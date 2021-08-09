## Code By: J. Carlos C. Guillermo
##      Version: 1
##      Specifications:
##          This Module was created to identify, validate and convert
##          the type of input data(String), according to each of the module's 
##          functions. 
##          Note: This module is only used in case the input data type is 
##                string.
##          For example:
##              if variable = "2.34" <<--- ""= indicate that the numeric value
##                                             is string 
##              the module validates the variable using the double_number()
##              function. 
##          * AVOID CODE BREAKING. 
##


symbol_List = ["°", "|", "¬", "!", '"', "#", "$", "%", "&", "/", "(", ")", "=", "?", "'", "\\", "¡", "¿", "@", "¨", "´", "*", "+", "~", "[", "]", "{", "}", "^", "`", "<", ">", ";", ",", ":", ".", "-", "_"]
lowercase_Alphabet_List = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_Alphabet_List = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers_List = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
point_List = ["."]
space_List = [" "]
special_Character_SPA_List = ["Ñ", "ñ"]
special_Character_List = ["Á", "É", "Í", "Ó", "Ú", "á", "é", "í", "ó", "ú", "à", "è", "ì", "ò", "ù", "À", "È", "Ì", "Ò", "Ù", "ä", "ë", "ï", "ö", "ü", "ÿ", "Ä", "Ë", "Ï", "Ö", "Ü", "â", "ê", "î", "ô", "û", "Â", "Ê", "Î", "Ô", "Û"]


def int_Number(var_Word):
    counter = 0
    for i in range(0, len(var_Word), 1):
        if(var_Word[i] in numbers_List):
            counter += 1
    if(len(var_Word) == counter):
        convert_String_To_Integer = int("".join(var_Word))
        return convert_String_To_Integer
    else:
        return False

def double_Number(var_Word):
    counter = 0
    word_Container = []
    for i in range(0, len(var_Word), 1):
        word_Container.append(var_Word[i])
    for i in range(0, len(word_Container), 1):
        if(point_List[0] == word_Container[i]):
            if((i < (len(word_Container)-1)) and (word_Container[i] in point_List)):
                counter += 1    
        if(word_Container[i] in numbers_List):
            counter += 1
    if(len(word_Container) == counter):
        convert_String_To_Double = float("".join(var_Word))
        return convert_String_To_Double
    else:
        return False

def number_identifier(var_Word):
    word_container = []

    return True


def alphabetic_Data_Identifier(var_Word):
    word_Container = []
    counter = 0
    for i in range(0, len(var_Word), 1):
        word_Container.append(var_Word[i])
    for i in range(0, len(word_Container), 1):
        if((word_Container[i] in lowercase_Alphabet_List) or (word_Container[i] in uppercase_Alphabet_List) or (word_Container[i] in special_Character_SPA_List) or (word_Container[i] in special_Character_List) or (word_Container[i] in space_List)):
            counter += 1
    if(counter == len(word_Container)):
        join_Word_Container = "".join(var_Word)
        return join_Word_Container
    else:
        return False


















        
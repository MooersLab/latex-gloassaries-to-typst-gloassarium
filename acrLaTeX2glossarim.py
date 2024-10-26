import re

"""
This script translates acronym glossary entries for LaTeX's glossaries package to entries for the glossarium package of typst.
The returned list of entries are to be inserted inside `#let entry-list = ( )` in the gloassary.typ file that is imported with 
the function `#import "glossary.typ": entry-list ` that comes before the command `#register-glossary(entry-list)` that loads 
the entries. The entries are written one per line for a more compact format.

Blaine Mooers October 26, 2024
OUHS
"""

# Function to translate LaTeX acronym glossary entries to Typst glossarium format
def translate_acronyms_to_typst(file_content):
    # Define the regex pattern for LaTeX acronym entries
    pattern = r'\\newacronym\{(.*?)\}\{(.*?)\}\{(.*?)\}'
    
    # Find all matches in the file content
    matches = re.findall(pattern, file_content)
    
    # Translate matches to the desired format
    translated_entries = [
        f'(key: "{abbr}", short: "{short}", long: "{full}", description: "", group: "Acronyms"),'
        for abbr, short, full in matches
    ]
    
    return translated_entries

# Read the content of the LaTeX file
with open('glossaries/acronyms.tex', 'r') as file:
    latex_content = file.read()

# Translate the acronyms
translated_acronyms = translate_acronyms_to_typst(latex_content)

# Write the translated acronyms to a .typ file
with open('translated_acronyms.typ', 'w') as file:
    for entry in translated_acronyms:
        file.write(entry + '\n')

print("Translated acronyms have been written to 'translated_acronyms.typ'.")

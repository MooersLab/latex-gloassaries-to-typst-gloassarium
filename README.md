![Version](https://img.shields.io/static/v1?label=latex-gloassaries-to-typst-gloassarium&message=0.1&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# latex-gloassaries-to-typst-gloassarium

## Background
Python scripts to translate glossary entries for LaTeX's **glossaries** package to entries for the **glossarium** package of Typst.
Insert the returned list of entries inside `#let entry-list = ( )` in the `glossary.typ` file.
This file is for the storage of **gloassarium** entries.
It is imported into the main file's namespace with the function `#import "glossary.typ": entry-list`.
This command is followed by the command `#register-glossary(entry-list)` that loads the entries. 
The acronym entries are written one per line to save space.

## Usage
Run Python script in the same directory as the `acronyms.tex` file or edit the file path accordingly.

LaTeX has three kinds of glossaries: main glossary, acronyms, and mathematical notation.
Examples are found in the glossaries folder.

Use the entries in the main text by entering `#gls("entry key")` in your prose. 
Set the show-all key to true to print all of the entries: `#print-glossary(entry-list, show-all: true)`.

<img width="908" alt="Screenshot 2024-10-26 at 8 35 56 AM" src="https://github.com/user-attachments/assets/10fcf83e-2840-4bb8-8b1e-a59ba22dd429">



## Status

Script for conversion of acronyms is ready.


## Update history

|Version      | Changes                                                                                                                                                                         | Date                 |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| Version 0.1 |   Added badges, funding, and update table.  Initial commit.                                                                                                                | 2024 October 26  |

## Sources of funding

- NIH: R01 CA242845
- NIH: R01 AI088011
- NIH: P30 CA225520 (PI: R. Mannel)
- NIH: P20 GM103640 and P30 GM145423 (PI: A. West)

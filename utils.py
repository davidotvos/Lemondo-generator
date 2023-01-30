# Import re for regex functions
import re

# Import sys for getting the command line arguments
import sys

# Import docx to work with .docx files.
# Must be installed: pip install python-docx
from docx import Document

from docx2pdf import convert
import lemondok

template_path = 'test_lemondo.docx'
replacements = ['_tervcim', '_tipus', '_iktatoszam']
save_folder = ''

# Lemondók listája
lemondoLi = []

testDict = {
    '_tervcim' : 'ABC',
    '_tipus' : '',
    '_iktatoszam' : '',
    '_varos' : 'Debrecen',
    '_datum' : '',
    '_felelos' : 'Alföldi Imre',
    '_pozicio' : 'Debrecen Run Team Lead'
}


def create_docxs(path, replacements_dict:dict):
    doc = Document(path)
    # Loop through replacer arguments
    for replaceArg in replacements_dict.keys():
        # Loop through paragraphs
        for para in doc.paragraphs:
            # Loop through runs (style spans)
            for run in para.runs:
                # if there is text on this run, replace it
                if run.text:
                    # get the replacement text
                    replaced_text = re.sub(replaceArg, replacements_dict.get(replaceArg), run.text, 999)
                    if replaced_text != run.text:
                        # if the replaced text is not the same as the original
                        # replace the text
                        run.text = replaced_text

    # make a new file name by adding "_new" to the original file name
    new_file_path = template_path.replace(".docx", "_new.docx")
    # save the new docx file
    doc.save(new_file_path)


# Docx fájlból Pdf formátumot készít és elmenti a megadott fájlba
def convert_to_pdf(input_path, output_path):
    convert(input_path, output_path)
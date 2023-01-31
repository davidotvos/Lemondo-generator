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
    '_tipus' : 'Építési',
    '_iktatoszam' : 'Debrecen123',
    '_varos' : 'Debrecen',
    '_datum' : '2023.01.02',
    '_felelos' : 'Alföldi Imre',
    '_pozicio' : 'Debrecen Run Team Lead'
}


def create_docxs(path, replacements_dict:dict):
    doc = Document(path)

    for i in replacements_dict:
        for p in doc.paragraphs:
            if p.text.find(i)>=0:
                p.text=p.text.replace(i,replacements_dict[i])
    
    # make a new file name by adding "_new" to the original file name
    new_file_path = template_path.replace(".docx", "_new.docx")
    # save the new docx file
    doc.save(new_file_path)

    # # Loop through replacer arguments
    # for replaceArg in replacements_dict.keys():
    #     # Loop through paragraphs
    #     for para in doc.paragraphs:
    #         # Loop through runs (style spans)
    #         for run in para.runs:
    #             # if there is text on this run, replace it
    #             if run.text:
    #                 # get the replacement text
    #                 replaced_text = re.sub(replaceArg, replacements_dict.get(replaceArg), run.text, 999)
    #                 if replaced_text != run.text:
    #                     # if the replaced text is not the same as the original
    #                     # replace the text
    #                     run.text = replaced_text

    # # make a new file name by adding "_new" to the original file name
    # new_file_path = template_path.replace(".docx", "_new.docx")
    # # save the new docx file
    # doc.save(new_file_path)


def docx_replace_regex(doc_obj, regex , replace):

    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex , replace)

def create_docx2(path, replacement_dict:dict):
    doc = Document(path)
    for word, replacement in replacement_dict.items():
        word_re=re.compile(word)
        docx_replace_regex(doc, word_re , replacement)
    
    # make a new file name by adding "_new" to the original file name
    new_file_path = template_path.replace(".docx", "_new.docx")
    # save the new docx file
    doc.save(new_file_path)



def create_docx3(path, replacement_dict:dict):
    doc = Document(path)

    for variable_key, variable_value in replacement_dict.items():
        for paragraph in doc.paragraphs:
            replace_text_in_paragraph(paragraph, variable_key, variable_value)

        for table in doc.tables:
            for col in table.columns:
                for cell in col.cells:
                    for paragraph in cell.paragraphs:
                        replace_text_in_paragraph(paragraph, variable_key, variable_value)

    # make a new file name by adding "_new" to the original file name
    new_file_path = template_path.replace(".docx", "_new.docx")
    # save the new docx file
    doc.save(new_file_path)

def replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)


# Docx fájlból Pdf formátumot készít és elmenti a megadott fájlba
def convert_to_pdf(input_path, output_path):
    convert(input_path, output_path)
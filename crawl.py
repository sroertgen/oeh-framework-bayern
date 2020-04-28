from bs4 import BeautifulSoup
import requests
import xlsxwriter

workbook = xlsxwriter.Workbook('curriculum_new.xlsx')
worksheet = workbook.add_worksheet()

row_sheet = 2

subjects = [
    'beruf_und_arbeit',
    'biologie',
    'buchführung',
    'bwl-rechnungswesen',
    'chemie',
    'daz',
    'deutsch',
    'englisch',
    'ernaehrung_und_gesundheit',
    'ethik',
    'evangelische-religionslehre',
    'franzoesisch',
    'geographie',
    'geschichte',
    'informatik',
    'italienisch',
    'katholische-religionslehre',
    'kunst',
    'latein',
    'mathematik',
    'musik',
    'physik',
    'russisch',
    'soziologie',
    'spanisch',
    'sport',
    'technologie',
]

educationalContext = [
    'grundschule',
    'foerderschule'
    'mittelschule',
    'realschule',
    'gymnasium'
]


# prepare xlsx-file
sheets_columns = [
    'identifier',
    'fullStatement',
    'humanCodingScheme',
    'smartLevel',
    'listEnumeration',
    'abbreviatedStatement',
    'conceptKeywords',
    'notes',
    'language',
    'educationLevel',
    'CFItemType',
    'license'
]

ch = "A"

for item in sheets_columns:
    worksheet.write((ch+'1'), item)
    ch = chr(ord(ch) + 1)


def get_item_title(soup, subject, context, grade):
    global row_sheet
    for item in soup.find_all('span', 'head-absatz-title-short'):
        fullStatement = item.get_text().strip()
        humanCodingScheme = context + '_' + subject + '_' + str(grade)
        listEnumeration = row_sheet
        row_b = 'B' + str(row_sheet)
        row_c = 'C' + str(row_sheet)
        row_d = 'D' + str(row_sheet)
        row_i = 'I' + str(row_sheet)
        row_j = 'J' + str(row_sheet)
        worksheet.write(row_b, fullStatement)
        worksheet.write(row_c, humanCodingScheme)
        worksheet.write(row_d, listEnumeration)
        worksheet.write(row_i, 'de')
        worksheet.write(row_j, grade)
        row_sheet += 1


for grade in range(1, 14):
    for subject in subjects:
        for context in educationalContext:
            if context == 'grundschule' and grade >= 5:
                continue
            if context == 'grundschule' and subject not in ['deutsch', 'mathematik', 'musik', 'ethik', 'sport', 'kunst', 'katholische-religionslehre', 'evangelische-religionslehre']:
                continue
            if context in ['gymnasium', 'realschule', 'mittelschule', 'foerderschule'] and grade <= 5:
                continue
            url = 'https://www.lehrplanplus.bayern.de/fachlehrplan/' + \
                context + '/' + str(grade) + '/' + subject
            print(url)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            get_item_title(soup, context, subject, grade)
workbook.close()

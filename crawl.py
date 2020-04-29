from bs4 import BeautifulSoup
import requests
import xlsxwriter

workbook = xlsxwriter.Workbook('curriculum.xlsx')
worksheet = workbook.add_worksheet()


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
    'foerderschule',
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


# global vars
row_sheet = 2
listEnumeration = [1, 0, 0]


def get_item_title(soup, subject, context, grade):
    global row_sheet
    global listEnumeration
    div = soup.find_all('div', 'toggable')
    try:
        for i, item in enumerate(div):
            if 'headline_lvl1' in item['class']:
                if item.find('div', 'thema_absch') != None:
                    description = ' - ' + item.find('div', 'thema_absch').get_text(
                    ).strip().replace('\n', ' ').replace('\r', '')
                else:
                    description = ''
                fullStatement = item.find(
                    'span', 'head-absatz-title-short').get_text().strip() + description
                fach_jgs = item.find(
                    'span', 'headline_fach_jgs').get_text().strip()
                humanCodingScheme = fach_jgs + '_' + subject + '_' + \
                    str(grade) + '_' + str(listEnumeration[0])
                row_b = 'B' + str(row_sheet)
                row_c = 'C' + str(row_sheet)
                row_d = 'D' + str(row_sheet)
                row_i = 'I' + str(row_sheet)
                row_j = 'J' + str(row_sheet)
                worksheet.write(row_b, fullStatement)
                worksheet.write(row_c, humanCodingScheme)
                worksheet.write(row_d, listEnumeration[0])
                worksheet.write(row_i, 'de')
                worksheet.write(row_j, grade)
                row_sheet += 1

                if 'headline_lvl2' in div[i+1]['class']:
                    listEnumeration[1] = listEnumeration[1] + 1
                else:
                    listEnumeration[0] = listEnumeration[0] + 1

            if 'headline_lvl2' in item['class']:
                if item.find('div', 'thema_absch') != None:
                    description = ' - ' + item.find('div', 'thema_absch').get_text(
                    ).strip().replace('\n', ' ').replace('\r', '')
                else:
                    description = ''
                fullStatement = item.find(
                    'span', 'head-absatz-title-long').get_text().strip() + description
                fach_jgs = item.find(
                    'span', 'headline_fach_jgs').get_text().strip()
                smartLevel = str(
                    listEnumeration[0]) + '.' + str(listEnumeration[1])
                humanCodingScheme = fach_jgs + '_' + subject + '_' + \
                    str(grade) + '_' + smartLevel
                row_b = 'B' + str(row_sheet)
                row_c = 'C' + str(row_sheet)
                row_d = 'D' + str(row_sheet)
                row_i = 'I' + str(row_sheet)
                row_j = 'J' + str(row_sheet)
                worksheet.write(row_b, fullStatement)
                worksheet.write(row_c, humanCodingScheme)
                worksheet.write(row_d, smartLevel)
                worksheet.write(row_i, 'de')
                worksheet.write(row_j, grade)
                row_sheet += 1

                if 'headline_lvl2' in div[i+1]['class']:
                    listEnumeration[1] = listEnumeration[1] + 1
                elif 'headline_lvl1' in div[i+1]['class']:
                    listEnumeration[0] = listEnumeration[0] + 1
                    listEnumeration[1] = 0

        listEnumeration[0] = listEnumeration[0] + 1
        listEnumeration[1] = 0
    except IndexError:
        listEnumeration[0] = listEnumeration[0] + 1
        listEnumeration[1] = 0
        pass


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

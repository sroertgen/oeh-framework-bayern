from bs4 import BeautifulSoup
import requests
import xlsxwriter

workbook = xlsxwriter.Workbook('curriculum_all.xlsx')
worksheet = workbook.add_worksheet()

subjects_all = [
    'aeb',
    'angewandte-informatik',
    'berufliche_orientierung',
    'beruf_und_arbeit',
    'biolog-chem-praktikum',
    'biologie',
    'biotechnologie',
    'bks',
    'blop_es',
    'blop_t',
    'BLOT',
    'blp',
    'bsk',
    'buchführung',
    'bwl-rechnungswesen',
    'chemie',
    'chi',
    'daz',
    'deutsch',
    'dgs',
    'ebc',
    'englisch',
    'ernaehrung_und_gesundheit',
    'es',
    'ethik',
    'evangelische-religionslehre',
    'experimentelles_gestalten',
    'fpa',
    'franzoesisch',
    'freizeit',
    'geographie',
    'geol',
    'geschichte',
    'geschichte-sozialkunde',
    'geschichte-sozialkunde-bo',
    'gestaltung',
    'gpg',
    'gpg_nt',
    'griechisch',
    'grundlegender_entwicklungsbezogener_unterricht',
    'gw',
    'gwr',
    'hsu',
    'ibv',
    'ikb',
    'informatik',
    'informatik_digitales_gestalten',
    'informationsverarbeitung',
    'internationale_politik',
    'isb',
    'it',
    'italienisch',
    'jap',
    'katholische-religionslehre',
    'ki',
    'kunst',
    'kwg',
    'latein',
    'leben_in_der_gesellschaft',
    'mathematik',
    'medien',
    'mensch-und-umwelt',
    'mobilitaet',
    'musik',
    'musischaesthetischebildung',
    'ngr',
    'nt',
    'nt-bo',
    'nt_gym',
    'paedagigik-psychologie',
    'persoenlichkeit_soziale_beziehungen',
    'pha',
    'phbio',
    'physik',
    'pln',
    'pug',
    'rechtslehre',
    'rme',
    'russisch',
    'sach_und_lebensbezogener_unterricht',
    'sg',
    'sozialkunde',
    'soziallehre',
    'sozialpraktische-grundbildung',
    'sozialpsychologie',
    'sozialwesen',
    'sozialwirtschaft-und-recht',
    'sozialwissenschaftl-arbeitsfelder',
    'soziologie',
    'spanisch',
    'sport',
    'sport_bewegung',
    'studier-und-arbeitstechniken',
    't',
    'tast',
    'technologie',
    'textiles-gestalten',
    'tr',
    'tsh',
    'uebungsunternehmen',
    'volkswirtschaftslehre',
    'werken',
    'werken-und-gestalten',
    'wib',
    'wik',
    'wirtschaft_aktuell',
    'wirtschaftsgeografie',
    'wirtschaftsinformatik',
    'wirtschaft-und-recht',
    'wohnen',
]


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

gs_subjects = ['deutsch', 'mathematik', 'musik', 'ethik', 'sport',
               'kunst', 'katholische-religionslehre', 'evangelische-religionslehre']

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


def write_item(fullStatement, humanCodingScheme, smartLevel, grade):
    global row_sheet

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
                smartLevel = str(listEnumeration[0])
                humanCodingScheme = fach_jgs + '_' + subject + '_' + \
                    str(grade) + '_' + str(listEnumeration[0])
                write_item(fullStatement,
                           humanCodingScheme, smartLevel, grade)

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
                write_item(fullStatement,
                           humanCodingScheme, smartLevel, grade)

                if 'headline_lvl2' in div[i+1]['class']:
                    listEnumeration[1] = listEnumeration[1] + 1
                elif 'headline_lvl3' in div[i+1]['class']:
                    listEnumeration[2] = listEnumeration[2] + 1
                elif 'headline_lvl1' in div[i+1]['class']:
                    listEnumeration[0] = listEnumeration[0] + 1
                    listEnumeration[1] = 0

            if 'headline_lvl3' in item['class']:
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
                    listEnumeration[0]) + '.' + str(listEnumeration[1]) + '.' + str(listEnumeration[2])
                humanCodingScheme = fach_jgs + '_' + subject + '_' + \
                    str(grade) + '_' + smartLevel
                write_item(fullStatement,
                           humanCodingScheme, smartLevel, grade)

                if 'headline_lvl2' in div[i+1]['class']:
                    listEnumeration[1] = listEnumeration[1] + 1
                    listEnumeration[2] = 0
                elif 'headline_lvl3' in div[i+1]['class']:
                    listEnumeration[2] = listEnumeration[2] + 1
                elif 'headline_lvl1' in div[i+1]['class']:
                    listEnumeration[0] = listEnumeration[0] + 1
                    listEnumeration[1] = 0
                    listEnumeration[2] = 0

        listEnumeration[0] = listEnumeration[0] + 1
        listEnumeration[1] = 0
    except IndexError:
        listEnumeration[0] = listEnumeration[0] + 1
        listEnumeration[1] = 0
        pass


try:
    for grade in range(1, 14):
        for subject in subjects_all:
            for context in educationalContext:
                if context == 'grundschule' and grade >= 5:
                    continue
                if context == 'grundschule' and subject not in gs_subjects:
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

except KeyboardInterrupt:
    workbook.close()

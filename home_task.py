from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
for contact in contacts_list:
    full_name = contact[0].split()
    contact[0] = full_name[0]
    contact.insert(1, full_name[1] if len(full_name) > 1 else '')
    contact.insert(2, full_name[2] if len(full_name) > 2 else '')

    contact[5] = re.sub(r'(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(?(доб\.\s*\d+)?\)?', r'+7(\2)\3-\4-\5 \6', contact[5])


new_contacts_list = []
seen = set()
for contact in contacts_list:
    key = (contact[0], contact[1])
    if key not in seen:
        seen.add(key)
        new_contacts_list.append(contact)
    else:
        for new_contact in new_contacts_list:
            if (new_contact[0], new_contact[1]) == key:
                for i, value in enumerate(contact):
                    if value and not new_contact[i]:
                        new_contact[i] = value

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
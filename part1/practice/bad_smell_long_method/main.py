# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


# def get_users_list():
#     # Чтение данных из строки
#     data = []
#     for line in csv.split('\n'):
#         name, age = line.split(';')
#         data.append({'name': name, 'age': int(age)})

#Функция чтения данных из строки
def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(csv):
    return [x.split(';')for x in csv.split('\n')]

def _sort(data):
    return sorted(sorted(data, key=lambda x: int(x[1])))

def _filter(data):
    return [x for x in data if int(x[1]) > 10]



    # Сортировка по возрасту по возрастанию
    # _new_data = []
    # used_person = set()
    # minimum_age_person = None
    # while len(used_person) != len(data):
    #     if minimum_age_person is None:
    #         for person in data:
    #             if minimum_age_person is None:
    #                 minimum_age_person = person
    #             else:
    #                 if person['name'] in used_person:
    #                     continue
    #                 else:
    #                     if person['age'] < minimum_age_person['age']:
    #                         minimum_age_person = person
    #         _new_data.append(minimum_age_person)
    #         used_person.add(minimum_age_person['name'])
    #     local_minimum = None
    #     for person in data:
    #         if person['name'] in used_person:
    #             continue
    #         else:
    #             if not local_minimum is None:
    #                 if person['age'] < local_minimum['age']:
    #                     local_minimum = person
    #             else:
    #                 local_minimum = person
    #     _new_data.append(local_minimum)
    #     used_person.add(local_minimum['name'])
    #
    # # Фильтрация
    # result_data = []
    # for person in _new_data:
    #     if person['age'] < 10:
    #         continue
    #     else:
    #         result_data.append(person)
    # return result_data


if __name__ == '__main__':
    print(get_users_list())

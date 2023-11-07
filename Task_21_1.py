## Task_21_1
'''
Составьте в произвольной форме список полей в таблице "Pupil",
предполагая, что она будет использоваться в системе учёта
и планирования курса "Разработчик на Питоне".
'''

import pandas as pd
df = pd.DataFrame(columns=[
    'number_in_order',                  # порядковый номер > {type = int}
    'id',                               # идентификационный номер > {type = def(?demon?)}
    'last_name',                        # имя {type = str}
    'first_name',                       # фамилия {type = str}
    'patronymic',                       # отчество {type = str}
    'gender',                           # пол {range(male, female)}
    'education_level',                  # уровень образования {range(primary, secondary_specialized, bachelor's, master's, upper_level)}
    'academic_degree',                  # учёная степень {range(None, Candidate_of_Sciences, Dr_f)}
    'academic_title',                   # учёное звание {range(None, Docent, Professor)}
    'start_date_of_training',           # дата начала обучения {mask = yyyy.mm.dd}
    'date_of_termination_of_training',  # дата приостановки обучения {range(None, mask = yyyy.mm.dd)}
    'date_of_continuation_of_training', # дата продолжения обучения {range(None, mask = yyyy.mm.dd)}
    'graduation_date',                  # дата окончания обучения {range(None, mask = yyyy.mm.dd)}
    'attendance',                       # посещаемость {(type = float, range(0, 1, 0.01)) or (type = def(?demon?)))}
    'tuition_fees',                     # оплата обучения {type = float, range(0, 1, 0.01)}
    'current control',                  # текущий контроль {(type = bool, range(Fouls, True)) or (type = def(?demon?)))}
    'border_control',                   # рубежный контроль {(type = float, range(0, 1, 0.01)) or (type = def(?demon?)))}
    'state_final_certification'         # ГИА {type = float, range(0, 1, 0.25)}
    ])
print(df)
df.to_excel (r'C:\Users\Fater in Haus\PycharmProjects\Python_Autumn_2023\PyPupil.xlsx')


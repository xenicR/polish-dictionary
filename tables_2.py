import pandas as pd
import urllib.request
import re
import time
start_time = time.time()

# принтить пустые
def F_1(list):
    i = 0

    for elem in list:
        if elem != (i+0):
            if elem != (i+1):
                print(elem)

# запись в файл
def F_write_file_w(data, f_name):
    f = open(f_name, 'w')
    f.write(data)
    #print(data)
    f.close()

# дозапись в файл
def F_write_file_a(data, f_name):
    f = open(f_name, 'a')
    f.write(data)
    #print(data)
    f.close()

# слепливает все файлы; создаёт файлы с
def M_1():
    f1_name = 'sgjp_pages_1-1500000.tsv'
    f2_name = 'sgjp_pages_125586-1500000.tsv'
    f3_name = 'sgjp_pages_368311-1500000.tsv'
    f4_name = 'sgjp_pages_653723-1500000.tsv'
    f5_name = 'sgjp_pages_850806-1500000.tsv'
    f6_name = 'sgjp_pages_1046852-1500000.tsv'
    f7_name = 'sgjp_pages_1205921-1500000.tsv'
    f8_name = 'sgjp_pages_1390496-1500000.tsv'

    df_1 = pd.read_csv(f1_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)
    df_2 = pd.read_csv(f2_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)
    df_3 = pd.read_csv(f3_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)
    df_4 = pd.read_csv(f4_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)
    df_5 = pd.read_csv(f5_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)
    df_6 = pd.read_csv(f6_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)
    df_7 = pd.read_csv(f7_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)
    df_8 = pd.read_csv(f8_name, sep='\t', usecols=['url', 'id', 'word_form', 'p_pp_codes'], low_memory=False)

    df_m = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8], ignore_index=True)

    df_m = df_m.rename(columns={'word_form': 'wordform'})

    f_name_wfd = 'wordforms_full_list.tsv'
    f_name_wf = 'wordforms_polish_ø.tsv'

    #df_m.to_csv('sgjp_full.tsv', columns=['url', 'id', 'wordform', 'p_pp_codes'], sep='\t', encoding='utf-8', index=False)

    df_m = df_m.loc[df_m['wordform'] != '""']
    #df_m.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

    df_m.to_csv(f_name_wfd, columns=['url', 'id', 'wordform', 'p_pp_codes'], sep='\t', encoding='utf-8', index=False)

    df_m.to_csv(f_name_wf, columns=['wordform'], sep='\t', encoding='utf-8', index=False)

# что-то там
def M_2():
    f_name_1 = 'wordforms_full_list.tsv'
    f1 = open(f_name_1, 'r')
    lines_1 = f1.readlines()
    f1.close()

    print(lines_1[-1])

    # проверка последней строки
    #print(f1_lines[-1])
    #print(f1_lines[0])
    #print(len(f1_lines))

    #lines_2 = lines_1[1:53]        # все слова: без первой строчки с названиями
    lines_2 = lines_1[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ

    lines_3 = [] # здусь будут все строки со всеми элементами
    for line in lines_2:
        line = line.split('\t')
        lines_3.append(line)

    # проверка нехватки строк
    #print(len(lines_3))
    #for i in range(0, (len(lines_3)-1)):
    #    j = i+1
    #    if lines_3[i][1] != lines_3[j][1]:
    #        if lines_3[i][1] != lines_3[i][1]:
    #            print(i) # это печатает ошибки

    # 6 — , ; -ać: -2 > len (adj) vs len(v) (самая короткая парадигма глагола)

    print('всё прочитано')

    # удаляет пустое
    lines_4 = []
    ff = open('wordforms_polish_bez_pustot.tsv', 'w')
    ff.write('url' + '\t' + 'id' + '\t' + 'wordform' + '\t' + 'p_pp_codes' + '\n')
    # вписать название стролбцов
    for line in lines_3:
        if line[2] != '':
            ff.write((line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + line[3]))

    ff.close()

    fffff = open('wordforms_polish_bez_pustot.tsv', 'r')
    ffffff = fffff.readlines()
    print(ffffff[-1])
    fffff.close()

    print('всё проверено и записано')

    #f = open('wordforms_polish_full_list.tsv', 'w')
    #f.write(afds)
    #f.close()

    #for k in range(0, len(lines_3)):
    #    if lines_3[k][2] != '':
    #        lines_4

# начальные формы
def M_3():
    print('f o')

    file_name = 'wordforms_polish_bez_pustot.tsv'
    df = pd.read_csv(file_name, sep='\t', usecols=['wordform'], low_memory=False)

    new_name = 'wordforms_polish.tsv'
    df.to_csv(new_name, columns=['wordform'], sep='\t', encoding='utf-8', index=False)


#M_1()

#M_2()

M_3()




print("--- %s seconds ---" % (time.time() - start_time))

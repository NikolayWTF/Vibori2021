import xlsxwriter

workbook = xlsxwriter.Workbook('OIK4.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'ОИК 4')
worksheet.write('A2', 'Число избирателей, внесенных в список избирателей на момент окончания голосования')
worksheet.write('A3', 'Число избирательных бюллетеней, полученных участковой избирательной комиссией')
worksheet.write('A4', 'Число избирательных бюллетеней, выданных избирателям в помещении для голосования в день голосования')
worksheet.write('A5', 'Число избирательных бюллетеней, выданных избирателям, проголосовавшим вне помещения для голосования')
worksheet.write('A6', 'Число погашенных избирательных бюллетеней')
worksheet.write('A7', 'Число избирательных бюллетеней, содержащихся в переносных ящиках для голосования')
worksheet.write('A8', 'Число избирательных бюллетеней, содержащихся в стационарных ящиках для голосования')
worksheet.write('A9', 'Число недействительных избирательных бюллетеней')
worksheet.write('A10', 'Число действительных избирательных бюллетеней')
worksheet.write('A11', 'Число открепительных удостоверений, полученных участковой избирательной комиссией')
worksheet.write('A12', 'Число открепительных удостоверений, выданных участковой избирательной комиссией избирателям')
worksheet.write('A13', 'Число избирателей, проголосовавших по открепительным удостоверениям на избирательном участке')
worksheet.write('A14', 'Число погашенных на избирательном участке открепительных удостоверений')
worksheet.write('A15', 'Число открепительных удостоверений, выданных территориальной комиссией избирателям')
worksheet.write('A16', 'Число утраченных открепительных удостоверений')
worksheet.write('A17', 'Число утраченных избирательных бюллетеней')
worksheet.write('A18', 'Число избирательных бюллетеней, не учтенных при получении')
worksheet.write('A19', 'Анисимов Дмитрий Игоревич')
worksheet.write('A20', 'Вавилина Нэлли Юрьевна')
worksheet.write('A21', 'Ковалев Алексей Анатольевич')
worksheet.write('A22', 'Семенова Ольга Сергеевна')
worksheet.write('A23', 'Смоктий Николай Иванович')
worksheet.write('A24', 'Чебыкин Константин Александрович')

i = 0
indA = 0
indB = 1
while i < 1999:

    text = list(input().split())
    l = len(text)
    if l == 0:
        i += 1
    else:
        if text[0] == "Результаты":
            worksheet.write(indA, indB, text[3])
            indA += 1
            i += 1
        elif text[0] == "Число":
            worksheet.write(indA, indB, text[-1])
            indA += 1
            i += 1
        elif text[0] == "Анисимов":
            worksheet.write(indA, indB, text[3])
            indA += 1
            i += 1
        elif text[0] == "Вавилина":
            worksheet.write(indA, indB, text[3])
            indA += 1
            i += 1
        elif text[0] == "Ковалев":
            worksheet.write(indA, indB, text[3])
            indA += 1
            i += 1
        elif text[0] == "Семенова":
            worksheet.write(indA, indB, text[3])
            indA += 1
            i += 1
        elif text[0] == "Смоктий":
            worksheet.write(indA, indB, text[3])
            indA += 1
            i += 1
        elif text[0] == "Чебыкин":
            worksheet.write(indA, indB, text[3])
            indA = 0
            indB += 1
            i += 1
workbook.close()

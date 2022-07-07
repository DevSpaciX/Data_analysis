import csv
import heapq

#Надо вывести немного статистики по этому файлу, а именно:
#
#Как часто люди берут кофе и чай в: А - выходные, Б - будние
#Топ-15 популярных товаров
# Распределение продаж по месяцам (сколько % на какой месяц пришлось)
# Распределение продаж по часам работы пекарни

with open('Bakery.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)


    def tea_coffe(header):
        tea_coffee_Weekend = 0
        tea_coffee_Weekday = 0

        for row in reader:
            if row[1] == 'Coffee' and row[4] == 'Weekend' or row[1] == 'Tea' and row[4] == 'Weekend':
                tea_coffee_Weekend += 1
            elif row[1] == 'Coffee' and row[4] == 'Weekend' or row[1] == 'Tea' and row[4] == 'Weekday':
                tea_coffee_Weekday += 1
        print(f'В выходные кофе и чай берут', tea_coffee_Weekend, 'раз')
        print(f'В будние кофе и чай берут', tea_coffee_Weekday, 'раз','\n')
    tea_coffe(header)

with open('Bakery.csv', 'r') as file:
    reader = csv.DictReader(file)


    def top_15(reader):

        list = []
        res = {}
        for row in reader:
            list.append(row['Items'])
        for row in list:
            if row not in res.keys():
                res[row] = 0
            res[row] += 1
        result = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])[:-16:-1]}
        my_list = [i for i in result]
        #orders = [i for i in result.values()]
        count = 0
        for i in my_list:
            count += 1
            print(count,i)

    print('Топ 15 продуктов:')
    top_15(reader)

with open('Bakery.csv', 'r') as file:
    reader_2 = csv.DictReader(file)

    def month_sales(reader):

        list = []
        final_list = []
        res = {}
        result_list = []
        for row in reader:
            list.append(row['DateTime'])
        for i in list:
            final_list.append(i[5:7])
        for row in final_list:
            if row not in res.keys():
                res[row] = 0
            res[row] += 1

        all_sales = [i for i in res.values()]
        all_month = [i for i in res]

        sum_of_sales = 0
        for i in range(0 , len(all_sales)):
            sum_of_sales = sum_of_sales+all_sales[i]

        for i in all_sales:
            each_percent = (i/sum_of_sales)*100
            result_list.append(round(each_percent , 2))

        dict_from_list = {k: v for k, v in zip(all_month, result_list)}

        sorted_dict = {k: v for k, v in sorted(dict_from_list.items(), key=lambda item: item[1])[::-1]}
        for key, value in sorted_dict.items():
            print("{0}: {1}%".format(key, value))




    print('\nТоп месяцев по продажам')
    month_sales(reader_2)

with open('Bakery.csv', 'r') as file:
    reader_3 = csv.DictReader(file)

    def hour_sales(reader):
        list = []
        final_list = []
        res = {}
        result_list = []
        for row in reader:
            list.append(row['DateTime'])
        for i in list:
            final_list.append(i[11:13])
        for row in final_list:
            if row not in res.keys():
                res[row] = 0
            res[row] += 1
        sum_of_hours = [i for i in res.values()]
        all_hours = [i for i in res]
        sum_of_sales = 0
        for i in range(0, len(sum_of_hours)):
            sum_of_sales = sum_of_sales + sum_of_hours[i]
        for i in sum_of_hours:
            each_percent = (i / sum_of_sales) * 100
            result_list.append(round(each_percent, 2))
        dict_from_list = {k: v for k, v in zip(all_hours, result_list)}
        sorted_dict = {k: v for k, v in sorted(dict_from_list.items(), key=lambda item: item[1])[::-1]}
        for key, value in sorted_dict.items():
            print("{0}: {1}%".format(key, value))


    print('\nТоп часов по продажам ')
    hour_sales(reader_3)



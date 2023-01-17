import csv

l = ["a", "b", "c", "d", "e", "f", "g", "1", "2"]
abc = l[:7]


new_item = {
    'cafe': 'ABC',
    'location_URL': 'https://www.google.com/maps/place/Sabel+Food+Ltd/@51.5702865,-0.0394903,18z/data=!4m12!1m6!3m5!1s0x48761db0ffba586b:0x93a04ceef20365f1!2sLighthaus!8m2!3d51.5701299!4d-0.0392306!3m4!1s0x487604bfbea0a9a3:0x14e968605e106aa5!8m2!3d51.5696695!4d-0.0383316',
    'open': '9AM',
    'close': '5PM',
    'rating': '☕',
    'wifi': '✘',
    'power': '🔌',
    'submit': True,
    'csrf_token': 'IjFkYTUxNjg5YjVlN2Y3ZWU5NTljOTU4ZmNhOGE4ZTU2ZGRiZmEzNTEi.Y6OW8A.heEqC8xKKmsSJHp8U5NpZlWeHvY'
            }

print(list(new_item.values()))

# with open('cafe-data.csv', "a", newline='') as csv_file:
# csv_file=open('cafe-data.csv', "a", newline='')
# new_csv = csv.writer(csv_file).writerow(l[:7])
# csv_file = open('cafe-data.csv', "a", newline='')
#     csv_file.close()
# print(csv_file)
#
# csv_data = csv.writer(csv_file).writerow(l[:7])
# print(csv_data)



# content = []
# for line in csv_data:
#     print(line)
#     content.append(line)
# list_of_rows = []
# for row in csv_data:
#     print(row)
#         list_of_rows.append(row)


# print(list_of_rows)




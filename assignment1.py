
def read_data2(filename):
    data = []
    with open(filename) as in_file:
        for line in in_file:
            data.append(str(line))
    return data

def read_data(filename):
    with open(filename) as in_file:
        lines = in_file.readlines()
    items = map(lambda x: str(x), lines)
    return list(items)

Mileage_car = read_data2('c:/Users/ksukh/Desktop/NIDA Python class/20200201/Mileage.txt')
car_dict = {}
print(len(Mileage_car))
for i in Mileage_car:
    model = i.split(",")[0]
    MPG = float(i.split(",")[1])
    if model in car_dict:
        car_dict[model]['MPG'] = car_dict[model]['MPG'] + MPG
        car_dict[model]['number'] = car_dict[model]['number'] + 1
    else:
        data = {'MPG':MPG, 'number':1}
        car_dict[model] = data

for i in car_dict:
    car_MPG_avg = car_dict[i]['MPG']/car_dict[i]['number']
    print(f'model: {i} average MPG is {car_MPG_avg}')
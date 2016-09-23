import json


def load_data(filepath):
    with open(filepath) as f:
        json_data = json.load(f)
    return json_data


def get_biggest_bar(data):
    biggest = data[0]
    for bar in data:
        if bar['Cells']['SeatsCount'] > biggest['Cells']['SeatsCount']:
            biggest = bar
    return biggest


def get_smallest_bar(data):
    smallest = data[0]
    for bar in data:
        if bar['Cells']['SeatsCount'] < smallest['Cells']['SeatsCount']:
            smallest = bar
    return smallest


def get_closest_bar(data, longitude, latitude):
    def calc_distance(a, b):
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    closest_bar = data[0]
    distance_to_closest_bar = calc_distance(
        (longitude, latitude), closest_bar['Cells']['geoData']['coordinates'])
    for bar in data:
        distance = calc_distance(
            (longitude, latitude), bar['Cells']['geoData']['coordinates'])
        if distance < distance_to_closest_bar:
            distance_to_closest_bar = distance
            closest_bar = bar
    return closest_bar


if __name__ == '__main__':
    json_data = load_data('bars.json')
    print('The biggest bar\n{}'.format(get_biggest_bar(json_data)))
    print('The smallest bar\n{}'.format(get_smallest_bar(json_data)))
    longitude = float(input('Enter longitude\t:'))
    latitude = float(input('Enter latitude\t:'))
    print('The closest bar\n{}'.format(
        get_closest_bar(json_data, longitude, latitude)))

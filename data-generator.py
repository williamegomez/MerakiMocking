import random
from faker import Faker
ssid_list = [
    'huge_cafe_guests', 'huge_cafe_develoment', 'huge_cafe_admin', 'huge_it_support']

apFloors_list = [
    '1stFloor', '2ndFloor', '3rdFloor', '4thFloor']

apTags_list = [
    'West', 'South', 'East', 'North', '1stFloor', '2ndFloor', '3rdFloor', '4thFloor', 'IT']

class FakeUser(object):
    def __init__(self):
        fake = Faker()
        self.data  = {
            'apMac': fake.mac_address(),
            'apTags': fake.words(nb=3, ext_word_list=apTags_list),
            'apFloors': fake.words(nb=3, ext_word_list=apFloors_list),
            'clientMac': fake.mac_address(),
            'ipv4': fake.ipv4_private(),
            'ipv6': fake.ipv6(),
            'seenTime': fake.date_time_between(start_date="-2y", end_date="now").isoformat() + 'Z',
            'seenEpoch': fake.unix_time(),
            'ssid': fake.word(ext_word_list=ssid_list),
            'rssi': random.randint(0, 255),
            'manufacturer': fake.company(),
            'os': fake.user_agent(),
            'location': fake.geo_coordinate(),
            'lat': fake.latitude(),
            'lng': fake.longitude(),
            'unc': fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'x': fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            'y': fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        }

if __name__ == '__main__':
    fakedUser = FakeUser()
    print(fakedUser.data)

# Send user to the end point
import requests
end_point_url = 'http://127.0.0.1'

# r = requests.post(end_point_url, data=fake_User)

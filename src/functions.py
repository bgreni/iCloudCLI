from pyicloud import PyiCloudService
from pyicloud.services.findmyiphone import AppleDevice
from webbrowser import open

class iCloudFunctions:
    def __init__(self, email: str, password: str=None) -> None:
        if password is None:
            self.api = PyiCloudService(email, password)
        else:
            self.api = PyiCloudService(email, password)

        self.funcs = {
            "findiphone": self.find_iphone
        }

    def exec(self, func: str):
        if self.api.requires_2sa or self.api.requires_2fa:
            print('Account requires 2sa or 2fa which is not currently supported')

        self.funcs[func]()
    
    def find_iphone(self):
        phones = [x for x in self.api.devices if  self.is_phone(x)]

        for i in range(len(phones)):
            print(f'{phones[i].status()["name"]}: {i+1}')

        phone = None
        
        try:
            number = int(input('select which device to find: ')) - 1
            phone = phones[number]
        except Exception:
            print('Invalid choice')
            return

        is_lost = input('Would you like to enable lost mode? [Y/n]: ').lower() == 'y'
        if is_lost:
            number = input('Enter a number to call for someone who finds your phone: ')
            phone.lost_device(number, 'Please call the number to return the device')

        do_sound = input("Would you like to play a sound from your phone? [Y/n]: ").lower() == "y"
        if do_sound:
            self.phone.play_sound()

        loc = phone.location()
        lat = loc['latitude']
        long = loc['longitude']

        maps_url = "http://www.google.com/maps/place/"
        open(maps_url + f'{lat}, {long}')

    def is_phone(self, device: AppleDevice):
        stats = device.status()
        return "iPhone" in stats['deviceDisplayName']
# coding: utf-8

import random
import reminders
import ui

#v = ui.load_view()
#v.present('sheet')

# NOTE: When you run this script, you will be prompted to allow access to your reminders. The script will (obviously) not work correctly if you deny this permission. You can change Pythonista's permissions from the Settings app.


def main():
    todo = reminders.get_reminders(completed=False)
    tdn_list = []
    for entry in todo:
        if entry.title.startswith('TDN: '):
            tdn_list.append(entry.title)
    if len(tdn_list):
        choice = random.randint(0, len(tdn_list) - 1)
        print(tdn_list[choice])


if __name__ == '__main__':
	main()

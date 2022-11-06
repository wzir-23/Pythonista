# Pythonista scripts

This is where I keep my very small collection of Pythonista[1] scripts for iOS.

[1] https://www.omz-software.com/pythonista/

## ToDoNow
Add reminders in the Reminder app where each new reminder is prepended with 'TDN: '. 
When called, the program will return a random entry from that list.

Example:
TDN: Practice Italian
TDN: Small physical exercise
TDN: Work on ToDoNow
TDN: Pick up a good book

Features:
- [X] Access reminders from iOS
- [X] Make it work in command line mode
- [ ] Create a GUI

## FastFasting
What: Keep track of intermittent fasting
My attempt at a utility for periodic fasting since I couldn't find anything
simple enough without login or subscriptions.

Features:
- [X] Start period  (either fasting or eating window)
- [X] Stop period
- [ ] Delete period
- [ ] Edit past values
- [ ] Show duration of current or last period
- [ ] Refresh/recalculate duration
- [X] Store values in sqlite3 database
- [ ] Use ui module to create basic GUI


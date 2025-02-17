import random 
list_bazi = ['sang','kaghaz','gheichi']
emtiyaze_karbar = 0
emtiyaze_computer = 0
while True :
    entekhabe_computer = random.choice(list_bazi)
    entekhabe_karbar = input('((sang / kaghaz / gheichi)) -  yeki ra entekhab konid: ').lower().strip()
    if entekhabe_karbar == 'end'.lower().strip() :
        print('payan. bazi tamam shod.')
        break
    elif entekhabe_karbar not in list_bazi :
        print('error... fahgat yeki az ((sang / kaghaz / gheichi)) ra vared konid.')
        continue
    elif entekhabe_karbar == 'sang' and entekhabe_computer == 'gheichi' :
        emtiyaze_karbar += 1
    elif entekhabe_karbar == 'sang' and entekhabe_computer == 'kaghaz' :
        emtiyaze_computer += 1
    elif entekhabe_karbar == 'kaghaz' and entekhabe_computer == 'sang' :
        emtiyaze_karbar += 1
    elif entekhabe_karbar == 'kaghaz' and entekhabe_computer == 'gheichi' :
        emtiyaze_computer += 1
    elif entekhabe_karbar == 'gheichi' and entekhabe_computer == 'sang' :
        emtiyaze_computer += 1
    elif entekhabe_karbar == 'gheichi' and entekhabe_computer == 'kaghaz' :
        emtiyaze_karbar += 1
    elif entekhabe_karbar == entekhabe_computer :
        print('barabar hastand va hich kodam emtiyaz nemigirand.')
    print(f'entekhabe shoma : {entekhabe_karbar}')
    print(f'entekhabe computer : {entekhabe_computer}')
    print(f'emtiyaze shoma : {emtiyaze_karbar}')
    print(f'emtiyaze computer = {emtiyaze_computer}')

# بازی سنگ کاغذ قیچی 

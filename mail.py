def check_amount(p_amount):
    try:
        p_amount = p_amount.replace(',','')
        p_amount = float(p_amount)
        des = "%.2f" % p_amount
        t_des = p_amount - float(des)
        if t_des == 0.0 and float(des) > 0:
            return float(des)
        else:
            print("Please only input two decimals or put in a positvie int")
            return False
    except ValueError:
        return False
def adddic(dic , name):
    dic[name] = [0.00, 0 ,0.00]
    return dic
def printdon(dic):
    for x, val in enumerate(dic):
        print()
        print(val)
def updatdic(dic, name, amount):
    diclist = dic.get(name)
    diclist[0] = diclist[0] + amount
    diclist[1] = diclist[1] + 1
    tep = diclist[0]/float(diclist[1])
    tep = "%.2f" % amount
    diclist[2] = float(tep)
    dic[name] = diclist
    return dic
def print_thank_you(name, amount):
    head = 'Dear ' +name + ','
    print(head)
    body = "\tThank you for donation of $" + str(amount) + '. South Carolina Association of Magicians appreciate your support!'
    print(body)

def mail():
    doner_info = {'a': [10.0,1,10.0]}
    ex = True
    while(ex):
        print()
        i1 = input("To send a thank you press T, to create a report press C, to quit press Q: ")
        if i1 == 'T':
            ex1 = True
            while(ex1):
                print()
                i2 = input("Please input a name, for a list of donors type list: ")
                if i2 == 'list':
                    dlist = list(doner_info.keys())
                    printdon(dlist)
                elif type(i2) == str:
                    ex2 = True
                    while ex2:
                        amount =input("Please put in the donation amount: Must consist only numbers, for example $1,000 shoud be typed in as 1000")
                        amount = check_amount(amount)
                        if amount >= 0:
                            if i2 not in doner_info:
                                dic = adddic(doner_info, i1)
                            dic =updatdic(doner_info, i1, amount)
                            print_thank_you(i2, amount)
                            ex2 = False
                            ex1 = False
                            
                        else:
                            print("Please put in a corrrect amount")
#work after this Jim

#work after Chis
print_thank_you('sean', 10)                   
mail()

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
def addDic(dic , name):
    dic[name] = [0.00, 0 ,0.00]
    return dic

def mail():
    dic = {'a': 1}
    ex = True
    while(ex):
        print()
        i1 = input("To send a thank you press 1, to create a report press 2, to quit press q: ")
        if int(i1) == 1:
            ex1 = True
            while(ex1):
                print()
                i1 = input("Please input a name, for a list of donors type list: ")
                if i1 == 'list':
                    dlist = list(dic.keys())
                    for x , val in enumerate(dlist):
                        print ()
                        print(val)
                elif i1 == 'name':
                    ex2 = True
                    while ex2:
                        amount =input("Please put in the donation amount: Must consist only numbers, for example $1,000 shoud be typed in as 1000")
                        if check_amount(amount):
                            print("here")
                            if i1 not in dic:
                                print('hi')
                        else:
                            print("Please put in a corrrect amount")
                    
mail()

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
                    printdon(dlist)
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
#work after this Jim
        elif il.lower() == 'c':
            print('|       Name       |  #  |   Average   |    Total    |')
            print('|------------------|-----|-------------|-------------|')
            for donor in donor_info:
                donor_name = cat_name_space(donor)
                donor_num = cat_num_space(donor_info[donor][1])
                donor_avg = cat_donation_space(donor_info[donor][2])
                donor_total = cat_donation_space(donor_info[donor][0])
                print('|{}|{}|{}|{}|').format(donor_name, donor_num, donor_avg, donor_total)

#work after Chis
                    
mail()


def cat_name_space(donor):
    """Add spaces to make the names the right length."""
    if len(donor) > 18:
        return donor[:19]
    else:
        extra_spaces = 18 - len(donor)
        extra_spaces = ' ' * extra_spaces
        return donor + extra_spaces


def cat_num_space(num):
    """Add spaces to make the number of donations the right length."""
    num = str(num)
    if len(num) > 5:
        return num[:6]
    else:
        extra_spaces = 5 - len(num)
        extra_spaces = ' ' * extra_spaces
        return num + extra_spaces


def cat_donation_space(num):
    """Add spaces to make the total/average the right length."""
    num = str(num)
    if len(num) > 13:
        return num[:14]
    else:
        extra_spaces = 13 - len(num)
        extra_spaces = ' ' * extra_spaces
        return num + extra_spaces

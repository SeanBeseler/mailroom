"""."""
quit = ['q', 'quit']


def check_amount(p_amount):
    """."""
    try:
        p_amount = p_amount.replace(',', '')
        p_amount = float(p_amount)
        des = "%.2f" % p_amount
        t_des = p_amount - float(des)
        if t_des == 0.0 and float(des) > 0:
            return float(des)
        else:
            print("Please only input two decimals or put in a positive int")
            return False
    except ValueError:
        return False



def add_dic(donor_info, name):
    """."""
    donor_info[name] = [0.00, 0, 0.00]
    return donor_info



def print_name(donor_info):
    """."""
    for x, val in enumerate(donor_info):
        print()
        print(val)



def update_dic(dic, name, amount):
    """."""
    diclist = dic.get(name)
    diclist[0] = diclist[0] + amount
    diclist[1] = diclist[1] + 1
    tep = diclist[0] / float(diclist[1])
    tep = "%.2f" % tep
    diclist[2] = float(tep)
    dic[name] = diclist
    print(dic)
    return dic


def print_thank_you(name, amount):
    """."""
    head = '\nDear ' + name + ',\n'
    print(head)
    amount = str(amount)
    if amount[len(amount) - 2] == '.':
        amount = amount + '0'
    body = "Thank you for donation of $" + amount + '. South Carolina \
Association of Magicians appreciate your support!\n\nSincerely,\nCode Dudes'
    print(body)
    return body


def cat_name_space(donor):
    """Add spaces to make the names the right length."""
    if len(donor) > 18:
        return donor[:18]
    else:
        extra_spaces = 18 - len(donor)
        extra_spaces = ' ' * extra_spaces
        return donor + extra_spaces


def cat_num_space(num):
    """Add spaces to make the number of donations the right length."""
    num = str(num)
    if len(num) > 5:
        return num[:5]
    else:
        extra_spaces = 5 - len(num)
        extra_spaces = ' ' * extra_spaces
        return num + extra_spaces


def cat_donation_space(num):
    """Add spaces to make the total/average the right length."""
    num = str(num)
    if num[len(num) - 2] == '.':
        num = num + '0'
    if len(num) > 13:
        return num[:13]
    else:
        extra_spaces = 13 - len(num)
        extra_spaces = ' ' * extra_spaces
        return num + extra_spaces


def mail(): # pragma: no cover
    """."""
    donor_info = {}
    ex = True
    while(ex):
        print()
        i1 = input("Please choose: (T)hank you, (C)reate report, (Q)uit: ").lower()
        if i1 == 't':
            ex1 = True
            while(ex1):
                print()
                i2 = input("Please input a name, for a list of donors type \
list: ")
                if i2 == 'list':
                    dlist = list(donor_info.keys())
<<<<<<< HEAD
                    printdon(dlist)
=======
                    print_name(dlist)
>>>>>>> 29354c743944eab8d16317ef66f4fe0fb9418f37
                elif type(i2) == str:
                    i2 = i2.split(' ')
                    new_name = ''
                    for word in i2:
                        word = word.title()
                        new_name = new_name + ' ' + word
                    i2 = new_name
                    ex2 = True
                    while ex2:
                        user_input = input("Please put in the donation amount: ")
                        amount = check_amount(user_input)
                        if user_input in quit:
                            ex1 = False
                            ex2 = False
                        elif amount >= 0 and amount is not False:
                            if i2 not in donor_info:
                                donor_info = add_dic(donor_info, i2)
                            donor_info = update_dic(donor_info, i2, amount)
                            print_thank_you(i2, amount)
                            ex2 = False
                            ex1 = False
                        else:
                            print("Please enter a numerical amount.\n")
                elif i2 in quit:
                    ex1 = False
        elif i1 == 'c':
            if donor_info:
                print()
                print('|       Name       |  #  |   Average   |    Total    |')
                print('|------------------|-----|-------------|-------------|')
                for donor in donor_info:
                    donor_name = cat_name_space(donor)
                    donor_num = cat_num_space(donor_info[donor][1])
                    donor_avg = cat_donation_space(donor_info[donor][2])
                    donor_total = cat_donation_space(donor_info[donor][0])
                    print('|{}|{}|{}|{}|'.format(donor_name, donor_num, donor_avg, donor_total))
            else:
                print('\nYou have no donors yet.')
        elif i1 in quit:
            print('\nThank you. Goodbye.\n')
            break


if __name__ == '__main__': # pragma: no cover
    mail()

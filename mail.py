"""."""
import sys
quit = ['Q', 'Quit']


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
            print("Please only input two decimals or put in a positvie int")
            return False
    except ValueError:
        return False


def adddic(donor_info, name):
    """."""
    donor_info[name] = [0.00, 0, 0.00]
    return donor_info


def printdon(donor_info):
    """."""
    for x, val in enumerate(donor_info):
        print()
        print(val)


def mail():
    """."""
    donor_info = {'a': 1}
    ex = True
    while(ex):
        print()
        i1 = input("Please choose: (T)hank you, (C)reate report, (Q)uit: ")
        if i1 == 'T':
            ex1 = True
            while(ex1):
                print()
                i2 = input("Please input a name, for a list of donors \
type list: ")
                if i2 == 'list':
                    dlist = list(donor_info.keys())
                    print(dlist)
                elif i2 == 'name':
                    ex2 = True
                    while ex2:
                        amount = input("""
Please put in the donation amount: Must consist only numbers,
(for example $1,000 shoud be typed in as 1000)
\n> """)
                        if check_amount(amount):
                            print("here")
                            if i2 not in donor_info:
                                print('hi')
                        elif amount in quit:
                            ex1 = False
                            ex2 = False
                        else:
                            print("Please put in a corrrect amount")
                elif i2 in quit:
                    ex1 = False
#work after this Jim



#work after Chis
        elif i1 in quit:
            sys.exit('\nThank you, good bye!\n')


mail()

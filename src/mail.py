"""
Mailroom program.

Keeps a working dictionary of donors and sends thank yous.
"""


def check_amount(donation):
    """Check the donation amount."""
    try:
        donation = donation.replace(',', '')
        if len(donation) > 14:
            print('\nWe can not accept a donation that size.\n')
            return False
        donation = float(donation)
        donation_with_change = "%.2f" % donation
        if float(donation_with_change) > 0:
            return float(donation_with_change)
        else:
            print("Please only input two decimals or put in a positive int")
            return False
    except ValueError:
        return False


def new_donor(donor_info, name):
    """Assign name to key with defualt value set."""
    donor_info[name] = [0.00, 0, 0.00]
    return donor_info


def print_name(donor_list):
    """Give the user the list of donors."""
    for name in donor_list:
        print('\n', name)
    return name


def update_dic(donor_list, name, amount):
    """
    Add donation amount to dictionary.

    Apply changes to the other values as appropriate.
    """
    donor = donor_list.get(name)
    donor[0] = donor[0] + amount
    donor[1] = donor[1] + 1
    average = donor[0] / float(donor[1])
    average = "%.2f" % average
    donor[2] = float(average)
    donor_list[name] = donor
    return donor_list


def print_thank_you(name, amount):
    """Create a thank you e-mail."""
    head = '\nDear ' + name + ',\n'
    print(head)
    amount = str(amount)
    if amount[len(amount) - 2] == '.':
        amount = amount + '0'
    body = "Thank you for donation of $" + amount + '. \nSouth Carolina \
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
        extra_spaces = 3 - len(num)
        extra_spaces = ' ' * extra_spaces
        return extra_spaces + num


def cat_donation_space(num):
    """Add spaces to make the total/average the right length."""
    num = str(num)
    if num[len(num) - 2] == '.':
        num = num + '0'
    extra_spaces = 14 - len(num)
    extra_spaces = ' ' * extra_spaces
    return extra_spaces + num


def main():  # pragma: no cover
    """
    Main function sends out to others.

    Based on user input creats a donation and thank you based
    on name and amount,
    or calls the list of current donors,
    or shows the table of donors with their data,
    or quits.
    """
    donor_info = {}
    mail_loop = True
    while(mail_loop):
        print()
        input_one = input("Please choose: (T)hank you, \
(C)reate report, (Q)uit: ").lower()
        if input_one == 't':
            donation_loop = True
            while(donation_loop):
                print()
                input_two = input("Please input a full name, for a list of donors \
type list: ")
                if input_two == 'list':
                    donor_list = list(donor_info.keys())
                    print_name(donor_list)
                elif str.isalpha(input_two):
                    input_two = input_two.split(' ')
                    new_name = ''
                    for word in input_two:
                        word = word.title()
                        new_name = new_name + ' ' + word
                    input_two = new_name
                    amount_loop = True
                    while amount_loop:
                        user_input = input("Please put in the \
donation amount: ")
                        amount = check_amount(user_input)
                        if user_input == 'q':
                            donation_loop = False
                            amount_loop = False
                        elif amount >= 0 and amount is not False:
                            if input_two not in donor_info:
                                donor_info = new_donor()(donor_info, input_two)
                            donor_info = update_dic(donor_info,
                                                    input_two, amount)
                            print_thank_you(input_two, amount)
                            amount_loop = False
                            donation_loop = False
                        else:
                            print("Please enter a new value.\n")
                elif input_two == 'q':
                    donation_loop = False
                else:
                    print('\nTry that again, maybe don\'t use numbers')
        elif input_one == 'c':
            if donor_info:
                print(' ____________________________________________________ ')
                print('|      Donors      | # |    Average   |     Total    |')
                print('|       Name       |   |   Donations  |   Donations  |')
                print('|------------------|---|--------------|--------------|')
                for donor in donor_info:
                    donor_name = cat_name_space(donor)
                    donations = cat_num_space(donor_info[donor][1])
                    donation_avg = cat_donation_space(donor_info[donor][2])
                    donor_total = cat_donation_space(donor_info[donor][0])
                    print('|{}|{}|{}|{}|'.format(donor_name, donations,
                                                 donation_avg, donor_total))
                print('|__________________|___|______________|______________|')
            else:
                print('\nYou have no donors yet.')
        elif input_one == 'q':
            print('\nThank you, goodbye.\n')
            break
        else:
            print('\nTry one of the letters next time.')


if __name__ == '__main__':  # pragma: no cover
    main()

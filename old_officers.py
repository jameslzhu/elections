# @author: Catherine Hu, James Zhu, Carolyn Wang (for add_users)

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from election.settings import OLD_OFFICER_RANGE

from election.cred import get_credentials
from election.sheets import get_election_data
from election.users import add_users
from election.groups import add_user_to_group, add_all_to_committes

def main():
    credentials = get_credentials()
    election_data = get_election_data(credentials, OLD_OFFICER_RANGE)[1:]
    for row in election_data:
        user = row[2]
        group = row[3][:-1]
        # print("{}->{}".format(user, group))
        add_user_to_group(credentials, user, '{}-officers'.format(group))
        add_user_to_group(credentials, user, 'current-{}'.format(group))
        print("{}->{}".format(user, group))

        if len(row) >= 5 and row[4].strip():
            for mailing_list in row[4].split(', '):
                add_user_to_group(credentials, user, mailing_list[:-1])
                print("{}->{}".format(user, mailing_list))

    # add_all_to_committes(credentials, election_data)

if __name__ == '__main__':
    main()

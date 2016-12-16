import vk
from getpass import getpass


APP_ID = 5702743


def get_user_login():
    return input("Login: ")


def get_user_password():
    return getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    online_friends_iter = filter(
        lambda friend: friend['online'] == 1,
        api.friends.get(fields='first_name, last_name, online')
    )
    return online_friends_iter


def output_friends_to_console(friends_online):
    for enum, friend in enumerate(friends_online, start=1):
        print('{0}. {1} {2}'.format(
            enum,
            friend['first_name'],
            friend['last_name'])
        )


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print('Friends online:')
    output_friends_to_console(friends_online)

import datetime
import json

USERS_FILE = 'files/users.txt'
POSTS_FILE = 'files/posts.txt'


def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


def register():
    full_name = input('To\'liq ismingiz: ')
    username = input('Foydalanuvchi nomi: ')
    gmail = input('Gmail: ')
    password = input('Parol: ')
    created_at = str(datetime.datetime.now())

    users = load_data(USERS_FILE)
    users.append(
        {'full_name': full_name, 'username': username, 'gmail': gmail, 'password': password, 'created_at': created_at})
    save_data(USERS_FILE, users)
    print('Foydalanuvchi muvaffaqiyatli ro\'yxatdan o\'tdi.')


def login():
    username = input('Foydalanuvchi nomi: ')
    password = input('Parol: ')

    users = load_data(USERS_FILE)
    for user in users:
        if user['username'] == username and user['password'] == password:
            print('Kirish muvaffaqiyatli.')
            return user
    print('Foydalanuvchi nomi yoki parol noto\'g\'ri.')
    return None


def create_post(username):
    message = input('Xabar: ')
    created_at = str(datetime.datetime.now())

    posts = load_data(POSTS_FILE)
    posts.append({'username': username, 'message': message, 'created_at': created_at})
    save_data(POSTS_FILE, posts)
    print('Post muvaffaqiyatli yaratildi.')


def get_user_posts(username):
    posts = load_data(POSTS_FILE)
    user_posts = [post for post in posts if post['username'] == username]

    for post in user_posts:
        print(post)


def show_all_users():
    users = load_data(USERS_FILE)
    for user in users:
        print(user)


def show_all_posts():
    posts = load_data(POSTS_FILE)
    for post in posts:
        print(post)


def main():
    while True:
        print('Auth menyusi:')
        print('1. Ro\'yxatdan o\'tish')
        print('2. Kirish')
        print('3. Chiqish')

        choice = input('Variantni tanlang: ')
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print('Foydalanuvchi menyusi:')
                    print('1. Post yaratish')
                    print('2. Mening barcha postlarim')
                    print('3. Chiqish')

                    user_choice = input('Variantni tanlang: ')
                    if user_choice == '1':
                        create_post(user['username'])
                    elif user_choice == '2':
                        get_user_posts(user['username'])
                    elif user_choice == '3':
                        break
        elif choice == '3':
            break


if __name__ == '__main__':
    main()

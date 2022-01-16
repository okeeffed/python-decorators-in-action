class User:
    def __init__(self, role='user'):
        self.role = role


def admin_only(func):
    def check_is_admin(*args, **kwargs):
        if (args[0].role == 'admin'):
            func(*args, **kwargs)
        else:
            print('You are not an admin')
    return check_is_admin


@admin_only
def delete_important_record(user):
    print('Allowed')


user1 = User()
user2 = User('admin')

delete_important_record(user1)  # You are not an admin
delete_important_record(user2)  # Allowed

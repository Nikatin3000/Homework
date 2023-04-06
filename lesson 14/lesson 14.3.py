def arg_rules(type_: type, max_length: int, contains: list):
    def decor(func):
        def res(name):
            error_list = []
            if len(name) > max_length:
                error_list.append(f'Довжина аргумента {name} більша ніж {max_length}')
            if type(name) != type_:
                error_list.append(f'Тип аргумента {name} не відповідає {type_}')
            resultat = 0
            for i in contains:
                if i in name:
                    resultat += 1
            if resultat != len(contains):
                error_list.append(f' {name} не містить {contains}')
            if error_list:
                print(*error_list, sep=' \n')
                return False
            return func(name)
        return res
    return decor




@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('jS@SH05'))


# assert create_slogan('johndoe05@gmail.com') is False
#
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

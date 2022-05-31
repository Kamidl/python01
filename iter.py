user_list = [{'role':'admin','user_name':'admin','password':'123456','dept':'boss'}]


result = {'code':0,'message':''}


def login(user_name,password):
    if user_name is None or user_name == '':
        result.update({'code':1,'message':'用户名不能为空'})
    return result
    if password is None or password == '':
        result.update({'code': 1, 'message': '密码不能为空'})
        return  result

    for user_info in user_list:
        if user_info.get('account') and password == user_info.get('password'):
            result.update({'message':'登录成功！','user_list':'请检查您的用户名或密码是否填写正确.'})
            return result

if __name__ == '__main__':
    username = input('请输入用户名:')
    password = input('请输入密码:')


print(login(username,password))







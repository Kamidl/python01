from loguru import logger
logger.info('hello word')
logger.debug('这是一条debug日志')
logger.warning('这是一条warning日志')
logger.success('这是一条success日志')
logger.error('这是一条error日志')

logger.add('a.log',format='{time}|{level}{module}|{line}|{message}',level='DEBUG')
logger.info('hello word')
logger.debug('这是一条debug日志')
logger.warning('这是一条warning日志')
logger.success('这是一条success日志')
logger.error('这是一条error日志')

logger.add('file.log',format='{time:yyyy-mm-dd at hh:mm:ss} | {level} |{message}')

logger.info('我的名字叫{},今天星期几{}','张三','1')






























# 1测试登录的用例


# case1:输入争取的用户和正确的密码进行登录

# def test_login_success(self):
#     except_value = 0
#     actual_value = login('admin','123456').get('code')
#     self.asserEqual(except_value,actual_value)
#
#
# # case2 :输入错误的用户名或密码登录
#
# def test_user_wrong(self):
#     except_value = 1
#     actual_value = login('bca','12345')

















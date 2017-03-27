# coding: utf8

SQLALCHEMY_TRACK_MODIFICATIONS = True
SESSION_COOKIE_NAME = 'session'
# flask-mail 
# SMTP邮件服务器地址，默认为localhost
# MAIL_SERVER = 
# SMTP邮件服务器端口，默认为25
# MAIL_PORT = 
# 邮件服务器用户名
# MAIL_USERNAME =
# 邮件服务器密码 
# MAIL_PASSWORD = 
# 默认发件人，如果Message对象里没指定发件人，就采用默认发件人
# MAIL_DEFAULT_SENDER = 
# 是否启用TLS，默认为False
# MAIL_USE_TLS = Fasle
# 是否启用SSL，默认为False
# MAIL_USE_SSL = False
# 邮件批量发送个数上限，默认为没有上限
# MAIL_MAX_EMAILS = 
# 将附件的文件名强制转换为ASCII字符，避免在某些情况下出现乱码，默认为False
# MAIL_ASCII_ATTACHMENTS
# 调用”Mail.send()”方法后，邮件不会真的被发送，在测试环境中使用，默认为False
# MAIL_SUPPRESS_SEND

# flask-babel
# BABEL_DEFAULT_LOCALE = 
# BABEL_DEFAULT_TIMEZONE = 

try:
      from local_config import *
except ImportError:
      pass

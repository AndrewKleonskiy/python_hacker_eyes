import smtplib as smtp
from getpass import getpass

email = 'test@yandex.ru' # почта с которой отправляем
password = '***' #пароль от почты отправителя
dest_email = 'inbox@yandex.ru' #куда отправляем
subject = 'Test'
email_text = ('hello')
message = 'From:{}\nTo:{}\nSubject:{}\n\n{}'.format(email, dest_email, subject, email_text)

server = smtp.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()

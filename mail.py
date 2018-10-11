#sending a mail
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("trishitagharai24@gmail.com", "23wexc@#12qwzx!@")
 
msg = "O_O"
server.sendmail("trishitagharai24@gmail.com", "tinaalex1307@gmail.com", msg)
print('Mail is sent ^.^')
server.quit()
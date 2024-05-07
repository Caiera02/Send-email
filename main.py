from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Corpo da mensagem do email #
msg = MIMEMultipart()
message = "Hellou Word:)"

# Credenciais e assunto do email #
password = "senha"
msg['From'] = "email que vai enviar "
msg['To'] = " e-mail que vai receber"
msg['Subject'] = "Assunto do e-mail" # Assunto do email

# Monta conexão e envia o email #
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print('Email enviado')
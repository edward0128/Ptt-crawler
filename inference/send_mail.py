#!/usr/bin/env python
# coding: utf-8

# In[4]:


import smtplib
from email.mime.text import MIMEText

gmail_user = 'support@geminiopencloud.com'
gmail_password = 'iltwagemini%$#@' # your gmail password

msg = MIMEText('訓練完成!')
msg['Subject'] = 'Trainning Complete'
msg['From'] = gmail_user
msg['To'] = 'a0981202524@gmail.com'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.send_message(msg)
server.quit()

print('訓練完成!')


# In[ ]:





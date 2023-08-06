import smtplib, os
from collections import namedtuple
from email.message import EmailMessage
from typing import List, Union

attachable = namedtuple('attachable', ['fn', 'maintype', 'subtype'])

def email_text(content: str, recipient: str = None, subject: str = 'Build Status Update', sender: str = None):
  """
  Sends a basic email from Bob the Builder to the specified recipient.

  :param content: The text to include in the email body
  :param recipient: The email of the person you're sending this to
  :param subject: The subject line of the email
  :param sender: The address to send from. If not present, we use the EMAIL_SENDER environment var
  """

  message = EmailMessage()
  message.set_content(content)
  if not sender:
    try:
      sender = os.environ['EMAIL_SENDER']
    except:
      raise Exception('No email sender provided')
  if not recipient:
    try:
      recipient = os.environ['EMAIL_RECIPIENT']
    except:
      raise Exception('No email recipient provided')
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = recipient

  s = smtplib.SMTP_SSL('smtp.mail.yahoo.com', port=465)
  s.login(sender, os.environ['EMAIL_APP_KEY']) # app password
  s.send_message(message)
  s.quit()
  return message

def email_attachment(content: str, attachment: Union[List[attachable], attachable], recipient: str = None, subject: str = 'Build Update! Files attached.', sender: str = None):
  """
  Sends an email with some number of attachments from Bob the Builder to the specified recipient

  :param content: The text to include in the email body
  :param attachment: The file or list of files to attach. These are tuples with 'fn', 'maintype', and 'subtype' fields
  :param recipient: The email of the person you're sending this to
  :param subject: The subject of the email
  :param sender: The address to send from. If not present, we use the EMAIL_SENDER environment var
  """
  message = EmailMessage()
  message.set_content(content)
  if not sender:
    sender = os.environ['EMAIL_SENDER']
  if not recipient:
    recipient = os.environ['EMAIL_RECIPIENT']
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = recipient

  if type(attachment) != list:
    attachment = [attachment]
  
  for a in attachment:
    try:
      att = open(a.fn, 'rb')
      att_content = att.read()
      message.add_attachment(att_content, maintype = a.maintype, subtype = a.subtype, filename = a.fn.split('/')[-1])
    finally:
      att.close()
  s = smtplib.SMTP_SSL('smtp.mail.yahoo.com', port=465)
  s.login('bob.builder@simoncomputing.com', os.environ['EMAIL_APP_KEY']) # app password
  s.send_message(message)
  s.quit()
  return message
  
def email_text_attachment(content: str, attachment: str, recipient: str = None, subject: str = 'Build Update! Text files attached.', sender: str = None):
  """
  Sends an email with a text document attachment from Bob the Builder to the specified recipient

  :param content: The text to include in the email body
  :param attachment: The text file to attach to the email
  :param recipient: The email of the person you're sending this to
  :param subject: The subject of the email
  :param sender: The address to send from. If not present, we use the EMAIL_SENDER environment var
  """
  return email_attachment(content, [attachable(attachment, 'text', 'plain')], recipient, subject, sender)

def email_html_attachment(content: str, attachment: str, recipient: str = None, subject: str = 'Build Update! Text files attached.', sender: str = None):
  """
  Sends an email with a HTML attachment from Bob the Builder to the specified recipient

  :param content: The text to include in the email body
  :param attachment: The html file to attach to the email
  :param recipient: The email of the person you're sending this to
  :param subject: The subject of the email
  :param sender: The address to send from. If not present, we use the EMAIL_SENDER environment var
  """
  return email_attachment(content, [attachable(attachment, 'text', 'html')], recipient, subject, sender)

def email_png_attachment(content: str, attachment: str, recipient: str = None, subject: str = 'Build Update! Text files attached.', sender: str = None):
  """
  Sends an email with a PNG image attachment from Bob the Builder to the specified recipient

  :param content: The text to include in the email body
  :param attachment: The png file to attach to the email
  :param recipient: The email of the person you're sending this to
  :param subject: The subject of the email
  :param sender: The address to send from. If not present, we use the EMAIL_SENDER environment var
  """
  return email_attachment(content, [attachable(attachment, 'image', 'png')], recipient, subject, sender)

def email_pdf_attachment(content: str, attachment: str, recipient: str = None, subject: str = 'Build Update! Files attached.', sender = None):
  """
  Sends an email with a PDF attachment from Bob the Builder to the specified recipient

  :param content: The text to include in the email body
  :param attachment: The pdf file to attach to the email
  :param recipient: The email of the person you're sending this to
  :param subject: The subject of the email
  :param sender: The address to send from. If not present, we use the EMAIL_SENDER environment var
  """
  return email_attachment(content, [attachable(attachment, 'application', 'pdf')], recipient, subject, sender)
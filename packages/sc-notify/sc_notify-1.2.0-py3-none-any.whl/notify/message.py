from notify import mail, pm

import os

def send_text_message(content: str, subject: str = 'Status Update'):
  """
  Sends a basic email or slack message to the default recipient. Prioritizes slack.

  FOR EMAIL: set EMAIL_APP_KEY, EMAIL_RECIPIENT, EMAIL_SENDER
  FOR SLACK: set SLACK_API_KEY, SLACK_DEFAULT_CHANNEL

  :param content: The text to include in the body
  :param subject: The subject line of the email (unused for slack message)
  """

  if ('SLACK_API_KEY' in os.environ):
    print(f'sending slack')
    pm.slack_message(content)
  elif ('EMAIL_APP_KEY' in os.environ):
    print(f'sending email')
    mail.email_text(content, subject=subject)
  else:
    print('neither')
    raise Exception('Neither Slack API key nor email app key is present as a env var. Failed to send message.')


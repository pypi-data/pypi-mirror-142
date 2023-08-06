from slack import WebClient
from slack.errors import SlackApiError, SlackClientError
import os

def slack_message(message: str = 'Default Build Message', user_id: str = None):
  if not user_id:
    user_id = os.environ['SLACK_DEFAULT_CHANNEL']
  try:
    client = WebClient(os.environ['SLACK_API_KEY'])
    response = client.chat_postMessage(
      channel = user_id,
      text = message,
      username = 'Bob the Builder',
      icon_url = 'https://i.imgur.com/JHK6tnu.png'
    )
    return response
  except SlackApiError as e:
    return {'ok': False, 'error': e.response['error']}
  except SlackClientError as e:
    return {'ok': False, 'error': e.response['error']}
  except:
    return {'ok': False, 'error': 'Unknown Error'}


def slack_upload(filename: str, user_id: str = None):
  if not user_id:
    user_id = os.environ['SLACK_DEFAULT_CHANNEL']
  try:
    client = WebClient(os.environ['SLACK_API_KEY'])
    response = client.files_upload(
      channels = user_id,
      file = filename,
      title = filename.split('/')[-1],
      username = 'Bob the Builder',
      icon_url = 'https://i.imgur.com/JHK6tnu.png'
    )
    return response
  except SlackApiError as e:
    return {'ok': False, 'error': e.response['error']}
  except SlackClientError as e:
    return {'ok': False, 'error': e.response['error']}
  except FileNotFoundError:
    return {'ok': False, 'error': 'File Not Found Error'}
  except:
    return {'ok': False, 'error': 'Unknown Error'}
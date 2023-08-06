# notify

Notification library for automated email and slack messages. Used by AWS Bootstrapper to report build status to us or client(s). The library is hosted for pip install at https://pypi.simoncomputing.com

## Installation notes

`pip install sc-notify --extra-index-url https://pypi.simoncomputing.com`

You'll need to supply email and/or slack environment variables, too:

```sh
export EMAIL_APP_KEY: _____________
export SLACK_API_KEY: _____________
export SLACK_DEFAULT_CHANNEL: _________
```

Note that the `SLACK_DEFAULT_CHANNEL` var is not strictly necessary for usage of the library, it just makes things more convenient.

## Usage

```python
# sending a slack message
response = slack_message('Text of the slack message', 'CHANNEL/USER ID')
# if you don't provide a channel/user id, the message will be sent to the id in $SLACK_DEFAULT_CHANNEL

# sending a file with slack
file_response = slack_upload('./path/to/file.abc', 'CHANNEL/USER')
# the message will just contain the file; if you want to add some text, just send messages
# before or after the upload and they'll get combined

# sending a text email
email_text('the text of the email', 'recipient@website.com', 'Optional Subject')
# if you don't provide a subject, it gets set to 'Build Status Update'

# emailing attachments
to_be_attached = {'fn': './path/to/file.abc', 'maintype':'text', 'subtype': 'plain'}
also_attached = {'fn': './path/to/another.abc', 'maintype':'application', 'subtype': 'pdf'}
email_attachment('the text of the email', to_be_attached, 'recipient@website.com', 'Optional Subject')
email_attachment('the text of the email', [to_be_attached, also_attached], 'recipient@website.com', 'Optional Subject')
# default subject is 'Build Update! Files attached.'
# you can send one or multiple files this way

# alternatively, you can send single attachments of preset types with the following functions
email_text_attachment('attached', './path/to/file.py', 'recipient@website.com')
email_html_attachment('attached', './path/to/file.html', 'recipient@website.com')
email_png_attachment('attached', './path/to/file.png', 'recipient@website.com')
email_pdf_attachment('attached', './path/to/file.pdf', 'recipient@website.com')

```

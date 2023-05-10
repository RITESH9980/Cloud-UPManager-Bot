# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("21347819"))
	API_HASH = os.environ.get("3d9e35374cc5aa394c123dd8062b3469")
	BOT_TOKEN = os.environ.get("6124896722:AAFwfLrJjdISzCcFheCEACyQz-RwdJvAtZ8")
	GOFILE_API = os.environ.get("GOFILE_API")
	STREAMTAPE_API_PASS = os.environ.get("bQ9j1GMrrltPkQK")
	STREAMTAPE_API_USERNAME = os.environ.get("ede3799345194ba16e61")
	SESSION_NAME = os.environ.get("SESSION_NAME", "CloudManagerBot")
	BOT_OWNER = int(os.environ.get("27723431"))
	LOG_CHANNEL = int(os.environ.get("-1001943348198"))
	DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
	HELP_TEXT = """
Send me any Media & Choose Upload Server,
I will Upload the Media to that server.

Currently I can Upload to:
> GoFile.io
> Streamtape.com
> Pixeldrain.com

Also I can do a lot of things from Inline!
__Check Below Buttons >>>__
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""

#!/usr/bin/env python3.8

#
# Imports Section
#

# The Usual Suspects
import os, sys, io

import re, random, time, datetime
from datetime import datetime

import requests, json

# Mail Library Stuff
import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import mimetypes
import base64

# My Stoof

import py_helper as ph
from py_helper import DebugMode, ModuleMode, Msg, DbgMsg, ErrMsg

#
# Variables
#

# Version Info
VERSION = (0,0,1)
Version = __version__ = ".".join([ str(x) for x in VERSION ])

# SMTP Server
Server = ""
ServerPort = 587

#
# Functions
#

# Create A Message With Attachments
def CreateMessageWithAttachments(sender,to,subject,message,attachments):
	msg = MIMEMultipart()

	msg["from"] = sender
	msg["to"] = to
	msg["subject"] = subject

	text_part = MIMEText(message)

	msg.attach(text_part)

	for attachment in attachments:
		content_type, encoding = mimetypes.gues_time(attachment)

		if content_type is None or encoding is not None:
			content_type = "application/octet-stream"

		main_type, sub_type = content_type.split('/',1)

		file = None

		if main_type == "text":
			with open(attachment,"rb") as fp:
				file = MIMEText(fp.read(), _subtype=sub_type)
		elif main_type == "image":
			with open(attachment,"rb") as fp:
				file = MIMEImage(fp.read(), _subtype=sub_type)
		elif main_type == "audio":
			with open(attachment,"rb") as fp:
				file = MIMEAudio(fp.read(), _subtype=sub_type)
		else:
			with open(attachment,"rb") as fp:
				file = MIMEBase(main_type,sub_type)
				file.set_payload(fp.read())
				encoders.encode_base64(file)

		filename = os.path.basename(attachment)

		file.add_header('Content-Disposition','attachment', filename=filename)
		msg.attach(file)

	# raw = base64.urlsafe_b64encode(msg.as_bytes())
	# return { "raw" : raw.encode() }

	return msg

# Create A Message (optionally with attachments)
def CreateMessage(sender,to,subject,message,attachments=None):
	msg = None

	if attachments:
		msg = CreateMessageWithAttachments(sender,to,subject,message,attachments)
	else:
		msg = MIMEText(message,"plain")

		msg["from"] = sender
		msg["to"] = to
		msg["subject"] = subject

		#raw = base64.urlsafe_b64encode(msg.as_bytes())
		#return { "raw" : raw.encode() }

	return msg

# Send MIME Formatted Message
def SendMessage(sender,to,msg,userid=None,password=None,server=None,port=None):
	global Server, ServerPort

	if not server:
		server = Server
	if not port:
		port = ServerPort

	objServer = smtplib.SMTP(server,port)

	objServer.starttls()
	objServer.login(userid,password)

	objServer.sendmail(sender,to,msg.as_string())

	objServer.quit()

# Test Stub
def test(sender,to,password):
	subject="A test"
	message = "This is only a test, had this been real... we'd have a problem"

	msg = CreateMessage(sender,to,subject,message)

	SendMessage(sender,to,msg,userid=sender,password=password)

#
# Requisite Main Loop
#

if __name__ == "__main__":
	print("This module was not intended to be run as a script")

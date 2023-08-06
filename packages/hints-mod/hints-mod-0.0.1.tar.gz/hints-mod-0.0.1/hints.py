#!/usr/bin/env python3.8

#
# Hints: Interface for hints and notations, a kind of free form quick and dirty defacto documentation
#

import os, sys, io, re
import argparse
import sqlite3 as sql
from sqlite3 import Error
import csv,json
import copy, uuid

from datetime import datetime,timedelta
import time

# Hmmm... probably not needed
from contextlib import contextmanager

# Debug Stoof
import pdb

# Ma stoof

import mysqlite as sql

import py_helper as ph
from py_helper import CmdLineMode, DebugMode, DbgMsg, Msg, ErrMsg

#
# Global Variables and Constants
#

# Version Info
VERSION=(0,0,1)
Version = __version__ = ".".join([ str(x) for x in VERSION ])

# Hint File Location
HintURL = None
# Default/Test Hint File
__HintFile__ = "/srv/storage/data/hints.sql3"

# Parser
Parser = None
# Subcommands
Subcommands = dict()

# AutoYes Flag
AutoYes = False

# Exact Flag
ExactStrings = False

# All Record Flag
AllRecords = False

#
# Classes
#

# HintEntry Class
class HintEntry:
	"""HintEntry Class"""

	RecordID = None
	PrimaryTag = None
	Tags = list()
	Description = None

	# Init Instance
	def __init__(self,primary=None,tags=None,description=None,recordid=None):
		"""Init Instance"""

		DbgMsg("Exitting HintEntry::__init__")

		if recordid:
			self.RecordID = recordid
		else:
			self.RecordID = uuid.uuid1()

		self.PrimaryTag = primary

		if tags != None:
			if type(tags) == list:
				self.Tags = tags
			else:
				self.Tags = tags.split(",")

		self.Description = description

		DbgMsg("Exitting HintEntry::__init__")

	# Print Instance Info
	def Print(self,output=True):
		"""Print Instance"""

		DbgMsg("Exitting HintEntry::Print")

		buffer = ""

		buffer = "{:<24} {}\n{}".format(self.PrimaryTag,self.Description,",".join(self.Tags))

		if output:
			Msg(buffer)

		DbgMsg("Exitting HintEntry::Print")

		return buffer

	# Format Instance Into JSON
	def Json(self):
		"""Output Contents as JSON"""

		jdoc = {
			"RecordID" : self.RecordID,
			"PrimaryTag" : self.PrimaryTag,
			"Tags" : self.Tags,
			"Description" : self.Description
		}

		return jdoc

	# Format Instance Into List
	def List(self):
		"""Output Contents as List (for CSV/TSV)"""

		lst = [
			self.RecordID,
			self.PrimaryTag,
			self.Tags,
			self.Description
		]

		return lst

	# Write Record to Open Connection
	def Write(self):
		"""Write to Open Connection"""

		DbgMsg("Exitting HintEntry::Write")

		ins = """
			INSERT INTO hints(recordid,primarytag,tags,description)
			VALUES(?,?,?,?)
		"""

		parameters = [ str(self.RecordID), self.PrimaryTag, ",".join(self.Tags), self.Description ]

		result = sql.Insert(ins,parameters)

		DbgMsg("Exitting HintEntry::Write")

		return result

	# Read Data For Instance From Open Connection
	def Read(self,datum):
		"""Read Data for Instance From Open Connection"""

		DbgMsg("Exitting HintEntry::Read")

		self.RecordID = uuid.UUID(datum[0])
		self.PrimaryTag = datum[1]
		self.Tags = datum[2].split(",")
		self.Description = datum[3]

		DbgMsg("Exitting HintEntry::Read")

	# Delte This Instance from Database
	def Delete(self):
		"""Delete From Database"""

		DbgMsg("Exitting HintEntry::Delete")

		ins = "DELETE FROM hints WHERE recordid = ?"

		parameters = [ str(self.RecordID) ]

		result = sql.Delete(ins,parameters)

		DbgMsg("Exitting HintEntry::Delete")

		return result

# Open DB
def OpenHintDB(url=None):
	"""Open Database"""

	DbgMsg("Entering hints::OpenHintDB")

	global HintURL

	conn = None

	if url == None: url = HintURL

	hint_table = """CREATE TABLE IF NOT EXISTS hints (
		recordid VARCHAR(36),
		primarytag VARCHAR(64),
		tags VARCHAR(924),
		description VARCHAR(1024)
	);"""

	table_specs = [ hint_table ]

	if sql.ActiveConnection != None:
		sql.Close(sql.ActiveConnection)

	try:
		conn = sql.Open(url,table_specs)
	except Error as dberr:
		ErrMsg(dberr,f"An error occurred trying to open {url}")
	except Exception as err:
		ErrMsg(err,f"An error occurred trying to open {url}")

	DbgMsg("Exitting hint::OpenHintDB")

	return conn

# Get Stats On Hint File
def HintFileInfo(output=True,**kwargs):
	"""Get Hint File Data"""

	global HintURL

	count = 0
	accessible = True

	buffer = "{:<20} : {}\n".format("Hint File",HintURL)

	try:
		buffer += "{:<20} : {}\n".format("File Size",os.path.getsize(HintURL))

		recs = Dump(None,noshow=True)
		count = len(recs)
	except Exception as err:
		accessible = False;

	buffer += "{:<20} : {}\n".format("Accessible",accessible)
	buffer += "{:<20} : {}".format("Records",count)

	if output:
		Msg(buffer)

	return buffer

# Ask user for Entry
def AskForEntry(allow_quit=False,**kwargs):
	"""Ask User for Entry"""

	DbgMsg("Entering hints::AskForEntry")

	primarytag = input("Primary Tag : ")

	if allow_quit and primarytag == "quit": return None

	description = input("Description : ")

	if allow_quit and description == "quit": return None

	tags = input("Tags (CSL) : ")

	if allow_quit and tags == "quit": return None

	he = HintEntry(primarytag,tags,description)

	DbgMsg("Exitting hint::AskForEntry")

	return he

# Add Hint
def Add(args,**kwargs):
	"""Add Hint"""

	DbgMsg("Entering hints::Add")

	he = None

	if len(args) > 0:
		he = HintEntry(args[0],args[1],args[2])
	else:
		he = AskForEntry(True)

	if he: he.Write()

	DbgMsg("Exitting hint::Add")

	return he

# Bulk Adds
def BulkAdd(args,**kwargs):
	"""Bulk Adds"""

	DbgMsg("Entering hints::BulkAdd")

	he = None

	hes = list()

	if len(args) > 0:
		for arg in args:
			he = HintEntry(arg[0],arg[1],arg[2])

			he.Write()

			hes.append(he)
	else:
		flag = True

		Msg("Type 'quit' when done")

		while flag:
			he = AskForEntry(True)

			if he:
				he.Write()
				hes.append(he)
			else:
				flag = False

	DbgMsg("Exitting hint::BulkAdd")

	return hes

# Delete Hint(s)
def Delete(args,**kwargs):
	"""Delete Hints from DB"""

	DbgMsg("Entering hints::Delete")

	cmd = "DELETE FROM hints where recordid = ?"

	result = None

	for arg in args:
		parameters = [ arg ]

		result = sql.Delete(cmd,parameters)

	DbgMsg("Exitting hint::Delete")

	return result

# Dump Hint DB
def Dump(args,**kwargs):
	"""Dump Database"""

	DbgMsg("Entering hints::Dump")

	noshow = kwargs.get("noshow",False)

	rows = sql.Select("SELECT * FROM hints")

	for row in rows:
		he = HintEntry()

		he.Read(row)

		if not noshow:
			Msg(f"{he.PrimaryTag}, {he.Description}, {he.Tags}, {he.RecordID}")

	DbgMsg("Exitting hint::Dump")

	return rows

# Search Hint DB
def Search(args,**kwargs):
	"""Search Hint File"""

	DbgMsg("Entering hints::Search")

	cmd = None
	records = list()
	noshow = kwargs.get("noshow",False)
	exact = kwargs.get("exact",False)
	all = kwargs.get("all",False)

	if not all:
		for arg in args:
			parameters = [ arg, arg, arg ]

			if exact:
				cmd = "SELECT * FROM hints where primarytag = ? or description = ? or tags = ?"
			else:
				cmd = "SELECT * FROM hints where primarytag like ? or description like ? or tags like ?"

			results = sql.Select(cmd,parameters)

			for result in results:
				records.append(result)
	else:
		cmd = "SELECT * FROM hints"

		results = sql.Select(cmd)

		for arg in args:
			exp = re.compile(arg)

			for row in results:
				flag = (exp.search(row[1]) or exp.search(row[2]) or exp.search(row[3]))

				if flag:
					records.append(row)

	if not noshow:
		for record in record:
			Msg(f"{record[0]}, {record[2]}, {record[3]}")

	DbgMsg("Exitting hint::Search")

	return records

# Set Hintfile/Location
def SetHintFile(fname=None):
	"""Set Hint File"""

	global HintURL

	if fname:
		HintURL = fname
	else:
		HintURL = __HintFile__

#
# Initialize Module
#
def Initialize():
	"""Initialize Module"""

	DbgMsg("Entering hints::Initialize")

	global Parser, Subcommands

	SetHintFile()

	Subcommands["add"] = Add
	Subcommands["bulk"] = BulkAdd
	Subcommands["del"] = Delete
	Subcommands["dump"] = Dump
	Subcommands["search"] = Search
	Subcommands["info"] = HintFileInfo

	choices = [ key for key in Subcommands.keys() ]

	Parser = parser = argparse.ArgumentParser(prog="Hints App",description="Hints App")

	parser.add_argument("--test",action="store_true",help="Enter test mode")
	parser.add_argument("-d","--debug",action="store_true",help="Enter debug mode")
	parser.add_argument("-e","--exact",action="store_true",help="Exact string search")
	parser.add_argument("--all",action="store_true",help="Return/Search all entries")
	parser.add_argument("-y","--yes",action="store_true",help="Always yes")
	parser.add_argument("--hint",help="Hint DB Url")
	parser.add_argument("cmd",choices=choices,nargs=1,help="Command")

	DbgMsg("Exitting hint::Initialize")

# Test Scaffolding
def Test():
	"""Test Scaffolding"""

	Msg("Entering Test Scaffolding")

	Msg("Does nothing ATM")

	Msg("Exitting Test Scaffolding")

# Parse Args
def ParseArgs():
	"""Parse Args"""

	DbgMsg("Entering hints::ParseArgs")

	global AutoYes, ExactStrings, HintURL

	args, unknowns = Parser.parse_known_args()

	AutoYes = args.yes
	ExactStrings = args.exact
	AllRecords = args.all

	if args.debug:
		DebugMode(True)
		DbgMsg("Debug mode turned on")

	if args.hint: SetHintFile(args.hint) # Can Directly set HintURL too

	if args.test:
		Test()

	DbgMsg("Exitting hint::ParseArgs")

	return args,unknowns

#
# Internal Init
#

Initialize()

#
# Main Loop
#

if __name__ == "__main__":
	# Parse Args
	args,unknowns = ParseArgs()

	CmdLineMode(True)

	OpenHintDB()

	subcmds = [ cmd for cmd in Subcommands.keys() ]

	cmd = ""

	if len(args.cmd) > 0:
		cmd = args.cmd[0]

	results = None

	if cmd in subcmds:
		f = Subcommands[cmd]

		if cmd == "info":
			results = f()
		else:
			results = f(unknowns,noshow=False,exact=ExactStrings,all=AllRecords)
	else:
		Msg(f"'{args.cmd}' is not recognized")

#
# Copyright (C) 2004 SIPfoundry Inc.
# Licensed by SIPfoundry under the GPL license.
#
# Copyright (C) 2004 SIP Forum
# Licensed to SIPfoundry under a Contributor Agreement.
#
#
# This file is part of SIP Forum Test Framework.
#
# SIP Forum Test Framework is free software; you can redistribute it 
# and/or modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation; either version 2 of the 
# License, or (at your option) any later version.
#
# SIP Forum Test Framework is distributed in the hope that it will 
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SIP Forum Test Framework; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# $Id: Contenttype.py,v 1.3 2004/03/19 18:38:44 lando Exp $
#
from HeaderFieldHandler import HeaderFieldHandler
from SCException import SCNotImplemented, HFHException

class Contenttype (HeaderFieldHandler):

	def __init__(self, value=None):
		HeaderFieldHandler.__init__(self)
		self.type = None
		self.subtype = None
		self.params = []
		if value is not None:
			self.parse(value)

	def __str__(self):
		return '[type:\'' + str(self.type) + '\', ' \
				+ 'subtype:\'' + str(self.subtype) + '\', ' \
				+ 'params:\'' + str(self.params) + '\']'

	def parse(self, value):
		v = value.replace("\r", "").replace("\t", "").strip()
		sep = v.find("/")
		if (sep != -1):
			self.type = v[:sep]
			st = v[sep+1:]
			sep = st.find(";")
			if (sep != -1):
				self.subtype = st[:sep].strip()
				pm = st[sep+1:]
				self.params = pm.split(";")
			else:
				self.subtype = st
		else:
			raise HFHException("ContentType", "parse", "failed to parse because seperator '/' missing")

	def create(self):
		ret = ''
		if self.type is not None:
			ret = str(self.type)
		if self.subtype is not None:
			ret = ret + '/' + str(self.subtype)
		for i in self.params:
			ret = ret + ';' + i
		return ret + '\r\n'

	def verify(self):
		raise SCNotImplemented("ContentType", "verify", "not implemented")

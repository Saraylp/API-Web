# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.dbservices.db_service import DBService

class GetFirstByFieldsPostService (IService):
	def __init__(self, core, parameters):
		super(GetFirstByFieldsPostService, self).__init__(core, parameters)
		self.core = core
		self.parameters = parameters
		
	def run(self):
		#TODO: Filters
		return DBService().getFirstByFields("Posts", self.parameters['fields'], {})
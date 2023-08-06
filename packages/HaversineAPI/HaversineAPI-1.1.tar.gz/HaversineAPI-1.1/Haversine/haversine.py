#!/usr/bin/env python3

# PYTHON_ARGCOMPLETE_OK

# pip3 install boto credstash Spanners Argumental

import os, re, sys, json, requests

from Spanners.Squirrel import Squirrel  # uses credstash, use your favourite password safe
from Argumental.Argue import Argue # decorator for command line calling, ./haversine.py -h

squirrel = Squirrel()
args = Argue() 


#________________________________________________________________________________________________
@args.command()
class Haversine(object):
	'''
	wrapper around the most excellent REST API for waypoints by joao @ haversine
	'''
	
	@args.property(default='https://haversine.com')
	def hostname(self): return
	
	@args.property(default='eddo888')
	def username(self): return
	
	@args.property(help='obtained from credstash, AWS dynamodb and crypto keys')
	def password(self):
		return squirrel.get(f'{self.username}@{self.hostname}')


#________________________________________________________________________________________________
@args.command(name='waypoints')
class Waypoints(Haversine):

	#____________________________________________________________________________________________
	@args.operation
	def list(self):
		'''
		return the full list of waypoints in json format
		'''
		url = f'{self.hostname}/webapi/waypoints'
		response = requests.get(url, auth=(self.username, self.password), verify=False)
		
		waypoints = []
		if response.status_code == 200:
			#json.dump(response.json(), sys.stdout,  indent='\t')
			waypoints = response.json()['waypoints']
			#for waypoint in waypoints:
			#	print(waypoint['id'], waypoint['description'])

		return waypoints
		
	#____________________________________________________________________________________________
	@args.operation
	@args.parameter(name='id', help='The point ID, max 7 chars')
	def get(self, id):
		'''
		get a single waypoint by id, todo
		'''
		waypoints = dict(map(lambda x: (x['id'], x), self.list()))
		if id in waypoints.keys():
			return waypoints[id]
		return
		
	#____________________________________________________________________________________________
	@args.operation
	@args.parameter(name='id', help='The point ID, max 7 chars')
	@args.parameter(name='description', help='The point description, max 63 chars')
	@args.parameter(name='latitude', type=float, help='y=DDD.DDDDDDD')
	@args.parameter(name='longitude', type=float, help='x=DDD.DDDDDDD')
	@args.parameter(name='elevation', short='e', type=float, help='EEEE.EEEE in feet', default=0.0)
	@args.parameter(name='update', flag=True, short='u', help='update instead of create')
	def create(self, id, description, latitude, longitude, elevation=0.0, update=False):
		'''
		create or update a single waypoint
		'''
		if update:
			url=f'{self.hostname}/webapi/waypoints/update/{id}'
		else:
			url=f'{self.hostname}/webapi/waypoints/new/{id}'
		print(url)
		
		response = requests.post(
			url, 
			auth=(self.username, self.password), 
			params=dict(
				description=description,
				latitude=latitude,
				longitude=longitude,
				elevation=elevation,
			), 
			verify=False
		)
		if response.status_code == 200:
			print(response.text)
			return True
		print(response, response.text)			
		return False

	#____________________________________________________________________________________________
	@args.operation
	@args.parameter(name='id', help='The point ID, max 7 chars')		
	def delete(self, id):
		''' 
		delete a single waypoint by id
		'''
		url=f'{self.hostname}/webapi/waypoints/delete/{id}'
		response = requests.post(
			url, 
			auth=(self.username, self.password), 
			params=dict(),
			verify=False
		)
		if response.status_code == 200:
			print(response.text)
			return True
		print(response, response.text)			
		return False		
		return

	
#________________________________________________________________________________________________
@args.command(name='routes')
class Routes(Haversine):

	#____________________________________________________________________________________________
	@args.operation
	def list(self):
		''' 
		get routes, bit broken at the moment
		'''
		url=f'{self.hostname}/webapi/routes'
		response = requests.get(url, auth=(self.username, self.password), verify=False)
		if response.status_code == 200:
			return response.text
		print(response, response.text)			
		return		

	
#________________________________________________________________________________________________
if __name__ == '__main__': 
	#args.parse(['waypoints','list'])
	#args.parse(['waypoints','create','-h'])
	#args.parse(['waypoints','create','0EDDO','daveedson','1.0','2.0'])
	#args.parse(['waypoints','create','-u','0EDDO',"dave edson",'2.0','3.0'])
	#args.parse(['waypoints','delete','0EDDO'])
	#args.parse(['waypoints','get','0EDDO'])
	#args.parse(['routes','list'])
	json.dump(args.execute(), sys.stdout, indent='\t')


import logging
from admin import ApiKey

class Auth():
	def validate_key(name, request):
		logging.info("validating request ")
		if 'api-key' in request.headers:
			api_key = request.headers.get('api-key')
			logging.info('api-key is' +  api_key)
			qAll = ApiKey.query(ApiKey.api_key == api_key)
			apiKeyEntity = qAll.get()
			logging.info("API key " + unicode(apiKeyEntity))
			if apiKeyEntity is None:
				return False
			return True
		else: 
			return False;	


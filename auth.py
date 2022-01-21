import logging
from google.cloud import datastore


class Auth():
    def validate_key(name, request):
        datastore_client = datastore.Client()

        logging.info("validating request ")
        if 'api-key' in request.headers:
            api_key = request.headers.get('api-key')
            logging.info('api-key is' + api_key)

            query = datastore_client.query(kind='ApiKey')
            query = query.add_filter('api_key', '=', api_key)

            apiKeyEntity = query.fetch()
            logging.info("API key " + str(apiKeyEntity))
            if apiKeyEntity is None:
                return False
            return True
        else:
            return False

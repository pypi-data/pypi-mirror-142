from zdynamodb.dynamo import DynamoDB
from boto3.dynamodb.conditions import Key
from zdynamodb import logger


class DynamoQueries:
    def __init__(self, table_name, connection_params=None):
        logger.info('[DynamoDB]: Initiating DynamoQueries Class')
        self.db = DynamoDB(connection_params)
        self.table_name = table_name
        self.table = self.db.connection.Table(table_name)

    def get_pk_context(self, pk, pk_value):
        try:
            response = self.table.query(KeyConditionExpression=Key(pk).eq(pk_value))
            model_data = response['Items']
            return model_data
        except Exception as e:
            logger.warning(f'[DynamoDB]: Unable to get data for {pk_value} from table {self.table_name}, e= {e}')
            raise e

    def get_index_context(self, index_key, index_value, index_name):
        try:
            response = self.table.query(IndexName=index_name, KeyConditionExpression=Key(index_key).eq(index_value))
            model_data = response['Items']
            return model_data
        except Exception as e:
            logger.warning(f'[DynamoDB]: Unable to get data for {index_value} from table {self.table_name}, e= {e}')
            raise e

from zdynamodb.dynamo import DynamoDB
from boto3.dynamodb.conditions import Key


class DynamoQueries:
    def __init__(self, table_name):
        self.db = DynamoDB()
        self.table = self.db.connection.Table(table_name)

    def get_pk_context(self, pk, pk_value, table_name):
        response = self.table.query(KeyConditionExpression=Key(pk).eq(pk_value))
        model_data = response['Items']
        return model_data

    def get_index_context(self, index_key, index_value, index_name, table_value):
        response = self.table.query(IndexName=index_name, KeyConditionExpression=Key(index_key).eq(index_value))
        model_data = response['Items']
        return model_data

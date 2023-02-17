from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Subscription:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.user_id = db_data['user_id']
        self.magazine_id = db_data['magazine_id'] 
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO subscriptions ( magazine_id, user_id, created_at , updated_at) " + 
                "VALUES (%(magazine_id)s, %(user_id)s, NOW(), NOW());")
        result = connectToMySQL('revistas_db').query_db(query, data)
        return result

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM subscriptions WHERE magazine_id = %(id)s;"
        return connectToMySQL('revistas_db').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM subscriptions WHERE magazine_id = %(magazine_id)s and user_id = %(user_id)s;"
        results = connectToMySQL('revistas_db').query_db(query, data)
        
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM subscriptions;"
        results = connectToMySQL('revistas_db').query_db(query)
        subscriptions = []
        for subscription in results:
            subscriptions.append(cls(subscription))
        return subscriptions

    # @classmethod
    # def get_subscriptions_num(cls, data):
    #     query = ("SELECT count(*) as num FROM thoughts "+
    #             "JOIN subscriptions ON thoughts.id = subscriptions.thought_id "+
    #             "where thoughts.id = %(id)s "+
    #             "order by subscriptions.id;")
    #     result = connectToMySQL('revistas_db').query_db(query, data)
    #     if not result:
    #         return 0
    #     return int(result[0]['num'])
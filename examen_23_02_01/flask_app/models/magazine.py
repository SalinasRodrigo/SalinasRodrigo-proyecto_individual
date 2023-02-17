from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import subscription

class Magazine:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.contents = db_data['contents']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user = None

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO magazines ( name, contents, user_id, created_at , updated_at) " + 
                "VALUES ( %(name)s, %(contents)s, %(user_id)s, NOW(), NOW());")
        result = connectToMySQL('revistas_db').query_db(query, data)
        return result

    @classmethod
    def destroy(cls,data):
        subscription.Subscription.destroy(data)
        query = "DELETE FROM magazines WHERE id = %(id)s;"
        return connectToMySQL('revistas_db').query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE magazines SET name=%(name)s, contents=%(contents)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('revistas_db').query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM magazines WHERE id = %(id)s;"
        print(query)
        results =  connectToMySQL('revistas_db').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_one_user_magazines(cls, data):
        query = ("SELECT * FROM magazines "+
                "LEFT JOIN users ON users.id = magazines.user_id "+
                "WHERE magazines.id = %(magazine_id)s;")
        results =  connectToMySQL('revistas_db').query_db(query, data)
        
        if not results:
            return results
        
        user_data = {
            "id" : results[0]["users.id"],
            "first_name" : results[0]["first_name"],
            "last_name" : results[0]["last_name"],
            "password" : results[0]["password"],
            "email" : results[0]["email"],
            "created_at" : results[0]["users.created_at"],
            "updated_at" : results[0]["users.updated_at"]
        }
        magazine = cls(results[0])
        magazine.user = user.User(user_data)
        return magazine

    @classmethod
    def get_all_by_user_id(cls, data):
        query = "SELECT * FROM magazines WHERE user_id=%(user_id)s;"
        results =  connectToMySQL('revistas_db').query_db(query, data)
        magazines = []
        for magazine in results:
            magazines.append(cls(magazine))
        return magazines

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM magazines;"
        results =  connectToMySQL('revistas_db').query_db(query)
        magazines = []
        for magazine in results:
            magazines.append(cls(magazine))
        return magazines

    @classmethod
    def get_all_user_magazines(cls):
        query = ("SELECT * FROM magazines "+
                "LEFT JOIN users ON users.id = magazines.user_id;")
        results =  connectToMySQL('revistas_db').query_db(query)
        magazines = []
        if not results:
            return results
        for row_db in results:
            user_data = {
                "id" : row_db["users.id"],
                "first_name" : row_db["first_name"],
                "last_name" : row_db["last_name"],
                "password" : row_db["password"],
                "email" : row_db["email"],
                "created_at" : row_db["users.created_at"],
                "updated_at" : row_db["users.updated_at"]
            }

            magazine = cls(row_db)
            magazine.user = user.User(user_data)
            magazines.append(magazine)
        return magazines

    def subs(self):
        query = ("SELECT * FROM magazines "+
                "LEFT JOIN subscriptions ON magazines.id = subscriptions.magazine_id "+
                "LEFT JOIN users ON users.id = subscriptions.user_id "+
                f"where magazines.id={self.id};")
        
        results =  connectToMySQL('revistas_db').query_db(query)

        subs = []

        for row_db in results:
            user_data = {
                "id" : row_db["users.id"],
                "first_name" : row_db["first_name"],
                "last_name" : row_db["last_name"],
                "password" : row_db["password"],
                "email" : row_db["email"],
                "created_at" : row_db["users.created_at"],
                "updated_at" : row_db["users.updated_at"]
            }

            subs.append(user.User(user_data))
        
        return subs

    def subnum(self):
        query = ("SELECT count(*) as num FROM magazines "+
                "JOIN subscriptions ON magazines.id = subscriptions.magazine_id "+
                f"WHERE magazines.id={self.id};")
        results =  connectToMySQL('revistas_db').query_db(query)
        
        return int(results[0]['num'])


    
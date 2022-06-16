from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask import flash
class User:
    # store the name of data base in DB ,here DB is a class variable and accessing it is done by cls.DB
    DB='dojo_survay_schema'
    #constructor function has to have all the info inside db and also should have same the name of form and prepared statement
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dojo_location = data['dojo_location']
        self.fav_language = data['fav_language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #CRUD
    #model create
    #create new USER by using query (insert) and the values by using prepared statemant
    @classmethod
    def create_new_user(cls,data):
        query="""INSERT INTO users (first_name,last_name,dojo_location,fav_language,comment)
        VALUES (%(first_name)s,%(last_name)s,%(dojo_location)s,%(fav_language)s,%(comment)s)
        ;"""
        result=connectToMySQL(cls.DB).query_db(query,data)#this will connect to db and insert the values in data base table
        return result

    #get the last element inserted into db
    @classmethod
    def get_each_user_with_info(cls):
        query = "SELECT * FROM users ORDER BY users.id DESC LIMIT 1;"
        result = connectToMySQL(cls.DB).query_db(query)
        return cls(result[0])


#static method for valdiation
    @staticmethod
    def validate_input(data):
        is_valid = True # we assume this is true
        if len(data['first_name']) < 3:
            flash("first_Name must be at least 3 or more characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("last_name must be at least 3 or more characters.")
            is_valid = False
        if not data['dojo_location']:
            flash("you should choose a location")
            is_valid = False
        #if nothing selected in select TAG so flash the message below
        if not data['fav_language']:
            flash("you should choose a language")
            is_valid = False
        if len(data['comment']) < 10:
            flash("comment must be at least 10 characters.")
            is_valid = False
        return is_valid
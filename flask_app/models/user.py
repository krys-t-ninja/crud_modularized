from flask_app.config.mysqlconnection import connectToMySQL

db= "users_cr4"


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    
    @classmethod
    def save(cls,data):
        query ="INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        user_id = connectToMySQL(db).query_db(query,data)
        return user_id            
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = results
        users = []
        for user in results:
            users.append(cls(user)) 
        return users
    # this took me a while , i kept getting an empty table.
    # I knew the save to add a new user links and method worked 
    # because it showed in the terminal and mysql database. 
    # The list  did not have anything to append to until i then added the 
    # name of list to equal the results
    # so  when i called the function in the route ,
    # it finally showed the table on the web page
    
    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id': user_id}
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(db).query_db(query,data)
        
    
    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM users WHERE id=%(id)s;"
        data = { 'id': user_id}
        return connectToMySQL(db).query_db(query,data)

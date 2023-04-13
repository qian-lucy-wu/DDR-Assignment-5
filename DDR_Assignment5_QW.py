#!/usr/bin/env python
# coding: utf-8

# ### Assignment 5: Extracting JSON Document from APIs

# In[221]:


pip install mysql-connector-python


# In[222]:


import mysql.connector
import warnings
import requests
import json
import codecs
from bs4 import BeautifulSoup


# ### 2. Extract the JSON corresponding to the first 100 contributors from this API.

# In[223]:


# To deal with the rate-limit of 60...
# Log into my Github account and generate a personal token:
# "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"


# In[224]:


token = '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'
headers = {'Authorization': 'token ' + token}


# In[225]:


# Hint: the variable name that handles the items per page is "per_page"
item_count = "?per_page=100"


# In[226]:


# Access API: the Apache Hadoop Github Repo's contributors’ endpoint
# fetch html and convert to json
api_url = "https://api.github.com/repos/apache/hadoop/contributors"


# In[227]:


# response_API = requests.get(api_url+ item_count, headers = headers)
# print(response_API.status_code)


# In[228]:


# Return a JSON object 
# jsonResponse = response_API.json()


# In[229]:


# Parse JSON object
# data = response_API.text
# parse_json = json.loads(data)


# In[262]:


# Hint: the API request is a GET request
page = requests.get(api_url+ item_count, headers = headers)
doc = BeautifulSoup(page.content, 'html.parser')

# The JSON function parses a valid JSON string and convert it into a Python Dictionary
json_dict = json.loads(str(doc))


# In[263]:


# View the JSON document
json_dict


# ### 3. For each of the 100 contributors extracted in (2), write code that accesses their user information

# In[231]:


# Initiate lists for storing info
login_list = []
id_list = []
info_list = []


# In[232]:


# Extract 'login' & 'id' key from JSON dictionary
for el in json_dict:
        
        login = el['login']
        id = el['id']
        url = el['url']
        
        login_list.append(login)
        id_list.append(id)
        info_list.append(url)


# In[233]:


# Check the length of created lists
print(len(login_list), len(id_list), len(info_list))


# In[234]:


print(login_list)


# In[235]:


# View the list of Github 'url's
print(id_list)


# In[236]:


print(info_list)


# In[237]:


# The following information are found under "url" of each contributor:
# "location", "email", "hireable", "bio", "twitter_username", 
# "public_repos", "public_gists", "followers", "following", "created_at" 

location_list = []
email_list = []
hireable_list = []
bio_list = []
twitter_username_list = []
public_repos_list = []
public_gists_list = []
followers_list = []
following_list = []
created_at_list = []


# In[238]:


# Write a for loop to go through the info_list:

for i in range(len(info_list)): 
    
    # Access the retrieved urls of Github contributors
    page = requests.get(info_list[i], headers = headers)
    doc = BeautifulSoup(page.content, 'html.parser')
    
    # Parse the JSON object into python dictionary
    json_dict = json.loads(str(doc))
    
    # Extract the following keys from JSON dictionary
    location = json_dict['location']
    email = json_dict['email']
    hireable = json_dict['hireable']
    bio = json_dict['bio']
    twitter_username = json_dict['twitter_username']
    public_repos = json_dict['public_repos']
    public_gists = json_dict['public_gists']
    followers = json_dict['followers']
    following = json_dict['following']
    created_at = json_dict['created_at']
    
    # Insert all the information into lists through every loop iteration
    location_list.append(location)
    email_list.append(email)
    hireable_list.append(hireable)
    bio_list.append(bio)
    twitter_username_list.append(twitter_username)
    public_repos_list.append(public_repos)
    public_gists_list.append(public_gists)
    followers_list.append(followers)
    following_list.append(following)
    created_at_list.append(created_at)


# In[239]:


# Check the length of created lists
print(len(location_list), 
      len(email_list), 
      len(hireable_list), 
      len(bio_list), 
      len(twitter_username_list), 
      len(public_repos_list), 
      len(public_gists_list), 
      len(followers_list), 
      len(following_list), 
      len(created_at_list))


# In[240]:


# "location" key
print(location_list)


# In[241]:


# "email" key
print(email_list)


# In[242]:


# "hireable" key
print(hireable_list)


# In[243]:


# "bio" key
print(bio_list)


# In[244]:


# "twitter_username" key
print(twitter_username_list)


# In[245]:


# "public_repos" key
print(public_repos_list)


# In[246]:


# "public_gists" key
print(public_gists_list)


# In[247]:


# "followers" key
print(followers_list)


# In[248]:


# "following" key
print(following_list)


# In[249]:


# "created_at" key
print(created_at_list)


# ### 4. Write code that creates an SQL database + table, and stores all the information obtained in (3) in it. 

# In[250]:


# ignore warnings
warnings.filterwarnings("ignore")


# In[251]:


# Give a name for a new database to be created
SQL_DB = "Github_DB"


# In[252]:


# To connect to server, enter your password in ''
conn = mysql.connector.connect(host='localhost', 
                               database='Github_DB',
                               user='root', 
                               password='') ## [enter password here to connect to MySQL]

cursor = conn.cursor()
print(cursor)


# In[253]:


# Give a name for the new table
SQL_TABLE_GITHUB = "GITHUB"

# Define the names and data types of each columns in the table
SQL_TABLE_GITHUB_DEF = "(" +             "_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY" +             ",login TEXT(50)" +             ",id INT" +             ",location VARCHAR(100)" +             ",email VARCHAR(50)" +             ",hireable VARCHAR(50)" +             ",bio VARCHAR(1000)" +             ",twitter_username VARCHAR(50)" +             ",public_repos INT" +             ",public_gists INT" +             ",followers INT" +             ",following INT" +             ",created_at VARCHAR(50)" +             ")"


#  "login", "id", "location", "email", "hireable", "bio", "twitter_username", "public_repos", "public_gists", "followers", "following", "created_at"

# ### Briefly justify your decisions.  What do you choose as Primary Key and why?

# As we see from the list print outs, "login", "location", email", "hireable", "bio", "twitter_username", "created_at" contain characters that should be stored as strings in MySQL. Note that "created_at" should not be treated as DATETIME because it does not follow the correct format, instead, it should be treated the same as other string content. Meanwhile, "public_repos", "public_gists",  "followers", "following" are numerical values that should be stored as integers in SQL database table.
# 
# I choose "_id" as primary key, because this is the inherent "id" generated in JSON documents. This is not decided by us when retrieving objects, and it is used to distinguish every entry/row from others. Note that in the code it didn't write "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY", because there is already a column named "id" that I want to insert into the SQL table. Thus, I wrote a different name for the two columns. 

# In[254]:


# Alternatively, create a function as below to execute the sql queries
# create_sql_table(SQL_TABLE_GITHUB, SQL_TABLE_GITHUB_DEF)

# Run the queries in SQL to create database and table
query1 = "CREATE DATABASE IF NOT EXISTS " + SQL_DB
print(query1)
cursor.execute(query1);
        
query2 = "CREATE TABLE IF NOT EXISTS " + SQL_DB + "." + SQL_TABLE_GITHUB + " " + SQL_TABLE_GITHUB_DEF + ";";
print(query2)
cursor.execute(query2);


# In[255]:


# api_url = "https://api.github.com/repos/apache/hadoop/contributors";
page = requests.get(api_url + item_count, headers = headers)
doc = BeautifulSoup(page.content, 'html.parser')
json_dict = json.loads(str(doc))


# In[256]:


# defines a parameterized SQL query that can be used to insert data into the "GITHUB" table
parameterized_stmt = "INSERT INTO " + SQL_TABLE_GITHUB + " (login, id, location, email, hireable, bio, twitter_username, public_repos, public_gists, followers, following, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"


#  "login", "id", "location", "email", "hireable", "bio", "twitter_username", "public_repos", "public_gists", "followers", "following", "created_at"

# In[257]:


# Write a for loop, extract 'login','id' and 'url' keys from JSON dictionary

for el in json_dict:
            
    login = el['login']
    id = el['id']
    url = el['url']

    # access url, obtain html content, and convert that to json document
    page = requests.get(url, headers = headers)
    doc = BeautifulSoup(page.content, 'html.parser')
    json_dict = json.loads(str(doc))


    # extract the following keys from dictionary
    location = json_dict['location']
    email = json_dict['email']
    hireable = json_dict['hireable']
    bio = json_dict['bio']
    twitter_username = json_dict['twitter_username']
    public_repos = json_dict['public_repos']
    public_gists = json_dict['public_gists']
    followers = json_dict['followers']
    following = json_dict['following']
    created_at = json_dict['created_at']
            
    # execute the query to store data in a SQL table
    cursor.execute(parameterized_stmt, (login, id, location, email, hireable, bio, twitter_username, public_repos, public_gists, followers, following, created_at))
    
conn.commit()   

# cursor.close()
# conn.close()


# ### Screenshot of the SQL database table

# ![Screen%20Shot%202023-02-18%20at%2017.24.03.png](attachment:Screen%20Shot%202023-02-18%20at%2017.24.03.png)

# ### 5. Optimize your code in (4) to allow for quick look-ups of "login", "location", and "hireable".  What choices do you make and why?

# Answer: I would use SQL Indexing to speed up the query look-ups. 
# 
# For example, write the following codes in Python to run SQL queries to create index in the target table Github_DB.GITHUB.

# In[264]:


# query = "Use Github_DB;"
query = "Use " + SQL_DB + ";"
print(query)
cursor.execute(query)


# In[268]:


# run queries to create index for the table

look_up_login = "CREATE INDEX idx_login ON GITHUB (login(50));"
print(look_up_login)
cursor.execute(look_up_login);
    
look_up_location = "CREATE INDEX idx_location ON GITHUB (location(50));"
print(look_up_location)
cursor.execute(look_up_location);   

look_up_hireable = "CREATE INDEX idx_hireable ON GITHUB (hireable(50));"
print(look_up_hireable)
cursor.execute(look_up_hireable);


# ### i.e., I would like, for example, to run the command  <<  SELECT * FROM table WHERE location = "Tokyo"  >>  fast.

# In[1]:


# Run similar sql queries as below to select rows based on filtering conditions of "login"/"location"/"hireable".


#     select_login = "SELECT * FROM GITHUB WHERE login is not null;"
# 
#     cursor.execute(select_login);
# 
# 
#     select_location = "SELECT * FROM GITHUB WHERE location = "Tokyo";"
# 
#     cursor.execute(select_location);  
# 
# 
#     select_hireable = "SELECT * FROM GITHUB WHERE hireable is not null;"
# 
#     cursor.execute(select_hireable); 

# In[279]:


# cursor.close()
# conn.close()


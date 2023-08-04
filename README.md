# API-Project

# T2A2 - API Webserver Project

#### [Github Repository](https://github.com/Patrick-Apilukpuvadol/API-Project)

#### [Trello Board](https://trello.com/invite/b/unih6lEL/ATTI3d6e43989909e7dbf9d9cc45ac5eabf15F178B57/api-project)

### R1	Identification of the problem you are trying to solve by building this particular app.

With the design of this app. I wanted to take a chance to try and establish an API that allows customers to booking holiday experiences within the one system. This system would allow Agents and tour guides to collaborate and create products that satisfy the customers needs. Customers would then have the convenience to choose the holiday they would like while being able to not be concerned about matters such as booking across multiple platforms to create an itinery 


### R2	Why is it a problem that needs solving?

This system would allow customers the opportunity to search for packages or experiences on 1 convenient web service.
Customers would be able to get in touch with agents which can connect them to a variety of tours/experiences provided by various tour guides. This webservice would be a great opportunity for agents and tour guides to work together to provide unique experiences that cater to customers needs. 

### R3	Why have you chosen this database system. What are the drawbacks compared to others?

The database management system that I'm utilising for this project is Postgres. As mentioned in my previous report. PostgreSQL is an open-source relational database management
system mainly known for its extensibility , powerful features , and support for complex data
types (structured and unstructured).

The following are potential drawbacks for Postgres. 

#### Slower Performance 
Due to Postgres being a relational database it reads from the first row and will search downwards until it can locate the result required. This as a result can affect performance speed especially in situations relating to larger commercial databases with extensive rows/columns.

#### Open Source
Postgres is an open sourced database management software which means that there is no one company that manages the version control and implementation of patches to the software. Although there are alot of communities that assist in developing and maintaining the software, this can cause inconsistencies in the version control which can affect the user friencly interfaces. 

#### High learning Curve
Postgres as a data management software has a very strict structure in the way data is organised and functions with a set of assumptions. All the data needs to serve a clear purpose and follows the schema so it is appropriately placed in the correct tables and rows. Finding support for specific matters can prove to be difficult due to the high learning curve which prevents simple searching for answers. 


### R4	Identify and discuss the key functionalities and benefits of an ORM

ORM is a programming technique that allows the integration of object oriented programming and Relational database management systems. It allows us to utilise the mapping of software objects into a relational database. ORM provides the following functionalities and benefits:

Ability to implement SQL queries
Object relational mapping allows programmers to use object - oriented language to create and query their databases. This allows the queries to be written in simpler methods on objects and gives developers more time to focus on improving the functionality of the code instead of being occupied with query specific issues. "Developers frequently employ ORM because of its simplicity in managing database queries. "(Tuama, 2022)

Reduction of development time and cost effective
Object relational mapping allowed a variety of methods to generate code that allowed portability to multiple database vendors. This gave developers alot more time to focus on the code instead of writing new lines of code to accommodate for database specific requirements. "SQL is a ridiculously powerful language, but most of us don’t write in it often. We do, however, tend to be much more fluent in one language or another and being able to leverage that fluency is awesome!" (Hoyos, 2019)

Cross Platform Support
Object Relational Mapping is supported across a large variety of platforms, programming languages and database management systems. This is really beneficial to developers due to portability and allowing them to improve the functionality of the code in their applications.

### R5	Document all endpoints for your API

#### Agent (auth_controller)

##### /register
HTTP METHOD - POST
No Authorisation required

###### Required Data
- First_Name (string) 
- Last_Name (string) 
- Email (string) - must be entered in valid email format
- Password (string) - encrypted with bcrypt before stored in database

###### Expected Response
- If it is successful, it will return Agent ID, First name, Last name, Contact Email and if they are admin status in JSON
- If duplicate email was added should display Integrity error along with error message.

- If the users email is not unique, an IntegrityError will be returned, accompanied with an error message.
- Validation error will be returned if fields are filled incorrectly with error message

##### /login
HTTP METHOD - POST
No Authorisation required

###### Required Data
- Email (string) - must be entered in valid email format
- Password (string) - encrypted with bcrypt before stored in database

###### Expected Response
- If the login is successful, it will return a message indicating this along with the First name, Last name, Contact email, JWT token and Is_admin status of agent.

#### Agent (agent_controller)

##### /agent
HTTP METHOD - GET
No Authorisation required

###### Required Data
None

###### Expected Response
- Successful request will display a list of all agents within the database and in JSON. Will be displayed in order

- agent_id
- first_name
- last_name
- contact_number
- contact_email
- emergency_contact
- password


##### /<int:agent_id>
HTTP METHOD - GET
No Authorisation required

###### Required Data
- agent_id (Integer)


###### Expected Response
- A Successful request will return the agent that matches the required data in JSON. Along with details such as first_name, last_name, contact_number, contact_email, emergency_contact.
- If unsuccessful will display error message


##### /agent
HTTP METHOD - POST
JWT required

###### Required Data
- agent_id (integer)
- first_name (string)
- last_name (string)
- contact_number (string)
- contact_email (string)
- emergency_contact (string)
- password (string)

###### Expected Response
- A successful request will create a new Agent with details provided and returned in JSON
- If unsuccessful will display error message

#### Customer (customer_controller)

##### /customer
HTTP METHOD - GET
No Authorisation required

###### Required Data
None

###### Expected Response
- Successful request will display a list of all customers within the database and in JSON. Will be displayed in order

- customer_id
- first_name
- last_name
- contact_number
- contact_email
- emergency_contact

##### /<int:customer_id>
HTTP METHOD - GET
No Authorisation required

###### Required Data
- customer_id (Integer)


###### Expected Response
- A Successful request will return the customer that matches the required data in JSON. Along with details such as first_name, last_name, contact_number, contact_email, emergency_contact.

##### /customer
HTTP METHOD - POST
JWT required

###### Required Data
- customer_id (integer)
- first_name (string)
- last_name (string)
- contact_number (string)
- contact_email (string)
- emergency_contact (string)


###### Expected Response
- A successful request will create a new Customer with details provided and returned in JSON

##### /<int:customer_id>
HTTP METHOD - DELETE
JWT required

###### Required Data
- customer_id (integer)


###### Expected Response
- A successful request will delete the Customer with matching customer_id provided along with confirmation message
- If unsuccessful will display error message

##### /<int:customer_id>
HTTP METHOD - PUT and PATCH
JWT required

###### Required Data
- customer_id (integer)


###### Expected Response
- A successful request will update the details of the Customer with matching customer_id provided along with confirmation message of update carried out
- If unsuccessful will display error message

#### Customer_tour_booking (customer_tour_booking_controllers)

##### /customer_tour_booking
HTTP METHOD - GET
No Authorisation required

###### Required Data
None

###### Expected Response
- Successful request will display a list of all customer tour bookings in order displayed in JSON

- customer_id
- first_name
- last_name
- contact_number
- contact_email
- tour_id

##### /<int:customer_id>
HTTP METHOD - GET
No Authorisation required

###### Required Data
- customer_id (Integer)


###### Expected Response
- A Successful request will return the customer tour booking that matches the required data in JSON. Along with details such as first_name, last_name, contact_number, contact_email, emergency_contact.


##### /<int:customer_id>
HTTP METHOD - DELETE
JWT required

###### Required Data
- customer_id (integer)


###### Expected Response
- A successful request will delete the Customer tour booking with matching customer_id provided along with confirmation message. 
- If unsuccessful will display error message

##### /<int:customer_id>
HTTP METHOD - PUT and PATCH
JWT required

###### Required Data
- customer_id (integer)


###### Expected Response
- A successful request will update the details of the Customer tour booking with matching customer_id provided along with confirmation message of update carried out
- If unsuccessful will display error message

#### Tour_group_log (tour_group_log_controllers)

##### /tour_group_log
HTTP METHOD - GET
No Authorisation required

###### Required Data
None

###### Expected Response
- Successful request will display a list of all tour group logs in order displayed in JSON

- tour_id
- customer_id
- agent_id
- duration
- activities
- booking_fee
- booking_id

##### /<int:tour_id>
HTTP METHOD - GET
No Authorisation required

###### Required Data
- tour_id (Integer)


###### Expected Response
- A Successful request will return the tour group log that matches the required data in JSON. Along with details such as customer_id, agent_id, duration, activities, booking_fee and booking_id.

##### /<int:tour_id>
HTTP METHOD - DELETE
JWT required

###### Required Data
- tour_id (integer)


###### Expected Response
- A successful request will delete the tour group log with matching tour_id provided along with confirmation message. 
- If unsuccessful will display error message


##### /<int:tour_id>
HTTP METHOD - PUT and PATCH
JWT required

###### Required Data
- tour_id (integer)


###### Expected Response
- A successful request will update the details of the tour group log with matching tour_id provided along with confirmation message of update carried out
- If unsuccessful will display error message


#### Tour_guide (tour_guide_controllers)

##### /tour_guide
HTTP METHOD - GET
No Authorisation required

###### Required Data
None

###### Expected Response
- Successful request will display a list of all tour guides in order displayed in JSON

- guide_id
- tour_id
- first_name
- last_name
- company_name
- emergency_contact


##### /<int:guide_id>
HTTP METHOD - GET
No Authorisation required

###### Required Data
- guide_id (Integer)


###### Expected Response
- A Successful request will return the tour guides that matches the required data in JSON. Along with details such as tour_id, first_name, last_name, company_name, emergency_contact.


##### /<int:tour_id>
HTTP METHOD - DELETE
JWT required

###### Required Data
- guide_id (integer)


###### Expected Response
- A successful request will delete the tour guide with matching guide_id provided along with confirmation message. 
- If unsuccessful will display error message

##### /<int:tour_id>
HTTP METHOD - PUT and PATCH
JWT required

###### Required Data
- guide_id (integer)


###### Expected Response
- A successful request will update the details of the guide with matching guide_id provided along with confirmation message of update carried out
- If unsuccessful will display error message

### R6	An ERD for your app
### R7	Detail any third party services that your app will use

#### Marshmallow
Marshmallow enables programmers to turn intricate data types into Python objects and the other way around. It supports custom serialisation and deserialization techniques as well as object validation and data normalisation.

#### JWT Token (JSON Web Token)
JSON Web Token (JWT) outlines a condensed and independent method for securely transferring data between parties as a JSON object. The header, payload, and signature are the three components that make up a JWT token. JWTs are extensively used and highly adaptable across a variety of computer languages and frameworks. Additionally, they can encode a number of claims such as issuer, subject, audience and expiration date.

#### Flask
Python-based Flask is a micro web framework that gives developers the tools, libraries, and technologies they need to create web applications like blogs, wikis, and calendars. Flask belongs to the micro-framework category, which typically has few to no dependencies on outside libraries and produces a lightweight framework. Every view function in Flask can use a global request object with the convenient name "request" that can be imported from the Flask package.

#### SQLAlchemy
With SQLAlchemy developers have access to a robust collection of tools through the use of the Python SQL toolkit and ORM (Object-Relational Mapping), SQLAlchemy, to interface with and manage databases. A schema metadata system, connection pooling, the SQL expression language, and query creation are some of the elements of the toolkit.

#### Psycopg2
The Python programming language has an adaptor called Psycopg2 that enables communication between Python code and PostgreSQL databases. Due to characteristics like thread safety, support for the most recent PostgreSQL features, and the capacity to handle enormous volumes of data, it is a well-liked option for database development.

#### Bcrypt
BCrypt is a password hashing mechanism. It is based on the Blowfish encryption algorithm, and since the salts and cost factors may be changed, it is a very flexible and secure way to store passwords. The slowness of BCrypt's hash mechanism makes brute force and dictionary attacks more challenging. It is supported by well-known web development frameworks and has become a widely used hashing function in several programming languages, including Python, Ruby, and PHP.

### R8	Describe your projects models in terms of the relationships they have with each other

AGENT MODEL

```py
class Agent(db.Model):
    __tablename__ = 'agent'
    
    agent_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    contact_number = db.Column(db.String)
    contact_email = db.Column(db.String, nullable=False, unique=True)
    emergency_contact = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String, nullable=False)
```
The Agent model is comprised of fields such as agent_id, first and last name, contact email, contact number, emergency contact, is_admin status and password

```py
class Tour_guide(db.Model):
    __tablename__ = 'tour_guide'
    
    guide_id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    company_name = db.Column(db.String)
    emergency_contact = db.Column(db.String)
```
The Tour_guide model is comprised of fields such as guide_id, tour_id (FK to link to tour_group_log model), first and last name, company_name and emergency contact.

```py
class Customer_tour_booking(db.Model):
    __tablename__ = 'customer_tour_booking'
    
    booking_id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    contact_number = db.Column(db.String)
    contact_email = db.Column(db.String)
```
The Customer_tour_booking model is comprised of fields such as booking_id, tour_id (FK to link to tour_group_log model), customer_id (FK to link to customer model), first and last name, contact number and contact email.

```py
class Tour_group_log(db.Model):
    __tablename__ = 'tour_group_log'
    
    tour_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('customer_tour_booking.booking_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.agent_id'), nullable=False)
    duration = db.Column(db.String)
    activities = db.Column(db.String)
    booking_fee = db.Column(db.Integer)
```
The Tour_group_log model is comprised of fields such as tour_id, booking_id (FK to link to customer_tour_booking model), agent_id (FK to link to agent model), duration, activities and booking_fee.

```py
class Customer(db.Model):
    __tablename__ = 'customer'
    
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    contact_number = db.Column(db.String)
    contact_email = db.Column(db.String, nullable=False, unique=True)
    emergency_contact = db.Column(db.String)
```
The Customer model is comprised of fields such as customer_id, first_name, last_name , contact_number, contact_email, emergency contact.

### R9	Discuss the database relations to be implemented in your application

For my project I have implemented the use of various PK to FK relations accross the database to ensure that all the information is appropriately linked via the different tables. 

I had to create a joining table (customer_tour_booking) that was used in the database with FK connections to bridge the connection of the Customers table and the tour_group_log table.

Each of the other tables such as agent, tour_guide, customer and tour_group_log were each designated a PK and FK to foster relationships and links between one another.

### R10	Describe the way tasks are allocated and tracked in your project

For this project I have been implementing the use of Trello which is a project management software that allows me to keep in tune and track of my existing tasks, allows me to add necessary tasks on the go when required. Trello employs a visual interface to arrange and rank tasks. Users can make boards, lists, and cards to represent various components of their work, and then drag and drop those items as necessary. 

It allows alot of flexibility for me to organise and prioritise my tasks. The software is free and simple to use which allows me more time to focus on the functionality of my code. 

REFERENCES

R4

Hoyos, M. (2019, March 22). What is an ORM and Why You Should Use it. Medium. https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a
(Hoyos, 2019)

Tuama, D. (2022, November 8). Object Relational Mapping: What is an ORM? - Code Institute Global. Code Institute Global. https://codeinstitute.net/global/blog/object-relational-mapping/
(Tuama, 2022)
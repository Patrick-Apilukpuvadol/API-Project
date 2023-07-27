# API-Project

### R1	Identification of the problem you are trying to solve by building this particular app.

With the design of this app. I wanted to take a chance to try and establish an API that allows customers to booking holiday experiences within the one system. This system would allow Agents and tour guides to collaborate and create products that satisfy the customers needs. Customers would then have the convenience to choose the holiday they would like while being able to not be concerned about matters such as booking across multiple platforms to create an itinery 


### R2	Why is it a problem that needs solving?
### R3	Why have you chosen this database system. What are the drawbacks compared to others?

### R4	Identify and discuss the key functionalities and benefits of an ORM

ORM is a programming technique that allows the integration of object oriented programming and Relational database management systems. It allows us to utilise the mapping of software objects into a relational database. ORM provides the following functionalities and benefits:

Ability to implement SQL queries
Object relational mapping allows programmers to use object - oriented language to create and query their databases. This allows the queries to be written in simpler methods on objects and gives developers more time to focus on improving the functionality of the code instead of being occupied with query specific issues. "Developers frequently employ ORM because of its simplicity in managing database queries. "(Tuama, 2022)

Reduction of development time and cost effective
Object relational mapping allowed a variety of methods to generate code that allowed portability to multiple database vendors. This gave developers alot more time to focus on the code instead of writing new lines of code to accommodate for database specific requirements. "SQL is a ridiculously powerful language, but most of us don’t write in it often. We do, however, tend to be much more fluent in one language or another and being able to leverage that fluency is awesome!" (Hoyos, 2019)

Cross Platform Support
Object Relational Mapping is supported across a large variety of platforms, programming languages and database management systems. This is really beneficial to developers due to portability and allowing them to improve the functionality of the code in their applications.

### R5	Document all endpoints for your API
### R6	An ERD for your app
### R7	Detail any third party services that your app will use
### R8	Describe your projects models in terms of the relationships they have with each other
### R9	Discuss the database relations to be implemented in your application

For my project I have implemented the use of various PK to FK relations accross the database to ensure that all the information is appropriately linked. 

I had to create another table (customer_tour_booking) that was used in the database with FK connections to bridge the connection of the Customers table and the tour_group_log table.

Each of the other tables such as agent, tour_guide, customer and tour_group_log were each designated a PK and FK to foster relationships and links between one another.

### R10	Describe the way tasks are allocated and tracked in your project

For this project I have been implementing the use of Trello which is a project management softwarte that allows me to keep in tune and track of my existing tasks, allows me to add necessary tasks on the go when required. 

It allows alot of flexibility for me to organise and prioritise my tasks. The software is free and simple to use which allows me more time to focus on the functionality of my code. 

REFERENCES

R4

Hoyos, M. (2019, March 22). What is an ORM and Why You Should Use it. Medium. https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a
(Hoyos, 2019)

Tuama, D. (2022, November 8). Object Relational Mapping: What is an ORM? - Code Institute Global. Code Institute Global. https://codeinstitute.net/global/blog/object-relational-mapping/
(Tuama, 2022)
from init import db, bcrypt
from flask import Blueprint
from models.agent import Agent, AgentSchema, agents_schema
from models.tour_guide import Tour_guide, Tour_guideSchema
from models.customer import Customer, CustomerSchema
from models.tour_group_log import Tour_group_log, Tour_group_logSchema
from models.customer_tour_booking import Customer_tour_booking, Customer_tour_bookingSchema


db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create') #command to create tables
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command('drop') #command to drop tables
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed') # command to seed tables
def seed_db():
    agents = [ #examples for agents
            Agent(
            agent_id='8',
            first_name='admin4',
            last_name="person",
            contact_number='0450987576',
            contact_email='adminp4@admin.com',
            password=bcrypt.generate_password_hash('admin1').decode('utf-8'),
            is_admin=True
            ),
            Agent(
            agent_id='9',
            first_name='not',
            last_name="admin4",
            contact_number='0430292918',
            contact_email='notadmin4@admin.com',
            password=bcrypt.generate_password_hash('notadmin1').decode('utf-8')
            ),
        ]

    db.session.add_all(agents)
    db.session.commit()
    
    customers = [ #examples for customers
        Customer(
        customer_id='6',
        first_name='Harrison',
        last_name='Ford',
        contact_number='0465789321',
        contact_email='indiana@jones.com',
        emergency_contact='0444999777'
        ),
        Customer(
        customer_id='7',
        first_name='Darth',
        last_name='Vader',
        contact_number='0452454636',
        contact_email='death@star.com',
        emergency_contact='0433123111'
        ),
        Customer(
        customer_id='8',
        first_name='Frodo',
        last_name='Baggins',
        contact_number='0400000456',
        contact_email='theone@ring.com',
        emergency_contact='0498765321'
        )
    ]
    
    db.session.add_all(customers)
    
    tour_guides = [ #examples for tour guides
        Tour_guide(
        guide_id='4',
        tour_id='4',
        first_name='Eikichi',
        last_name='Onizuka',
        company_name='Kresta',
        emergency_contact='0499999999'
        ),
        Tour_guide(
        guide_id='5',
        tour_id='5',
        first_name='Sebastian',
        last_name='Michaelis',
        company_name='Company',
        emergency_contact='0466666666'
        )
    ]
    
    db.session.add_all(tour_guides)
    
    tour_group_logs = [ #examples for tour group logs
        Tour_group_log(
            tour_id='6',
            booking_id='6',
            agent_id='8',
            duration='10Days',
            activities='Cruise',
            booking_fee='1350'
        ),
        Tour_group_log(
            tour_id='7',
            booking_id='7',
            agent_id='9',
            duration='6Days',
            activities='Hiking',
            booking_fee='590'
        )
    ]
    
    db.session.add_all(tour_group_logs)
    
    customer_tour_bookings = [ #examples for customer tour bookings
        Customer_tour_booking(
            booking_id='6',
            first_name='Harrison',
            last_name='Ford',
            contact_number='0465789321',
            contact_email='indiana@jones.com',
            tour_id='4'
        ),
        Customer_tour_booking(
            booking_id='7',
            first_name='Darth',
            last_name='Vader',
            contact_number='0452454636',
            contact_email='death@star.com',
            tour_id='5'
        )
    ]
    
    db.session.add_all(customer_tour_bookings)
    
    db.session.commit()
    
    print("Tables have been seeded.") # Printing confirmation that tables are seeded
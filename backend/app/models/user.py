from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum('admin', 'professional', 'customer'), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    
    service_type = db.Column(db.String(100), nullable=True)
    experience = db.Column(db.Integer, nullable=True)
    is_verified = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)



class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)  # Required, unique service name
    base_price = db.Column(db.Float, nullable=False)  # Required for service pricing
    time_required = db.Column(db.Integer, nullable=False)  # Required, defines service duration in minutes
    description = db.Column(db.Text, nullable=True)  # Optional, can provide more info about the service



class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)  # Required, must reference a service
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Required, must reference a customer
    professional_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # Optional, can be assigned later
    date_of_request = db.Column(db.DateTime, default=db.func.current_timestamp())  # Automatically set
    date_of_completion = db.Column(db.DateTime, nullable=True)  # Optional, only set if completed
    service_status = db.Column(db.Enum('requested', 'assigned', 'closed'), nullable=False)  # Required, to track status
    remarks = db.Column(db.Text, nullable=True)  # Optional, for notes or comments
    
    service = db.relationship('Service', backref=db.backref('requests', lazy=True))
    customer = db.relationship('User', foreign_keys=[customer_id], backref='service_requests')
    professional = db.relationship('User', foreign_keys=[professional_id], backref='assigned_requests')



class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_requests.id'), nullable=False)  # Required, must reference a service request
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Required, must reference a customer
    rating = db.Column(db.Integer, nullable=False)  # Required, rating must be given
    comments = db.Column(db.Text, nullable=True)  # Optional, comments can be provided by the customer
    
    service_request = db.relationship('ServiceRequest', backref=db.backref('reviews', lazy=True))
    customer = db.relationship('User', backref='reviews')

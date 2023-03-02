from organiser import db
# from dateutil.relativedelta import relativedelta
from dateutil import relativedelta


class Category(db.Model):
    """ schema for the Category model """
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name


class Task(db.Model):
    """ schema for the Task model """
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"


GENDER_CHOICES = (
    ('---','---'),
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('other','OTHER'),
    ('pnts','PNTS'),
)

class User(db.Model):
    """ schema for the User model """
    id = db.Column(db.Integer, primary_key=True)
    user_fname = db.Column(db.String(50), unique=True, nullable=False)
    user_lname = db.Column(db.String(10), unique=True, nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.String(50), unique=True, nullable=False)
    profession = db.Column(db.String(50), unique=True, nullable=False)
    in_house = db.Column(db.Boolean, default=False, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"{self.id} - User: {self.task_name} | In House: {self.in_house}"

    def __str__(self):
        today = date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)

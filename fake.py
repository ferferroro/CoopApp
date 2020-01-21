from main import app, db
from main.models.user import User
from main.models.company import Company
from main.models.sequence import Sequence
import uuid
from main.models.loan import Loan
from main.models.loan_detail import LoanDetail

from main.models.contribution import Contribution

from main.models.member import Member
from main.models.borrower import Borrower

app.config.from_object('config.HerokuProdConfig')

get_user = User.query.filter_by(username='dev').first()
if not get_user:
    dev_user = User(username='dev', password='dev', display_name='Developer')
    dev_user.uuid = str(uuid.uuid4()) 
    dev_user.hash_password(password=dev_user.password)
    db.session.add(dev_user)
    db.session.commit()

get_company = Company.query.first()
if not get_company:
    company = Company(
        company_name = 'Hello Cooperative',
        address = 'Novaliches Quezon City',
        phone = '1234-123',
        mobile = '09321234567',
        total_fund = 0,
        available_fund = 0,
        lended_fund = 0,
        total_profit = 0,
        interest_rate = 1.5
    )
    company.uuid = str(uuid.uuid4())
    db.session.add(company)
    db.session.commit()

get_sequence = Sequence.query.filter_by(name='Member').first()
if not get_sequence:
    sequence_member = Sequence(name='Member',prefix='MEMB', increment=1,current=1000)
    db.session.add(sequence_member)
    db.session.commit()

get_sequence = Sequence.query.filter_by(name='Borrower').first()
if not get_sequence:
    sequence_borrower = Sequence(name='Borrower',prefix='BORR', increment=1,current=1000)
    db.session.add(sequence_borrower)
    db.session.commit()

get_sequence = Sequence.query.filter_by(name='Loan').first()
if not get_sequence:
    sequence_loan = Sequence(name='Loan',prefix='Loan', increment=1,current=1000)
    db.session.add(sequence_loan)
    db.session.commit()

all_loans = Loan.query.all()
for record in all_loans:
    db.session.delete(record)
    db.session.commit()

all_loan_details = LoanDetail.query.all()
for record in all_loan_details:
    db.session.delete(record)
    db.session.commit()

all_contributions = Contribution.query.all()
for record in all_contributions:
    db.session.delete(record)
    db.session.commit()

all_members = Member.query.all()
for record in all_members:
    db.session.delete(record)
    db.session.commit()

all_borrowers = Borrower.query.all()
for record in all_borrowers:
    db.session.delete(record)
    db.session.commit()
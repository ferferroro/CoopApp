from app import db
from main.models.user import User
from main.models.company import Company
from main.models.sequence import Sequence
# import uuid

if not get_user := User.query.filter_by(username='dev').first():
    dev_user = User(username='dev', password='dev', display_name='Developer')
    # print(dev_user.password)    
    dev_user.hash_password(password=dev_user.password)
    # dev_user.uuid = str(uuid.uuid4())
    # print(dev_user.password, dev_user.check_password(password='devx'))
    db.session.add(dev_user)
    db.session.commit()

if not get_company := Company.query.first():
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
    # company.uuid = str(uuid.uuid4())
    db.session.add(company)
    db.session.commit()

if not get_sequence := Sequence.query.filter_by(name='Member').first():
    sequence_member = Sequence(name='Member',prefix='MEMB', increment=1,current=1000)
    db.session.add(sequence_member)
    db.session.commit()

if not get_sequence := Sequence.query.filter_by(name='Borrower').first():
    sequence_borrower = Sequence(name='Borrower',prefix='BORR', increment=1,current=1000)
    db.session.add(sequence_borrower)
    db.session.commit()

if not get_sequence := Sequence.query.filter_by(name='Loan').first():
    sequence_loan = Sequence(name='Loan',prefix='Loan', increment=1,current=1000)
    db.session.add(sequence_loan)
    db.session.commit()


# dev_user = User.query.first()
# db.session.delete(dev_user)
# db.session.commit()

# dev_comp = Company.query.first()
# db.session.delete(dev_comp)
# db.session.commit()
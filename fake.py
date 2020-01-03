from app import db
from main.models.user import User
from main.models.company import Company
# import uuid

dev_user = User(username='dev', password='dev', display_name='Developer')
# print(dev_user.password)    
dev_user.hash_password(password=dev_user.password)
# dev_user.uuid = str(uuid.uuid4())
# print(dev_user.password, dev_user.check_password(password='devx'))
db.session.add(dev_user)
db.session.commit()

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


# dev_user = User.query.first()
# db.session.delete(dev_user)
# db.session.commit()

# dev_comp = Company.query.first()
# db.session.delete(dev_comp)
# db.session.commit()
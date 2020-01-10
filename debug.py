# from datetime import datetime  
# from datetime import timedelta  
  
# #Add 1 day  
# print(datetime.now() + timedelta(days=14))


# import calendar
# print(calendar.monthrange(2019,1))
# print(calendar.monthrange(2020, 2)[1])


from app import db
from main.models.loan import Loan
from main.models.loan_detail import LoanDetail
from datetime import datetime, timedelta

all_loans = Loan.query.all()
all_loan_details = LoanDetail.query.all()

for loan in all_loans:
    print(loan.code, loan.terms, loan.type_schedule)
    # db.session.delete(loan)
    # db.session.commit()
    loan.is_approved = False
    db.session.commit()

    # running_date = loan.date_start
    # for i in range(0, loan.terms):
    #     running_date = running_date + timedelta(days=30)
    #     print(running_date)

# for loan_detail in all_loan_details:
#     print(loan_detail.loan_code, loan_detail.date_to_pay, loan_detail.amount_to_pay)
#     # db.session.delete(loan_detail)
#     # db.session.commit()
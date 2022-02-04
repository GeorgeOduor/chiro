from core.models import *
from clients.models import *
from django.db.models import Sum
from django.shortcuts import redirect

class LoanManager:
    lender_account = "001"

    def __init__(self):
        pass
    def createAccountNo(self, client_type="C"):
        client = tbl_Clients.objects.filter(ClientType = client_type)
        if client_type == 'C':
            if client.exists():
                last_account_created = client.values_list(
                    'AccountNumber').latest('CreatedOn')
                new_account = "00"+str(int(last_account_created[0])+1)
            else:
                new_account = "0018010000001"
        elif client_type == "S":
            if client.exists():
                last_account_created = client.values_list(
                    'AccountNumber').latest('CreatedOn')
                new_account = "00"+str(int(last_account_created[0])+1)
            else:
                new_account = "0017010000001"
        else:
            new_account = None
        return new_account

    def createProfile(self,client_id, client_type, **kwargs):
        client = tbl_Clients(
            user_id = client_id,
            mobile_no=kwargs['mobile_no'],
            ClientType = client_type,
            AccountNumber=self.createAccountNo(client_type=client_type)
        ).save()
        
    def updateProfile(self,client_type,**kwargs):
        client = tbl_Clients.objects.filter(user_id = client_id)
        client.update(
            user_id = client_id,
            first_name=kwargs['first_name'],
            last_name=kwargs['last_name'],
            mobile_no=kwargs['mobile_no'],
            national_id=kwargs['national_id'],
            gender=kwargs['gender'],
            date_of_birth=kwargs['date_of_birth'],
            AmountEligible=kwargs['AmountEligible'],
            BusinessName=kwargs['businessname'],
            ClientType = client_type,
            AccountNumber=self.createAccountNo(client_type=client_type))  

    def get_limit(self):
        client = tbl_Clients.objects.filter(id=self.cleintid).values(
            'AmountEligible')[0]['AmountEligible']
        return float(client)

    def loan_request(self,sp_id,**kwargs):
        interest = kwargs['amount'] * kwargs['interest_rate']
        charges = interest * kwargs['charge_rate']
        client = tbl_Clients.objects.all()
        transaction_account = tbl_Clients.objects.filter(
            id=self.cleintid).values_list('AccountNumber')[0][0]
#         service providers account_no
        service_provider_ac = client.filter(id=int(sp_id.lstrip("0"))).values('AccountNumber')[0]['AccountNumber']
#         return service_provider_ac
        #         save trx to transaction account
        amount_eligible = self.get_limit() - self.loan_balance()
        if kwargs['amount'] > amount_eligible:
            raise Exception(
                "Sorry amount you've requested is above your loan limit at the moment!")
        else:
            tbl_Transactions.objects.bulk_create([
                #                 debit the borowers loan account
                tbl_Transactions(AccountID=transaction_account, TransactionType='Debit',
                                 TrxNarration=kwargs['naration'], Amount=kwargs['amount'], TrxTypeID='TD',
                                 ClientType='C', ClientID=client.get(id=self.cleintid)),
                tbl_Transactions(AccountID=transaction_account, TransactionType='Debit', TrxNarration="Loan Interest charges",
                                 Amount=interest, TrxTypeID='TD', ClientType='C', ClientID=client.get(id=self.cleintid)),
                tbl_Transactions(AccountID=transaction_account, TransactionType='Debit', TrxNarration="Excise Duty",
                                 Amount=charges, TrxTypeID='TD', ClientType='C', ClientID=client.get(id=self.cleintid)),
                #                 credit supliers account
                tbl_Transactions(AccountID=service_provider_ac, TransactionType='Credit', TrxNarration="Item Purchase",
                                 Amount=kwargs['amount'], TrxTypeID='TC', ClientType='S', ClientID=client.get(id=self.cleintid)),
                #                 debit lenders account
                tbl_Transactions(AccountID=self.lender_account, TransactionType='Debit',
                                 TrxNarration=f"Loan Disbursed to {transaction_account}",
                                 Amount=charges, TrxTypeID='TD', ClientType='L',
                                 ClientID=client.get(id=self.cleintid)
                                 )
            ])

    def pay_loan(self, **kwargs):
        client = tbl_Clients.objects.all()
        transaction_account = tbl_Clients.objects.filter(
            id=kwargs['clientid']).values_list('AccountNumber')[0][0]
        loanbalance = self.loan_balance()
        if kwargs['amount'] > loanbalance:
            excess = kwargs['amount'] - loanbalance
            amount = loanbalance
        else:
            amount = kwargs['amount']
        tbl_Transactions(AccountID=transaction_account, TransactionType='Credit',
                         TrxNarration=kwargs['naration'], Amount=amount, TrxTypeID='TC',
                         ClientType='Client', ClientID=client.get(id=kwargs['clientid'])).save()

    def loan_balance(self):
        client = tbl_Clients.objects.all()
        transaction_account = tbl_Clients.objects.filter(
            id=self.cleintid).values_list('AccountNumber')[0][0]
        total_debit = tbl_Transactions.objects.filter(
            AccountID=transaction_account,
            TransactionType='Debit').aggregate(Sum('Amount'))['Amount__sum']
        total_credit = tbl_Transactions.objects.filter(
            AccountID=transaction_account,
            TransactionType='Credit').aggregate(Sum('Amount'))['Amount__sum']
        if total_credit is None:
            total_credit = 0
        if total_debit is None:
            total_debit = 0
        balance = float(total_debit - total_credit)
        return balance


# check profile complitenes

class checkProfile:

    def __init__(self) -> None:
        pass

    def checkProfile(client_type,client_id):
        clientinfo = tbl_Clients.objects.filter(user_id=client_id)
        available = sum([i is not None for i in clientinfo.values()[0].values()])
        completenes = round(available/15 * 100)
        if completenes < 85:
    #         notify
            redirect('core:profile_landing')
        else:
            if client_type == 'C':
    #             allow to make loans
                pass
            elif client_type == 'S':
                pass
    #         allow to confirm payments
            else:
                pass
    #         allow to view dashboards



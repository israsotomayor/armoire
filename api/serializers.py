from django.contrib.auth.models import User
from rest_framework import serializers

from billing.models import Company, Person, Product, Invoice, Table, Petition, Detail, ClosingCash, AccountingEntry, \
    History, Activity, ReceivableAccount, Rol, UserAccount, Fee, Setting


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'companyName', 'companyRuc', 'companyDescription', 'companyType', 'companyFirstFactureNumber',
                  'companyFirstFactureNumber1', 'companyFirstFactureNumber2')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'prFirstName', 'prLastName', 'prAddress', 'prEmail', 'prPhone', 'prIdentification', 'company')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'pdDescription', 'pdSalePrice', 'pdName', 'pdCode', 'pdBarcode', 'pdIvaState', 'pdStock',
                  'productState', 'company')


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'inSubtotal', 'inSubtotalIvazero', 'inSubtotalIva', 'inIva', 'inTotal', 'inChange', 'inCash',
                  'inAuthorizationDate', 'inIssueTime', 'inNumber', 'inDiscount', 'inIssueDate', 'inState',
                  'invoicePaymentMethod', 'inPetitionName', 'person', 'company')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'tableNumber', 'tableDetails', 'company')


class PetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petition
        fields = ('id', 'ptIssueDate', 'ptState', 'ptTotal', 'table', 'company')


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('id', 'detType', 'detDescription', 'detSalePrice', 'detQuantity', 'detTotal', 'detailDate', 'invoice',
                  'petition', 'product')


class ClosingCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosingCash
        fields = ('id', 'ccDateFrom', 'ccDateTo', 'ccInitialCashValue', 'ccTotalCash', 'ccTotalCheks',
                  'ccTotalCreditCard', 'ccTotalDebitCard', 'ccTotalInflow', 'closingCashTotalLeftOverMoney',
                  'closingCashTotalLackMoney', 'closingCashTotalCashierInflow', 'closingCashTotalCashierCheks',
                  'closingCashTotalCashierCreditCard', 'closingCashTotalCashierDebitCard', 'ccTotalOutflow',
                  'ccTotalReceivableAccounts', 'ccTotal', 'ccObservation', 'company')


class AccountingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingEntry
        fields = ('id', 'aeType', 'aeCreatedDate', 'aeDescription', 'aeValue', 'company')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'hisCreatedDate', 'hisType')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'actDescription', 'history')


class ReceivableAccountSerializer(serializers.ModelSerializer):
    class Meta:
        models = ReceivableAccount
        fields = ('id', 'receivableAccountDate', 'receivableAccountInterest', 'receivableAccountInvoiceNumber',
                  'receivableAccountAdvance', 'receivableAccountTotal', 'receivableAccountBalance',
                  'receivableAccountFee', 'receivableAccountState', 'person', 'company')


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        models = Rol
        fields = ('id', 'rolName')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserAccount
        fields = ('id', 'usrName', 'usrPassword', 'rol', 'person')


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = ('id', 'feeDate', 'feeValue', 'feeState', 'receivableAccount')


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ('id', 'FIRST_INVOICE_NUMBER', 'IVA_VALUE', 'SECOND_INVOICE_NUMBER', 'THIRD_INVOICE_NUMBER',
                  'ACCURACY_VALUE', 'AUTHORIZATION_NUMBER', 'SHOW_PRINT_PREVIEW', 'FACTURE_REPORT_SRC',
                  'COMPANY_TYPE', 'END_HOUR_JOURNEY', 'company')

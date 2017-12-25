from django.db import models


# Create your models here.
class Company(models.Model):
    companyName = models.CharField(max_length=150)
    companyRuc = models.CharField(max_length=15)
    companyDescription = models.TextField()
    companyType = models.CharField(max_length=100)
    companyFirstFactureNumber = models.IntegerField()
    companyFirstFactureNumber1 = models.IntegerField()
    companyFirstFactureNumber2 = models.IntegerField()

    def __str__(self):
        return self.companyName


class Person(models.Model):
    prFirstName = models.CharField(max_length=150)
    prLastName = models.CharField(max_length=150)
    prAddress = models.CharField(max_length=250)
    prEmail = models.CharField(max_length=150)
    prPhone = models.CharField(max_length=20)
    prIdentification = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Product(models.Model):
    pdDescription = models.CharField(max_length=200)
    pdSalePrice = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    pdName = models.CharField(max_length=150)
    pdCode = models.CharField(max_length=100)
    pdBarcode = models.CharField(max_length=150)
    pdIvaState = models.IntegerField()
    pdStock = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    productState = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Invoice(models.Model):
    inSubtotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inSubtotalIvazero = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inSubtotalIva = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inIva = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inTotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inChange = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inCash = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inAuthorizationDate = models.DateField()
    inIssueTime = models.DateTimeField()
    inNumber = models.CharField(max_length=200)
    inDiscount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    inIssueDate = models.DateField()
    inState = models.CharField(max_length=50)
    invoicePaymentMethod = models.CharField(max_length=50)
    inPetitionName = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Table(models.Model):
    tableNumber = models.IntegerField()
    tableDetails = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Petition(models.Model):
    ptIssueDate = models.DateTimeField()
    ptState = models.BooleanField(default=False)
    ptTotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Detail(models.Model):
    detType = models.CharField(max_length=50)
    detDescription = models.CharField(max_length=200)
    detSalePrice = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    detQuantity = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    detTotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    detailDate = models.DateField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ClosingCash(models.Model):
    ccDateFrom = models.DateField()
    ccDateTo = models.DateField()
    ccInitialCashValue = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotalCash = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotalCheks = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotalCreditCard = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotalDebitCard = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotalInflow = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    closingCashTotalLeftOverMoney = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    closingCashTotalLackMoney = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    closingCashTotalCashierInflow = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    closingCashTotalCashierCheks = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    closingCashTotalCashierCreditCard = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    closingCashTotalCashierDebitCard = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotalOutflow = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotalReceivableAccounts = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccTotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    ccObservation = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class AccountingEntry(models.Model):
    aeType = models.CharField(max_length=50)
    aeCreatedDate = models.DateField()
    aeDescription = models.CharField(max_length=200)
    aeValue = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class History(models.Model):
    hisCreatedDate = models.DateTimeField()
    hisType = models.CharField(max_length=100)


class Activity(models.Model):
    actDescription = models.CharField(max_length=200)
    history = models.ForeignKey(History, on_delete=models.CASCADE)


class ReceivableAccount(models.Model):
    receivableAccountDate = models.DateTimeField()
    receivableAccountInterest = models.IntegerField()
    receivableAccountInvoiceNumber = models.CharField(max_length=11)
    receivableAccountAdvance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    receivableAccountTotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    receivableAccountBalance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    receivableAccountFee = models.CharField(max_length=11)
    receivableAccountState = models.CharField(max_length=11)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Rol(models.Model):
    rolName = models.CharField(max_length=11)


class UserAccount(models.Model):
    usrName = models.CharField(max_length=50)
    usrPassword = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    person = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Fee(models.Model):
    feeDate = models.DateTimeField()
    feeValue = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    feeState = models.CharField(max_length=11)
    receivableAccount = models.ForeignKey(ReceivableAccount, on_delete=models.CASCADE)


class Setting(models.Model):
    FIRST_INVOICE_NUMBER = models.CharField(max_length=25)
    IVA_VALUE = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    SECOND_INVOICE_NUMBER = models.CharField(max_length=25)
    THIRD_INVOICE_NUMBER = models.CharField(max_length=25)
    ACCURACY_VALUE = models.IntegerField()
    AUTHORIZATION_NUMBER = models.CharField(max_length=25)
    SHOW_PRINT_PREVIEW = models.BooleanField(default=False)
    FACTURE_REPORT_SRC = models.CharField(max_length=250)
    COMPANY_TYPE = models.CharField(max_length=50)
    END_HOUR_JOURNEY = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

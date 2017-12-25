from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer, CompanySerializer, PersonSerializer, PetitionSerializer, TableSerializer, \
    InvoiceSerializer, ProductSerializer, DetailSerializer, ClosingCashSerializer, AccountingEntrySerializer, \
    HistorySerializer, ActivitySerializer, ReceivableAccountSerializer, RolSerializer, UserAccountSerializer, \
    FeeSerializer, SettingSerializer
from billing.models import Company, Person, Product, Petition, Table, Invoice, Detail, ClosingCash, AccountingEntry, \
    History, Activity, ReceivableAccount, Rol, UserAccount, Fee, Setting


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class PetitionViewSet(viewsets.ModelViewSet):
    queryset = Petition.objects.all()
    serializer_class = PetitionSerializer


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer


class ClosingCashViewSet(viewsets.ModelViewSet):
    queryset = ClosingCash.objects.all()
    serializer_class = ClosingCashSerializer


class AccountingEntryViewSet(viewsets.ModelViewSet):
    queryset = AccountingEntry.objects.all()
    serializer_class = AccountingEntrySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ReceivableAccountViewSet(viewsets.ModelViewSet):
    queryset = ReceivableAccount.objects.all()
    serializer_class = ReceivableAccountSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

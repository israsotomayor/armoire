# Serializers define the API representation.
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from api.viewsets import UserViewSet, CompanyViewSet, PersonViewSet, ProductViewSet, InvoiceViewSet, TableViewSet, \
    PetitionViewSet, DetailViewSet, ClosingCashViewSet, AccountingEntryViewSet, HistoryViewSet, ActivityViewSet, \
    ReceivableAccountViewSet, RolViewSet, UserAccountViewSet, FeeViewSet, SettingViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'products', ProductViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'tables', TableViewSet)
router.register(r'petitions', PetitionViewSet)
router.register(r'details', DetailViewSet)
router.register(r'closing-cashes', ClosingCashViewSet)
router.register(r'accounting-entries', AccountingEntryViewSet)
router.register(r'histories', HistoryViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'receivable-account', ReceivableAccountViewSet)
router.register(r'roles', RolViewSet)
router.register(r'user-accounts', UserAccountViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'settings', SettingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]


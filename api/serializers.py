from rest_framework import serializers
from api.models import Company, employee

# Create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id= serializers.ReadOnlyField()
    class Meta:
        model = Company 
        fields = "__all__"


class EnployeeSerialiser(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=employee
        fields = "__all__"
      
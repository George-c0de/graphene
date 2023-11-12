import graphene
from graphene_django.types import DjangoObjectType
from .models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        filter = '__all__'


class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)

    def resolve_all_cars(self, info):
        return Car.objects.all()


schema = graphene.Schema(query=Query)

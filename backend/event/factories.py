import factory
from faker import Faker
from .models import EventTag, AudienceType, Ticket

fake = Faker()


class EventTagFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: fake.unique.word())

    class Meta:
        model = EventTag


class AudienceTypeFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: fake.unique.word())

    class Meta:
        model = AudienceType


class TicketFactories(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: fake.unique.word())
    price = factory.Sequence(lambda n: n)

    class Meta:
        model = Ticket


# class RunSeed(factory.django.DjangoModelFactory):
#     EventTagFactory().create_batch(size=50)
#     AudienceTypeFactory().create_batch(size=50)
#     TicketFactories().create_batch(size=50)

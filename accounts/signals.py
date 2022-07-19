from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer

# remember to add ready func in apps.py and to add app class name in settings.py otherwise it will not work
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="customer")
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)
        print("Profile created")

post_save.connect(customer_profile, sender=User)
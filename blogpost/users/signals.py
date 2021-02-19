from django.db.models.signals import post_save # Tha action the we want to be performed after an object is saved
from django.contrib.auth.models import User # When an object of this model is saved, it sends a signal for the action to be taken
from django.dispatch import receiver # A function that receives the signal and performs some task
from .models import Profile


@receiver(post_save, sender=User) # When a user is created, send this signal(post_save)
# Thsi signal is then going to be received by this receiver decorator
def create_profile(sender,  instance, created, **kwargs):
    """
    Creates a profile for each newly created user
    sender: The model that a creation of an instance of it fires the signal for the action to be taken
    instance: The instance that was created
    created: Boolean value to represent whether the instance was created or not.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User) # When a user is saved, send this signal(post_save)
# Thsi signal is then going to be received by this receiver decorator
def save_profile(sender,  instance, **kwargs):
    """
    Saves a profile after its creation by the create_profile function
    sender: The model that a creation of an instance of it fires the signal for the action to be taken
    instance: The instance that was created(user instance).
    """
    instance.profile.save()
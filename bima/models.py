from django.db import models
import uuid

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Policy(models.Model):
    POLICY_TYPES = [
        ('auto', 'Auto Insurance'),
        ('health', 'Health Insurance'),
        ('home', 'Home Insurance'),
        # Add more policy types as needed
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=10, choices=POLICY_TYPES)
    policy_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client}: {self.policy_type} - {self.policy_number}"



class Reminder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    reminder_date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return f"Reminder for {self.client}: {self.policy}"

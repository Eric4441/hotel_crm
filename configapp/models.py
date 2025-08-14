from django.db import models

class room_type(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title
class room_size(models.Model):
    title=models.CharField(max_length=30)
    discription=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class employee(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    seria_id = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} {self.surname}"


class rooms(models.Model):
    title=models.CharField(max_length=32)
    id_room_size=models.ForeignKey(room_size,on_delete=models.CASCADE)
    price=models.IntegerField()
    id_room_type=models.ForeignKey(room_type,on_delete=models.CASCADE)
    id_employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
class users(models.Model):
    name=models.CharField(max_length=15)
    surname=models.CharField(max_length=15)
    seria_id=models.CharField(max_length=10)
    phone=models.CharField(max_length=15)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class deal(models.Model):
    id_user=models.ForeignKey(users,on_delete=models.CASCADE)
    id_room=models.ForeignKey(rooms,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    def __str__(self):
        return  f"{self.id_user} - {self.id_room} ({self.start_time})"








# Create your models here.

from django.db import models

VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)
# Create your models here.
class Movie(models.Model):
    Movie_id = models.CharField(max_length=20)
    Movie_name = models.CharField(max_length=200)
    Movie_year = models.CharField(max_length=50)
    genre = models.CharField(max_length=250)

    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']


    def __str__(self):
        return self.Movie_id

class Attend(models.Model):
    ATTN_Number = models.IntegerField()
    Movie_Name = models.TextField(max_length=20)
    Seat_Number = models.TextField(max_length=20)
    Show_Time = models.TextField(max_length=20)

    def __str__(self):
        return self.ATTN_Number



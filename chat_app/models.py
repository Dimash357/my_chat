from django.db import models

class Message(models.Model):
    room_name = models.CharField(max_length=255)  # Имя комнаты
    username = models.CharField(max_length=255)  # Имя пользователя
    content = models.TextField()                 # Текст сообщения
    timestamp = models.DateTimeField(auto_now_add=True)  # Время сообщения

    def __str__(self):
        return f"[{self.timestamp}] {self.username}: {self.content}"

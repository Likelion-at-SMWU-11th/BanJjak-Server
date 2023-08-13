from django.db import models
from users.models import User
from posts.models import Post
from founds.models import Found
from losts.models import Lost


class UserPostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.post}'


class UserFoundLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    found = models.ForeignKey(Found, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.found}'


class UserLostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lost = models.ForeignKey(Lost, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.lost}'

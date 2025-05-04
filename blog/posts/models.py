from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    full_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# a = Post(title='Преступление и наказание', full_text = 'Grose TEXT')
# a.save()

# for i in range(10):
#     Post.objects.create(
#         title=f'Преступление и наказание #{i + 1}',
#         full_text=f'Grose TEXT #{i + 1}',
#     )
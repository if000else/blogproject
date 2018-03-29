from django.test import TestCase

# Create your tests here.
from blog import models

models.Post.objects.create(
    title='测试文章',
    body='如果，爱能重来，你会不会愿意出现，在当初那个地点。',
    excerpt='没什么摘要',
    category_id=1,
)
print('success')
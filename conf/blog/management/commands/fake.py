from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
from blog.models import Post, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            Post.objects.create(
                title = fake.sentence(nb_words=10),
                content = fake.paragraph(nb_sentences=5),
                category = Category.objects.get(id=1),
                status = True,
                published_date = datetime.now()
            )
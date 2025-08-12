import django
import os
import random
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from faker import Faker
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Life_In_Words.settings")
django.setup()

from Life_Stories.models import MembershipPlan, UserMembership, Profile, Category, Series, Post, Tag, Comment

User = get_user_model()
fake = Faker()

# Create Membership Plans
def create_membership_plans():
    plans = [
        {"name": "Basic Monthly", "plan_type": "basic", "duration_type": "monthly", "price": 9.99},
        {"name": "Premium Monthly", "plan_type": "premium", "duration_type": "monthly", "price": 19.99},
        {"name": "Premium Yearly", "plan_type": "premium", "duration_type": "yearly", "price": 199.99},
    ]
    for plan in plans:
        MembershipPlan.objects.get_or_create(**plan)

# Create Users + Profile + Membership
def create_users(n=5):
    create_membership_plans()
    plans = list(MembershipPlan.objects.all())
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        user = User.objects.create_user(username=username, email=email, password='password123')
        
        profile = Profile.objects.create(
            user=user,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.msisdn()[:11],
            location=fake.city(),
            about=fake.text(),
        )

        UserMembership.objects.create(
            user=user,
            membdership=random.choice(plans),
            is_active=True,
            end_date=timezone.now() + timedelta(days=30)
        )

# Create Categories
def create_categories():
    categories = ['Web Dev', 'AI', 'Design', 'Marketing']
    for name in categories:
        Category.objects.get_or_create(name=name, slug=slugify(name))

# Create Series
def create_series():
    profiles = Profile.objects.all()
    for _ in range(3):
        Series.objects.create(
            title=fake.sentence(nb_words=3),
            description=fake.paragraph(),
            created_by=random.choice(profiles)
        )

# Create Posts
def create_posts():
    profiles = Profile.objects.all()
    categories = list(Category.objects.all())
    series = list(Series.objects.all())

    for _ in range(10):
        title = fake.sentence(nb_words=5)
        post = Post.objects.create(
            author=random.choice(profiles),
            title=title,
            content=fake.paragraph(nb_sentences=10),
            slug=slugify(title),
            category=random.choice(categories),
            series=random.choice(series),
            order=random.randint(1, 10),
            is_published=True,
            is_free=random.choice([True, False]),
        )

# Create Tags
def create_tags():
    posts = Post.objects.all()
    labels = ['Python', 'Django', 'Startup', 'ML', 'JavaScript']
    for label in labels:
        tag = Tag.objects.create(label=label)
        tag.post.set(random.sample(list(posts), k=3))  # attach to 3 posts

# Create Comments
def create_comments():
    posts = Post.objects.all()
    for _ in range(20):
        Comment.objects.create(
            post=random.choice(posts),
            name=fake.name(),
            comment=fake.sentence(),
            rating=random.choice(['5', '4', '3', '2', '1']),
        )


if __name__ == "__main__":
    create_users()
    create_categories()
    create_series()
    create_posts()
    create_tags()
    create_comments()
    print("✅ Database seeded with dummy data!")

from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from pages.models import Post


class AdminTest(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", email="admin@example.com", password="testpass123"
        )

        self.client = Client()
        self.client.login(username="admin", password="testpass123")

        self.post = Post.objects.create(
            name="Admin Post",
            about="Testing the admin",
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=open("media/uploads/test_image.jpeg", "rb").read(),
                content_type="image/jpeg",
            ),
        )

    def test_admin_page_accessible(self):
        url = reverse("admin:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_model_in_admin(self):
        url = reverse("admin:pages_post_change", args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Post")  # Check if post details are present

    # Add more admin-related tests as needed


class PostModelTest(TestCase):
    def setUp(self):
        image = SimpleUploadedFile(
            name="test_image.jpeg",
            content=open("media/uploads/test_image.jpeg", "rb").read(),
            content_type="image/jpeg",
        )
        Post.objects.create(name="Post Test", about="Hello World!", image=image)


class HomepageTests(TestCase):
    def test_homepage(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_homepage_templates(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")


class UserTest(TestCase):
    def test_create_new_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Derrell", email="derrell@email.com", password="testpassword123456"
        )
        self.assertEqual(user.username, "Derrell")
        self.assertEqual(user.email, "derrell@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

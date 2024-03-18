"""
Tests for models.
"""
from django.test import TestCase
# Best Practice
# get_user_model function nutzt IMMER das default user_model
# des Django Models - ändert es sich, wird der "neue Default geholt"
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_sucessful(self):
        """Test creating a user with an email is successful."""
        # example.com is reserved to Testing - especially when sending out real mails! ;-)
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

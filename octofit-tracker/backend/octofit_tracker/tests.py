from django.test import TestCase
from .models import Team, User, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        self.batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=self.spiderman, type='Running', duration=30)
        Leaderboard.objects.create(team=marvel, points=75)
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(name='Duplicate', email='spiderman@marvel.com', team=self.spiderman.team)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

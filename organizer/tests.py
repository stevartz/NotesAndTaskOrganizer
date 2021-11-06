from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from .models import Class, Assignment, Note, ClassForm, AssignmentForm, NoteForm
from django.contrib.auth import get_user_model

# Create your tests here.
class example_tests(TestCase):
    def example_test1(self):
        # setup (none for this one)
        # expected outcome
        expected = 2
        # run to get actual amount
        actual = 1+1
        self.assertEqual(expected, actual, msg="example test returned " + str(actual) + " instead of " + str(expected))

# Create your tests here.        
class ClassViewTests(TestCase):
    def test_past_classes(self):
        """
        Classes are displayed on assignments/notes page.
        """
        c = Class.objects.create(course_abbr='CS 3240', course_num='3240')
        response = self.client.get(reverse('organizer:assignments'))
        self.assertQuerysetEqual(
            response.context['latest_class_list'],
            [c],
        )

class NoteViewTests(TestCase):
    def test_past_notes(self):
        """
        Notes are displayed on assignments/notes page.
        """
        n = Note.objects.create(note_name='syllabus', for_class='CS 3240')
        response = self.client.get(reverse('organizer:assignments'))
        self.assertQuerysetEqual(
            response.context['notes'],
            [n],
        )

class AssignmentViewTests(TestCase):
    def test_past_assignments(self):
        """
        Assignments are displayed on assignments/notes page.
        """
        a = Assignment.objects.create(name='assign1', due_date='2021-10-28', description='testing assignment 1', for_class='CS 3240', checkbox=False, colorcode='green')
        response = self.client.get(reverse('organizer:assignments'))
        self.assertQuerysetEqual(
            response.context['assignments'],
            [a],
        )
    
class LoginTesets(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username='testuser')
        user.set_password('password1')
        user.save()

    def test_correct(self):
        c = Client()
        logged_in = c.login(username='testuser', password='password1')
        self.assertTrue(logged_in)

    def test_logout(self):
        c = Client()
        c.login(username='testuser', password='password1')
        User = get_user_model()
        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)
        c.logout()
        self.assertFalse(user.is_anonymous)
        
        
class TestAssignmentForm(SimpleTestCase):
    # def test_Assignment_form_valid_data(self):
    #     form = AssignmentForm(data={
    #         'name': 'Homework1',
    #         'due_date': '01-01-2021',
    #         'description': 'This is simple',
    #         'for_class': 'CS 3240',
    #         'checkbox': True,
    #         'colorcode': 'red'
    #     })
    #     self.assertTrue(form.is_valid())

    def test_Assignment_form_no_data(self):
        form = AssignmentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),5)

class TestClassForm(SimpleTestCase):

    def test_Class_form_valid_data(self):
        form = ClassForm(data={
            'course_abbr': 'STS',
            'course_num': '4600'
        })

        self.assertTrue(form.is_valid())


    def test_Class_form_no_data(self):
        form = ClassForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)



class TestNoteForm(SimpleTestCase):

    def test_Note_form_valid_data(self):
        form = NoteForm(data={
            'note_name': 'This is just an Intro',
            'for_class': 'STS 4600'
        })

        self.assertTrue(form.is_valid())


    def test_Class_form_no_data(self):
        form = NoteForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

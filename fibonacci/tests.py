from django.test import TestCase
from .models import Fibonacci
from .views import calculate_nth_fibonacci
from django.test import Client

# Create your tests here.
class FibonacciTest(TestCase):

  def create_fibonacci(self, position=0, value=1, frequency=1):
    return Fibonacci.objects.create(position=position, value=value, frequency=frequency)

  def test_create_fibonacci(self):
    fibonacci_obj = self.create_fibonacci()
    self.assertTrue(isinstance(fibonacci_obj, Fibonacci))
    self.assertEqual(fibonacci_obj.__str__(), str(fibonacci_obj.position))

  def test_calculate_nth_fibonacci(self):
  	fib_arr=[0,0]
  	calculate_nth_fibonacci(3, fib_arr)
  	self.assertEqual(fib_arr[0], 2)
  	calculate_nth_fibonacci(6, fib_arr)
  	self.assertEqual(fib_arr[0], 8)



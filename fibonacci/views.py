from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.db.models import F
from .models import Fibonacci
import json
import time

MOD = 1000000007

# Create your views here.
def index(request):
  fibonacci_stats = Fibonacci.objects.filter(frequency__gt=1).order_by('-frequency')
  context = {
    'fibonacci_stats': fibonacci_stats
  }
  return render(request, 'fibonacci/index.html', context)

def fibonacci(request):
  # data = {"status": "error", "messages": ["Error #1", "Error #2", "etc."]}
  # raise json.dumps(data)
  start_time = time.time()
  if request.method == 'POST':
    nth_position = request.POST['number']
    value_at_position = get_nth_fibonacci(nth_position)
    total_time = time.time() - start_time

    response_data = {}
    if value_at_position > 0:
      response_data['result'] = 'success'
      response_data['number'] = value_at_position
      response_data['time'] = total_time
      response_data['position'] = nth_position
    else:
      response_data['result'] = 'Number too big!'

    return HttpResponse(
      json.dumps(response_data),
      content_type="application/json"
    )
  else:
    return HttpResponse(
      json.dumps({"nothing to see": "this isn't happening"}),
      content_type="application/json"
    )

def get_nth_fibonacci(nth_position):
  nth_position = int(nth_position)
  try:
    number = Fibonacci.objects.get(position=nth_position).value
    # update frequency if exists
    Fibonacci.objects.filter(position=nth_position).update(frequency=F('frequency')+1)
  except Fibonacci.DoesNotExist:
    print "%s Not in db, adding..." % nth_position
    ans = [0, 0]
    calculate_nth_fibonacci(nth_position, ans)
    number = ans[0]
    # create new entery if the number is queried first time
    Fibonacci(position=nth_position, value=number, frequency=1).save()
  except OverflowError as e:
    return -1

  return number

def calculate_nth_fibonacci(n, ans=[]):
  if(n == 0):
    ans[0], ans[1] = 0, 1
    return
  calculate_nth_fibonacci((n/2), ans)
  a, b = ans
  c = 2*b - a
  if(c < 0):
    c += MOD;
  c = (a * c) % MOD
  d = (a*a + b*b) % MOD
  if(n%2 == 0):
    ans[0], ans[1] = c, d
  else:
    ans[0], ans[1] = d, c+d

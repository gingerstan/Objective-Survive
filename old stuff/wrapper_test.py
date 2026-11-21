import inspect
from python_event_bus import EventBus

# print(inspect.getsource(EventBus.call))
# print(inspect.getsource(EventBus.on))


# def allow_call(state):
#   def allow_call(func):
#     def inner():
#       if state == "hi":
#         a = func()
#         print("dog")
#       else:
#         a = "loser!"
#       return a
#     return inner
#   return allow_call


# @allow_call("hi")
# @EventBus.on("left")
# def left_click():
#   return 12


# print(left_click())


# EventBus.call("left")




# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(1)
# def myfunction():
#   return "Hello Linus"

# print(myfunction())

def changecase(func):
  print("upper")
  def myinner2():
    return func().upper()
  print(myinner2())
  return myinner2

def addgreeting(func):
  print("greeting")
  def myinner1():
    return "Hello " + func() + " Have a good day!"
  print(myinner1())
  return myinner1

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
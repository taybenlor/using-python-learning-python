print('Have you done any programming before?')
print('1: I have done a lot of programming')
print('2: I have done some programming')
print('3: I have never done programming')

experience = input('Enter number: ')

# If they don't have any experience
# We want them to do our getting started activity
if experience == '3':
  print()
  print("That's totally fine. This course doesn't require experience.")
  print('Please start your lesson with this activity:')
  print('realwebsite.code/starting-python')
  exit()

# Now we know they have done programming in the past
# Check if they have done Python before
done_python_answer = input('Have you done python programming? ')

# If they have not done Python
# They should learn the syntax of Python first
if 'n' in done_python_answer.lower():
  print()
  print('Okay, you should start with a lesson on Python Syntax!')
  print('Please do this activity:')
  print('realwebsite.code/python-syntax')
  exit()


# From now on they know Python
print("Okay! Lets check where you're up to.")
print()

# They have some experience, lets see how experienced
if experience == '2':
  # Check if they know variables with input
  print()
  print("name = input('What is your name? ')")
  print("print('Hello', name)")
  print()

  print('If I run this program and type in Julia, what will the program print out?')
  var_answer = input('Answer: ')
  if var_answer.replace(' ', '').lower() == 'hellojulia':
    print()
    print('Great!')
    print()
  else:
    print()
    print('Okay, it will help if you practice variables!')
    print('Do this activity:')
    print('realwebsite.code/variables')
    exit()

  # Continue testing like this...
  # If they get everything right, 
  # it will fall through to the experienced tests

# From now on they have either said they are experienced
# Or they have passed all the tests before

# Check if they have done functions
print()
print('I want to make a function that turns minutes into seconds.')
print('There are 60 seconds in a minute, so we need to multiply the minutes by 60.')
print('Fill in this code:')
print()
print('def minutes_to_seconds(minutes):')
function_body = input()

result = 0
try:
  exec(f'''
def minutes_to_seconds(minutes):
  {function_body}
result = minutes_to_seconds(5)
''')
except:
  pass

if result == 5 * 60:
  print()
  print('Great!')
  print()
else:
  print()
  print('It looks like you should practice functions.')
  print('Do this activity:')
  print('realwebsite.code/functions')
  exit()

# Check if they have done loops
recursion_example = open('recursion.py').read()
print(recursion_example)
recursion_answer = input('What is this an example of? ')
if 'recurs' not in recursion_answer.lower():
  print()
  print('You should learn more about recursion!')
  print('Do this activity:')
  print('realwebsite.code/recursion')
  exit()

print()
print('You should work on a project')
print('Start here:')
print('realwebsite.code/project')



class Node:
 def __init__(self, data):
  self.data = data
  self.next = None
class Stack_structure:
 def __init__(self):
  self.head = None
def push_val(self, data):
 if self.head is None:
  self.head = Node(data)
 else:
  newNode = Node(data)
  newNode.next = self.head
 self.head = newNode
def pop_val(self):
 if self.head is None:
  return None
 else:
  del_Val = self.head.data
 self.head = self.head.next
 return del_Val
my_instance = Stack_structure()
while True:
 print('push <value>')
 print('pop')
 print('quit')
 my_input = input('What action would you like to perform ? ').split()
 operation = my_input[0].strip().lower()
 if operation == 'push':
  my_instance.push_val(int(my_input[1]))
 elif operation == 'pop':
  del_Val = my_instance.pop_val()
 if del_Val is None:
  print('The stack is empty.')
 else:
  print('The deleted value is : ', int(del_Val))
   elif operation == 'quit':
  break
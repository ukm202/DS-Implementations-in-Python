
# Node Class

class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
# Linked List

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert_at_the_begining(self,data):
    node = Node(data,self.head)
    self.head = node

  def print(self):
    if self.head is None:
      print("Linked List is empty.\n")
      return
    itr = self.head
    llstr = ""
    while itr:
      llstr = llstr + str(itr.data) + "-->"
      itr = itr.next
    print(llstr,"\n")
  
  def insert_at_the_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return

    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data, None)

  def insert_list_values(self, values):
    for value in values:
      self.insert_at_the_end(value)
  
  def get_length(self):
    count = 0
    
    itr = self.head
    while itr:
      count+=1
      itr = itr.next

    return count

  def remove_at(self, index):
    if index < 0 or index >= self.get_length():
      raise Exception("Invalid index!\n")

    if index == 0:
      self.head = self.head.next
      return

    itr = self.head
    idxCount = 0

    while itr:
      
      
      if idxCount == index - 1:
        itr.next = itr.next.next
        break
      itr = itr.next
      idxCount+=1
  def insert_at(self, data, pos):

    if pos < 0 or pos > self.get_length():
      raise Exception("Invalid index!")
    if pos == 0:
      self.insert_at_the_begining(data)
      return
    
    itr = self.head
    count = 0

    while itr:
      if count == pos - 1:
        node = Node(data, itr.next)
        itr.next = node
        break

      itr = itr.next
      count+=1

  def insert_after_value(self, data_after, data_to_insert):

    itr = self.head
    while itr:
      if itr.data == data_after:
        node = Node(data_to_insert, itr.next)
        itr.next = node
        break
      itr = itr.next

  def remove_by_value(self, data):

    itr = self.head
    count = 0

    while itr:
      if itr.data == data:
        print(count, "adsad \n")
        self.remove_at(count)
        break
      itr = itr.next
      count+=1


    
    
      
      
if __name__ == "__main__":
  ll = LinkedList()

  ll.insert_at_the_end(4)

  ll.insert_at_the_begining(3)
  ll.insert_at_the_begining(2)
  ll.insert_at_the_begining(1)

  ll.insert_at_the_end(5)

  values = ["banana", "mango", "orange", 9,8,7]
  ll.insert_list_values(values)
  ll.print()
  count = ll.get_length()
  print(f"Linked List length: {count}\n")

  # ll.remove_at(0)
  ll.remove_at(3)



  ll.print()
  count = ll.get_length()
  print(f"Linked List length: {count}\n")

  ll.insert_at("Suraj", 0)
  ll.insert_at("Chandan", 11)

  ll.insert_at("Uttam",1)
  ll.insert_at("Priti",4)

  ll.print()
  count = ll.get_length()
  print(f"Linked List length: {count}\n")

  ll.insert_after_value("Suraj","Ujwal")
  ll.insert_after_value("Priti","Jyoti")
  ll.insert_after_value("Chandan","Mishra")


  ll.print()
  count = ll.get_length()
  print(f"Linked List length: {count}\n")

  ll.remove_by_value("Mishra")
  ll.remove_by_value("Uttam")

  ll.print()
  count = ll.get_length()
  print(f"Linked List length: {count}\n")
        


        








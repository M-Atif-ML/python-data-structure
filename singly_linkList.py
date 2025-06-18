class Node:
	def __init__(self,data=None,next = None):
		self.data= data
		self.next= next
class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_begining(self,data):
		node = Node(data,self.head)
		self.head = node

	def print(self):
		if self.head is None:
			print("Linked list is empty")
			return -1

		itr = self.head
		listr = ""
		while itr:
			listr += str(itr.data) + "--->"
			itr= itr.next
		print(listr)

	def insert_at_end(self,data):
		if self.head is None:
			self.head= Node(data,None)
			return

		self.tail = None
		self.newNode = Node(data,self.tail)

		itr = self.head
		while True:
			
			if itr.next == None:
				
				itr.next = self.newNode
				break
			itr = itr.next
	def insert_values(self,data_list):
		self.head = None

		for i in range(len(data_list)):
			self.insert_at_end(data_list[i])

	def get_length(self):
		count = 0

		itr = self.head
		while itr:
			itr = itr.next
			count+=1
		return count

	def remove_node(self,index):
		if index < 0 or index >= self.get_length():
			raise Exception("Segmentation fault")
		count = 0

		if index == 0:
			self.head = self.head.next
		itr =self.head

		while itr:
			if count == index -1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count+=1

	def insert_at(self,index,data):
		if index  < 0 or index >= self.get_length():
			raise Exception("Segmentation fault")
		if index == 0:
			self.insert_at_begining(data)
			return 

		count = 0
		itr = self.head 

		while itr:
			if count == index-1:
				node = Node(data,itr.next)
				itr.next = node
				break
			itr = itr.next
			count+=1

	def insert_by_value(self,data_after,data):
		isFound = False

		itr = self.head

		while itr:
			
			if itr.data == data_after:
				node = Node(data,itr.next)
				itr.next = node
				isFound = True
				break
			itr = itr.next
		if isFound == False:
			raise Exception(f"Could not found {data_after} in your linklist")
	def remove_by_value(self,data):
		itr = self.head
		ind = 0 
		isFound = False
		while itr:
			if itr.data == data:
				self.remove_node(ind)
				isFound = True
				break
			ind += 1
			itr = itr.next
		if isFound == False:
			raise Exception(f"Could not found {data} in your linklist")

l = LinkedList()
l.insert_at_begining(23)
l.insert_at_begining(4)
l.insert_at_begining(98)
l.insert_at_begining(-12)
l.remove_by_value(-12)
l.print()
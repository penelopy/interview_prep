#From Danielle's tech talk

class Node(object):

	def __init__(self, value, next):
		"""Create a node for a linked list"""
		self.value = value
		self.next = next


class LinkedList(object):

	def __init__(self):
		"""Create a linked list"""

		# initialize the list with a first node that has .value and .next = None
		self.first_node = Node(None, None)

		# initialize node with reference to last node set to the first_node
		self.last_node = self.first_node

		# initialize the size of the linked list to 0, since first node is None
		self.size = 0


	#####################
	#     ADD NODES     #
	#####################

	def append(self, value):
		"""Add a new node to the list.  Like .append"""
		node = Node(value, None)

		# check if this node is the first node in the list
		if self.first_node.value == None:
			# set first node and last node to equal the new node
			self.first_node = node
			self.last_node = node
		else:
			# set next node in the list to equal the new node
			self.last_node.next = node
			# reassign last_node to this new node
			self.last_node = node

		# increment the list size
		self.size += 1

	def extend(self, value_list):
		"""Add a list of value to the linked list. Create a node for each datum"""
		for value in value_list:
			self.append(value)


	#####################
	#   REMOVE NODES    #
	#####################

	def remove(self, value):
		"""Remove a node from the linked list"""

		# check if the linked list has ANY nodes
		if self.size == 0:
			pass

		# initialize variables to track list traversal and removed status
		current_node = self.first_node # start at the beginning
		removed = False

		# If node being removed is the first node
		if value == current_node.value:
			# Is there only one node in the whole list?
			if current_node == self.last_node:
				# remove node .value and .next
				# could alternatively write self.first_node = Node(None, None)
				self.first_node.value = None
				self.first_node.next = None

				# set last_node to equal updated first_node
				self.last_node = self.first_node
			else:
				# update the first_node to equal what was the second
				self.first_node = current_node.next

			# update removed to reflect status of removed node
			removed = True

		# Loop through the linked list to find the node to delete
		while True:

			# check to see if current_node contains anything
			if current_node == None:
				break

			# check for match in next node (current_node starts at first_node)
			next_node = current_node.next
			if next_node != None: # don't check if there isn't a next node
				if value == next_node.value:
					# match found. 

					#is next_node the last_node? i.e. will you remove last_node?
					if next_node == self.last_node:
						# update last_node
						self.last_node = current_node
					else:
						# Redirect current_node's pointer to next_node.next
						current_node.next = next_node.next

					# update next_node and status of removed
					next_node = None
					removed = True

					# break loop since node was removed
					break

			# update current_node for next loop
			current_node = current_node.next

		# update size if a node was removed
		if removed:
			self.size -= 1

	def remove_list(self, value_list):
		"""Remove several nodes"""
		for value in value_list:
			self.remove(value)


	#####################
	#      HELPERS      #
	#####################

	def contains(self, value):
		"""Check if linked list contains a certain value"""

		# start with first node
		current_node = self.first_node

		# loop through list for value match
		while current_node != None:
			if current_node.value == value:
				return True
			else:
				# update position in list
				current_node = current_node.next

		return False

	def get_index(self, value):
		"""Get the index of a certain value in the list using .size"""

		# start with the first node
		current_node = self.first_node
		index = 0

		# loop through node for value match
		while current_node != None:
			if current_node.value == value:
				return index
			else:
				# update current_node and increment index
				current_node = current_node.next
				index += 1

		# if value does not exist in list
		return -1

	def get_value_at_index(self, index):
		"""Get the value of the node at the given index position"""

		# check if list has any nodes
		if self.size == 0:
			pass

		# check for index out of range
		if index >= self.size:
			pass

		# start with the first node, set position to 0
		current_node = self.first_node
		position = 0

		# loop through nodes for index and position match
		while current_node != None:
			if position == index:
				return current_node.value
			else:
				# update current_node to next node and increment position
				current_node = current_node.next
				position += 1

		return None






def main():
	# create list
	linked_list = LinkedList() 
	print linked_list

	# create a node!  Testing the Node class
	new_node = Node("first", None)
	print new_node.value

	# add new_node to linked_list (pass only the value!)
	linked_list.append(new_node.value)

	# add a node to linked_list --> .append takes only a value!
	linked_list.append("second")

	print "Testing the attributes: "
	print "linked_list.first_node.value = ", linked_list.first_node.value
	print "linked_list.first_node.next.value = ", linked_list.first_node.next.value
	print "linked_list.last_node.value = ", linked_list.last_node.value
	print "linked_list.size = ", linked_list.size

	print "Testing .append and .extend to add values."
	linked_list.append("third")
	linked_list.extend(["fourth", "fifth", "sixth"])
	print "Size: ", linked_list.size # 6

	print "Testing .get_index: "
	print "Index of 'first': ", linked_list.get_index("first") # 0
	print "Index of 'fourth': ", linked_list.get_index("fourth") # 3

	print "Testing .contains: "
	print "Contains 'second'? ", linked_list.contains("second") # True
	print "Contains the number 2? ", linked_list.contains(2) # False

	print "Testing .remove: "
	linked_list.remove("second")
	print "Removed second."
	print "Contains 'second'? ", linked_list.contains("second") # False
	print "New size: ", linked_list.size # 5

	print "Testing .next.next: "
	print linked_list.first_node.next.value
	print linked_list.first_node.next.next.value
	
	linked_list.remove("fourth")
	print "Contains fourth ", linked_list.contains("fourth") # False

	print "Testing .get_value_at_index: "
	print linked_list.get_value_at_index(0) # "first"
	print linked_list.get_value_at_index(1) # "third"
	print linked_list.get_value_at_index(2) # "fifth"

	linked_list2 = LinkedList()
	linked_list2.append("something")
	print linked_list2.get_value_at_index(2) # None due to out of range



if __name__=="__main__":
	main()





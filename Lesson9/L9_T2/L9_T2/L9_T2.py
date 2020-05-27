class Stack(list):
	#stc_ is used to mark original or chaged methods of Stack obj

	def stc_is_ismpty(self):
		return self == []
	
	def stc_get_size(self):
		return len(self)
	
	def _last_idx(self):
		return self.stc_get_size() - 1

	def stc_push(self, something):
		self.append(something)
	
	def stc_pop(self):
		return self.pop()

	def stc_top(self):
		return self[self._last_idx()]



my_stack = Stack([1,2,3,4,5,6])

print(my_stack)
print(my_stack.stc_is_ismpty())

my_stack.stc_push(7)
print(my_stack)

print(my_stack.stc_top())
print(my_stack.stc_pop())
print(my_stack)

print(my_stack.stc_get_size())
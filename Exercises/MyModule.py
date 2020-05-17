class ListKeeper:
 
	dictionary = dict()
    
	def __init__(self):
        self.dictionary['example'] = [1, 2, 3, 4, 5]
  
    def show(self):
        return self.dictionary.keys()
  
	def add(self, key, list):
        self.dictionary[key] = list
   
	def delete(self, key):
        self.dictionary.pop(key)
   
	def sort(self, key):
        self.dictionary[key].sort()
   
	def append(self, key, list):
		self.dictionary[key].extend(list)
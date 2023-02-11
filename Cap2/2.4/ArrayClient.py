import Array
maxSize = 14                    # Max size of the array
arr = Array.Array(maxSize)      # Create an array object

arr.insert(77)                  # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)
# agregamos nuevos elementos
arr.insert("bar")
arr.insert(77)
arr.insert("baz")
arr.insert(55)

print("Array containing", len(arr), "items")
arr.traverse()

#print("Search for 12 returns", arr.search(12))

#print("Search for 12.34 returns", arr.search(12.34))

#print("Deleting 0 returns", arr.delete(0))
#print("Deleting 17 returns", arr.delete(17))

#print("Setting item at index 3 to 33")
#arr.set(3, 33)

#print("Array after deletions has", len(arr), "items")
#arr.traverse()

#llamamos a removeDupes(). Imprime la matriz antes y después de eliminar duplicados para verificar que funcione correctamente.
print("Array before removing duplicates:")
arr.traverse()
arr.removeDupes()
print("Array after removing duplicates:")
arr.traverse()

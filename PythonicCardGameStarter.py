color_queue.put('red')
color_queue.put('green')
color_queue.put('blue')

# Dequeue colors
print(color_queue.get())  # Output: 'red'
print(color_queue.get())  # Output: 'green'

print(color_queue.get())

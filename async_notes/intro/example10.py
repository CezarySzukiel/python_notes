from asyncio import Future

my_future = Future()  # Feature to mój paragon na kebaba

print(f'Is my_future done? {my_future.done()}')

my_future.set_result(42), # ustawia wynik na 42 i oznacza, że future jest zakończony, w js to resolve

print(f'Is my_future done? {my_future.done()}')
print(f'What is the result of my_future? {my_future.result()}')
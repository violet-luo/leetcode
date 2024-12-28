class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.snake = collections.deque([(0,0)])
        self.snake_set = set([(0, 0)])
        self.food = collections.deque(food)
        self.score = 0
        
    def move(self, direction: str) -> int:
        mapping = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        head = self.snake[0]
        move = mapping[direction]
        new_head = (head[0] + move[0], head[1] + move[1])

        # check if outbound
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1
        
        # check if snake bits itself: if it overlaps with any part of the snake's body except for the tail
        if new_head in self.snake_set and new_head != self.snake[-1]:
            return -1

        # check if snake eats food
        if self.food and self.food[0] == list(new_head): # food is stored as list while head is tuple
            self.food.popleft()
            self.score += 1
        else:
            tail = self.snake.pop()
            self.snake_set.remove(tail)
        
        self.snake.appendleft(new_head)
        self.snake_set.add(new_head)
        
        return self.score

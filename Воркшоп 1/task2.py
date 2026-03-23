def sort_stack(stack):

    add_stack = []
    
    while stack:
        current = stack.pop()
        
        while add_stack and add_stack[-1] > current:
            stack.append(add_stack.pop())
        
        add_stack.append(current)
    
    while add_stack:
        stack.append(add_stack.pop())
    
    return stack

# Пример использования:
if __name__ == "__main__":
    stack = [3, 1, 4, 2]
    print(f"Исходный стек: {stack[::-1]}")
    
    sorted_stack = sort_stack(stack)
    print(f"Отсортированный стек: {sorted_stack[::-1]}")
class Stack:
    """
    최대 크기가 10으로 제한된 스택(Stack) 구조를 구현하는 클래스입니다.
    """
    MAX_SIZE = 10

    def __init__(self):
        """
        스택의 내용을 저장할 리스트를 초기화합니다.
        """
        self._items = []

    def push(self, item):
        """
        스택에 새로운 원소를 추가합니다. (최대 10개)
        """
        if len(self._items) < self.MAX_SIZE:
            self._items.append(item)
            print(f"PUSH: '{item}'이(가) 스택에 추가되었습니다.")
        else:
            print(f"경고: 스택이 가득 찼습니다. ({self.MAX_SIZE}개 제한)")

    def pop(self):
        """
        스택에서 가장 마지막에 추가된 원소를 제거하고 반환합니다.
        """
        if not self.empty():
            item = self._items.pop()
            print(f"POP: '{item}'을(를) 스택에서 제거하고 반환합니다.")
            return item
        else:
            print("경고: 스택이 비어 있어 가져올 내용이 없습니다.")
            return None

    def empty(self):
        """
        스택이 비어있는지 확인합니다. (True/False 반환)
        """
        return len(self._items) == 0

    def peek(self):
        """
        가장 마지막 원소를 삭제하지 않고 내용만 확인합니다.
        """
        if not self.empty():
            item = self._items[-1]
            print(f"PEEK: 가장 위 내용: '{item}'")
            return item
        else:
            print("경고: 스택이 비어 있어 확인할 내용이 없습니다.")
            return None


# ----------------------------------------
# 스택 구조 동작 확인
# ----------------------------------------
if __name__ == '__main__':
    my_stack = Stack()
    
    print("--- 1. 내용 입력 및 스택 채우기 ---")
    
    # 10개 원소 추가 (정상적인 push)
    for i in range(1, 11):
        # 고유한 번호(i)를 붙여서 스택 동작 확인
        item_data = f'내용_{i:02d}'
        my_stack.push(item_data)
        
    print("\n--- 2. 용량 초과 경고 확인 ---")
    
    # 11번째 원소 추가 (용량 초과 경고 발생)
    my_stack.push('추가_내용_11')

    print("\n--- 3. 마지막 내용 확인 (peek) ---")
    # 마지막 내용 확인 (삭제 안 함)
    my_stack.peek()
    print(f"스택이 비었는지 확인 (empty): {my_stack.empty()}")

    print("\n--- 4. 마지막 내용 가져오기 (pop) ---")
    
    # 가장 마지막에 추가된 내용 (내용_10) 가져오기
    item_popped_1 = my_stack.pop()
    
    # 다시 peek()로 확인하여 내용_10이 제거되고 내용_09가 최상단인지 확인
    my_stack.peek()
    
    # 가장 마지막에 추가된 내용 (내용_09) 가져오기
    item_popped_2 = my_stack.pop()

    print("\n--- 5. 스택 내용 전부 가져오기 및 비어있을 때 경고 확인 ---")
    
    # 남은 8개 원소 전부 pop
    while not my_stack.empty():
        my_stack.pop()
        
    print(f"\n스택이 비었는지 확인 (empty): {my_stack.empty()}")
    
    # 스택이 비어 있을 때 pop 시도 (경고 발생)
    my_stack.pop()
    
    # 스택이 비어 있을 때 peek 시도 (경고 발생)
    my_stack.peek()
class BinarySearchTree:
    """
    이진 탐색 트리(Binary Search Tree)를 구현하는 클래스입니다.
    """

    class _Node:
        """
        트리 노드를 위한 내부 클래스입니다.
        """
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        BinarySearchTree 클래스의 생성자입니다.
        """
        self.root = None

    # ----------------------------------------
    # 원소 추가 함수 (insert)
    # ----------------------------------------

    def insert(self, data):
        """
        트리에 새로운 원소를 추가합니다.
        """
        if self.root is None:
            self.root = self._Node(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = self._Node(data)
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = self._Node(data)
                    return
                current = current.right
            else:
                # 중복 값은 삽입하지 않음
                return

    # ----------------------------------------
    # 원소 탐색 함수 (find)
    # ----------------------------------------

    def find(self, data):
        """
        트리에서 원하는 값의 존재 유무를 확인합니다.
        """
        current = self.root
        while current is not None:
            if data == current.data:
                return current.data
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    # ----------------------------------------
    # 특정 원소 삭제 함수 (delete)
    # ----------------------------------------

    def _find_min(self, node):
        """
        주어진 노드 서브트리에서 가장 작은 값(가장 왼쪽 노드)을 찾고 반환합니다.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursively(self, current, data):
        """
        삭제 연산을 수행하는 재귀 헬퍼 함수입니다.
        """
        if current is None:
            return current

        if data < current.data:
            current.left = self._delete_recursively(current.left, data)
        elif data > current.data:
            current.right = self._delete_recursively(current.right, data)
        else:
            # 삭제할 노드를 찾았을 때

            # 1. 자식 노드가 없거나 하나만 있을 경우
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # 2. 자식 노드가 둘 다 있을 경우
            # 오른쪽 서브트리에서 가장 작은 값(successor)을 찾아 대체합니다.
            successor = self._find_min(current.right)
            current.data = successor.data
            current.right = self._delete_recursively(current.right, successor.data)

        return current

    def delete(self, data):
        """
        트리에서 특정 원소를 삭제합니다.
        """
        self.root = self._delete_recursively(self.root, data)


# ----------------------------------------
# 테스트 및 사용 예제
# ----------------------------------------
if __name__ == '__main__':
    # binarytree라는 이름으로 인스턴스 생성 (요청사항 준수)
    binarytree = BinarySearchTree()

    # 원소 추가 (insert)
    print('--- 원소 추가 (insert) ---')
    elements_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for el in elements_to_insert:
        binarytree.insert(el)
        print(f'Inserted: {el}')

    # 원소 탐색 (find)
    print('\n--- 원소 탐색 (find) ---')
    print(f'Find 40: {binarytree.find(40)}')
    print(f'Find 99: {binarytree.find(99)}')

    # 원소 삭제 (delete)
    print('\n--- 원소 삭제 (delete) ---')

    # 잎 노드 삭제 (20)
    binarytree.delete(20)
    print(f'Delete 20: Find 20 -> {binarytree.find(20)}')

    # 자식이 하나인 노드 삭제 (70)
    binarytree.delete(70)
    print(f'Delete 70: Find 70 -> {binarytree.find(70)}')
class B:
    """문서화 테스트를 위한 임시 클래스
    """
    def __init__(self, b: int):
        # 클래스 생성자
        # :param a: 생성자 파라미터
        # a = A(10)
        
        self.b = b
    def print_value(self):
        # """ 멤버변수 a를 출력하는 메소드
        # >>> A(10).print_value()
        # 10
        # """
        print(self.b)
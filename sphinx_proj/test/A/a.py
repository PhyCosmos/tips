"""
https://hooni-playground.com/1101/
====================================
 :mod:`a` 모듈 a
====================================
.. moduleauthor:: hooni <hooni@hoo.ni>
.. note:: LGPLv3

설명
=====

이 모듈은 문서화 테스트를 위한 모듈입니다.

Revision History
-------------------

 * [2021/04/23] - 모듈 작성
"""

class A:
    """문서화 테스트를 위한 임시 클래스
    """
    def __init__(self, a: int):
        # """ 클래스 생성자

        # :param a: 생성자 파라미터

        # >>> a = A(10)
        # """
        self.a = a

    def print_value(self):
        # """ 멤버변수 a를 출력하는 메소드

        # >>> A(10).print_value()
        # 10
        # """
        print(self.a)
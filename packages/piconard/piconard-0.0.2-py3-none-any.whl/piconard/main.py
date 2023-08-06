"""
Create Date : 2021/11/07
Auther :madscientist

Test pypi
command
>poetry config repositories.testpypi https://test.pypi.org/legacy/

"""
class set_gpio:
    def __init__(self,arg1,arg2):
        self.A0  = 14
        self.A1  = 15
        self.A2  = 16
        self.A3  = 17
        self.A4  = 18
        self.A5  = 19
        self.D0  = 0
        self.D1  = 1
        self.D2  = 2
        self.D3  = 3
        self.D4  = 4
        self.D5  = 5
        self.D6  = 6
        self.D7  = 7
        self.D8  = 8
        self.D9  = 9
        self.D10 = 10
        self.D11 = 11
        self.D12 = 12
        self.D13 = 13

        if(arg1 == "rpi3" and arg2 == "1.0.0"):
            self.A0  = 4
            self.A1  = 5
            self.A2  = 6
            self.A3  = 12
            self.A4  = 2
            self.A5  = 3
            self.D0  = 15
            self.D1  = 14
            self.D2  = 17
            self.D3  = 18
            self.D4  = 7
            self.D5  = 27
            self.D6  = 22
            self.D7  = 23
            self.D8  = 24
            self.D9  = 25
            self.D10 = 8
            self.D11 = 10
            self.D12 = 9
            self.D13 = 11



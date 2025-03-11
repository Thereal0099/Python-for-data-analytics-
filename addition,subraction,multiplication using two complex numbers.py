#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

if __name__ == "__main__":
    c1 = Complex(2, 3)
    c2 = Complex(1, 4)
    result_add = c1 + c2
    print(f"Addition: {result_add}")
    result_sub = c1 - c2
    print(f"Subtraction: {result_sub}")
    result_mull = c1 * c2
    print(f"Multiplication: {result_mull}")


# In[ ]:





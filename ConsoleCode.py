Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> z = [2.0, 1.0, 0.l]
SyntaxError: invalid syntax
>>> z = np.array([2.0, 1.0, 0.l])
SyntaxError: invalid syntax
>>> z = [2.0,1.0,0.1]
>>> exp = [np.exp(i) for i in z]
>>> exp
[7.38905609893065, 2.718281828459045, 1.1051709180756477]
>>> sumExp = sum(emp)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sumExp = sum(emp)
NameError: name 'emp' is not defined
>>> sumExp = sum(exp)
>>> sumExp
11.212508845465344
>>> softmax = [j/sumExp for j in z]
>>> softmax
[0.1783722115687656, 0.0891861057843828, 0.00891861057843828]
>>> softmax = [j/sumExp for j in exp]
>>> softmax
[0.6590011388859679, 0.2424329707047139, 0.09856589040931818]
>>> sum(softmax)
1.0
>>> a = ['hello', 'hi', 'python', 'bye']
>>> "python" in a
True
>>> eval('12+3')
15
>>> eval('12' + '+' + '20')
32
>>> import scholarly
>>> scholarly.search_pubs_query("Refibrillation managed by EMT-Ds: incidence and outcome without paramedic back-up")
<generator object _search_scholar_soup at 0x000001C1E3C3E0A0>
>>> x = scholarly.search_pubs_query("Refibrillation managed by EMT-Ds: incidence and outcome without paramedic back-up")
>>> y  = next(x).fill()
>>> y.citedby
16
>>> x = np.array([1,2,3,4])
>>> y = np.array([5,6,7,8])
>>> np.meshgrid(x,y)
[array([[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]]), array([[5, 5, 5, 5],
       [6, 6, 6, 6],
       [7, 7, 7, 7],
       [8, 8, 8, 8]])]
>>> xx,yy = np.meshgrid(x,y)
>>> xx
array([[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]])
>>> yy
array([[5, 5, 5, 5],
       [6, 6, 6, 6],
       [7, 7, 7, 7],
       [8, 8, 8, 8]])
>>> np.arange(1,20)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19])
>>> np.arange(1,20, 0.1)
array([ 1. ,  1.1,  1.2,  1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9,  2. ,
        2.1,  2.2,  2.3,  2.4,  2.5,  2.6,  2.7,  2.8,  2.9,  3. ,  3.1,
        3.2,  3.3,  3.4,  3.5,  3.6,  3.7,  3.8,  3.9,  4. ,  4.1,  4.2,
        4.3,  4.4,  4.5,  4.6,  4.7,  4.8,  4.9,  5. ,  5.1,  5.2,  5.3,
        5.4,  5.5,  5.6,  5.7,  5.8,  5.9,  6. ,  6.1,  6.2,  6.3,  6.4,
        6.5,  6.6,  6.7,  6.8,  6.9,  7. ,  7.1,  7.2,  7.3,  7.4,  7.5,
        7.6,  7.7,  7.8,  7.9,  8. ,  8.1,  8.2,  8.3,  8.4,  8.5,  8.6,
        8.7,  8.8,  8.9,  9. ,  9.1,  9.2,  9.3,  9.4,  9.5,  9.6,  9.7,
        9.8,  9.9, 10. , 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8,
       10.9, 11. , 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9,
       12. , 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13. ,
       13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9, 14. , 14.1,
       14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8, 14.9, 15. , 15.1, 15.2,
       15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9, 16. , 16.1, 16.2, 16.3,
       16.4, 16.5, 16.6, 16.7, 16.8, 16.9, 17. , 17.1, 17.2, 17.3, 17.4,
       17.5, 17.6, 17.7, 17.8, 17.9, 18. , 18.1, 18.2, 18.3, 18.4, 18.5,
       18.6, 18.7, 18.8, 18.9, 19. , 19.1, 19.2, 19.3, 19.4, 19.5, 19.6,
       19.7, 19.8, 19.9])
>>> 
============= RESTART: C:/Users/asus/Desktop/DL_NITTTR/Lambda.py =============
True
>>> 
============= RESTART: C:/Users/asus/Desktop/DL_NITTTR/Lambda.py =============
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
>>> 
============= RESTART: C:/Users/asus/Desktop/DL_NITTTR/Lambda.py =============
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> 
============= RESTART: C:/Users/asus/Desktop/DL_NITTTR/Lambda.py =============
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> 
============== RESTART: C:/Users/asus/Desktop/DL_NITTTR/Map.py ==============
94.1
91.76
100.03999999999999
85.64
82.03999999999999
>>> 
============== RESTART: C:/Users/asus/Desktop/DL_NITTTR/Map.py ==============
[94.1, 91.76, 100.03999999999999, 85.64, 82.03999999999999]
>>> 
============== RESTART: C:/Users/asus/Desktop/DL_NITTTR/Map.py ==============
[34.5, 33.2, 37.8, 29.8, 27.8]
>>> import numpy as np
>>> np.array([3,54,6,8,9,4,3,4])
array([ 3, 54,  6,  8,  9,  4,  3,  4])
>>> x = np.array([3,54,6,8,9,4,3,4])
>>> np.argmax(x)
1
>>> np.argsort(x)
array([0, 6, 5, 7, 2, 3, 4, 1], dtype=int64)
>>> 

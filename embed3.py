import numpy as np

a=np.array([1,2,3])
b=np.array([2,4,6])
c=np.array([33,193,66])


def cos_similar(a,b):
    dot_product=np.dot(a,b)
    n_a=np.linalg.norm(a)
    n_b=np.linalg.norm(b)

    if n_a == 0 or n_b == 0:
        return 0
    return dot_product/(n_a * n_b)


print('a vs b: ',cos_similar(a,b))
print('a vs c: ',cos_similar(a,c))


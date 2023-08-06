"""C Program Interface"""

'''File: dll.dll

typedef struct Matrix {
    int height;
    int width;
    int value[16][16];
} mat;

mat* MatMul(mat m1, mat m2) {
    mat* mp = (mat*)malloc(sizeof(mat));
    int i, j, k;
    int sum;

	mp->height = m1.height;
	mp->width = m2.width;
    for(i = 0; i < m1.height; i++)
        for(j = 0; j < m2.width; j++) {
            sum = 0;
            for(k = 0; k < m1.width; k++)
                sum += m1.value[i][k] * m2.value[k][j];
            mp->value[i][j] = sum;
        }
    return mp;
}

mat* MatNew(int height, int width) {
    mat* mp = (mat*)malloc(sizeof(mat));
    int i, j;
    int sum = 0;

	mp->height = height;
	mp->width = width;
    for(i = 0; i < height; i++)
        for(j = 0; j < width; j++)
            mp->value[i][j] = sum++;
    return mp;
}

int MatSum(mat m) {
    int i, j;
    int sum = 0;
    for(i = 0; i < m.height; i++)
        for(j = 0; j < m.width; j++)
            sum += m.value[i][j];
    return sum;
}
'''

import ctypes


def struct(fields):
    class Struct(ctypes.Structure):
        _fields_ = fields
    return Struct


class Type:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return Type(self.value * item)


CINT = Type(ctypes.c_int)


def fields(cls):
    return [(k, v.value) for k, v in cls.__dict__.items() if isinstance(v, Type)]


if __name__ == '__main__':
    class Mat:
        height = CINT
        width  = CINT
        value  = CINT[16][16]

    print(fields(Mat))
    Mat = struct(fields(Mat))
    print(Mat)

    dll = ctypes.CDLL(r"D:\lsx\cf\dll\mingw5\dll.dll")

    # - (int, int) -> Mat ---------------------------------------

    dll.MatNew.restype = ctypes.POINTER(Mat)

    ret = dll.MatNew(3, 4).contents
    print([row[:ret.width] for row in ret.value[:ret.height]])

    # - (Mat, Mat) -> Mat ---------------------------------------

    dll.MatMul.argtype = (Mat, Mat)
    dll.MatMul.restype = ctypes.POINTER(Mat)

    m1 = Mat()
    m1.height = 3
    m1.width = 3
    for i in range(3):
        for j in range(3):
            m1.value[i][j] = i * 3 + j

    ret = dll.MatMul(m1, m1).contents
    print([row[:ret.width] for row in ret.value[:ret.height]])

    # - Mat -> int ---------------------------------------

    dll.MatSum.argtype = Mat

    m1 = Mat()
    m1.height = 3
    m1.width = 3
    for i in range(3):
        for j in range(3):
            m1.value[i][j] = i * 3 + j

    ret = dll.MatSum(m1)
    print(ret)

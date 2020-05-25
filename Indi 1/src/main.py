import PIL.Image as Image
import subprocess


def create_file(data, name):
    f_out = open(name, 'w')
    str_data = ''
    for e in data:
        if e <= 9:
            str_data += '00'+str(e)
        elif 10 <= e <= 99:
            str_data += '0'+str(e)
        else:
            str_data += str(e)
    f_out.write(str_data)
    f_out.flush()
    f_out.close()


def to_list(mat):
    res = []
    for i in mat:
        for j in i:
            res += [j]
    return res


def main():
    # foto = Image.open("Indi 1/res/ferrariC.bmp")
    # foto = foto.convert('L')
    # data = foto.getdata()
    # foto.close()
    # create_file(data, 'mybin.bin')
    # # create_file(to_list([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), 'asdf.txt')
    # ker = [[2, 1, 2], [1, 7, 1], [2, 1, 2]]
    # create_file(to_list(ker), 'kernel.bin')

    create_file([1,2,3,4,5,6,7,8,9,10,11,12,13], 'mybin.bin')

    # res = combu(datamatrix, ker)
    # newdata = []
    # for i in res:
    #     for j in i:
    #         newdata.append(j)
    # newPic = Image.new('L', foto.size)
    # newPic.putdata(newdata)
    # newPic.save('test.bmp')
    # newPic.close()
    # foto.close()


main()

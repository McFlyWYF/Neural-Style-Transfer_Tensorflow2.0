import xlrd
import matplotlib.pyplot as plt
import os
from PIL import Image

data = xlrd.open_workbook(filename="./loss/loss_sum.xlsx")
table = data.sheet_by_name('Sheet1')    #表名
nrows = table.nrows      #行号
ncols = table.ncols     #列号
dataset = []

for i in range(1,ncols):    #按列读取
    cells = table.col_values(i)     #每列赋值给cell
    dataset.append(cells)

alldata = []
for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        alldata.append(dataset[i][j])

print(alldata)

x = []
for i in range(len(alldata)):
    x.append(i)

print(len(x))
plt.plot(x,alldata)
plt.savefig('./samples/loss.jpg')
plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
girl = Image.open(os.path.join('./samples/girl.jpg'))
plt.subplot(1,2,1)
plt.imshow(girl)
plt.title('原始图')


transform_girl = Image.open(os.path.join('./output/20.jpg'))
transform_girl = transform_girl.resize((1024,1024))
plt.subplot(1,2,2)
plt.imshow(transform_girl)
plt.title('风格转换图')
plt.savefig('./samples/girl_transform.jpg')
plt.show()


#file      stardust.py
#author    取不到名字的Z先生, https://blog.csdn.net/qq_42233962/article/details/105482765
#version   
#date      2020_08_07
#github    https://github.com/stardust-scitech/OpenCM
#copyright 
#license   

#从Python的PIL库中导入Image模块
from PIL import Image
 
class node: #节点的类
    #定义节点构造方法
    def __init__(self,right=None,left=None, parent=None, weight=0, code=None):
        self.left = left 
        self.right = right 
        self.parent = parent 
        self.weight = weight #权重
        self.code = code #节点值
        
#定义函数，将彩色图转为灰色图，此时图像的每个像素点可以用单独的像素值表示
def picture_convert(filename,newfilename): 
    picture = Image.open(filename)
    picture = picture.convert('L')#将bmp 图片转换为灰值图
    picture. save(newfilename)#保存灰度图像
    return picture
 
#定义函数，统计每个像素出现的次数
def pixel_number_caculate(list):
    pixel_number={}
    for i in list:
        if i not in pixel_number. keys():
            pixel_number[i]=1 #若此像素点不在字符频率字典里则直接添加
        else:
            pixel_number[i] += 1 #若存在在字符频串字典里则对应值加一 
    return pixel_number
 
#构造节点，分別陚予其值和对应的权值 
def node_construct(pixel_number): 
    node_list =[]
    for i in range(len(pixel_number)):
        node_list.append(node(weight=pixel_number[i][1],code=str(pixel_number[i][0])))
    return node_list
 
#构造节点，分別陚予其值和对应的权值 
def node_construct(pixel_number): 
    node_list =[]
    for i in range(len(pixel_number)):
        node_list.append(node(weight=pixel_number[i][1],code=str(pixel_number[i][0])))
    return node_list
 
#根据叶子结点列表，生成对应的霍夫曼编码树
def tree_construct(listnode):
    listnode = sorted(listnode,key=lambda node:node.weight) 
    while len(listnode) != 1:
        #每次取权值的两个像素点进行合并
        low_node0,low_node1 = listnode[0], listnode[1]
        new_change_node = node()
        new_change_node.weight = low_node0.weight + low_node1.weight
        new_change_node.left = low_node0
        new_change_node.right = low_node1
        low_node0.parent = new_change_node
        low_node1.parent = new_change_node
        listnode.remove(low_node0)
        listnode.remove(low_node1)
        listnode.append(new_change_node)
        listnode = sorted(listnode, key=lambda node:node.weight) 
    return listnode
#霍夫曼编码的主函数，通过对其他函数的调用完成对像素点的编码
def Huffman_Coding(picture):
   #得到图片的宽度和高度
    width = picture.size[0]
    height = picture.size[1]
    im = picture.load()
    print ("灰度图宽为"+str(width)+"像素")
    print ("灰度图高为"+str(height)+"像素")
 
    #将像素点保存在list中，原来的二维矩阵变为一维数组 
    list =[]
    for i in range(width):
        for j in range(height): 
            list.append(im[i,j])
    #统计每个像素点的次数，并根据出现的次数由小到大排序 
    pixel_number = pixel_number_caculate(list)
    pixel_number = sorted(pixel_number.items(),key=lambda item:item[1])
           
    #根据像素点的值和其出现次数构造节点list 
    node_list = node_construct(pixel_number)
    # 构 造 哈 夫 曼 树 ，保 存 头 结 点
    head = tree_construct(node_list)[0]
           
    #构造编码表
    coding_table = {}
    for e in node_list:
        new_change_node = e
        coding_table.setdefault(e.code,"")
        while new_change_node !=head:
            if new_change_node.parent.left == new_change_node: 
                coding_table[e.code] = "1" + coding_table[e.code] 
            else:
                coding_table[e.code] = "0" + coding_table[e.code] 
            new_change_node = new_change_node. parent
    #输出每个像累点灰度值和编码
    for key in coding_table.keys():
        print ("信源像素点"+ key+"编码后的码字节:" + coding_table[key])
 
 
    #输出编码表
    print ("编码表为：",coding_table)
 
    #将图像的编码结果转换成字符串井保存到txt里 
    coding_result = ''
    for i in range(width):
        for j in range(height):
            for key,values in coding_table.items(): 
                if str(im[i,j]) == key:
                    coding_result = coding_result+values 
    file = open('coding_result.txt','w') 
    file.write(coding_result)
#还原原始的bmp图像,遍历霍夫曼编码的结果，对于每一个被遍历到的字符均在码字列表 
#中进行查找，若未找到则加上后续一个字符，继续查找，重复此步骤，直到在码字列表中找 
#到该码字对应的像素点，将其码字对应的像素值放入到像素点列表中。
def Decoding(width,height,coding_table,coding_result): 
    code_read_now=''#当前读到的编码 
    new_pixel =[] 
    i = 0
    while (i != coding_result.__len__()):
        #每次往后读一位
        code_read_now = code_read_now + coding_result[i]
        for key in coding_table.keys():
            #如果当前读到的编码在编码表里存在 
            if str(code_read_now) == str(coding_table[key]): 
                new_pixel. append(key) 
                code_read_now =''
                break
        i +=1
    #构造新图像
    decode_image = Image.new( 'L' ,(width,height)) 
    k = 0 
    #篇予像聚值
    for i in range(width):
        for j in range(height):
            decode_image.putpixel((i,j),(int(new_pixel[k]))) 
            k+=1
    decode_image.save('decode.bmp') 
    print("译码已经完成：图片存储为decode.bmp")

#彩色图转灰度
picture = picture_convert('lab.jpg','new.jpg')
#灰度图进行哈夫曼编码
Huffman_Coding(picture)

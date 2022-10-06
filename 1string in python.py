# nháy đơn
#''
# nháy kép
#""

#in chuỗi
str='Howkteam'
str1="Howkteam"
str2="""I'm Nguyet"boyfriend"""
str3='''abcdefg\nhijklmn
opqrsxtv
'''
print(str)
print(str1)
print(str2)
print(str3)
print('\a\a')

#\a: phát tiếng bíp
#\n: xuống dòng
#\b: đưa con trỏ về lại khoảng trắng
#\t: in ra dấu cách
#\(\,',"): in ra \,',"

#phép toán với chuỗi
str4='abc'
str5='def'
stra=str4+str5 #abcdef
#stra=str4*3 #abcabcabc
#stra=str5 in str4 #true-str5 có trong str4 và ngược lại
#str6=stra[-2]
#len(str): độ dài chuỗi str

#cắt chuỗi trái qua phải
#strb=stra[a:b]  lấy từ a+1 đến b-1
strb=stra[1:2]
#ép kiểu dữ liệu
ac= '69'
bd=int(ac)
print(bd)
print(hash(ac))

s1='My nam is %s' %('kieu')
print(s1)

s2='diem toan va hoa la %s %s' %('1','2')
print(s2)

#r='1: {1}, 2: {0}'.format(111,222)
#print(r)

#căn lề trái {:(c)<n}
#căn lề phải {:(c)>n}
#căn giữa {:(c)^n}

strc= '{:^10}'.format('kieu')
print(strc) 

#hàm viết hoa chữ cái đầu :: str.capitalize()
#hàm viết hoa tất cả chữ cái :: str.upper()
#hàm viết thường tất cả chữ cái :: str.lower()
#thường thành hoa, hoa thành thường :: str.swapcase()
#viết hoa chữ cái đầu mỗi từ :: str.title()
#trả về 1 chuỗi được căn giữa với chiều rộng width :: str.center(width,[fillchar])
#căn phải :: str.rjust()
#căn trái :: str.ljust()
#mã hóa :: str.encode()
#cộng chuỗi tuần tự :: str.join('str1','str2','str3)
#hàm thay thế :: str.replace('str bị thay thế','str đc thay thế', số lượng)
#hàm cắt chuỗi :: str.strip('str bị cắt')
#hàm cắt chuỗi trái phải : str.lstrip(), str.rstrip()
#hàm tách chuỗi :: str.split(char, số lượng)  kieu cắt e thành ki u
#..................str.rsplit()
#hàm tách chuỗi :: str.partition(char)  kieu nhập e thành ki e u
#......................rpartition
#đếm chuỗi trong chuỗi :: str.cout('str1',bắt đầu, kết thúc)
#kiểm tra chuỗi bắt đầu bằng ký tự :: str.startswith('char',bắt đầu, kết thúc)
#tìm kiếm :: str.find('char') trả về -1 nếu không thấy
#tìm kiếm :: str.rindex('char') 
#kiểm tra viết hoa viết thường trả về true false :: str.islower(chuỗi thường), str.isupper(chuỗi hoa)
#kt chuỗi trắng :: str.isspace()
strd='kieu'
stre=strd.capitalize()
print(strd)
print(stre)
def tinh_tuoi(namsinh):
	return 2021-namsinh
def sinh_ma_tinh(tenTinh,dictTinh):
	for key,value in dictTinh.items():
		if(tenTinh==value):
			return key
def sinh_gioi_tinh(namsinh,gioitinh):
	ma_gioi_tinh=0
	if(1900<=namsinh<=1999 and gioitinh==1):
		ma_gioi_tinh=0
	if(1900<=namsinh<=1999 and gioitinh==0):
		ma_gioi_tinh=1	
	if(2000<=namsinh<=2099 and gioitinh==1):
		ma_gioi_tinh=2	
	if(2000<=namsinh<=2099 and gioitinh==0):
		ma_gioi_tinh=3
	if(2100<=namsinh<=2199 and gioitinh==1):
		ma_gioi_tinh=4
	if(2100<=namsinh<=2199 and gioitinh==0):
		ma_gioi_tinh=5		
	if(2200<=namsinh<=2299 and gioitinh==1):
		ma_gioi_tinh=6
	if(2200<=namsinh<=2299 and gioitinh==0):
		ma_gioi_tinh=7
	if(2300<=namsinh<=2399 and gioitinh==1):
		ma_gioi_tinh=8		
	if(2300<=namsinh<=2399 and gioitinh==0):
		ma_gioi_tinh=9	
	return ma_gioi_tinh
def sinh_email_B19DCCN427(hoTen):
	lst=hoTen.lower().split()
	email=""
	for i in range(0,len(lst)-1):
		email=email+lst[i][0]
	email = lst[-1]+email+"@gmail.com"
	return email
class Fullname_NamDinh():
	"""docstring for ClassName"""
	def __init__(self,ho,dem,ten):
		self.ho=ho
		self.dem=dem
		self.ten=ten
class CongDan_NhatMinh:
	def __init__(self,hoten,namsinh,gioitinh,quequan):
		self.hoten=hoten
		self.namsinh=namsinh
		self.gioitinh=gioitinh
		self.fullname=hoten.ho+' '+hoten.dem+' '+hoten.ten
		self.tuoi=tinh_tuoi(namsinh)
		self.email=sinh_email_B19DCCN427(self.fullname)
		self.quequan = quequan		
dictTinh={'001':'Hà Nội','008':'Tuyên Quang','004':'Cao Bằng','019':'Thái Nguyên','020':'Lạng Sơn','022':'Quảng Ninh','026':'Vĩnh Phúc','031':'Hải Phòng','035':'Ha Nams'}

cd1=CongDan_NhatMinh(Fullname_NamDinh('Nguyen','Trần','Anh'),1984,'Nam','Hà Nội')
cd2=CongDan_NhatMinh(Fullname_NamDinh('Nguyen','Hoang','Bách'),1986,'Nam','Thái Nguyên')
cd3=CongDan_NhatMinh(Fullname_NamDinh('Nguyen','Minh','Anh'),1988,'nữ','Hải Phòng')
cd4=CongDan_NhatMinh(Fullname_NamDinh('Nguyen','Hoang','Giang'),2004,'Nam','Lạng Sơn')
cd5=CongDan_NhatMinh(Fullname_NamDinh('Võ','Hoang','Anh'),2005,'Nữ','Hà Nội')
cd6=CongDan_NhatMinh(Fullname_NamDinh('Nguyen','Linh','Anh'),2011,'Nữ','Hải Phòng')
cd7=CongDan_NhatMinh(Fullname_NamDinh('Nguyen','Lê','Anh'),1995,'Nam','Quảng Ninh')
cd8=CongDan_NhatMinh(Fullname_NamDinh('Lê','Quang','Anh'),1996,'Nam','Cao Bằng')
cd9=CongDan_NhatMinh(Fullname_NamDinh('Trần','Hoàng','Minh'),1999,'Nam','Tuyên Quang')
cd10=CongDan_NhatMinh(Fullname_NamDinh('Vũ','Hoang','Việt'),2000,'Nam','Vĩnh Phúc')

list_cd=[cd1,cd2,cd3,cd4,cd5,cd6,cd7,cd8,cd9,cd10]
info=""
for item in list_cd:
	info=item.fullname+" "+ item.gioitinh+" "+str(item.tuoi)+" "+item.quequan+" "+item.email
	print(info)
#Cau 4
list_copy=list_cd[:]
list_random=[]
import random
for i in range(0,5,1):
	cdx=random.choice(list_copy)
	list_random.append(cdx)
	list_copy.remove(cdx)
def sinh_ma_cccd(congdan):
	ma_tinh=sinh_ma_tinh(congdan.quequan,dictTinh)
	gioi_tinh=0
	if(congdan.gioitinh=="Nam"):
		gioi_tinh=1
	ma_gioi_tinh=sinh_gioi_tinh(congdan.namsinh,gioi_tinh)
	ma_namsinh=str(congdan.namsinh)[-2:]
	so_ngau_nhien=random.randint(100000,999999)
	ma_can_cuoc=str(ma_tinh)+str(ma_gioi_tinh)+str(ma_namsinh)+str(so_ngau_nhien)
	return ma_can_cuoc
for item in list_random:
	info=item.fullname +" "+str(item.namsinh)+" "+item.gioitinh+" "+item.quequan+" "+sinh_ma_cccd(item)
	print(info)

#Cau5
def doc_cccd(cccd):
	ma_tinh=cccd[0:3]
	ma_gioi_tinh=int(cccd[3])
	ma_nam_sinh=cccd[4:6]
	so_ngau_nhien=cccd[7::]
	ten_tinh=""
	for key,value in dictTinh.items():
		if(key==ma_tinh):
			ten_tinh=value
	the_ki=0
	gioi_tinh=""
	if(ma_gioi_tinh==0):
		the_ki=19
		gioi_tinh="Nam"
	elif ma_gioi_tinh==1:
		the_ki=19
		gioi_tinh="Nu"
	elif ma_gioi_tinh==2:
		the_ki=20
		gioi_tinh="Nam"
	elif ma_gioi_tinh==3:
		the_ki=20
		gioi_tinh="Nu"	
	elif ma_gioi_tinh==4:
		the_ki=21
		gioi_tinh="Nam"
	elif ma_gioi_tinh==5:
		the_ki=21
		gioi_tinh="Nu"
	elif ma_gioi_tinh==6:
		the_ki=22
		gioi_tinh="Nam"
	elif ma_gioi_tinh==7:
		the_ki=22
		gioi_tinh="Nu"
	elif ma_gioi_tinh==8:
		the_ki=23
		gioi_tinh="Nam"
	else:
		the_ki=23
		gioi_tinh="Nu"
	namsinh=str(the_ki)+ma_nam_sinh
	print(f"ten Tinh {ten_tinh}")
	print(f"Gioi tinh {gioi_tinh}, song o the ki {the_ki}")
	print(f"Nam Sinh {namsinh}")
	print(f"so ngau nhien {so_ngau_nhien}")
doc_cccd("035153000257")


from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
import json, os
from saleapp import app, db

class Masanpham(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    def __str__(self):
        return self.name


class Danhmucsanpham(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ghichu = Column(String(255))
    giatien = Column(Float, default=0)
    anh = Column(String(100))
    masanpham = Column(Integer,ForeignKey("masanpham.id"),nullable=False)
    
    def __str__(self):
        return self.name


class User(db.Model):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ten = Column(String(50), nullable=False, unique=True)
    matkhau = Column(String(50), nullable=False)
    def __str__(self):
        return self.name


class themsp(db.Model):
    id = Column(db.Integer, primary_key=True)
    ten = Column(String(100),  nullable=False)
    giatien = Column(Float,  nullable=False)
    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        db.create_all()




















        # c1 = Masanpham(name='Áo Thun')
        # c2= Masanpham(name='Quần')
        # c3= Masanpham(name='Áo khoác')
        # c4= Masanpham(name='Áo sơ mi')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.add(c4)
        # db.session.commit()

        # #Danh sách sản phẩm mẫu của bạn
        # products = [
        #     {
        #         "name": "Áo thun",
        #         "ghichu": "Áo thun cotton",
        #         "giatien": 199000,
        #         "anh": "images/aothun1.jpg",
        #         "masanpham": 1
        #     },
        #     {
        #         "name": "Áo sơ mi",
        #         "ghichu": "Chất liệu kate cao cấp",
        #         "giatien": 349000,
        #         "anh": "images/aosomi.jpg",
        #         "masanpham": 2
        #     },
        #     {
        #         "name": "Quần jean",
        #         "ghichu": "Quần rộng",
        #         "giatien": 499000,
        #         "anh": "images/quanjean.jpg",
        #         "masanpham": 3
        #     },
        #     {
        #         "name": "Áo Gió",
        #         "ghichu": "Phong cách năng động",
        #         "giatien": 699000,
        #         "anh": "images/aokhoac1.jpg",
        #         "masanpham": 4
        #     },
        #     {
        #         "name": "Áo Len",
        #         "ghichu": "Giữ ấm mùa đông",
        #         "giatien": 599000,
        #         "anh": "images/aolen.jpg",
        #         "masanpham": 4
        #     }
        # ]

        # for p in products:
        #     db.session.add(Danhmucsanpham(**p))
            
        # db.session.commit()
        
        # print("Đã thêm dữ liệu")
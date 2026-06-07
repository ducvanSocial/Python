import json, os
from saleapp import app, db
from saleapp.models import Masanpham, Danhmucsanpham, User, themsp

def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def read_users():
    return User.query.all()

def load_masp():
    return Masanpham.query.all()


def load_san_pham(maid=None, ten=None, giabatdau=None):
    products = Danhmucsanpham.query
    if maid:
        products = products.filter(Danhmucsanpham.masanpham == int(maid))
    if ten:
        products = products.filter(Danhmucsanpham.name == ten)
    if giabatdau:
        products = products.filter(Danhmucsanpham.giatien >= (giabatdau))
    return products



def trasp(product_id):
    products = Danhmucsanpham.query.all()
    for p in products:
        if p.id == product_id:
            return p



def read_product_by(lay_id):
    products = Danhmucsanpham.query.all()
    for x in products:
        if x.id == lay_id:
            return x
        

def thanhtoan(id):
    sanpham = Danhmucsanpham.query.all()
    for s in sanpham:
        if s.id == id:
            return s


def dangnhap(ten, matkhau):
    user = User.query.filter_by(ten=ten).first()
    if user and user.matkhau == matkhau:
        return user


def add_user(name, username, password):
    user = User(name=name, ten=username, matkhau=password)
    db.session.add(user)
    db.session.commit()


def themsanpham(name, ghichu ,giatien, anh,masanpham):
    p = Danhmucsanpham(name=name, ghichu=ghichu, giatien=giatien, anh=anh, masanpham=masanpham)
    db.session.add(p)
    db.session.commit()

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


def dangnhap(ten, matkhau):
    user = User.query.filter_by(ten=ten).first()
    if user and user.matkhau == matkhau:
        return user

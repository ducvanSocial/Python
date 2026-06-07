from saleapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Danhmucsanpham, Masanpham

admin = Admin(app=app, name="Quản lý sản phẩm ")
admin.add_view(ModelView(Masanpham, db.session))
admin.add_view(ModelView(Danhmucsanpham, db.session))




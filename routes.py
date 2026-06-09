from flask import render_template, request, url_for, redirect
from saleapp import app, db
from saleapp import utils
from saleapp.utils import load_san_pham, load_masp, add_user, read_users, themsanpham ,  User, Danhmucsanpham, dangnhap, trasp, thanhtoan,  read_product_by



@app.route("/")
def home():
    sp = load_san_pham()
    return render_template("home.html", sp=sp)


@app.route("/sanpham")
def sanphams():
    maid = request.args.get("masanpham")
    ten = request.args.get("keyword")
    giabatdau = request.args.get("from_price")
    products = Danhmucsanpham.query
    if maid:
        products = products.filter(Danhmucsanpham.masanpham == int(maid))
    if ten:
        products = products.filter(Danhmucsanpham.name == ten)
    if giabatdau:
        products = products.filter(Danhmucsanpham.giatien >= (giabatdau))
    return render_template("san_pham.html", danh_muc=products)
    



@app.route("/chitietsp/<int:product_id>")
def xemchitietsp(product_id):
    products = Danhmucsanpham.query.get(id)
    return render_template("chitietsanpham.html", products=products)



@app.route("/dangnhap", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = dangnhap(ten=username, matkhau=password)
        if user:
            return redirect("/")
    return render_template("login.html")


@app.route("/dangki", methods=['GET', 'POST'])
def dang_ki():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        add_user(name, username, password)
    return render_template('dang_ki.html')



@app.route("/them", methods=['GET', 'POST'])
def them():
    if request.method == 'POST':
        name = request.form.get('name')
        ghichu = request.form.get('description')
        giatien = request.form.get('price')
        masanpham = request.form.get('category_id')
        anh = request.files.get('image')
        themsanpham(name=name, ghichu=ghichu, giatien=giatien, anh=anh, masanpham=masanpham)
    return render_template('themsp.html')

        
@app.route("/delete/<int:id>")
def delete_student(id):
    xoasanpham = Danhmucsanpham.query.get_or_404(id)
    db.session.delete(xoasanpham)
    db.session.commit()
    return redirect(url_for('quanly'))


@app.route("/quanlysp")
def quanly():
    quanly = Danhmucsanpham.query.all()
    return render_template('quanlysp.html', quanly=quanly)


@app.route('/thanhtoan/<int:id>')
def thanhtoanhoan(id):
    sanpham = Danhmucsanpham.query.get(id)
    return render_template('thanhtoan.html',sanpham=sanpham)


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)



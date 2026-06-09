from flask import render_template, request, url_for, redirect
from saleapp import app, db
from saleapp import utils
from saleapp.utils import User, Danhmucsanpham, dangnhap



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
        user = User(name=name, ten=username, matkhau=password)
        db.session.add(user)
        db.session.commit()
    return render_template('dang_ki.html')



@app.route("/them", methods=['GET', 'POST'])
def them():
    if request.method == 'POST':
        name = request.form.get('name')
        ghichu = request.form.get('description')
        giatien = request.form.get('price')
        masanpham = request.form.get('category_id')
        anh = request.files.get('image')
        p = Danhmucsanpham(name=name, ghichu=ghichu, giatien=giatien, anh=anh, masanpham=masanpham)
        db.session.add(p)
        db.session.commit()
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


@app.route("/capnhat/<int:id>", methods=["GET", "POST"])
def update_student(id):
    sapnhatsanpham = Danhmucsanpham.query.get_or_404(id)
    if request.method == "POST":
        sapnhatsanpham.name = request.form["name"]
        sapnhatsanpham.ghichu = request.form["description"]
        sapnhatsanpham.giatien = request.form["price"]
        sapnhatsanpham.masanpham = request.form["category_id"]
        sapnhatsanpham.anh = request.files["image"]
        db.session.commit()
        return redirect(url_for('quanly'))
    
    return render_template("capnhatsp.html", sapnhatsanpham=sapnhatsanpham)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)



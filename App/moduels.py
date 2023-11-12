from sqlalchemy import Column, Integer, String, Float , Boolean, ForeignKey
from sqlalchemy.orm import  relationship
from App import db, app




class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer,primary_key=True,autoincrement=True)



class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(50),nullable=True)
    products = relationship('Product', backref='category', lazy=True)



class Product(BaseModel):
    name = Column(String(50),nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), default = "https://p4-ofp.static.pub/fes/cms/2023/03/28/7dch8vg9lz0tzeg74u3x9paoln4o8z319478.png")
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()
        p1 = Product(name='iPhone 15 ProMax',price='2000000',category_id=1)
        p2 = Product(name='iPad Pro 2023', price='2500000', category_id=2)
        p3 = Product(name='Galaxy Tab S9', price='2300000', category_id=2)
        p4 = Product(name='iPhone 12 ProMax', price='2100000', category_id=1)
        p5 = Product(name='iPhone 13 ProMax', price='1700000', category_id=1)
        p6 = Product(name='Galaxy S20', price='2000000', category_id=1)
        db.session.add_all([p1,p2,p3,p4,p5,p6])
        db.session.commit()
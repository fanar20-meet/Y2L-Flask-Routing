from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_session():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session


def add_product(name,price,picture_link ,description):
	session = create_session()
	product_object = Product(
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(product_object)
	session.commit()


def update_price(Id,price):
	session = create_session()
	product_object = session.query(
		Product).filter_by(
		Id=Id).first()

	product_object.price = price
	session.commit()


def delete_product(Id):
	session = create_session
	session.query(Product).filter_by(
		Id=Id).delete()
	session.commit()




def query_all():
	session = create_session()
	products = session.query(
		Product).all()
	return products



def query_by_Id(Id):
	session = create_session()
	product = session.query(
	Product).filter_by(
	Id=Id).first()
	return product



def check():
	print("plese workkk")




check()



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
	session.close()

# add_product("jeans",20,"jeans3.jpg","this is nice")
add_product("glasses" , 15 ,"jeans3.jpg","good")


def update_price(Id,price):
	session = create_session()
	product_object = session.query(
		Product).filter_by(
		Id=Id).first()

	product_object.price = price
	session.commit()
	session.close()


def delete_product(name):
	session = create_session()
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()
	session.close()

# delete_product("jeans")
# delete_product("glasses")


def query_all():
	session = create_session()
	products = session.query(
		Product).all()
	session.close()
	return products



def query_by_Id(Id):
	session = create_session()
	product = session.query(
	Product).filter_by(
	Id=Id).first()
	return product


def add_to_cart(productID):
	session = create_session()
	cart_object =Cart(
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(product_object)
	session.commit() 


# def check():
# 	print("plese workkk")




# check()
session = create_session()


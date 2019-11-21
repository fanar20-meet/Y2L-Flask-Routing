from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class product(Base):
	__tablename__ = 'products'
	Id = Column(Integer , primary_key=True)
	name = Column(String)
	price = (Float)
	pricture_link =(String)
	description = (String)



class Cart():
	__table__ = "cart"
	product_id = Column(Integer,primary_key=True)

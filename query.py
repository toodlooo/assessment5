"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette',brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter( (Brand.founded==1903) & (Brand.discontinued == None) ).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter( (Brand.discontinued != None) | (Brand.founded<1950) ).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter( ~ Model.brand_name.in_(['Chevrolet']) ).all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    select_year = year

    models = db.session.query(Model.name, Model.brand_name, Model.year, Brand.headquarters).join(Brand).all()

    for model, brand, year, headquarters in models:
    	if year == select_year:
    		print "Ah yes, the {} {}. That particular model's brand is based in {}!".format(brand, model, headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # brand_models = db.session.query(Brand.name, Model.name).join(Model).group_by('Brand.name').all()

    brand_models = db.session.query(Model.brand_name, Model.name).group_by('Model.brand_name').all() # I feel like this should work but I'm getting this error: sqlalchemy.exc.InternalError: (psycopg2.InternalError) current transaction is aborted, commands ignored until end of transaction block

    for brand, model in brand_models:
    	print brand, model


# -------------------------------------------------------------------

# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# Value is <flask_sqlalchemy.BaseQuery object at 0x10fa33650>
# Type is type(Brand.query.filter_by(name='Ford')), which is <class 'flask_sqlalchemy.BaseQuery'>


# 2. In your own words, what is an association table, and what *type* of relationship does an association table manage?
# Association tables manage many-to-many table relationships, meaning that they act as a connector type of table that connects two tables that associate with each other as a many-to-many relationship. Association tables typically comprise only of the IDs/primary keys of the two tables that are connected to the association table.


# -------------------------------------------------------------------


# Part 3: Advanced and Optional
def search_brands_by_name(mystr):
    results = Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()

    return results
    # for result in results:
    # 	print result

def get_models_between(start_year, end_year):
    results = Model.query.filter( (Model.year > start_year) & (Model.year < end_year) ).all()

    return results
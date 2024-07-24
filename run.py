# this module is responsible for starting server

from app import create_app

app=create_app()

# with app.app_context():
#     db.create_all()  # Create database tables

if __name__ == '__main__':
    # db.create_all()  # Create database tables
    app.run(debug=True)
# if __name__ == '__main__':
#     app.run(debug=True)
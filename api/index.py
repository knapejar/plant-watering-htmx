from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
db = SQLAlchemy(app)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    last_watered = db.Column(db.String(120), nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'last_watered': self.last_watered
        }

with app.app_context():
    db.drop_all()
    db.create_all()
    plant1 = Plant(name='Fiddle Leaf Fig', description='Likes to be watered once a week.', last_watered='2024-05-18 12:00:00')
    plant2 = Plant(name='Peace Lily', description='Tolerates low light.', last_watered='2024-05-18 12:00:00')
    plant3 = Plant(name='Basil', description='The most delicious herb.', last_watered='2024-05-18 12:00:00')
    db.session.add(plant1)
    db.session.add(plant2)
    db.session.add(plant3)
    db.session.commit()

@app.route('/')
def index():
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)
@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.form
    new_plant = Plant(name=data['name'], description=data['description'])
    db.session.add(new_plant)
    db.session.commit()
    return render_template('_plant.html', plant=new_plant), 201

@app.route('/plants/<int:id>', methods=['PUT'])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.form
    plant.name = data.get('name', plant.name)
    plant.description = data.get('description', plant.description)
    db.session.commit()
    return render_template('_plant.html', plant=plant)

@app.route('/plants/<int:id>/water', methods=['POST'])
def water_plant(id):
    plant = Plant.query.get_or_404(id)
    plant.last_watered = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.session.commit()
    return render_template('_plant.html', plant=plant)

@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return '', 201

if __name__ == '__main__':
    app.run(debug=True)

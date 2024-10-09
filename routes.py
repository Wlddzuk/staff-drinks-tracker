from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import db, Staff, Drink, DrinkOrder
# Routes
bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/staff', methods=['POST'])
def add_staff():
    data = request.json
    new_staff = Staff(staff_name=data['staff_name'])
    db.session.add(new_staff)
    try:
        db.session.commit()
        return jsonify({'message': 'Staff member added successfully', 'staff_id': new_staff.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error adding staff member', 'error': str(e)}), 400

@bp.route('/staff', methods=['GET'])
def get_all_staff():
    staff = Staff.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.staff_name,
        'tab': s.drink_tab
    } for s in staff])

@bp.route('/staff/<int:staff_id>', methods=['DELETE'])
def remove_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    
    # Delete associated drink orders
    DrinkOrder.query.filter_by(staff_id=staff.id).delete()
    
    db.session.delete(staff)
    db.session.commit()
    return jsonify({'message': 'Staff member removed successfully'})

@bp.route('/drinks', methods=['POST'])
def add_drink():
    data = request.json
    new_drink = Drink(drink_name=data['drink_name'], drink_cost=data['drink_cost'])
    db.session.add(new_drink)
    try:
        db.session.commit()
        return jsonify({'message': 'Drink added successfully', 'drink_id': new_drink.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error adding drink', 'error': str(e)}), 400

@bp.route('/drinks', methods=['GET'])
def get_all_drinks():
    drinks = Drink.query.all()
    return jsonify([{
        'id': d.id,
        'name': d.drink_name,
        'cost': d.drink_cost
    } for d in drinks])

@bp.route('/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    drink = Drink.query.get_or_404(drink_id)  # This will return a 404 if the drink doesn't exist
    db.session.delete(drink)
    db.session.commit()
    return jsonify({'message': 'Drink removed successfully'})

@bp.route('/order', methods=['POST'])
def add_drink_order():
    data = request.json
    staff = Staff.query.get_or_404(data['staff_id'])
    drink = Drink.query.get_or_404(data['drink_id'])
    
    new_order = DrinkOrder(staff_id=staff.id, drink_id=drink.id)
    staff.drink_tab += drink.drink_cost
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({
        'message': 'Order added successfully',
        'staff_name': staff.staff_name,
        'drink': drink.drink_name,
        'cost': drink.drink_cost,
        'new_tab_total': staff.drink_tab
    })

@bp.route('/staff/<int:staff_id>/orders', methods=['GET'])
def get_staff_orders(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    orders = DrinkOrder.query.filter_by(staff_id=staff_id).all()
    return jsonify({
        'staff_name': staff.staff_name,
        'total_tab': staff.drink_tab,
        'orders': [{
            'drink': order.drink.drink_name,
            'cost': order.drink.drink_cost,
            'date': order.order_date.strftime('%Y-%m-%d %H:%M:%S')
        } for order in orders]
    })

@bp.route('/staff/<int:staff_id>/reset_tab', methods=['POST'])
def reset_tab(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    staff.drink_tab = 0.0  # Reset the drink tab to zero
    db.session.commit()
    return redirect(url_for('routes.index'))  # Redirect to the index page

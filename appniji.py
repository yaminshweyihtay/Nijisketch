from flask import Flask, render_template, request, redirect, url_for
from databasenijisketch import insert_reservation, get_all_reservations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menuniji.html')

@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
        guest_name = request.form['guest_name']
        guest_phone = request.form['guest_phone']
        guest_email = request.form['guest_email']
        reservation_date = request.form['reservation_date']
        reservation_time = request.form['reservation_time']
        num_guests = request.form['num_guests']
        special_requests = request.form['special_requests']
        
        insert_reservation(guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests)
        return redirect(url_for('reservations'))
    
    reservations = get_all_reservations()
    return render_template('reservation.html', reservations=reservations)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

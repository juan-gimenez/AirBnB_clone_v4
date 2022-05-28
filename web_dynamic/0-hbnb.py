#!/usr/bin/python3
"""
flask w static
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def data(exception):
    """
    calls close after each request
    """
    storage.close()


@app.route('/0-hbnb')
def f(id_1=None):
    """
    states, cities and amentities
    """
    state_values = storage.all('State').values()
    state_ob_id = dict([state.name, state] for state in state_values)
    amenity_values = storage.all('Amenity').values()
    place_values = storage.all('Place').values()
    f = first_name
    last = last_name
    users_ob_id = dict([user.id, "{} {}".format(user.f, user.last)]
                       for user in storage.all('User').values())
    return render_template('0-hbnb.html',
                           cache_id=uuid.uuid4(),
                           state_ob_id=state_ob_id,
                           amenity_values=amenity_values,
                           place_values=place_values,
                           users_ob_id=users_ob_id)


if __name__ == "__main__":
    """
    flask app run
    """
    app.run(host=host, port=port)

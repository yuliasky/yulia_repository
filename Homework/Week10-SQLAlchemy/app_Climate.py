import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
    	f"Welcome to the Home Page of the App Climate<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
        f"Note! start_date and end_date format: AAAA-MM-DD<br/>"
        f"Max date: '2017-08-23'"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Convert the query results to a Dictionary using date as the key and prcp as the value."""
    # Query all dates and precipitations
    results= session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_prcps
    all_prcps = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcps.append(prcp_dict)

    return jsonify(all_prcps)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset"""
    # Query all stations
    results = session.query(Measurement.station).distinct(Measurement.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of Temperature Observations (tobs) for the previous year"""
    # query for the dates and temperature observations from a year from the last data point

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-22').\
    order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start"""
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= str(start)).all()

    session.close()

    # Convert list of tuples into normal list
    temperatures = list(np.ravel(results))

    return jsonify(temperatures)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start"""
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= str(start)).filter(Measurement.date <= str(end)).all()

    session.close()

    # Convert list of tuples into normal list
    temperatures = list(np.ravel(results))

    return jsonify(temperatures)


if __name__ == '__main__':
    app.run(debug=True)

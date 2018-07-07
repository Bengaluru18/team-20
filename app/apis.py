from app import app, api, db
from flask_restful import Resource, reqparse
from .models import appointment, specialist, unavailability, patient
import json
#Profiles.query.filter_by(username= current_user.username).first()
colors = {"approved": "green", "done": "grey", "pending": "yellow"}


class Event():
    def __init__(self, appointment):

        def get_title():
            name = specialist.query.filter_by(
                sid=appointment.sid).first().sname
            return name

        def get_start():

            time_t = str(appointment.timing)
            y = time_t.replace(" ", "T")
            return y

        def get_color():
            return colors[appointment.status]

        def get_text_color():
            return "white"

        self.id = appointment.aid
        self.title = get_title()
        self.start = get_start()
        self.color = get_color()
        self.textColor = get_text_color()


class Appointment(Resource):
    def get(self):
        parser = reqparse.RequestParser()

        req_args = ['timing', 'pid', 'sid']

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)

        query = appointment.query
        if args.timing:
            query = appointment.query.filter_by(timing=args.timing)

        if args.pid:
            query = appointment.query.filter_by(pid=args.pid)

        if args.sid:
            query = appointment.query.filter_by(sid=args.sid)

        appointments = query.all()

        print appointments
        events = []
        for appt in appointments:
            events.append((Event(appt).__dict__))

        response = {"events": events}
        if len(events) == 0:
            return "No Record Found"
        return response["events"]

    def post(self):
        parser = reqparse.RequestParser()
        req_args = ['aid', 'timing', 'pid', 'sid', 'status']

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)
        existing_appointment = None
        if args.pid:
            existing_appointment = appointment.query.filter_by(
                aid=args.aid).first()

        if existing_appointment is not None:
            existing_appointment.status
            db.session.commit()
            return "Updated {}".format(args.aid)
        else:
            new_appointment = appointment(
                aid=args.aid, timing=args.timing, sid=args.sid, status=args.status, pid=args.pid)
            db.session.add(new_appointment)
            db.session.commit()
            return "Created {}".format(args.aid)


class Unavail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        req_args = ['sid', 'startdate', 'enddate']

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()

        new_unavail = unavailability( sid = args.sid, startdate = args.startdate, enddate = args.enddate)
        db.session.add(new_unavail)
        db.session.commit()

        return "Add {} - {}".format(args.startdate, args.enddate)

class Patient (Resource):
    def get(self):
        parser = reqparse.RequestParser()

        req_args = ['pid', 'pname', 'dob', 'parent_name', 'phno', 'address' ]

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)
        query = patient.query
        if args.timing:
            query = patient.query.filter_by(timing=args.pid)

        if args.pid:
            query = patient.query.filter_by(pid=args.pname)

        if args.sid:
            query = patient.query.filter_by(sid=args.dob)

        if args.timing:
            query = patient.query.filter_by(timing=args.parent_name)

        if args.pid:
            query = patient.query.filter_by(pid=args.phno)

        if args.sid:
            query = patient.query.filter_by(sid=args.address)

        patients = query.all()
        data = []
        for p in patients:
            data.append(p.__dict__)

        response = {"patients": data}
        return response["patients"]

    def post(self):
        parser = reqparse.RequestParser()

        req_args = ['pid', 'pname', 'dob', 'parent_name', 'phno', 'address' ]

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)
        new_patient = patient.query.filter_by(pid= args.pid).first()

        if new_patient is not None:
            new_patient = patient(pid = args.pid, pname = args.pname, phno = args.phno, address= args.address, dob=args.dob, parent_name= args.dob)
            db.session.add(new_patient)
            db.session.commit()
            return "added {}".format(args.pname)

        


        




api.add_resource(Appointment, '/api/event')
api.add_resource(Unavail, '/api/unavail')
api.add_resource()

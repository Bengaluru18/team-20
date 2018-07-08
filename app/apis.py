from app import app, api, db
from flask_restful import Resource, reqparse
from flask import jsonify
from .models import appointment, specialist, unavail, patient
import json
from datetime import datetime
from sqlalchemy import func


#Profiles.query.filter_by(username= current_user.username).first()
colors = {"Approved": "green", "done": "grey", "pending": "yellow"}


class Event():
    def __init__(self, appointment):

        def get_title():
            name = specialist.query.filter_by(
                sid=appointment.sid).first().sname
            return appointment.pid

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
            query = query.filter(appointment.timing==args.timing)

        if args.pid:
            query = query.filter(appointment.pid==args.pid)

        if args.sid:
            query = query.filter(appointment.sid==args.sid)

        appointments = query.all()

       # print appointments
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
            existing_appointment.status = 'Approved'
            db.session.commit()
            return "Updated {}".format(args.aid)

        elif args.timing is not None:
            new_datetime_object = datetime.strptime(args.timing,"%Y-%m-%d %H:%M:%S")
            
            slots = unavail.query.filter_by(sid = args.sid).all()

            for s in slots:
                start_time_obj = datetime.strptime(str(s.start_date), "%Y-%m-%d %H:%M:%S")
                end_time_obj = datetime.strptime(str(s.end_date), "%Y-%m-%d %H:%M:%S")
                if ( new_datetime_object > start_time_obj  and new_datetime_object < end_time_obj):
                    return "Appointed Slot Unavailable", 301
            
        
            new_appointment = appointment(
                aid=args.aid, timing=args.timing, sid=args.sid, status=args.status, pid=args.pid)
            db.session.add(new_appointment)
            db.session.commit()
            return "Created {}".format(args.aid)

        else:
            existing_appointment.status= 'Approved'
            db.session.commit()
            return "Created {}".format(args.aid)

    def delete(self):
        parser = reqparse.RequestParser()
        req_args = ['aid']

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)
        apt = appointment.query.filter_by(aid = args.aid).first()

        db.session.delete(apt)
        db.session.commit()
        return "{} deleted.".format(args.aid)
        




class Unavail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        req_args = ['sid', 'start_date', 'end_date']

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()

        new_unavail = unavail( sid = args.sid, start_date = args.start_date, end_date = args.end_date)
        db.session.add(new_unavail)
        db.session.commit()

        return "Add {} - {}".format(args.start_date, args.end_date)

    def delete(self):
        parser = reqparse.RequestParser()
        req_args = ['sid']

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)
        apt = unavail.query.filter_by(sid = args.sid).all()
        for a in apt:
            db.session.delete(a)
        db.session.commit()
        return "deleted"

class Patient (Resource):
    def get(self):
        parser = reqparse.RequestParser()

        req_args = ['pid', 'pname', 'dob', 'parent_name', 'phno', 'address', 'comment' ]

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        # print (args)
        query = patient.query
        if args.pid:
            query = patient.query.filter_by(pid=args.pid).all()

        if args.pname:
            query = patient.query.filter_by(pname=args.pname).all()

        if args.dob:
            query = patient.query.filter_by(dob=args.dob).all()

        if args.parent_name:
            query = patient.query.filter_by(parent_name=args.parent_name).all()

        if args.phno:
            query = patient.query.filter_by(phno=args.phno).all()

        if args.address:
            query = patient.query.filter_by(address=args.address).all()

        if args.comment:
            query = patient.query.filter_by(comment=args.comment).all()

        patients = query.all()
        data = []
        for p in patients:
            fe_dict = p.__dict__
            del fe_dict['_sa_instance_state']
            data.append( fe_dict)

        response = {"patients": data}
        return response["patients"]

    def post(self):
        parser = reqparse.RequestParser()

        req_args = ['pid', 'pname', 'dob', 'parent_name', 'phno', 'address', 'comment' ]

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)
        new_patient = patient.query.filter_by(pid= args.pid).first()

        if new_patient is None:
            new_patient = patient(pname = args.pname, phno = args.phno, address= args.address, dob=args.dob, parent_name= args.dob, comment =args.comment)
            db.session.add(new_patient)
            db.session.commit()
            return "added {}".format(args.pname)

    def delete(self):
        parser = reqparse.RequestParser()
        req_args = ['pid']

        for r in req_args:
            parser.add_argument(r)
        args = parser.parse_args()
        print (args)
        apt = patient.query.filter_by(pid = args.pid).first()
        
        db.session.delete(apt)
        db.session.commit()
        return "deleted {}".format(args.pid)

        


        




api.add_resource(Appointment, '/api/event')
api.add_resource(Unavail, '/api/unavail')
api.add_resource(Patient,'/api/patient')

from flask import *
from app_master.config import *
from flask_sqlalchemy import *
import boto3
from apscheduler.schedulers.background import BackgroundScheduler

app_master = Flask(__name__)
app_master.config.from_object(Config)

db = SQLAlchemy(app_master)

# AWS services
cw_client = boto3.client('cloudwatch', **AWS_CONNECTION_ARGS)
ec2_resource = boto3.resource('ec2', **AWS_CONNECTION_ARGS)
ec2_client = boto3.client('ec2', **AWS_CONNECTION_ARGS)
s3_resource = boto3.resource('s3', **AWS_CONNECTION_ARGS)
elb_client = boto3.client('elb', **AWS_CONNECTION_ARGS)

from app_master import routes

# scheduler, it will be used for periodic (2 min) checks for auto scaling
scheduler = BackgroundScheduler()
job = scheduler.add_job(routes.autoScaling, 'interval', minutes=2)
scheduler.start()

import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://ec2-35-154-176-120.ap-south-1.compute.amazonaws.com:27017/sports_feed_stg')  # Replace with your MongoDB URI
    
from pymongo import MongoClient
import json
uri = "mongodb+srv://Aftab355201:Aftab355201@cluster0.cn5rpym.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
database = client.get_database("Hospital_Langgraph")
Appointment = database.get_collection("Appointment")
Doctor = database.get_collection("Doctor")

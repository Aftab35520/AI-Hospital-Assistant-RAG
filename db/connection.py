from pymongo import MongoClient
import json
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
database = client.get_database("Hospital_Langgraph")
Appointment = database.get_collection("Appointment")
Doctor = database.get_collection("Doctor")

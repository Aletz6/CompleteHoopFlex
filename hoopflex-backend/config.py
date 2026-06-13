from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["hoopflex"]

collection_logs = db["trainingLogs"]
collection_sync_changes = db["syncChanges"]
collection_routines = db["rutinas"]
collection_achievements = db["achievements"]
collection_unlocked = db["unlockedAchievements"]
collection_profiles = db["userProfiles"]
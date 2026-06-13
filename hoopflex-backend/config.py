from pymongo import MongoClient

client = MongoClient("mongodb+srv://hoopflex:kamikazi@hoopflex.cxtvprh.mongodb.net/?appName=HoopFlex")
db = client["hoopflex"]

collection_logs = db["trainingLogs"]
collection_sync_changes = db["syncChanges"]
collection_routines = db["rutinas"]
collection_achievements = db["achievements"]
collection_unlocked = db["unlockedAchievements"]
collection_profiles = db["userProfiles"]

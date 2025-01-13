import pickle

gameOption = {
    "Sound" : 8,
    "VideoQuality" : "HIGH",
    "Money" : 100000,
    "WeaponList" : ["gun", "missile", "knife"]
}

file = open("text_file/save.p", "wb")
pickle.dump( gameOption, file)
file.close()
import requests
import json
import pandas as pd

csvOutput = {
    "id": [],
    "market.transactionCount": [],
    "name": [],
    "gender": [],
    "ethnicity": [],
    "state": [],
    "country": [],
    "birthYear": [],
    "birthMonth": [],
    "diseaseYear": [],
    "diseaseMonth": [],
    "symptoms": [],
    "medicalHistory": [],
    "familyHistory": [],
    "lifestyle": [],
    "tests": [],
    "struggle": [],
    "otherInfo": [],
    "primaryBodySystem": [],
    "primaryComplaint": [],
    "picnicHealth": [],
    "solutionOnly": [],
    "confirmedDiagnosis": [],
    "reward": [],
    "reported": [],
    "resolved": [],
    "active": [],
    "initialPackagePurchased": [],
    "packagePurchased": [],
    "started": [],
    "moderator": [],
    "age": [],
    "began": [],
    "location": [],
    "daysActive": [],
    "ratings": [],  # dump
    "allRatings": [],  # dump
    "maxReward": [],
    "invitedMds": [],  # dump
    "firedModerators": [],  # dump
    "uploads": [],  # dump
    "patientChats": [],  # dump
    "dicomImages": [],  # dump
    "bodySystems": [],  # dump
    "oldPatientDiagnoses": [],  # dump
    "partialDiagnoses": [],  # dump
    "falseDiagnoses": [],  # dump
    "medications": [],  # dump
}


def getJson(_id):
    url = 'https://www.crowdmed.com/case/{}'.format(_id)
    print(url)
    r = requests.get(url)
    return r.json()


def writeOutput():
    df = pd.DataFrame(csvOutput)
    df.to_csv('out.csv', index=False)


def appendJson(obj):
    csvOutput["id"].append(obj["id"])
    csvOutput["market.transactionCount"].append(
        obj["market"]["transactionCount"])
    csvOutput["name"].append(obj["name"])
    csvOutput["gender"].append(obj["gender"])
    csvOutput["ethnicity"].append(obj["ethnicity"])
    csvOutput["state"].append(obj["state"])
    csvOutput["country"].append(obj["country"])
    csvOutput["birthYear"].append(obj["birthYear"])
    csvOutput["birthMonth"].append(obj["birthMonth"])
    csvOutput["diseaseYear"].append(obj["diseaseYear"])
    csvOutput["diseaseMonth"].append(obj["diseaseMonth"])
    csvOutput["symptoms"].append(obj["symptoms"])
    csvOutput["medicalHistory"].append(obj["medicalHistory"])
    csvOutput["familyHistory"].append(obj["familyHistory"])
    csvOutput["lifestyle"].append(obj["lifestyle"])
    csvOutput["tests"].append(obj["tests"])
    csvOutput["struggle"].append(obj["struggle"])
    csvOutput["otherInfo"].append(obj["otherInfo"])
    csvOutput["primaryBodySystem"].append(obj["primaryBodySystem"])
    csvOutput["primaryComplaint"].append(obj["primaryComplaint"])
    csvOutput["picnicHealth"].append(obj["picnicHealth"])
    csvOutput["solutionOnly"].append(obj["solutionOnly"])
    csvOutput["confirmedDiagnosis"].append(obj["confirmedDiagnosis"])
    csvOutput["reward"].append(obj["reward"])
    csvOutput["reported"].append(obj["reported"])
    csvOutput["resolved"].append(obj["resolved"])
    csvOutput["active"].append(obj["active"])
    csvOutput["initialPackagePurchased"].append(obj["initialPackagePurchased"])
    csvOutput["packagePurchased"].append(obj["packagePurchased"])
    csvOutput["started"].append(obj["started"])
    csvOutput["moderator"].append(obj["moderator"])
    csvOutput["age"].append(obj["age"])
    csvOutput["began"].append(obj["began"])
    csvOutput["location"].append(obj["location"])
    csvOutput["daysActive"].append(obj["daysActive"])
    csvOutput["maxReward"].append(obj["maxReward"])
    csvOutput["invitedMds"].append(json.dumps(obj["invitedMds"]))
    csvOutput["firedModerators"].append(json.dumps(obj["firedModerators"]))
    csvOutput["uploads"].append(json.dumps(obj["uploads"]))
    csvOutput["patientChats"].append(json.dumps(obj["patientChats"]))
    csvOutput["dicomImages"].append(json.dumps(obj["dicomImages"]))
    csvOutput["bodySystems"].append(json.dumps(obj["bodySystems"]))
    csvOutput["oldPatientDiagnoses"].append(
        json.dumps(obj["oldPatientDiagnoses"]))
    csvOutput["partialDiagnoses"].append(json.dumps(obj["partialDiagnoses"]))
    csvOutput["falseDiagnoses"].append(json.dumps(obj["falseDiagnoses"]))
    csvOutput["medications"].append(json.dumps(obj["medications"]))
    csvOutput["ratings"].append(json.dumps(obj["ratings"]))
    csvOutput["allRatings"].append(json.dumps(obj["allRatings"]))


def readInput():
    file1 = open('temp', 'r')
    ans = set()
    lines = file1.readlines()
    for l in lines:
        ans.add(l.strip())
    file1.close()
    return ans


allCaseIds = readInput()
print(len(allCaseIds))
# for caseId in allCaseIds:
#     out = getJson(caseId)
#     appendJson(out)
#     writeOutput()

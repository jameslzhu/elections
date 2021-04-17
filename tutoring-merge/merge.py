import json
import sys

def writeJSONtoFile(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def readJSONtoDict(file):
    with open(file, 'r') as f:
        return json.load(f)

#purely for readability, this is a one-line job
def mergeCourseNames(web, rails):
    return rails["courseName"]

def mergeTutors(web, rails):
    #add all hkn-web tutors + info
    webNames = {}
    for tutor in web["tutors"]:
        cache = {}
        for element in ["name", "timeSlots", "officePrefs", "adjacentPref", "numAssignments"]:
            cache[element] = tutor[element]
        webNames[cache["name"]] = cache

    #add all hkn-rails tutors + info
    railNames = {}
    for tutor in rails["tutors"]:
        cache = {}
        for element in ["name", "tid", "courses"]:
            cache[element] = tutor[element]
        railNames[cache["name"]] = cache

    not_matched_rails = []
    for name in webNames.keys():
        if name in railNames:
            keys = railNames[name].keys()
            for key in keys:
                webNames[name][key] = railNames[name][key]
        else:
            not_matched_rails += [name]

    not_matched_web = []
    for name in railNames.keys():
        if not name in webNames:
            not_matched_web += [name]

    mergedTutors = list(webNames.values())
    return mergedTutors, not_matched_rails, not_matched_web

def mergeSlots(web, rails):
    #create dictionary for both web and rails that maps the tuple
    # (hour, day) to the corresponding data in each database
    webDict = {}
    for element in web["slots"]:
        cache = {}
        for key in element:
            if not key in ["hour", "day"]:
                cache[key] = element[key]
        webDict[(element["hour"], element["day"])] = cache

    railsDict = {}
    for element in rails["slots"]:
        if element["office"] == "Cory":
            cache = {}
            for key in element:
                if not key in ["hour", "day"]:
                    cache[key] = element[key]
            railsDict[(element["hour"], element["day"][:3])] = cache

    #map web slot ids to rails slot ids
    webIDtorailsID = {}
    for key in webDict:
        webID = webDict[key]["sid"]
        if key in railsDict:
            railsID = railsDict[key]["sid"]
        webIDtorailsID[webID] = railsID

    mergedList = []
    errors = []
    for key in webDict:
        if key in railsDict:
            merge = {}
            merge["hour"] = key[0]
            merge["name"] = railsDict[key]["name"]
            merge["day"] = key[1]
            merge["office"] = webDict[key]["office"]
            merge["courses"] = [0] * len(railsDict[key]["courses"])
            merge["adjacentSlotIDs"] = [webIDtorailsID[id] for id in webDict[key]["adjacentSlotIDs"]]
            merge["sid"] = railsDict[key]["sid"]
            mergedList += [merge]
        else:
            errors += [key]
    return mergedList, errors

if __name__ == "__main__":
    if len(sys.argv) == 1:
        outfile = "DESTINATION_NAME.json"
        railsfile = "hkn-rails-tutoring.json"
        webfile = "hknweb-tutoring.json"
    elif len(sys.argv) == 4:
        outfile = sys.argv[3]
        railsfile = sys.argv[2]
        webfile = sys.argv[1]
    else:
        print("Error - please specify three file names in order of web JSON, rails JSON, and destination JSON")

    webJSON = readJSONtoDict(webfile)
    railsJSON = readJSONtoDict(railsfile)
    outJSON = {}
    outJSON["courseName"] = mergeCourseNames(webJSON, railsJSON)
    outJSON["tutors"], notInRails, notInWeb = mergeTutors(webJSON, railsJSON)
    outJSON["slots"], errors = mergeSlots(webJSON, railsJSON)
    """ Uncomment or comment for error output
    print("Tutors exist in hkn-web but not in hkn-rails")
    print(notInRails)
    print("Tutors exist in hkn-rails but not in hkn-web")
    print(notInWeb)
    print("(Hour, Day) entries in hkn-web but not in hkn-rails")
    print(errors)
    """
    writeJSONtoFile(outJSON, outfile)

import pandas as pd


def proceed():
    txt = input(
        "If you want to review the format of the designed document, type 'help'.\nIf you want to quit, type 'q'.\n"
        "Otherwise, press enter to continue.\n"
        "> ")
    if txt == 'q':
        quit()
    elif txt == 'help':
        get_help()
    else:
        pass


def check_csv(txt):
    if txt[-4:] != ".csv":
        print("\n**Please input a .csv file within your folder.")
        return True
    return False


def read_file(prompt):
    f = input("\nWhat's the name of the .csv file {0}Exp: analysis.csv \n".format(prompt) +
              "> ")
    if check_csv(f):
        proceed()
        return read_file(prompt)
    else:
        return process_file(f, prompt)


def process_file(f, prompt):
    try:
        if prompt == "that you want to label? ":
            response = pd.read_csv("{0}".format(f)).T.to_dict()
        else:
            response = pd.read_csv("{0}".format(f)).to_dict()
    except IOError:
        print(
            "\n**Cannot find {0} in the directory. Please make sure the file is in the folder and renter the file name.".format(
                f))
        proceed()
        return read_file(prompt)
    return response


def get_referrer(name, response):
    if (not pd.isna(name)) and str(name).lower() in response.lower():
        return True


def label_one(answer, labels, marked):
    label = ""
    for key in labels:
        for name in labels[key].values():
            if not pd.isna(answer) and key not in marked and get_referrer(name, answer):
                label = key
    return label


def label(response, labels):
    try:
        for k in range(len(response)):
            answer = response[k]['Source']
            marked = []
            for i in range(1, 4):
                label = label_one(answer, labels, marked)
                marked.append(label)
                response[k]["label{0}".format(i)] = label
        return response
    except Exception:
        print("\n**Wrong input file format.\n")
        proceed()


def analysis(response, labels):
    dict = {}
    try:
        for i in range(len(response)):
            labels = []
            labels.append(response[i]["label1"])
            labels.append(response[i]["label2"])
            labels.append(response[i]["label3"])
            for label in labels:
                if label not in dict.keys():
                    dict[label] = 1
                else:
                    dict[label] += 1
            dict.pop("")
            return dict
    except Exception:
        print("\n**Wrong input file format.\n")
        proceed()


def get_help():
    print("------------------\n"
          "Input file (csv):\n"
          "File to be labeled: There should be a column named 'Source' for all entries that needs to be labeled.\n"
          "Each entry should be a row in the column, and the labels assigned by this program will appear to the\nright of that column in a newly created file called 'LABELED_FILE.csv'.\n\n"
          "------------------\n"
          "File containing the labels (csv):\n"
          "The columns should be named by the labels, and key words associated with that label should be in the column.\n"
          "This program will help you count how many times each label is assigned in the input and return a result in For example:\n"
          "Fruits\t|\tMeat\n"
          "----------------\n"
          "Apple\t|\tBeef\n"
          "Peach\t|\tPork\n"
          "Melon\t|\tLamb\n\n"
          "----------------\n")
    proceed()


while True:
    txt = input(
        "Welcome to automatic labeling. Please dragged the .csv file you want to label and the .csv file containing labels into this folder."
        "Type in a command to continue. \n "
        "Common commands:\n"
        "'label' -- label your input and return the stats\n"
        "'help' -- understand the input format for files\n"
        "'q' -- quit the program\n"
        "> ")
    if txt == "q":
        quit()
    if txt == "label":
        response = read_file("that you want to label? ")
        labels = read_file("containing the labels? ")
        label(response, labels)
        output = analysis(response, labels)
        labeledFile = pd.DataFrame(data=response).T
        stats = pd.DataFrame(data=output, index=[0]).T
        labeledFile.to_csv('LABELED_FILE.csv', index=False, encoding='utf-8')
        stats.to_csv('STATS.csv', encoding='utf-8')
        print("Please check 'LABELED_FILE.csv' and 'STATS.csv' in the current folder for labeling results")
        break
    if txt == "help":
        get_help()
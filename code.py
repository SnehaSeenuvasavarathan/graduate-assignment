import os
import re
import sys
import shutil
from git import Repo
from fnmatch import fnmatch
from tree_sitter import Language, Parser
import enchant
import numpy as np
import inbuilt_list
from inbuilt_list import python_list, javascript_list, ruby_list, go_list
# pip install pyenchant==2.0.0

def prep_parser(lang):
    Language.build_library(
      # Store the library in the `build` directory
      'build/my-languages.so',

      # Include one or more languages
      [
        'tree-sitter-go',
        'tree-sitter-javascript',
        'tree-sitter-python',
        'tree-sitter-ruby'
      ]
    )
    SELECTED_LANGUAGE = Language('build/my-languages.so', lang)
    parser = Parser()
    parser.set_language(SELECTED_LANGUAGE)
    return parser, SELECTED_LANGUAGE

def clone_repo(url):
    Repo.clone_from(url, 'gitRepo/')

def load_file_list(ext):
    file_list = []
    root = os.getcwd() + '/gitRepo'
    pattern = "*" + ext
    for path, _, files in os.walk(root):
        for file in files:
            if fnmatch(file, pattern):
                a = 'gitRepo' + (path+'/'+file).split('gitRepo')[1]
                print(a)
                file_list.append(a)
    return file_list

def parse_file(parser, file):
    with open(file) as f:
        lines = f.readlines()
        source_code = bytes(''.join(lines), 'utf-8')
        code_list = lines
    tree = parser.parse(source_code)
    return tree, source_code, code_list

def find_identifiers(LANGUAGE, tree, code_list):
    identifier_details = []
    query = LANGUAGE.query("""
    ((identifier) @identifier)
    """)
    captures = query.captures(tree.root_node)
    print()
    for c in captures:
        print("Start", c[0].start_point, "End", c[0].end_point)
        node_text = code_list[c[0].start_point[0]][c[0].start_point[1]:c[0].end_point[1]]
        print(node_text)
        identifier_details.append({"ID": node_text, "Line": c[0].start_point[0],
                                   "Start Column": c[0].start_point[1], "End Column": c[0].end_point[1]})
    print(identifier_details)
    return identifier_details

def validate_identifiers(identifier_details, lang):
    error_identifiers = []
    options={'python':python_list,'javascript':javascript_list,'ruby':ruby_list,'go':go_list}
    builtin_list=options[lang]+['c', 'd', 'e', 'g', 'in','i', 'out', 'inOut','j','k','m','n','o','t','x','y','z']


    for identifier in identifier_details:
        name = identifier['ID']
        if name in builtin_list:
            continue
        else:
            if '_' in name:
                res_list=[s for s in re.split("_", name) if s]
            else:
                res_list=[s for s in re.split("([A-Z][^A-Z]*)", name) if s]

            # capitalization error and naming convention anomaly
            if '_' not in name and (re.search(r'^[a-z0-9_]*[A-Z]{2,}[a-z0-9_]*', name) or name.islower()):
                error_identifiers.append([identifier," Capital Error"])
            else:
                all_upper=[x.upper() for x in res_list]
                all_lower=[x.lower() for x in res_list]
                if res_list!=all_upper and res_list!=all_lower and '_' in name:
                    error_identifiers.append([identifier," Naming convention anomaly"])

            # check for consecutive underscores
            for i in range(len(name)-1):
                if name[i]=='_' and name[i+1]=='_':
                    error_identifiers.append([identifier," consecutive underscore"])
                    break

            # check against dictionary words

            d = enchant.Dict("en_US")
            acronyms=['AWS','AES','AP','API','CLI','DDOS','FTP','IP','ISP','LAN','MDM','MFA','RDP','SSO','AD','AI','AMD',
            'ASCII','BASIC','BIOS','DDL','GNU','GSM','GUI','SQL','TCP','UDP','HTML','XHTML','WWW','VOIP']
            acronyms=[a.lower() for a in acronyms]
            if (d.check(name.lower()) or np.prod([d.check(x.lower()) for x in res_list]) or name.lower() in acronyms):
                pass
            else:
                error_identifiers.append([identifier," not a dictionary word"])


            # check for excessive words and Number of words
            if len(res_list)>4:
                error_identifiers.append(name," Excessive wordse")
            elif len(res_list)<2:
                error_identifiers.append([identifier," Less than 2 words"])

            #External underscore
            if name[0]=='_' and name[len(name)-1]=='_':
                error_identifiers.append([identifier," Leading and Trailing underscore"])

            #identifier encoding
            typePrefixes=['int', 'float','char', 'byte', 'long', 'arr', 'str','byte','bool','b','i', 'f','c','l','s']

            if any(item in typePrefixes for item in res_list):
                error_identifiers.append([identifier," No Hungarian notation"])

            #Long identifier
            if len(res_list)>4:
                error_identifiers.append(name," Long Identifier")
            #Less than 8 characters
            if name not in ['c', 'd', 'e', 'g', 'in','i', 'out', 'inOut','j','k','m','n','o','t','x','y','z']:
                if len(name)<8:
                    error_identifiers.append([identifier," Short identifier name"])

            #No numbers
            listOfnames=["one","two","three","four","five","six","seven","eight","nine", "ten",
                         "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                         "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty","sixty", "seventy",
                         "eighty","ninety", "hundred", "thousand"]
            lowName = name.lower()

            if '_' in lowName:
                res_list=[s for s in re.split("_", lowName) if s]
            else:
                res_list=[s for s in re.split("([A-Z][^A-Z]*)", lowName) if s]
                if all(item in listOfnames for item in res_list):
                    error_identifiers.append([identifier," Numeric identifier name"])

    return error_identifiers



def main():

    url = sys.argv[1]
    ext = sys.argv[2]
    lang = sys.argv[3]
    op1 = sys.argv[4]
    op2 = sys.argv[5]

    print(url)
    print(ext)
    print(lang)

    if os.path.exists(op1):
        pass
    else:
        print("Output 1 Path does not exist. Saving in current directory...")
        op1 = ''
    if os.path.exists(op2):
        pass
    else:
        print("Output 2 Path does not exist. Saving in current directory...")
        op2 = ''
    if os.path.exists(op1+"output1.txt"):
        print('deleting file1')
        print(os.remove(op1+"output1.txt"))
    if os.path.exists(op2+"output2.txt"):
        print('deleting file1')
        print(os.remove(op2+"output2.txt"))

    # clear
    if os.path.exists(os.getcwd() + '/gitRepo') and os.path.isdir(os.getcwd() + '/gitRepo'):
        print('deleting dir..')
        shutil.rmtree(os.getcwd() + '/gitRepo')

    # setting up the parser
    parser, LANGUAGE = prep_parser(lang)

    # cloning repo
    clone_repo(url)

    # load files from Repo
    file_list = load_file_list(ext)

    # parse the files in file_list
    for file in file_list:
        tree, source_code, code_list = parse_file(parser, file)

        identifier_details = find_identifiers(LANGUAGE, tree, code_list)
        with open (op1+'output1.txt', 'a') as f:
            for identifier in identifier_details:
                    a = str('File: ' + file + ' Identifier: '+identifier['ID']+' Line: '+str(identifier['Line'])+
                            ' Start Column: '+str(identifier['Start Column'])+ ' End Column: '+str(identifier['End Column'])+'\n')
                    f.write(a)

        error_identifiers = validate_identifiers(identifier_details, lang)
        with open (op2+'output2.txt', 'a') as f:
            for identifier in error_identifiers:
                    a = str('File: ' + file +' Identifier: '+identifier[0]['ID']+ ' Error: '+identifier[1]+' Line: '
                    +str(identifier[0]['Line'])+' Start Column: '+str(identifier[0]['Start Column'])+
                     ' End Column: '+str(identifier[0]['End Column'])+'\n')
                    f.write(a)

if __name__ == "__main__":
    main()

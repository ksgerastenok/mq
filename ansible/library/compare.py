#from ansible.module_utils.basic import *

try:
    import re as re
    import ansible.module_utils.basic as basic
    reason = str()
except Exception as ex:
    import re as re
    import yaml as yaml
    reason = str(ex.message)


def mqsc2split(string):

    element = str()
    for line in string.splitlines():
        element += (str(line.decode("cp866").encode("utf-8")) + str("\n")) if((not(line.strip().startswith("*")))) else (str())

    result = list()
    for (i_item, item) in enumerate(re.compile("(((((\s*)(.*?)(\s*))(((\s*)([+])(\s*))|((\s*)([-])(\s*))))*)(((\s*)(.*?)(\s*))(((\s*)(\n)(\s*))|((\s*)($)(\s*)))))").findall(element.strip())):
        if((not(element.strip() in [str()]))):
            result.append(item[0].strip())

    return(result)


def mqsc2list(string):

    element = str()
    for line in string.splitlines():
        element += (str(line.decode("cp866").encode("utf-8")) + str(" ")) if((not(line.strip().endswith("+")))) else (str(line.replace("+", "").strip()) + str(" "))

    result = list()
    for (i_item, item) in enumerate(re.compile("((((\s*)(\w*)(\s*))|((\s*)(\d*)(\s*)))((((\s*)([(])(\s*))(((\s*)(['])(.*?)(['])(\s*))|((\s*)(.*?)(\s*)))((\s*)([)])(\s*)))?))").findall(element.strip())):
        if((not(element.strip() in [str()]))):
            result.append(item[2].upper().replace("ALTER", "DEFAULT").replace("DEFINE", "DEFAULT").split("@")[0].strip() + item[5].upper().replace("ALTER", "DEFAULT").replace("DEFINE", "DEFAULT").split("@")[0].strip())
            result.append(item[20].strip().replace("ALTER", "DEFAULT").replace("DEFINE", "DEFAULT").split("@")[0].strip() + item[23].strip().replace("ALTER", "DEFAULT").replace("DEFINE", "DEFAULT").split("@")[0].strip())

    return(result)


def hashmake(string):

    result = list()

    for (i_item, item) in enumerate(mqsc2split(string)):
        mqsc = mqsc2list(item)
        if((not(len(mqsc) in [0]))):
            element = dict()
            element["key"] = str()
            element["key"] += str(mqsc[0])
            element["key"] += str(mqsc[1])
            element["key"] += str(mqsc[2])
            element["key"] += str(mqsc[3])
            if((mqsc[2] in ["QMGR"])):
                element["key"] += str(mqsc[mqsc.index("CCSID") + 1])    if((not(mqsc.count("CCSID") in [0])))    else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("DEADQ") + 1])    if((not(mqsc.count("DEADQ") in [0])))    else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("CHLAUTH") + 1])  if((not(mqsc.count("CHLAUTH") in [0])))  else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("MAXMSGL") + 1])  if((not(mqsc.count("MAXMSGL") in [0])))  else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("CONNAUTH") + 1]) if((not(mqsc.count("CONNAUTH") in [0]))) else str("EMPTY")
            if((mqsc[2] in ["QLOCAL"])):
                element["key"] += str(mqsc[mqsc.index("USAGE") + 1])    if((not(mqsc.count("USAGE") in [0])))    else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("MAXMSGL") + 1])  if((not(mqsc.count("MAXMSGL") in [0])))  else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("TRIGDATA") + 1]) if((not(mqsc.count("TRIGDATA") in [0]))) else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("TRIGDPTH") + 1]) if((not(mqsc.count("TRIGDPTH") in [0]))) else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("TRIGMPRI") + 1]) if((not(mqsc.count("TRIGMPRI") in [0]))) else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("TRIGTYPE") + 1]) if((not(mqsc.count("TRIGTYPE") in [0]))) else str("EMPTY")
            if((mqsc[2] in ["QREMOTE"])):
                element["key"] += str(mqsc[mqsc.index("RNAME") + 1])   if((not(mqsc.count("RNAME") in [0])))   else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("XMITQ") + 1])   if((not(mqsc.count("XMITQ") in [0])))   else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("RQMNAME") + 1]) if((not(mqsc.count("RQMNAME") in [0]))) else str("EMPTY")
            if((mqsc[2] in ["QALIAS"])):
                element["key"] += str(mqsc[mqsc.index("TARGET") + 1])   if((not(mqsc.count("TARGET") in [0])))   else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("TARGTYPE") + 1]) if((not(mqsc.count("TARGTYPE") in [0]))) else str("EMPTY")
            if((mqsc[2] in ["CHANNEL"])):
                element["key"] += str(mqsc[mqsc.index("XMITQ") + 1])   if((not(mqsc.count("XMITQ") in [0])))   else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("CHLTYPE") + 1]) if((not(mqsc.count("CHLTYPE") in [0]))) else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("MAXMSGL") + 1]) if((not(mqsc.count("MAXMSGL") in [0]))) else str("EMPTY")
            if((mqsc[2] in ["LISTENER"])):
                element["key"] += str(mqsc[mqsc.index("TRPTYPE") + 1]) if((not(mqsc.count("TRPTYPE") in [0]))) else str("EMPTY")
            if((mqsc[2] in ["AUTHREC"])):
                element["key"] += str(mqsc[mqsc.index("GROUP") + 1])     if((not(mqsc.count("GROUP") in [0])))     else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("AUTHADD") + 1])   if((not(mqsc.count("AUTHADD") in [0])))   else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("OBJTYPE") + 1])   if((not(mqsc.count("OBJTYPE") in [0])))   else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("PROFILE") + 1])   if((not(mqsc.count("PROFILE") in [0])))   else str("EMPTY")
                element["key"] += str(mqsc[mqsc.index("PRINCIPAL") + 1]) if((not(mqsc.count("PRINCIPAL") in [0]))) else str("EMPTY")
            element["value"] = str()
            element["value"] += str(item.strip())
            result.append(element.copy())

    return(result)


def compare(params):

    result = str()

    src = open(params.get("src"), "rb").read()
    dest = open(params.get("dest"), "rb").read()
    hashsrc = hashmake(src)
    hashdest = hashmake(dest)
    for itemsrc in hashsrc:
        if((not(any(((itemsrc.get("key") in [itemdest.get("key")])) for itemdest in hashdest)))):
            result += (str(itemsrc.get("value")) + str("\n"))
    open(params.get("result"), "wb").write(result)
    open(params.get("result"), "wb").write(result)

    return(result)


def main():

    if((reason == str())):
        mod = basic.AnsibleModule({"src": {"type": "str", "required": True}, "dest": {"type": "str", "required": True}, "result": {"type": "str", "required": True}})
        compare(mod.params)
        mod.exit_json()
    else:
        params = yaml.load(open("mq.yml", "rb").read())
        compare(params.get("mq"))

    return


if((__name__ == "__main__")):
    main()

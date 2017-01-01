import re


ip_pattern = re.compile(r"[a-z]+|\[[a-z]+\]")


def has_abba(string):
    for i in range(len(string) - 3):
        a, b = string[i], string[i+1]
        c, d = string[i+2], string[i+3]
        if a == d and b == c and a != b:
            return True
    return False


def supports_tls(ip):
    strings = ip_pattern.findall(ip)
    result = False
    for string in strings:
        if string[0] == '[':
            if has_abba(string[1:-1]):
                return False
        else:
            result |= has_abba(string)
    return result


def abas(string):
    abas_found = []
    for i in range(len(string) - 2):
        a, b, c = string[i], string[i+1], string[i+2]
        if a == c and a != b:
            abas_found.append(string[i:i+3])
    return abas_found


def invert(triple):
    return "".join([triple[1], triple[2], triple[1]])


def supports_ssl(ip):
    strings = ip_pattern.findall(ip)

    babs_wanted = []
    for string in strings:
        if string[0] != '[':
            babs_wanted += [invert(triple) for triple in abas(string)]

    babs_found = []
    for string in strings:
        if string[0] == '[':
            babs_found += abas(string[1:-1])

    for bab in babs_found:
        if bab in babs_wanted:
            return True
    return False

if __name__ == '__main__':
    with open("day7.in") as f:
        ips = f.read().split("\n")
        if ips[-1] == "":
            del ips[-1]

    print(sum([1 for ip in ips if supports_tls(ip)]))
    print(sum([1 for ip in ips if supports_ssl(ip)]))

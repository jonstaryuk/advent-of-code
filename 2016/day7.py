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


if __name__ == '__main__':
    with open("day7.in") as f:
        ips = f.read().split("\n")
        if ips[-1] == "":
            del ips[-1]

    print(sum([1 for ip in ips if supports_tls(ip)]))

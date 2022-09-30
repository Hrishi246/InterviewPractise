def subdomainVisits(cpdomains):
    ref_dict = {}
    res = []
    for d in cpdomains:
        count, domain = int(d.split(" ")[0]),d.split(" ")[1]
        ref_dict[domain] = ref_dict.get(domain, 0) + count
        r = len(domain) - 1
        while r >= 0:
            if domain[r] == ".":
                ref_dict[domain[r+1:]] = ref_dict.get(domain[r + 1:], 0) + count
            r = r - 1
    for key,value in ref_dict.items():
        res.append(str(value)+" "+key)
    return res

print(subdomainVisits(["900 google.mail.com"]))
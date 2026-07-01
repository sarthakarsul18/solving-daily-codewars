def remove_url_anchor(url):
    n_url = ""
    if "#" not in url:
        return url
    else:
        for i in url:
            if i=="#":
                break
            else:
                n_url+=i
                
        return n_url
        
def new_resumes(existing_ids, names, urls):
    output = []
    for i, url in enumerate(urls):
        url_id = url[-5:]
        if int(url_id) not in existing_ids:
            output.append((names[i], url_id))
    return output

existing_ids = [15234, 20485, 34536, 95342, 94857]

names = ['Calvin', 'Jason', 'Cindy', 'Kevin']
urls = [
    'domain.com/resume/15234', 
    'domain.com/resume/23645', 
    'domain.com/resume/64337', 
    'domain.com/resume/34536',
]

print(new_resumes(existing_ids, names, urls))
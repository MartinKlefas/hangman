import http.client
def get_words():
    try:
        conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "8cf0eb0ea3msh3bb1762b245e7b6p148f6cjsn74972c17d84b",
            'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com"
            }

        conn.request("GET", "/words/?letterPattern=%5E%5Ba-zA-Z%5D%2B&limit=100&page=1&hasDetails=hasDetails", headers=headers)

        res = conn.getresponse()
        data = res.read()
        
        conn.close()

        return(data.decode("utf-8"))
    except:
        return["Apple","Banana","Pear","Orange","Plum"]
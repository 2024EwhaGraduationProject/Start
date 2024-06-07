data = {'title': title,
        'period': period,
        'postdate' : postdate,
        'modifydate': modifydate,
        'person': person,
        'view' : view,
        'category': category,
        'details': details,
        'section' : section,
        'process': process,
        'phonenum_yn': phonenum_yn,
        'phonenum' : phonenum,
        'place': place,
        'place_details': place_details,
        'state' : state,
        'image': image,
        'text': text
       }
data = pd.DataFrame(data)

data.info()
data.head()

data.to_csv('bunsilmul_0517.csv', index=False,encoding="utf-8-sig")

data['image']

def get_age(age):
    assert age >=20,  "age should be rater than 20"
    print('your age is :', age)

get_age(20)


def start(data: dict):
    assert isinstance(data, dict), 'data is not Dictionary type'
    assert data,'No data found'
    print("data loaded sucessfully")

json = {'name': 'patha'}
start(json)




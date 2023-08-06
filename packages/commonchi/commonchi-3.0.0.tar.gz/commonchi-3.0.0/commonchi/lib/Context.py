import datetime,random
class Context:
    #pass
    time_1=datetime.datetime.strftime(datetime.datetime.now(), "%m%d%H")
    random_n = ''.join(random.sample('123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRESTUVWXYZ', 3))
    random_num = time_1 + random_n
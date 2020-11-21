import re
str_names = ['이유덕','이재영','권종표','이재영','박민호','강상희','이재영','김지완','최승혁','이성연','박영서','박민호','전경헌','송정환','김재성','이유덕','전경헌']

def count(pattern):
    cnt = 0
    for name in str_names:
        if None != re.match(pattern, name):
            cnt += 1
    return cnt

print(count('^[김|이]+'))
print(count('^이재영'))
print(len(set(str_names)))
print(sorted(list(set(str_names))))

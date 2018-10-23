from contextlib import redirect_stdout
import re

regex = re.compile("RT")
with open("tweets.in", encoding="utf-8") as f:
    tweets = [line.strip() for line in f.readlines()]
    tweets.sort()
    tweets_rt = set()
    user_rt = set()
    dc = {}
    for line in tweets:
        if re.match(regex,line):
            tweets_rt.add(line)
            st_with_rt = re.findall(r"RT @\w+",line)
            tst = re.findall(r"https://[^\s]+",line)
            if len(st_with_rt) is not 0 and len(re.findall(r"https://\w+",line)) is not 0:
                st_with_rt[0] = st_with_rt[0].replace("RT ","")
                if st_with_rt[0] not in user_rt:
                    if len(tst) >=1 :
                        dc[st_with_rt[0]] = tst[0]
        
with open("tweets.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        for key,value in dc.items():
            print(key,"\t",value)
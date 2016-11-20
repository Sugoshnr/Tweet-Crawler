
# -*- coding: utf-8 -*-

import json
import datetime
import re


tweets = []
tweets_nrt=[]
for q in xrange(11,12):
    open_file=str(q)+"_9_16_usopen_finals_es.json"
    for line in open(open_file, 'r'):
        tweets.append(json.loads(line))
    final={}
    smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^) 
                 :D 8-D 8D x-D xD X-D XD =( =-D =D =-3 =3 B^D :( -_- (: ): :-v
                :-V :-w :-W :-r :-f :-p :-* :-T :-D :-P :-y :-o :-{ =| :-)
                :-# :-B :-| :-? <:> :-) :-J :*) :-8 :_) :( ;) :* """.split()

    pattern2 = "|".join(map(re.escape, smileys))

    kaomojis=u"""(-‿‿-) (￣▽￣) (ノ*ﾟ▽ﾟ*) ¯\_(ツ)_/¯ 🐬 🍑 👗 🎀 ⚫ 🐥 💜 🍂 ★ ಥ_ಥ ಸ‿ಸ ಠ_ಠ ((­_­;) (╯°□°）╯︵╯ ┻━┻ ヽ(￣▼￣*)ノ """.split()
    pattern3 = "|".join(map(re.escape, kaomojis))
    
    spec_char="""! ? . " # @ % & ( ) * + , - _ / :""".split()
    pattern4="|".join(map(re.escape, spec_char))
    for i in xrange(len(tweets)):
        final[i]={};
        #em=re.findall(u'('u'\ud83d[\udE00-\udfff]|'u'\ud83e[\ud000-\udd17])',tweets[i]['text'],re.UNICODE)
        #em=re.findall(u'(' u'\ud83c[\udf00-\udfff]|' u'\ud83d[\udc00-\ude4f\ude80-\udeff]|' u'[\u2600-\u26FF\u2700-\u27BF])+', re.UNICODE)
        myre= re.compile(u'(' u'\ud83c[\udf00-\udfff]|'u'\ud83d[\ude00-\udfff]|'u'\ud83e[\ud000-\udd17]|' u'[\u2600-\u26FF\u2700-\u27BF])+', re.UNICODE)
        em=myre.findall(tweets[i]['text'])
        sm=re.findall(pattern2,tweets[i]['text'].encode('raw_unicode_escape'))
        ka=re.findall(pattern3,tweets[i]['text'])
        x=em+sm+ka;
        emoticons=x
        date=datetime.datetime.strptime(str(tweets[i]['created_at']), '%a %b %d %H:%M:%S +%f %Y').strftime('%Y/%m/%dT%H:00:00Z')
        date1=datetime.datetime.strptime(date,'%Y/%m/%dT%H:00:00Z').isoformat()
        final[i]={'topic':'Sports','tweet_text':tweets[i]['text'],'tweet_lang':tweets[i]['lang'],'hashtags':[],'mentions':[],'tweet_urls':[],'tweet_emoticons':emoticons,'tweet_date':date1};
        if tweets[i]['entities']['hashtags']:
            for j in xrange(len(tweets[i]['entities']['hashtags'])):
                final[i]['hashtags'].append(tweets[i]['entities']['hashtags'][j]['text']);
        if tweets[i]['entities']['urls']:
            for j in xrange(len(tweets[i]['entities']['urls'])):
                final[i]['tweet_urls'].append(tweets[i]['entities']['urls'][j]['url']);
        if tweets[i]['entities']['user_mentions']:
            for j in xrange(len(tweets[i]['entities']['user_mentions'])):
                final[i]['mentions'].append(tweets[i]['entities']['user_mentions'][j]['screen_name']);
        if tweets[i]['geo'] is not None:
            x=str(tweets[i]['geo']['coordinates'][0]);y=str(tweets[i]['geo']['coordinates'][1])
            z=x+', '+y;
            #final[i]['tweet_loc']=tweets[i]['geo']['coordinates']
            final[i]['tweet_loc']=z;
        if 'media' in tweets[i]['entities'].keys():
            final[i]['tweet_urls'].append(tweets[i]['entities']['media'][0]['media_url'])
        final[i]['text_es']=final[i]['tweet_text'];
        for j in xrange(len(final[i]['hashtags'])):
            final[i]['text_es']=final[i]['text_es'].replace("#"+final[i]['hashtags'][j],"")
        for j in xrange(len(final[i]['mentions'])):
            final[i]['text_es']=final[i]['text_es'].replace("@"+final[i]['mentions'][j],"")
        for j in xrange(len(final[i]['tweet_urls'])):
            final[i]['text_es']=final[i]['text_es'].replace(final[i]['tweet_urls'][j],"")
        for j in xrange(len(final[i]['tweet_emoticons'])):
            final[i]['text_es']=final[i]['text_es'].replace(final[i]['tweet_emoticons'][j],"")
        final[i]['text_es']=re.sub(pattern4,"",final[i]['text_es'])
        #print i,'\n',final[i]['text_en'],'\n',final[i]['tweet_text'],'\n'


    x=[]
    for i in xrange(len(final)):
        x.append(final[i])
    s=json.dumps(x)
    with open("parsed_"+open_file,"w") as f:
        f.write(s)



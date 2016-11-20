
# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json

c_key=''
c_sec=''
a_tok=''
a_sec=''

class listener(StreamListener):
    
    def __init__(self):
        self.count=0;
        #es.count=0;
        #ko.count=0;
        #tr.count=0;
        
    def on_data(self,data):
            if ('retweeted_status' not in json.loads(data).keys()):
                x=json.loads(data)
                if(x['lang']=='en'):
                    #print data;
                    savefile=open("test.json","a")
                    savefile.write(data)
                    savefile.close()
                    self.count+=1
                    print self.count;
            return True
    
    def on_error(self,status):
        print status;

auth=OAuthHandler(c_key,c_sec)
auth.set_access_token(a_tok,a_sec)
stream=Stream(auth,listener())


stream.filter(languages=['en','es','ko','tr'],track=['hillary','clinton','potus','trump','hilary2016','trump2016','makeamericagreatagain',u'클린턴',u'도날드 트럼프'])
#stream.filter(languages=['ko'],track=['appleevent','iphone7','airpod','iphone',u'아이폰',u'애플 이벤트'])
#stream.filter(languages=['ko'],track=['usopen','espntennis','espn tennis',u'US오픈'])
#stream.filter(languages=['tr'],track=['syriancivilwar','syria','pray4syria','prayforsyria','refuge','syriacrisis','refugecrisis','syrianconflict','syriawar','syriaconflict','suriye'])



#Turk==== Syria-Suriye; 
#Korea==== Iphone-아이폰, appleevent-애플 이벤트,clinton-클린턴, donald trump-도날드 트럼프
#       USOpen-US오픈, syria-시리아, 
#
#
#

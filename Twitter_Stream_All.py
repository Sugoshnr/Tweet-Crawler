
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
lang=['en','es','ko','tr'];
class listener(StreamListener):
    
    def __init__(self):
        self.en=0;
        self.es=0;
        self.ko=0;
        self.tr=0;
        
    def on_data(self,data):
            if ('retweeted_status' not in json.loads(data).keys()):
                x=json.loads(data)
                if(x['lang']=='en' and self.en<=500):
                    #print data;
                    savefile=open("H:\\CSE535-Information_Retrieval\\Project_1\\9_9_16\\syria_en.json","a")
                    savefile.write(data)
                    savefile.close()
                    self.en+=1
                    print 'en',self.en;
                elif(x['lang']=='es' and self.es<=1000):
                    savefile=open("H:\\CSE535-Information_Retrieval\\Project_1\\9_9_16\\syria_es.json","a")
                    savefile.write(data)
                    savefile.close()
                    self.es+=1
                    print 'es',self.es;
                elif(x['lang']=='ko' and self.ko<=1000):
                    savefile=open("H:\\CSE535-Information_Retrieval\\Project_1\\9_9_16\\syria_ko.json","a")
                    savefile.write(data)
                    savefile.close()
                    self.ko+=1
                    print 'ko',self.ko;
                elif(x['lang']=='tr' and self.tr<=1000):
                    savefile=open("H:\\CSE535-Information_Retrieval\\Project_1\\9_9_16\\syria_tr.json","a")
                    savefile.write(data)
                    savefile.close()
                    self.tr+=1
                    print 'tr',self.tr;                    
            return True
    
    def on_error(self,status):
        print status;

auth=OAuthHandler(c_key,c_sec)
auth.set_access_token(a_tok,a_sec)
stream=Stream(auth,listener())


#stream.filter(languages=['en','es','ko','tr'],track=['hillary','clinton','potus','trump','hilary2016','trump2016','makeamericagreatagain',u'클린턴',u'도날드 트럼프'])
#stream.filter(languages=['ko'],track=['appleevent','iphone7','airpod','iphone',u'아이폰',u'애플 이벤트'])
#stream.filter(languages=['ko'],track=['usopen','espntennis','espn tennis',u'US오픈'])
stream.filter(languages=lang,track=['syriancivilwar','syria','pray4syria','prayforsyria','refuge','syriacrisis','refugecrisis','syrianconflict','syriawar','syriaconflict','suriye',u'시리아'])



#Turk==== Syria-Suriye; 
#Korea==== Iphone-아이폰, appleevent-애플 이벤트,clinton-클린턴, donald trump-도날드 트럼프
#       USOpen-US오픈, syria-시리아, 
#
#
#

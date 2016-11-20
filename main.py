
# -*- coding utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

c_key=''
c_sec=''
a_tok=''
a_sec=''

class listener(StreamListener):

    def on_data(self,data):
            #print data;
            savefile=open("trial.txt","a")
            savefile.write(data)
            savefile.close()
            return True
    
    def on_error(self,status):
        print status;

auth=OAuthHandler(c_key,c_sec)
auth.set_access_token(a_tok,a_sec)
stream=Stream(auth,listener())


#stream.filter(languages=['en','es','tr','ko'],track=['hillary','clinton','potus','trump','hilary2016','trump2016','makeamericagreatagain'])
stream.filter(languages=['en'],track=['appleevent','iphone7','airpod'])
#stream.filter(languages=['en'],track=['usopen','espn'])
#stream.filter(languages=['tr'],track=['syriancivilwar','syria','pray4syria','prayforsyria','refuge','syriacrisis','refugecrisis','syrianconflict','syriawar','syriaconflict'])

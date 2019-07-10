# -*- coding: utf-8 -*-
__author__ = "Carlos Abreu"

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.api import FacebookAdsApi
from facebookads.exceptions import FacebookError
from unicodedata import normalize

import json, os, sys
import time, gzip

# Python 3 async sintax is defined by async_

class Analyze:

    def __init__(self, token, act_id, secret):
        self.token = token
        self.act_id = act_id
        self.secret = secret
        self.api = 0

        self.getfacebookApi()

    def getfacebookApi(self):
        if self.secret != '-':
            self.api = FacebookAdsApi.init(access_token = self.token, app_secret = self.secret, api_version='v3.2')
        else:
            self.api = FacebookAdsApi.init(access_token = self.token, api_version='v3.2')
        
        self.account = AdAccount('act_' + act_id)


    #******************************************************
    # Interest search FacebookAd Plataform
    #******************************************************

    def getInterestIDFromText(self, text):
        params = {
            'q': text,        
            'type': 'adinterest',
            'limit': 1000,        
        }
        resp = TargetingSearch.search(params = params, api = self.api)
        return resp

    def getSuggestions(self, element):
        params = {
            'type': TargetingSearch.TargetingSearchTypes.interest_suggestion,
            'interest_list': list(element),
            'limit':1000
        }
        
        resp = TargetingSearch.search(params = params, api = self.api)
        return resp

    def validateInterestIdByInterest(self, list_interests): 
        params = {
            'type': 'adinterestvalid',
            #'interest_list': list_interests,
            'interest_fbid_list': list_interests,
        }
        resp = TargetingSearch.search(params = params, api = self.api)  
        return resp

    def getLocationElement(self, element, location_type="country"):
        # type=adgeolocation&location_types=['region']:   
        params = {
            'q': element,
            'type': 'adgeolocation',
            # 'location_types': ['city'],
            # 'location_types': ['region'],
            'location_types': [location_type],
            # 'countries': ['US']
            # 'match_country_code' :True 
        }
        responses = TargetingSearch.search(params = params, api = self.api)
        return responses

    def testSearchForLocationCode(self, city, type_location):
        # available location types: country, country_group, region, city,
        resp = self.getLocationElement(str(city), location_type = str(type_location))  
        print('###### Searching for {} - {} #######'.format(type_location, city))
        print(resp)

    def testSuggestions(self, intereses):
        # intereses = ["",""]
        for interest in intereses:
            print('**********  SUGGESTIONS SEARCHING FOR %s  **********'  % interest)
            search_result = self.getSuggestions(interest)

            for element in search_result: 
                print("interest_id: %s" % element["id"]) 
                print("name: %s" % element["name"])
                print("audience_size: %s" % element["audience_size"])

    def  testeValidateInterests(self):
        interests_list = ['6003602262503','6003136682117','6003262996193', '6003058819532']
        resp = self.validateInterestIdByInterest(interests_list)
        for valid_element in resp: 
            print('******* valid *******')
            print(valid_element["id"])

    def testInterestSearch(self, interesets): 
        list_of_interests_to_search = interesets
        # list_of_interests_to_search = ["Feijoada"]
        for interest in list_of_interests_to_search:
            print('**********  SEARCHING FOR %s  **********'  % interest)       
            search_result = self.getInterestIDFromText(interest)
            # print search_result
            
            for element in search_result: 
                print("interest_id: %s" % element["id"])
                print("name: %s" % element["name"])
                print("audience_size: %s" % element["audience_size"])
    #             not all responses have a topic and category defined.  
    #             print "topic: %s" % element["topic"] 
    #             print "disambiguation_category: %s" % element["disambiguation_category"]  


    #******************************************************
    # Request for FacebookAd Plataform
    #******************************************************


    def make_request(self, targeting_spec):
        api_params = {
            'targeting_spec': targeting_spec
        }
        reach_estimate = self.account.get_reach_estimate(params=api_params)
        number = reach_estimate[0]['users']
        return number

    def interests_and_demographics_and_race(self, id_interest, age_min, age_max):
        targeting_spec['interests'] = list(id_interest)
        targeting_spec['age_min'] = age_min 
        targeting_spec['age_max'] = age_min
        targeting_spec['education_statuses'] = [9,11]
        targeting_spec['flexible_spec'] = [{'behaviors': [{"id":"6003133212372","name":"Hispanic (US - All)"}]}]   
        print('audience_size: %s' % make_request(targeting_spec))

    def interest_and_behavior(self):
        donald_trump_interest = "6003210792176"
        targeting_spec = {
            'interests' : [donald_trump_interest],
            'flexible_spec' : [{'behaviors': [{"id":"6018745176183","name":"African American (US)"}]}]
        }
        print('audience_size: %d' % self.make_request(targeting_spec))

    def multiple_interests_and(self, interesets):

        total_interesets = []

        for interest in interesets:
            total_interesets.append({'interesets' : [{"id" : str(interest)}]})

        targeting_spec['age_min'] = 13
    #     targeting_spec['age_max']=65    
    #     targeting_spec['interests'] = [donald_trump_interest]    
    #     targeting_spec['interests'] = [donald_trump_interest,hillary_clinton_interest] 
        targeting_spec['flexible_spec'] = total_interesets  
        print('audience_size: %d' % make_request(targeting_spec))



token = "EAAbPAyrnxo0BAIcp9t9AknLzPdZCDY9ZBcJnzK8cSdQerT3vzyTyNPYHKggoFh2HUFWcYpphCDRaMYGsJ237FBTnlcDl8I7nKLfuxkDTRZAf0GcTtdr8FKCZBNJY7Q51UDbttXLxyPeMn9qzrZByJzyfeZC8rZALBZAZCMEGN4ZC7UlgZDZD"
act_id = "607949019296375"
secret = "-"

facebookAnalize = Analyze(token, act_id, secret)
facebookAnalize.testSuggestions(["Diabetes"])
facebookAnalize.interest_and_behavior()
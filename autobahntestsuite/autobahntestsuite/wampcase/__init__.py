###############################################################################
##
##  Copyright 2013 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

__all__ = ("Cases",
           "CaseCategories",
           "CaseSubCategories",
           "CaseBasename",)

CaseBasename = "WampCase"


CaseCategories = {"0": "Message format",
                  "1": "Sessions",
                  "2": "Publish and Subscribe",
                  "3": "Remote Procedure Calls",
                  "4": "Authentication and Authorization",
                  "5": "Reflection",
                  "6": "Performance"}

CaseSubCategories = {"2.1": "Different payloads",
                     "2.2": "Exclude and eligible",
                     "2.3": "Publisher identification",
                     "2.4": "Unsubscribe",
                     "2.5": "Pattern-based subscriptions",
                     "2.6": "Metaevents",

                     "3.1": "Different argument and return types",
                     "3.2": "Call timeouts",
                     "3.2": "Cancel calls",
                     "3.3": "Progressive results",
                     "3.4": "Partitioned calls",
                     "3.5": "Call results and errors",
                     "3.6": "",
                         }


from wampcase1 import *

## all WAMP test cases
##
Cases = []
Cases.extend(WampCase1_x_x)

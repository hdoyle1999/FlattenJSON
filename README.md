# FlattenJSON
MongoDB code challenge  

### To run
cd to the repo  
There are a few different running methods  
1) python flatten.py name.json (where name.json is the name of a json file in the repo)  
2) echo insert_json_data | python flatten.py (where insert_json_data is a json object as a string i.e. for linux command line echo '{ "key1": "value 1", "key2": "value 2" }' | python flatten.py OR for windows commandline (not powershell as thats linux based) echo { "key1": "value 1", "key2": "value 2" } | python flatten.py . However this does not work for JSON objects with JSON objects corresponding to a key as the commandline cant read the data, so I recommend method no. 1)  
3) python flatten.py (if the above commands cannot be executed the try statements will fail and default to the JSON object in the challenge)   

### To test
cd to the repo  
Simply execute terminal/console command in the repo    
python test_flatten.py

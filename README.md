JsonSir
=======

A serializer for JSON-like data in Python.


Serialization Rules
-------------------

### Serializing

Convert Python data to JSON:

Value in Python                           | Value in JSON              | Value in JSON (`WITH_TYPE_NAME` == True)
----------------------------------------- | -------------------------- | --------------------------
10                                        | 10                         | 10
True                                      | true                       | true
"string"                                  | "string"                   | "string"
re._pattern_type                          | "/russ/"                   | "regex(/russ/)"
bson.ObjectId("543934671d41c812802711f3") | "543934671d41c812802711f3" | "objectid(543934671d41c812802711f3)"
datetime.datetime(2014, 10, 11)           | "2014-10-11T00:00:00Z"     | "datetime(2014-10-11T00:00:00Z)"

### Deserializing

Convert JSON data to Python:

Value in JSON                        | Value in Python
------------------------------------ | -----------------------------------------
"int(10)"                            | 10
"bool(true)"                         | True
"string"                             | "string"
"regex(/russ/)"                      | re._pattern_type
"objectid(543934671d41c812802711f3)" | bson.ObjectId("543934671d41c812802711f3")
"datetime(2014-10-11T00:00:00Z)"     | datetime.datetime(2014, 10, 11)

# User Activity

## Steps to install and Use
    
1. Create virtual env - [see how](https://docs.python.org/3/library/venv.html)
 
2. Go to the checkout folder and run ``pip install -r requirements.txt``

3. Then to start server run ``python manage.py runserver``

    1. visit [http://127.0.0.1:8000/activity/upload]
       Here you can upload a JSON file with activity data which follows
       this [Schema](#Schema)
    2. visit [http://127.0.0.1:8000/activity/getdata]
       At this endpoint data is server in JSON format
       following this [schema](#Schema)

4. The web application is deployed on Heroku, you can access following
   links to perform the operation as above.
    
   1. https://full-throttle-saif.herokuapp.com/activity/upload
   2. https://full-throttle-saif.herokuapp.com/activity/getdata

5. To insert the dummy data, use the following command
    - ``python manage.py import_data_json path/to/file.json`` 


## Schema

```json
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "required": [
        "ok",
        "members"
    ],
    "additionalProperties": true,
    "properties": {
        "ok": {
            "$id": "#/properties/ok",
            "type": "boolean",
            "default": false
        },
        "members": {
            "$id": "#/properties/members",
            "type": "array",

            "additionalItems": true,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/members/items/anyOf/0",
                        "type": "object",
                        "default": {},
                        "required": [
                            "id",
                            "real_name",
                            "tz",
                            "activity_periods"
                        ],
                        "additionalProperties": true,
                        "properties": {
                            "id": {
                                "$id": "#/properties/members/items/anyOf/0/properties/id",
                                "type": "string"
                            },
                            "real_name": {
                                "$id": "#/properties/members/items/anyOf/0/properties/real_name",
                                "type": "string"
                            },
                            "tz": {
                                "$id": "#/properties/members/items/anyOf/0/properties/tz",
                                "type": "string"
                            },
                            "activity_periods": {
                                "$id": "#/properties/members/items/anyOf/0/properties/activity_periods",
                                "type": "array",
                                "additionalItems": true,
                                "items": {
                                    "anyOf": [
                                        {
                                            "$id": "#/properties/members/items/anyOf/0/properties/activity_periods/items/anyOf/0",
                                            "type": "object",
                                            "required": [
                                                "start_time",
                                                "end_time"
                                            ],
                                            "additionalProperties": true,
                                            "properties": {
                                                "start_time": {
                                                    "$id": "#/properties/members/items/anyOf/0/properties/activity_periods/items/anyOf/0/properties/start_time",
                                                    "type": "string"
                                                },
                                                "end_time": {
                                                    "$id": "#/properties/members/items/anyOf/0/properties/activity_periods/items/anyOf/0/properties/end_time",
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    ],
                                    "$id": "#/properties/members/items/anyOf/0/properties/activity_periods/items"
                                }
                            }
                        }
                    }
                ],
                "$id": "#/properties/members/items"
            }
        }
    }
}
```
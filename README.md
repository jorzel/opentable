Open table app for training purposes.
Create application in DDD style, trying to keep domain layer agnostic of external dependencies (ORM/DB, External Services)

## Install packages
```>> pip install -r requirements.txt```

## Run nameko application
```>> nameko run --config src/api/nameko/config.yml src.api.nameko```

## Run tests
```
>> pip install -r test_requirements.txt
>> pytest
```

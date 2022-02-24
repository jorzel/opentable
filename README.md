## Overview

Open table app for training purposes.

The project implements Ports and Adapters architecture in DDD style, trying to keep domain layer agnostic of external dependencies (ORM/DB, External Services).

Inner layers should not have any knowledge about outer layers.
Application core (domain + application), should provide orchestration of whole business process exploiting existing ports. There are two types of ports:
- primary port, that is an entry exposing application core to outside world. It is usually a fascade **called** by a primary adapter (e.g. REST API, CLI, etc.),
- secondary port, enables application core to communicate with external world (e.g. database, mail sender, etc). It is an interface that is **implemented** by a secondary adapter.

The crucial thing here is that our application core does not have any knowledge about infrastructure and API, it operates only on interfaces. If we need a database access, we should define a repository interface and injected it into our service. Or, if there is a need for notification sending, we should make a notification sender interface that can be implemented by SMS or Email sender adapter in the infrastructure layer. But inside the application core we know nothing about infrastructure implementations (thanks to it the application logic can be easily unit tested). And this is the main gain of using this architecture.

![Alt text](clean.png?raw=true "Application diagram")

## Install packages
```>> pip install -r requirements.txt```

## Run nameko application
```>> nameko run --config src/api/nameko/config.yml src.api.nameko```

## Run tests
```
>> pip install -r test_requirements.txt
>> PYTHONPATH=src pytest
```

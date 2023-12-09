# Airbnb_clone - Console

## Installing and Running the console

    clone this Repo to wherever you like
```bash
$ cd <where you put this repo>
$ ./console.py
```

## Data Types (and their properties) 

* BaseModel : attributes ==> `id`, `created_at`, `updated_at` (children) :
    * User      : attributes ==> `first_name`, `last_name`, `email`, `password`.
    * State     : attributes ==> `name`.
    * City      : attributes ==> `name`, `state_id`.
    * Place     : attributes ==> `name`, `description`, `user_id`, `city_id`,`number_rooms`,`number_bathrooms`,`max_guest`, `price_by_night`,`latitude`,`longitude`, `amenity_ids`.
    * Amenity   : attributes ==> `name`.
    * Review    : attributes ==> `place_id`, `user_id`, `text`


## commands

- `help`     
- `quit`   
- `EOF`  
- `all [<clsName>]`      
- `show <clsName> <id>`  
- `create <clsName`  
- `destroy <clsName> <id>` 
- `update <clsName> <id> <attribute> <new value>` 

## Using the console

* show all available data of class User

```bash
(hbnb)show User
```

* set number of rooms of a Place data with id x-y-z to 5 rooms :

```bash
(hbnb)update Place x-y-z number_rooms 5
```

for more info type `help`:
```bash
(hbnb)help
```
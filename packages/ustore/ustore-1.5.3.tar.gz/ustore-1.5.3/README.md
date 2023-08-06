
# UStore

A simple library for the managment/usage for users

## Features

> AES encryption on config files.

> Automatic sha256 hashing on passwords with salt

> High speeds for user R/W

## Getting Started

### Installing

```
pip install ustore
```

### Example

```
import ustore
ustore.init(".")                 # Set user storage location to current dir
register_account("user","pass")  # Make a user with the username user and a password bar
setconfig("user","data","pass")  # Set the config value for the user user to data
getconfig("user","pass")         # Get the config for the user user
valid_password("user","pass2")    # Check if the user user's password is pass
```

### Documentation

#### ustore.init(location-for-data-storage) 
> Will Initialise the user system to location-for-data-storage


#### register_account(username,password)
> Create an account.


#### valid_password(username,password)
> Validates if the supplied password is valid for the account.
> Returns Bool value


#### setconfig(username,configvar,password)
> Will set the config file for the user to configvar, Password must be supplied due to config file encryption


#### getconfig(username,password)
> Will get the config file for the user, Password must be supplied due to config file encryption
> returns variable


#### Initialisation_Error 
> Will be thrown if init() is not called


#### Invalid_Input_Error
> Will be thrown if an illegal username/password was supplied


#### User_Exists_Error
> Will be thrown if a user was trying to register an already registered user


#### Invalid_Password_Error
> Will be thrown if the password validation failed unless called by valid_password()
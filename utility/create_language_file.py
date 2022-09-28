import configparser

config = configparser.ConfigParser()

config['CREATE'] = {
    'name': 'create',
    'description': 'Set a voice channel as a automatic voice channel',
    'argument_description': 'Select a voice channel that will be used as a automatic voice channel',
    'success': 'Success!',
    'success_description': 'The bot will now create a new voice channel when someone joins {0}!',
    'error': 'Error!',
    'error_description': 'There was an error while trying to create the automatic voice channel!',
    'duplicate': 'Error!',
    'duplicate_description': 'This voice channel is already an automatic voice channel!'
}

config['DELETE'] = {
    'name': 'delete',
    'description': 'Deactivate a automatic voice channel',
    'argument_description': 'Select a voice channel that will be deactivated',
    'success': 'Success!',
    'success_description': 'The bot will no longer create a new voice channel when someone joins {0}!',
    'error': 'Error!',
    'error_description': 'There was an error while trying to deactivate the automatic voice channel!',
    'not_found': 'Error!',
    'not_found_description': 'This voice channel is not an automatic voice channel!'
}


with open('../language.ini', 'w') as configfile:
    config.write(configfile)

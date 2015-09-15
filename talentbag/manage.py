#!/usr/bin/env python
import os
import sys


if os.getcwd() == "/Users/vish/Desktop/talentbag/talentbag":
        

	if __name__ == "__main__":
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talentbag.settings.local")
    	

    	from django.core.management import execute_from_command_line

    	execute_from_command_line(sys.argv)

    	

else:	
	if __name__ == "__main__":

		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talentbag.settings.production")
    	

    	from django.core.management import execute_from_command_line
    	execute_from_command_line(sys.argv)

    





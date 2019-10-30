import argparse
def prep_cmd():
    small_interface = argparse.ArgumentParser(description='Automate process of aquarying quidian stones')
    small_interface.add_argument('--r', action='store_true', default=False, help="If you want to record new position of widnows add --r to command line")
    small_interface.parse_args()
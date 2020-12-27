This code is to work with a given csv File containing the turnover from Amazon VisaCard
We only want to import bookings that are really booked on the account.
Bookings that are just reserved shall not imported to GnuCash

Folderstructure:
src - the given source File
dst - the destination File (only the last one)
arc - the last 100 destination files are stored here
log - contains the log files. The current one and that before the last
script - the folder with all scripts

If you want to use this little Project you have to do the follow steps:
1. Copy the whole Folder structure to your machhine
2. Go to /script/settings.py and change the working dir to your needs
3. Put the csv that should be moved to the src folder
4. go to /run/run.py and start it

Script Folder:
- run - run this to use the program
- visaFunc - the main function for reading and writing csv
- loghandler - as the name says
- housekeeping - holds the cleaning scripts for dst/log/arc Folder
- settings contains the working dir and the vars for the other folders

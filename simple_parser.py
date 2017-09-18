import unicodecsv
from datetime import datetime
from difflib import SequenceMatcher

# To do:
# - Limit to X updates per day
# - Post tweets!
# - Screenshot
# - ???

csvNumber = 1
deduplicate = True

while csvNumber < 5:
    with open('crest_lite_' + str(csvNumber) + '.csv') as csvfile:
        print "Opening Crest Lite " + (str(csvNumber))
        reader = unicodecsv.DictReader(csvfile)
        for row in reader:
            if row['document_publication_date'] != '':
                datetime_object = datetime.strptime(row['document_publication_date'], '%B %d, %Y')
                csv_file = open(str(datetime_object.strftime('%m')) + '-' + str(datetime_object.strftime('%d')) + '.csv', 'a')
                csv_file_row_checker = csv_file
    #            try:
    #                updates_so_far = len(list(csv_file))
    #                print str(updates_so_far)
    #            except:
    #                updates_so_far = 0
                csv_writer = unicodecsv.writer(csv_file)
                if row['title'] != "(UNTITLED)" and row['title'] != "(SANITIZED)" and row['title'] != "(Classified)":
                    csv_writer.writerow([row['title'][0:115] + " " + row['url']])
    #            elif row['more1_title'] != '': # Double check this actually works to check if there's no more title
    #                csv_writer.writerow([row['more1_title'][0:115] + " " + row['url']])
                else:
                    csv_writer.writerow(["The mysterious file known only as " + row['document_number'][0:20] + " " + row['url']])
            else:
                print "No date"

        print "All done."
        csvNumber += 1

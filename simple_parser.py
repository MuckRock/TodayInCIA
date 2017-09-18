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
            if row['publication_date'] != '':
                datetime_object = datetime.strptime(row['publication_date'], '%B %d, %Y')
                csv_file = open(str(datetime_object.strftime('%m')) + '-' + str(datetime_object.strftime('%d')) + '.csv', 'a')
                csv_file_row_checker = csv_file
    #            try:
    #                updates_so_far = len(list(csv_file))
    #                print str(updates_so_far)
    #            except:
    #                updates_so_far = 0
                csv_writer = unicodecsv.writer(csv_file)
                if row['title'] != "(UNTITLED)" and row['title'] != "(SANITIZED)" and row['title'] != "(Classified)":
                    csv_writer.writerow(["OTD in 19" + str(datetime_object.strftime('%y')) + ": " + row['title'][0:100] + " " + row['url'] + " (" + row['document_page_count']+ " pgs)"])
    #            elif row['more1_title'] != '': # Double check this actually works to check if there's no more title
    #                csv_writer.writerow([row['more1_title'][0:115] + " " + row['url']])
                else:
                    csv_writer.writerow(["OTD in 19" + str(datetime_object.strftime('%y')) + ": " + "A mysterious " + row['content_type'] + " with document number  " + row['document_number'][0:20] + " " + row['url'] + " (" + row['document_page_count']+ " pgs)"])
            else:
                print "No date"

        print "All done."
        csvNumber += 1

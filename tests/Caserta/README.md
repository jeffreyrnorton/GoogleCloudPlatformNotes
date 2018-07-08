# Caserta Google Cloud Platform Test

The test objective is to test familiarity with critical parts of the Google Cloud platform such as bucket storage and using BigQuery.  Another objective is to test the ability to effectively use an API, especially one that is throttled.  In particular, the following tasks are performed:

* Writing a data ingestion script to pull cryptocurrency data from an API
* Saving the data inside a Google Cloud Storage bucket
* Loading the data into Google BigQuery
* Running queries in Google Datalab

## Instructions

### Overview:
1. Pull current data for all cryptocurrencies using the CoinMarketCap API
2. Save this data as a CSV file
3. Upload the CSV to a Google Cloud Storage Bucket
4. Move cryptocurrency data from GCS bucket to BigQuery
5. Create a Google Datalab notebook instance
6. Execute these five queries inside the notebook:
	* How many coins have a USD price greater than $8,000?
	* What is the total market cap of the top 100 cryptocurrencies (in USD)?
	* Which coins have an available supply less than $5M?
	* Which 5 coins have seen the greatest percentage growth in the last week?
	* How many ticker symbols contain the letter "X" ?
7. Download the notebook as a .ipynb file by choosing correct option under "Notebook" on the top left
8. Email deliverables back to recruiter

### Deliverables:
1.	Google DataLab notebook (.ipynb) containing data ingestion script and SQL queries including answers to above questions
2. Public URL of Google Cloud Storage bucket containing CoinMarketCap data

### Extra Credits
1.	Explain thinking at each step
	.	Include Markdown text
	.	Log steps and errors
	.	Push to Github Repository
	.	Publicly accessible link to Google Storage bucket
	.	Use Google Cloud APIs instead of web console whenever possible

## Results

**Note on Timestamps**

*The two different compute environments are using different time zones. So you may note that the timestamps for notebook 1 seem to come after notebook 2.  Notebook 1 is on Eastern time while GCP is on Pacific time.*

**Note on Environment**

*All code is written using Python 3.  In some cases, I refer to this explicitely, so you will see the command line ```python3``` being used instead of just ```python``` which is Python 2.*

All steps were executed with scripts or in notebooks except for one which will be pointed out.

### Local Code

Part 1 - Steps (1) and (2) were accomplished in a Jupyter notebook running on my local computer (VM/Linux - Suse Leap).  The notebook is [on github](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/Caserta_GCP_Test_Part1.ipynb) and is best visualized using the Jupyter NB Viewer - [Viewable Notebook](https://nbviewer.jupyter.org/github/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/Caserta_GCP_Test_Part1.ipynb)

Step 3 is using a standalone Python script which is also stored on [github](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/utils/upload_blob.py).

That one operation!  The one operation that was not done with a script was to change the ACL of the [uploaded CSV file (@ Github)](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/cryptocurrency_prices.csv) on GCP such that it can be publically read.  From what I can tell, that operation can only be done through the web interface.

The public URL of the CSV file on GCP bucket storage is [https://storage.googleapis.com/jrnorton_caserta_test_cryptocurrencies/cryptocurrency_prices.csv](https://storage.googleapis.com/jrnorton_caserta_test_cryptocurrencies/cryptocurrency_prices.csv).

### GCP Dataflow Notebook

The second part of the exercise was all completed on GCP Datalab.  Following good big data principles (compute as close to storage as possible), I went ahead and performed the move (copy) of the file from the GCP bucket into BigQuery on the cloud in Datalab.  The remaining steps were perfomed in the [Caserta Test - Part 2 Datalab notebook (@github)](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/GCP/caserta_part2_test.ipynb) best viewed
[using the Jupyter Notebook Viewer](https://nbviewer.jupyter.org/github/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/GCP/caserta_part2_test.ipynb).

# Deliverables
## Notebooks and Scripts
[https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/Caserta_GCP_Test_Part1.ipynb](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/Caserta_GCP_Test_Part1.ipynb)

[https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/utils/upload_blob.py](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/utils/upload_blob.py)

[https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/GCP/caserta_part2_test.ipynb](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/GCP/caserta_part2_test.ipynb)

## CSV File

Public URL: [https://storage.googleapis.com/jrnorton_caserta_test_cryptocurrencies/cryptocurrency_prices.csv](https://storage.googleapis.com/jrnorton_caserta_test_cryptocurrencies/cryptocurrency_prices.csv)

and at Github:
[https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/cryptocurrency_prices.csv](https://github.com/jeffreyrnorton/GoogleCloudPlatformNotes/blob/master/tests/Caserta/Local/cryptocurrency_prices.csv).



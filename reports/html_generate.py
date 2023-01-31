import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_name = "report_{}.html".format(timestamp)

# Pass the report name as a command-line argument to pytest
arguments = "--html=reports/{}".format(report_name)

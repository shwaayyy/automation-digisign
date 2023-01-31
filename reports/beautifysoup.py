from bs4 import BeautifulSoup

# create a new BeautifulSoup object
# new_soup = BeautifulSoup("<html><head><title>Test Report</title></head><body></body></html>", "html.parser")
#
# # read each HTML file into BeautifulSoup object
# soup_1 = BeautifulSoup(open("report_test_1.html"), "html.parser")
# soup_2 = BeautifulSoup(open("report_test_2.html"), "html.parser")
#
# # extract the table element from each HTML file
# table_1 = soup_1.find("table")
# table_2 = soup_2.find("table")
#
# # append the extracted table element to the new BeautifulSoup object
# new_soup.body.append(table_1)
# new_soup.body.append(table_2)
#
# # write the new BeautifulSoup object to a new HTML file
# with open("merged_report.html", "w") as f:
#     f.write(str(new_soup))


# Load the HTML file into BeautifulSoup
with open("report.html") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the environment table in the HTML
try:
    table = soup.find("table", attrs={"id": "environment-table"})
    rows = table.find_all("tr")
    for row in rows:
        if "ROW_NAME" in row.text:
            row.decompose()
except AttributeError as e:
    print("Error:", e)


# Save the modified HTML to a new file
with open("modified_report.html", "w") as file:
    file.write(str(soup))

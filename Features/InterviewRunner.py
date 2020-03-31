import glob
from json2html import *
import sys
from behave import __main__ as runner_with_options
import shutil

"""
Purpose of the Script to Execute the Feature File and Generate the HTML Test Report.
Author - KamatchiRajan
Date - 31Mar20
"""

if __name__ == '__main__':
    sys.stdout.flush()
    reporting_folder_name = 'Test_Report'
    
    # remove if any reporting folder exists
    shutil.rmtree(reporting_folder_name, ignore_errors=True)
    
    # allure reporting related command line arguments
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o ' + reporting_folder_name + '  '
    
    # run Behave + BDD + Python code
    featureFilePath = 'Interview.feature'
    # commonRunnerOptions = ' --no-capture --no-capture-stderr -of plain '
    fullRunnerOptions = featureFilePath + reportingRelated # + commonRunnerOptions
    runner_with_options.main(fullRunnerOptions)
    
    # read resultant json file
    listOfJson = glob.glob(reporting_folder_name + "/*.json")
    finalJson = ''
    for cnt in range(0, len(listOfJson)):
        listOfJson[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJson[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJson)):
            listOfJson[cnt] = listOfJson[cnt] + ','
        finalJson = finalJson + listOfJson[cnt]
    finalJson = '[ ' + finalJson + ' ]'
    
    # convert json to html using simple utility and publish report
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(reporting_folder_name + '/' + 'Report.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()
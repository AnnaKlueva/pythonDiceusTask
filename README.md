## Test task

## How to start

## Run locally:

Use python 3.8 + Create and activate virtual environments

`python3 -m venv env
source env/bin/activate`

Run in terminal

`pip install -r requirements.txt`

#### Install allure reporter on your local machine: </br>
Windows:</br>
`
scoop install allure
`</br>
Mac:</br>
`
brew install allure
`

#### Run tests with report:
Chrome:</br>
`pytest --driver=chrome --alluredir=allure-results`
</br>Firefox:</br>
`pytest --driver=firefox --alluredir=allure-results`

Note: </br>
if `--driver` parameter is not mentioned, the Chrome driver is used by default

#### Optional: Run in parallel
Run tests across several CPU cores (`pytest -n <num_workers>`): </br>
`pytest -n 2 --alluredir=allure-results`

</br>To see report run:
`allure serve allure-results`


## Run throw GitHub pipeline:
* Navigate to 'Actions'
* Select workflow 'Run Tests with Allure report ...'
* Select browser. Possible options: chrome or firefox

NOTE:
1. Test report can be found in github pages:
[https://annaklueva.github.io/pythonDiceusTask](https://annaklueva.github.io/pythonDiceusTask)
Note: 
Tests are passed locally, but nnot all of them passed remotely(due lack of time I didn't fix flakines and changing of window size)



## 🧪 UI Automation Task Description
### ✅ Steps to Automate:

1. **Visit Home Page**
   - Navigate to [https://useinsider.com/](https://useinsider.com/)
   - Verify that the **Insider home page** is successfully loaded.

2. **Navigate to Careers Page**
   - In the top navigation bar, hover over or select the **“Company”** menu.
   - Click on **“Careers”**.
   - Verify the **Careers page** is opened.
   - Ensure the presence of the following sections:
     - **Locations**
     - **Teams**
     - **Life at Insider**

3. **Filter QA Jobs in Istanbul**
   - Navigate directly to [https://useinsider.com/careers/quality-assurance/](https://useinsider.com/careers/quality-assurance/)
   - Click the **“See all QA jobs”** button.
   - Use filters to:
     - Select **Location**: *Istanbul, Turkey*
     - Select **Department**: *Quality Assurance*
   - Verify that the **jobs list** is displayed.

4. **Validate Job Listings**
   - For each job listed:
     - **Position** must contain *“Quality Assurance”*
     - **Department** must be *“Quality Assurance”*
     - **Location** must be *“Istanbul, Turkey”*

5. **Check Application Page**
   - Click on the **“View Role”** button for any job.
   - Verify that the user is redirected to a **Lever.co application form page**.

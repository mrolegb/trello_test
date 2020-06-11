#### Trello tests

Created and executed with `Python 2.7.36`

To execute:
* Install dependencies from `requirements.txt`
* Download and install `geckodriver` and `Firefox`
* Run `pytest` from the project root folder

* **Beware**: teardown code will delete all boards
(as it should, don't want to leave a mess)

Comments:
* The task, as given, implies dependency between tests - it is a bit
against the best practice, but tolerable, if the intent was to verify
if the competitor could implement a shareable context
* Mixing UI and API tests is usually not a great idea, unless the API
ones serve more as data setup - which, probably is the case here
* `pytest-bdd` was tried and discarded, as it brings more pain then
efficiency (never used it, wanted to have a look)
* `behave` would most likely be a better option
* It was fun
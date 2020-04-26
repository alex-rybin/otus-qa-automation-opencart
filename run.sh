trap "rm -rf allure-results" HUP INT QUIT TERM

pytest --alluredir allure-results

sleep infinity

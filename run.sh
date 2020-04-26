trap "rm -rf app/allure-results" HUP INT QUIT TERM

pytest --alluredir allure-results

sleep infinity

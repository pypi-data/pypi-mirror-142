from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask

def anticap(id,driver):
    with open(".env","r") as file:
        keys=file.read()
    api_key,site_key=keys.split(",")
    url = r'https://gcmb.mylicense.com/verification/'
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)
    job = client.createTask(task)
    print("Waiting to solution by Anticaptcha workers")
    job.join()
    # Receive response
    response = job.get_solution_response()
    print("Received solution", response)

    # Inject response in webpage
    driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % response)

    # Wait a moment to execute the script (just in case).
    #time.sleep(1)

    # Press submit button
    driver.find_element_by_id(id).click()
    
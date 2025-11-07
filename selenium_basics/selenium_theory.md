# Selenium Basics

## Difference between `presence_of_element_located` vs. `visibility_of_element_located`
`presence_of_element_located` checks whether this element is present in DOM. It returns the WebElement if it's found. This means the element's HTML tag exists in the page's source code, regardless of whether it's visible to the user.  whether it is visible for users.

**User case**: When you need to verify that an element exists in the DOM, even if it's not immediately visible. This is useful for backend checks, such as verifying that a dynamic element has been added to the page before it becomes visible.

**Example**: Verifying that a loading spinner element has been added to the page, even though it may be hidden briefly before the content appears.

`visibility_of_element_located` checks whether this element is not only present in the DOM but is also visible to the user.

**User case**: When you need to interact with an element (click, type, etc.) and want to ensure it is ready for user interaction. This is the more common choice for most UI automation tasks.

**Example**: Clicking a button or filling out a form field, where the element must be visible and clickable for the action to succeed.

## Difference between `Explicit Wait ` vs. `Implicit Wait`

`Explicit Wait` is a type of wait in Selenium that is used to pause the execution of a test script for a specific condition to be met before proceeding. It's a more intelligent and flexible approach compared to an implicit wait. It's especially useful when dealing with dynamic web pages where elements may not load at the same time. Throws `TimeoutError`.

`Implicit Wait` is a type of wait in Selenium that sets a timeout for **all subsequent calls to find an element**. Once an implicit wait is set, it remains in effect for the entire session. If the element is not found immediately, the driver will wait for the specified duration before throwing a `NoSuchElementException`.

## Most used `exepecited_conditions` aka `EC` in Selenium

### Element-related conditions
- `presence_of_element_located(locator)`

Waits until the element is present in the DOM (but not necessarily visible).

- `visibility_of_element_located(locator)`

Waits until the element is present and visible (height and width > 0).

- `visibility_of(element)`

Similar to above, but takes a WebElement instead of a locator.

- `element_to_be_clickable(locator)`

Waits until the element is visible and enabled, so you can click it.

- `element_located_to_be_selected(locator)`

Waits until an element (like a checkbox) is selected.

- `element_to_be_selected(element)`

Similar, but works with a WebElement.

### Multiple elements

- `presence_of_all_elements_located(locator)`

Waits until all elements matching locator are present in the DOM.

- `visibility_of_all_elements_located(locator)`

Waits until all elements are visible.

- `visibility_of_any_elements_located(locator)`

Waits until at least one element is visible.

### Text / Value

- `text_to_be_present_in_element(locator, text)`
Waits until the given text is found in the element. Returns `bool`.

- `text_to_be_present_in_element_value(locator, text)`
Waits until the given text is in the element’s value attribute. Returns `bool`.

### Frames, Alerts, Windows

- `frame_to_be_available_and_switch_to_it(locator_or_element)`

Waits until a frame is available and switches to it. Returns `bool`.

- `alert_is_present()`

Waits until an alert pops up. Returns `bool`.

- `number_of_windows_to_be(num)`

Waits until the number of open windows/tabs equals num. Returns `bool`.

## Selenium vs. Playwright

`Playwright`
- Faster and More Reliable: Playwright is generally faster because it uses a direct WebSocket connection to the browser, which is more efficient than Selenium's HTTP requests. It's also less prone to flaky tests due to its built-in auto-waiting mechanism.
- Playwright comes with powerful built-in tools for debugging and analysis, such as the Playwright Inspector, Trace Viewer, and a code generator (Codegen) that records user actions to create test scripts.

`Selenium`
- Selenium supports a broader range of browsers, including older ones like Internet Explorer, and more programming languages than Playwright, which is a key advantage for teams with diverse tech stacks.
- Selenium boasts a vast community, comprehensive documentation, and a wealth of third-party tools and extensions.

## Most used Seleinum chrome options

### Performance and Headless Mode
`--headless`: The most widely used option. It runs Chrome in the background without a graphical user interface (GUI). This makes tests much faster and is ideal for Continuous Integration/Continuous Delivery (CI/CD) pipelines where a visible browser is not needed.

`--headless=new`: A newer version of the headless option that uses the full Chrome browser instead of a separate shell, making it more authentic and reliable.

`--disable-gpu`: Disables GPU hardware acceleration. This can resolve rendering issues and flakiness on some systems, particularly in headless mode.

### Window and UI Control
`--window-size=WIDTH,HEIGHT`: Sets the initial size of the browser window. This is essential for testing responsive web designs and ensuring a consistent viewport size for screenshots.

`--start-maximized`: Opens the browser window in a maximized state.

`--incognito`: Starts the browser in incognito mode, which prevents it from using or storing cookies, browsing history, or other session data. This is useful for running clean, isolated tests.

`--disable-infobars`: Prevents the "Chrome is being controlled by automated test software" info bar from appearing.

`--disable-notifications`: Disables browser notifications and pop-ups, which can interrupt test execution.

### Debugging and Troubleshooting
`--auto-open-devtools-for-tabs`: Automatically opens the DevTools panel for every new tab. This is extremely helpful for debugging and inspecting the browser's state during a test.

`--remote-debugging-port=9222`: Allows you to connect to the browser instance with a remote debugger, which can be invaluable for troubleshooting. The port number can be customized.

### Security and Stability
`--no-sandbox`: Disables the sandbox feature. This is often required when running in containerized environments like Docker, or on Linux systems, as the sandbox can cause permission issues.

`--ignore-certificate-errors`: Ignores SSL certificate errors. This is useful for testing in development or staging environments that may use self-signed certificates.
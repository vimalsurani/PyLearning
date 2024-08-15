## **Why API & Web Automation Framework ? (Setup)**
- Can we write all the code in _**single python file**_ and this is what we call automation?
    - No
    - High Maintenance
    - Code duplicated. 
    - Properly Maintenance code it will be difficult to maintain such a large files /files. 
    - Not scalable -> TC 10, tc 100, TC 1000, TC 10,000 -> Impossible to maintain this. 

### What is the Framework?
A framework is a **structure **that provides a foundation for developing software applications / testAutomation. 

### Key characteristics of frameworks:

- They provide a structure for organizing code and resources.
- Proper folder structure to maintain the testcases. 
- They follow best practices and design patterns
- They promote scalability and flexibility.

One -> If we use the framework -> TC 10, 100, 10,000 -> Always easy to maintain, develop, no code duplicate AY

**Framework vs Library**

- Library - just bunch of reusable code - request module, pytest - library you can use in your framework.


### _Types of Framework in Automation Testing_

#### Linear Automation Framework.

- Record and Playback - here - TC scripts - Simple manner, where we will not maintain them 
- Record and Playback -> Find a API Test case -> Create Booking - create_booking.py -> run it. 
- test_create_booking.py
- test_update_booking.py 
- Utils, Payload, URLs - we don't care much about them. 
- Test Scripts -> Robot. 
- Better - Example - Selenium - Record Steps and Playback 
    - Code Duplicates
    - Maintenance is high
  
**Pros**: Simple to start
**Cons**: Code Duplicates , Maintenance is high, Not much used. 


#### Modular Driven Framework

- **Modular frameworks divides the test scripts into small modules** where modules are small scripts written to perform certain tasks.
- Each module is tested separately, allowing for**easier maintenance and scalability.**
- E-COM - API ->    Registration ->. Login ->   Add to Cart -> Payments -> Orders -> Orders Fulfilment -> Confirmations -> Shipping. -> refund / cancellation . 
- Registration  -> 10 
- Login -> 15
- [﻿VWO.com](https://vwo.com/) -> Sign up -> Login -> Dashboard -> Support 
- **Pros**: Facilitates independent script creation and better organization.
- **Cons**: Requires more time for analysis and identification of **reusable modules.**


#### Data-Driven Testing Framework
Data driven testing allows testers to input a single test script that can execute tests for all test data from a table and expect the test output in the same table.

100 U/P ->  tc_vwo_login.py -? u/p - from csv / excel / json/  text file -> 100 Times

This framework allows testers to run the same test with multiple sets of data stored externally (e.g., in Excel or CSV files)

**Pros**: Reduces the number of scripts needed; efficient for testing various scenarios.
**Cons**: Requires testers to have strong programming skills to manage data sources effectively


#### Keyword-Driven Testing Framework

- To make it reusable -> keywords inn the Test Automation. 
- login -> loginToApplication -> Code 
- loginWithIncorrect ->  Code
**Also known as table-driven testing**, this framework uses keywords defined in an external file (like an Excel sheet) to execute test cases. Each _**keyword corresponds to a specific action in the application.**_

- hbd -> hapy birth day
- cong ->  
- gm 
- gn
- fyi
- asap
- ikwym
- bf
- brb
- mom
- afk
- yolo -> ooo
functions - create booking() -> 

- **Pros**: Promotes **code reusability **through the use of shared keywords.
- **Cons**: Initial setup can be complex and time-consuming; requires a solid understanding of the framework
e.g -> Robot Framework

  
**Behavior Driven Development (BDD) Framework**

- This framework emphasizes collaboration among developers, testers, and business analysts by using natural language to define test cases.
- Feature Files - PM / PO / BA -> Gherkin Syntax (Given, When, Then)
- Test Runner - Glue - Feature File -> Step?
- Steps(Code) - test_creatbooking_code.py  -> AT/ SDET
- **Pros**: Non-technical stakeholders can contribute to test design, improving communication.
- **Cons**: Requires some technical knowledge and nowdays(PO) don't write the Feature file. (tester)


Feature File -> Test Runner -> Steps (Code)


**Hybrid Testing Framework ( Mixture of Modular / DDT / Keyword ) - 75%**

- Combines elements from various frameworks to leverage their strengths while minimizing weaknesses
- It can incorporate aspects of data-driven and keyword-driven frameworks.

- **Pros**: Offers flexibility and adaptability to different testing needs; maximizes code reuse.
- **Cons**: Can increase automation effort due to scripting, may be complex. 


**Test Driven Development**  -> Develop -> Softwares

- Test Driven Development -> loginpage -> dashbaordpage ( vwo.com)
- _login -> valid u/p -> click submit -> dashboardpage._
- _login -> invalid u/p -> click submit -> login with error message. _
- 2 TC - Dev -> Create Application which focus on 2 TC , TC should be passed. 
- Small startups 

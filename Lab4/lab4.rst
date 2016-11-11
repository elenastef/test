Format of Robot Framework Scripts

The robotframework executable scripts are at the end of this document.  Each script contains FOUR lines and an explaination of each line follows:

The first line in each script is the Test Case Name

EX:  Valid Highway Prefix IH and Valid Number 1234

The second line in each script specifies the expected results of the test for both the highway prefix and the highway number

EX:  Set Tags  Valid Prefix Valid Number

The third line in each script invokes the Python program, passes it the highway name for verification, and receives the results back

EX:  ${result} =     Valid highway  IH1234

The fourth line in each script specifies the expected result of the Python program, thus expecting True and receiving a True is a passing test case, as well as expecting Not True and receiving Not True is a passing test case

Test Script Mapping

There are six working test cases provided in this file.  They can be mapped back to the Truth Table Cases as follows:

Test Case		Truth Table Case

    1                  1
    2                  2
    3                  3
    4                  1
    5                  2
    6                  2
   


Robot Framework Script

.. code:: robotframework

    *** Variables ***
    ${HIGHWAY}                RR456

    *** Settings ***
    Library           OperatingSystem
    Library           naming.py

    *** Keywords ***
    Check highway type and number
        [Arguments]             ${highway}
        Valid highway           ${highway}
    
    *** Test Cases ***
    Valid Highway Prefix IH and Valid Number 1234
        Set Tags  Valid Prefix Valid Number
        ${result} =     Valid highway  IH1234    
        Should Be True  ${result}
    Valid Highway Prefix IH and Invalid Number 12345
        Set Tags  Valid Prefix Invalid Number
        ${result} =     Valid highway  IH12345    
        Should Not Be True  ${result}
    Invalid Highway Prefix Lowercase ih and Valid Number 1234
        Set Tags  Invalid Prefix Valid Number
        ${result} =     Valid highway  ih1234    
        Should Not Be True  ${result}    
    Valid Highway Prefix IH and Valid Number 12
        Set Tags  Valid Prefix Valid Number
        ${result} =     Valid highway  IH12    
        Should Be True  ${result}   
    Valid Highway Prefix IH and Invalid Number 1
        Set Tags  Valid Prefix Invalid Number
        ${result} =     Valid highway  IH1    
        Should Not Be True  ${result}
    Valid Highway Prefix IH and Invalid Number ABC
        Set Tags  Valid Prefix Invalid Number
        ${result} =     Valid highway  IHABC    
        Should Not Be True  ${result}
   
   
    
    

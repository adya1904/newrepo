Feature: Finding the pets using pet id using GET API
Scenario: Get pet by pet id
	Given I set GET pet/10 API endpoint
	And I have valid petid
	When I send GET HTTPS request pet/10
	Then I receive a valid HTTPS response code 200 from pet/10 using GET
 
Scenario: Get order by order id
	Given I set GET store/order/2 API endpoint
	And I have valid orderid
	When I send GET HTTPS request store/order/2
	Then I receive a valid HTTPS response code 200 from store/order/2 using GET
 
Scenario: log user using user id
	Given I set GET user/login API endpoint
	And I have valid userid
	When I send GET HTTPS request user/login
	Then I receive a valid HTTPS response code 200 from user/login using GET
 
Scenario: get user by user name
	Given I set GET user/user1 API endpoint
	And I have valid username
	When I send GET HTTPS request user/user1
	Then I receive a valid HTTPS response code 200 from user/user1 using GET
 
Scenario: adding pet
	Given I set POST pet API endpoint
	And I have valid petnumber
	When I send POST HTTPS request pet
	Then I receive a valid HTTPS response code 200 from pet using POST
 
Scenario: ordering pet
	Given I set POST store/order API endpoint
	And I have valid petorder
	When I send POST HTTPS request store/order
	Then I receive a valid HTTPS response code 200 from store/order using POST
 
Scenario: update pet
	Given I set PUT pet API endpoint
	And I have valid existingpetid
	When I send PUT HTTPS request pet
	Then I receive a valid HTTPS response code 200 from pet using PUT
 
Scenario: delete order by order id
	Given I set DELETE store/order/1 API endpoint
	And I have valid deleteorderid
	When I send DELETE HTTPS request store/order/1
	Then I receive a valid HTTPS response code 200 from store/order/1 using DELETE

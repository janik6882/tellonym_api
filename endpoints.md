# Endpoints:<br/><br/>
## Scheme:<br/>
URl -- description (parameter--Value, optional: parameter--Value)(request Limits and other stuff)<br/><br/>
https://api.tellonym.me/answers/{userID} -- get users answers to tells by their id (userId--uses-ID(self explanatory), pos--position to get, optional:limit--limit of Results, max 100)(no Limits found, No auth)<br/><br/>
https://api.tellonym.me/tells -- get own tells to answer (None)(Auth required)<br/><br/>
https://api.tellonym.me/followings/id/{user_id} -- get users followings by their id (None)(No auth required)<br/><br/>
https://api.tellonym.me/followers/id/{user_id} -- get a users followers by their id (None)(No auth required)<br/><br/>
https://api.tellonym.me/profiles/id/{userID} -- get a users profile details by their id (None)<br/><br/>
https://api.tellonym.me/profiles/name/{username} -- get a users profile details by their username (None)<br/><br/>
https://api.tellonym.me/answers/create -- create an answer to a tell (limit--limit for tells to fetch, answer--answer as written text, tellId--Tell id to respond to)<br/><br/>
https://api.tellonym.me/tells/new -- create a new tell (tell--text which tell should contain, userId--user to send the tell to, limit--limit of tells to fetch, isInstagramInAppBrowser--False, isSenderRevealed--bool which shows if senders name should be revealed, captcha--some kind of captcha needed)(captcha needed, currently nor fully worked out)<br/><br/>
https://api.tellonym.me/search/users -- search for users by their username (searchString--String to search for, optional:limit--limit for search Results)(Token necessary)

|Endpoint|Description|parameters|Other|
|--------|-----------|----------|-----|
|https://api.tellonym.me/answers/{userID}|get users answers to tells by their id|userId--uses-ID(self explanatory), pos--position to get, optional:limit--limit of Results, max 100)|no Limits found, No authr|
|https://api.tellonym.me/tells | get own tells to answer|None|Auth required|
|https://api.tellonym.me/followings/id/{user_id}|get users followings by their id|None|No auth required|
|https://api.tellonym.me/followers/id/{user_id}|get a users followers by their id|None|No auth required|
|https://api.tellonym.me/profiles/id/{userID}|get a users profile details by their id|None|No auth required|
|https://api.tellonym.me/profiles/name/{username}|get a users profile details by their username|None|No auth required|
|https://api.tellonym.me/answers/create |create an answer to a tell|limit--limit for tells to fetch, answer--answer as written text, tellId--Tell id to respond to|Auth required|
|https://api.tellonym.me/tells/new |create a new tell||tell--text which tell should contain, userId--user to send the tell to, limit--limit of tells to fetch, isInstagramInAppBrowser--False, isSenderRevealed--bool which shows if senders name should be revealed, captcha--some kind of captcha needed|captcha needed, currently nor fully worked out|
|https://api.tellonym.me/search/users |search for users by their username|searchString--String to search for, optional:limit--limit for search Results|Token necessary|

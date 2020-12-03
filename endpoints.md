# Endpoints:<br/><br/>
|Endpoint|Description|parameters|Other|
|--------|-----------|:--------:|-----|
|https://api.tellonym.me/answers/{userID}|get users answers to tells by their id|userId--user-ID(self explanatory),<br/> pos--position to get,<br/> optional:limit--limit of Results, max 100)|no Limits found, No auth required|
|https://api.tellonym.me/tells | get own tells to answer|None|Auth required|
|https://api.tellonym.me/followings/id/{user_id}|get users followings by their id|None|No auth required|
|https://api.tellonym.me/followers/id/{user_id}|get a users followers by their id|None|No auth required|
|https://api.tellonym.me/profiles/id/{userID}|get a users profile details by their id|None|No auth required|
|https://api.tellonym.me/profiles/name/{username}|get a users profile details by their username|None|No auth required|
|https://api.tellonym.me/answers/create |create an answer to a tell|limit--limit for tells to fetch,<br/>answer--answer as written text,<br/>tellId--Tell id to respond to|Auth required|
|https://api.tellonym.me/tells/new |create a new tell||tell--text which tell should contain,<br/>userId--user to send the tell to,<br/>limit--limit of tells to fetch,<br/>isInstagramInAppBrowser--False,<br/>isSenderRevealed--bool which shows if senders name should be revealed,<br/>captcha--some kind of captcha needed|captcha needed, currently nor fully worked out|
|https://api.tellonym.me/search/users |search for users by their username|searchString--String to search for,<br/>optional:limit--limit for search Results|Token necessary|
|https://api.tellonym.me/followings/list |gets the useres own followings| optional: limit--how many results to fetch,<br/>pos--at which position to fetch|Max limit is 500, Auth token required|
|https://api.tellonym.me/likes/id/{answerId}|gets likes for an answer|none|No auth required|

# Endpoints:<br /><br />
|Endpoint|Description|parameters|Other|
|--------|-----------|:--------:|:-----:|
|<h2> Endpoints for answers</h2>|
|https://api.tellonym.me/answers/create |create an answer to a tell|limit--limit for tells to fetch,<br />answer--answer as written text,<br />tellId--Tell id to respond to|Auth required|
|https://api.tellonym.me/answers/{userID}|get users answers to tells by their id|userId--user-ID(self explanatory),<br />pos--position to get,<br /> optional:limit--limit of Results, max 100)|max Limit 100,<br />No auth required|
|<h2>Endpoints for tells</h2>
|https://api.tellonym.me/tells | get own tells to answer|optional:<br />limit--limit for number of fetches, max. 300,<br />pos--position to start fetching|Auth required,<br />max. limit 300|
|https://api.tellonym.me/tells/new |create a new tell||tell--text which tell should contain,<br />userId--user to send the tell to,<br />limit--limit of tells to fetch,<br />isInstagramInAppBrowser--False,<br />isSenderRevealed--bool which shows if senders name should be revealed,<br />optional:senderStatus--should be 2 if sender revealed. If not, won't show sender in Tellonym|Auth needed|
|https://api.tellonym.me/tells/destroy |destroy a tell based on its tellId|tellId--Tell id for a certain tell you want to destroy,<br />optionak: limit--limit for following request||Auth required, won't generate a server response|
|<h2>Endpoints for followings</h2>|
|https://api.tellonym.me/followings/id/{user_id}|get users followings by their id|None|No auth required,<br />max Limit 500|
|https://api.tellonym.me/followings/name/{user_name}|get users followings by their name|None|No auth required,<br />max Limit 500|
|https://api.tellonym.me/followings/list |gets the useres own followings| optional: limit--how many results to fetch,<br />pos--at which position to fetch|Max limit is 500,<br />Auth token required|
|https://api.tellonym.me/followings/create |follow a user|userId--userId to follow,<br />isFollowingAnonymous--bool if anonymous| Auth required|
|https://api.tellonym.me/followings/destroy |destroy the following of a user|userId--userId to destroy follow with|Auth required|
|<h2>Endpoints for followers</h2>|
|https://api.tellonym.me/followers/id/{user_id}|get a users followers by their id|None|No auth required,<br />max Limit 500|
|https://api.tellonym.me/followers/name/{user_name}|get a users followers by their name|None|No auth required,<br />max Limit 500|
|<h2>Endpoints for profiles</h2>|
|https://api.tellonym.me/profiles/id/{userID}|get a users profile details by their id|None|No auth required|
|https://api.tellonym.me/profiles/name/{username}|get a users profile details by their username|None|No auth required|
|<h2>Other endpoints, might me be sorted later</h2>|
|https://api.tellonym.me/search/users |search for users by their username|searchString--String to search for,<br />optional:limit--limit for search Results|Token necessary,<br />max Limit 50|
|https://api.tellonym.me/likes/id/{answerId}|gets likes for an answer|none|No auth required,<br />max Limit 50|
|<h1>Experimental endpoints</h1>|
|https://api.tellonym.me/accounts/settings |auth required|implemented|
|https://api.tellonym.me/announcements/list |auth required|implemented|
|https://api.tellonym.me/check/updates |auth required|implemented|
|https://api.tellonym.me/feed/ids |auth required|implemented|
|https://api.tellonym.me/feed/olderthan | check auth, error: missing parameter|
|https://api.tellonym.me/feed/list |check auth|implemented|
|https://api.tellonym.me/suggestions/friends |auth required|
|https://api.tellonym.me/suggestions/sendtell |auth required|
|https://api.tellonym.me/suggestions/people |auth required|
|https://api.tellonym.me/reports/list |not allowed to perform action|
|https://api.tellonym.me/reports/moderationinfo |not allowed|
|https://api.tellonym.me/notifications/ids |check auth|
|https://api.tellonym.me/notifications |
|https://api.tellonym.me/suggestions/contacts | auth required|
|https://api.tellonym.me/accounts/myself | check auth|
|https://api.tellonym.me/accounts/challenges/statusemoji | check auth|
|https://api.tellonym.me/accounts/statusemoji | check auth|
|https://api.tellonym.me/search/history | check auth|
|https://api.tellonym.me/suggestions/tagging |check auth, missing param|
|https://api.tellonym.me/tells/ids | check auth|
|https://api.tellonym.me/tells/olderthanid/{tell_id} |check auth|
|https://api.tellonym.me/blocks/list |check auth|
|https://api.tellonym.me/followings/create/multiple |check auth|not found|
|https://api.tellonym.me/info/adexperiment |check auth|check meaning|
|https://api.tellonym.me/info/experiments |check auth| check meaning|
|https://api.tellonym.me/accounts/check |check auth| param missing|
|https://api.tellonym.me/notifications/sendpush | check auth|returns "ok", check meaining, |sends push to device|
|https://api.tellonym.me/profiles/swiping |check auth| check working|
|https://api.tellonym.me/profiles/swiping/matches | check auth|
|https://api.tellonym.me/profiles/swiping/likedBy |check auth| not allowed|
|https://api.tellonym.me/feed/featured/list |check auth|
|https://api.tellonym.me/likes/id/{answerId} |check auth| revisit and check|
|https://api.tellonym.me/accounts/settings/badwords | check auth| ?show bad words?|
|https://api.tellonym.me/ |
|<h2>Not working endpoints</h2>|
|https://api.tellonym.me/suggestions/contacts |Not working, Error: invalid token|

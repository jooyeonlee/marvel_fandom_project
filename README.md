Marvel Character DB RESTFul API 

Get all characters
[GET] http://127.0.0.1:5000/api/characters
Returns all Marvel chacters from a database

Get a single character
[GET]http://127.0.0.1:5000/api/characters/{param}
Path Param: character_id: integer, required
 
Delete a Character
[DELETE] http://127.0.0.1:5000/api/characters/{param}
Path Param: character_id, integer, required

Add a new character
[POST] http://127.0.0.1:5000/api/addcharacters
Body Param: json
{
    "name": "Character Name", (required)
    "description": "Character Description",
    "comic": "Comics the character appeard in",
    "superpower": "Super Power the character has"
}

Update a character
[PUT] http://127.0.0.1:5000/api/characters/{param}
Path Param: character_id: integer, required
Body Param: json
{
    "name": "Character Name",
    "description": "Character Description",
    "comic": "Comics the character appeard in",
    "superpower": "Super Power the character has"
}

Get user favorite character
[GET]http://127.0.0.1:5000/api/favcharacter/{param}
Path Param: user_id: string, required

Add a character to a user's favorite character
[POST] http://127.0.0.1:5000/api/favcharacter/{param1}/{param2}
Path Param: {param1} user_id: string, required
{param2} character_id: integer, required

Remove a chracter from a user's favorite character
[DELETE] http://127.0.0.1:5000/api/favcharacter/{param1}/{param2}
Path Param: {param1} user_id: string, required
{param2} character_id: integer, required
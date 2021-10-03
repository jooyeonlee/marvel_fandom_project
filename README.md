Marvel Character DB RESTFul API 

1. Get all characters
[GET] http://127.0.0.1:5000/api/characters
- Description: Returns all Marvel chacters from a database
- Responses: application/json

2. Get a single character
[GET]http://127.0.0.1:5000/api/characters/{character_id}
- Description: Returns a single character that matches with the character id
- Path Parameters:
character_id: integer, required
- Responses: application/json
 
3. Delete a Character
[DELETE] http://127.0.0.1:5000/api/characters/{character_id}
- This can only be done by authenticated user
- Description: Delete a character that matches with the character id from database
- Path Parameters:
character_id: integer, required

4. Add a new character
[POST] http://127.0.0.1:5000/api/addcharacters
- This can only be done by authenticated user
- Description: Add a new character to the database
- Body Parameter: application/json
{
    "name": "Character Name", (required)
    "description": "Character Description",
    "comic": "Comics the character appeard in",
    "superpower": "Super Power the character has"
}

5. Update a character
[PUT] http://127.0.0.1:5000/api/characters/{character_id}
- This can only be done by authenticated user
- Description: Update a character that matches with the character id to database
- Path Parameters:
character_id: integer, required
- Body Parameter: application/json
{
    "name": "Character Name",
    "description": "Character Description",
    "comic": "Comics the character appeard in",
    "superpower": "Super Power the character has"
}

6. Get user favorite character
[GET]http://127.0.0.1:5000/api/favcharacter/{user_id}
- This can only be done by authenticated user
- Description: Returns all characters in favorite character list of a user that matches with the user id
- Path Parameters:
user_id: string, required
- Responses: application/json

7. Add a character to a user's favorite character
[POST] http://127.0.0.1:5000/api/favcharacter/{user_id}/{character_id}
- This can only be done by authenticated user
- Description: Add a character of character id to the favorite character list of a user that matches with the user id
- Path Parameters:
user_id: string, required
character_id: integer, required

8. Remove a chracter from a user's favorite character
[DELETE] http://127.0.0.1:5000/api/favcharacter/{user_id}/{character_id}
- This can only be done by authenticated user
- Description: Remote a character of character id from the favorite character list of a user that matches with the user id
- Path Parameters:
user_id: string, required
character_id: integer, required
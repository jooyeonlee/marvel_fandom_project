Marvel Character DB RESTFul API 
- WEB URL: https://marvel-fandom.herokuapp.com/

1. Get all characters
- [GET] https://marvel-fandom.herokuapp.com/api/characters
- Description: Returns all Marvel chacters from a database
- Responses: application/json

2. Get a single character
- [GET] https://marvel-fandom.herokuapp.com/api/characters/{character_id}
- Description: Returns a single character that matches with the character id
- Path Parameters:
character_id: integer, required
- Responses: application/json
 
3. Delete a Character
- [DELETE] https://marvel-fandom.herokuapp.com/api/characters/{character_id}
- This can only be done by authenticated user
- Description: Delete a character that matches with the character id from database
- Path Parameters:
  character_id: integer, required

4. Add a new character
- [POST] https://marvel-fandom.herokuapp.com/api/addcharacters
- This can only be done by authenticated user
- Description: Add a new character to the database
- Header: 
 {'x-access-token': 'your token string', 'Content-Type': 'application/json'}
- Body Parameter: application/json
  {
      "name": "Character Name", (required)
      "description": "Character Description",
      "comic": "Comics the character appeard in",
      "superpower": "Super Power the character has"
  }

5. Update a character
- [PUT] https://marvel-fandom.herokuapp.com/api/characters/{character_id}
- This can only be done by authenticated user
- Description: Update a character that matches with the character id to database
- Path Parameters:
character_id: integer, required
- Header: 
 {'x-access-token': 'your token string', 'Content-Type': 'application/json'}
- Body Parameter: application/json
  {
      "name": "Character Name",
      "description": "Character Description",
      "comic": "Comics the character appeard in",
      "superpower": "Super Power the character has"
  }

6. Get user favorite character
- [GET]https://marvel-fandom.herokuapp.com/api/favcharacter/{user_id}
- This can only be done by authenticated user
- Description: Returns all characters in favorite character list of a user that matches with the user id
- Path Parameters:
  user_id: string, required
- Header: 
 {'x-access-token': 'your token string', 'Content-Type': 'application/json'}
- Responses: application/json

7. Add a character to a user's favorite character
- [POST] https://marvel-fandom.herokuapp.com/api/favcharacter/{user_id}/{character_id}
- This can only be done by authenticated user
- Description: Add a character of character id to the favorite character list of a user that matches with the user id
- Path Parameters:
  user_id: string, required
  character_id: integer, required
- Header: 
 {'x-access-token': 'your token string', 'Content-Type': 'application/json'}

8. Remove a chracter from a user's favorite character
- [DELETE] https://marvel-fandom.herokuapp.com/api/favcharacter/{user_id}/{character_id}
- This can only be done by authenticated user
- Description: Remote a character of character id from the favorite character list of a user that matches with the user id
- Path Parameters:
  user_id: string, required
  character_id: integer, required
- Header: 
 {'x-access-token': 'your token string', 'Content-Type': 'application/json'}

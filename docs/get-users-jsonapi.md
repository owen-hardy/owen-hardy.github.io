# GET /users

**Method**: `GET`  
**Endpoint**: `/users`

## Description
Returns a list of all users in the system. This endpoint is commonly used to populate user directories, autocomplete fields, dropdown menus, or display member lists in applications.

## Authentication
- **Type**: None
- **Requirements**: This is a public endpoint. No authentication required.

## Request

### Path Parameters

| Parameter | Type  | Required | Description |
|-----------|-------|----------|-------------|
| NULL      | NULL  | NULL     | NULL        |

### Query Parameters

| Parameter    | Type  | Required | Default | Description |
|--------------|-------|----------|---------|-------------|
| NULL         | NULL  | NULL     | NULL    | NULL        |

### Request Body (POST, PUT, PATCH)

Not applicable (GET Request).

## Response

### Success Response

**Status Code: 200 OK**

```json
{
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874"
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org"
}
```

### Error Responses

| Status Code | Description           | Example Body |
|-------------|-----------------------|--------------|
| 500         | Internal Server Error | N/A          |

## Code Samples

### cURL

```bash
curl -X GET https://jsonplaceholder.typicode.com/users
```

### Python

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    print(f"Successfully retrieved {len(users)} users.")
    # Example: Print first user's name
    if users:
        print(f"First user: {users[0]['name']}")
else:
    print(f"Error: {response.status_code}")
```

### JavaScript (Fetch)

```javascript
fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(users => {
    console.log(`Retrieved ${users.length} users`);
    console.log("First user:", users[0]);
  })
  .catch(error => console.error('Error:', error));
```

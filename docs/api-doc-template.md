# [Endpoint Name]

**Method**: `GET | POST | PUT | DELETE | PATCH`  
**Endpoint**: `/path/to/endpoint`

## Description
A clear, concise explanation of what this endpoint does, why it exists, and when it should be used.

## Authentication
- **Type**: None | API Key | Bearer Token | OAuth 2.0 | JWT
- **Requirements**: [Describe how to authenticate, where to get the token/key, etc.]

## Request

### Path Parameters

| Parameter       | Type     | Required | Description                          |
|-----------------|----------|----------|--------------------------------------|
| `param_name`    | string   | Yes      | Description of this parameter        |

### Query Parameters

| Parameter       | Type     | Required | Default | Description                          |
|-----------------|----------|----------|---------|--------------------------------------|
| `limit`         | integer  | No       | 20      | Maximum number of items to return    |
| `page`          | integer  | No       | 1       | Page number for pagination           |

### Request Body (POST, PUT, PATCH)

```json
{
  "field_name": "value",
  "another_field": 123,
  "is_active": true
}
```

## Response

### Success Response

**Status Code: 200 OK**

```json
{
  "id": 123,
  "name": "Example Name",
  "created_at": "2026-05-28T12:00:00Z",
  "status": "active"
}
```

### Error Responses

| Status Code | Description           | Example Body                            |
|-------------|-----------------------|-----------------------------------------|
| 400         | Bad Request           | { "error": "Invalid input data" }       |
| 401         | Unauthorized          | { "error": "Missing or invalid token" } |
| 404         | Not Found             | { "error": "Resource not found" }       |
| 429         | Too Many Requests     | { "error": "Rate limit exceeded" }      |
| 500         | Internal Server Error | { "error": "Unexpected server error" }  |

## Code Samples

### cURL

```bash
curl -X GET "https://api.example.com/path/to/endpoint" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

### Python

```python
import requests

headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get("https://api.example.com/path/to/endpoint", headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
```

### JavaScript (Fetch)

```javascript
fetch('https://api.example.com/path/to/endpoint', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer YOUR_TOKEN',
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```








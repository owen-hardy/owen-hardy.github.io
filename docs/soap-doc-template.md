# InitiateInstantTransfer

## Service
TransferService v2

## Description
Initiates an instant, irrevocable transfer of funds between two accounts. Transfers are typically completed in under 3 seconds when all validation checks pass.

## WSDL Location
https://api.example.com/services/TransferService?wsdl

## SOAP Version
SOAP 1.2 over HTTPS

## Authentication
WS-Security UsernameToken (digest) or OAuth 2.0 Bearer Token in SOAP Header

## Request

### SOAP Action
http://example.com/TransferService/InitiateInstantTransfer

## Request Body Example

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:tns="http://example.com/TransferService">
  <soap:Header>
    <!-- WS-Security header goes here -->
  </soap:Header>
  <soap:Body>
    <tns:InitiateInstantTransfer>
      <tns:SourceAccountId>acc_987654321</tns:SourceAccountId>
      <tns:DestinationAccountId>acc_123456789</tns:DestinationAccountId>
      <tns:AmountInCents>25075</tns:AmountInCents>   <!-- 250.75 USD -->
      <tns:Currency>USD</tns:Currency>
      <tns:Memo>Rent payment for June</tns:Memo>
      <tns:IdempotencyKey>unique-string-12345</tns:IdempotencyKey>
    </tns:InitiateInstantTransfer>
  </soap:Body>
</soap:Envelope>
```

## Key Request Parameters

| Element                | Type    | Required | Description                                       |
|------------------------|---------|----------|---------------------------------------------------|
| `SourceAccountId`      | string  | Yes      | The account to debit from                         |
| `DestinationAccountId` | string  | Yes      | The account to credit to                          |
| `AmountInCents`        | integer | Yes      | Amount in the smallest currency unit (e.g. cents) |
| `Currency`             | string  | Yes      | ISO 4217 currency code                            |
| `Memo`                 | string  | No       | Optional transfer description                     |
| `IdempotencyKey`       | string  | Yes      | Unique key to prevent duplicate processing        |

## Response

### Success Response

``` xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:tns="http://example.com/TransferService">
  <soap:Body>
    <tns:InitiateInstantTransferResponse>
      <tns:TransferId>trf_abc123xyz</tns:TransferId>
      <tns:Status>COMPLETED</tns:Status>
      <tns:AmountInCents>25075</tns:AmountInCents>
      <tns:Currency>USD</tns:Currency>
      <tns:Timestamp>2026-06-09T14:32:10Z</tns:Timestamp>
      <tns:FeeInCents>0</tns:FeeInCents>
    </tns:InitiateInstantTransferResponse>
  </soap:Body>
</soap:Envelope>
```

## Code Samples

### cURL

``` bash
curl -X POST https://api.example.com/services/TransferService \
  -H "Content-Type: text/xml; charset=utf-8" \
  -H "SOAPAction: http://example.com/TransferService/InitiateInstantTransfer" \
  -d @request.xml
```
### Python (zeep)

``` python
from zeep import Client
from zeep.wsse.username import UsernameToken

client = Client('https://api.example.com/services/TransferService?wsdl')
client.settings.wsse = UsernameToken('username', 'password')

response = client.service.InitiateInstantTransfer(
    SourceAccountId="acc_987654321",
    DestinationAccountId="acc_123456789",
    AmountInCents=25075,          # 250.75 USD
    Currency="USD",
    Memo="Rent payment for June",
    IdempotencyKey="unique-string-12345"
)

print(response)
```

### JavaScript / Node.js

``` javascript
const soap = require('soap');

const url = 'https://api.example.com/services/TransferService?wsdl';

const args = {
  SourceAccountId: "acc_987654321",
  DestinationAccountId: "acc_123456789",
  AmountInCents: 25075,           // 250.75 USD
  Currency: "USD",
  Memo: "Rent payment for June",
  IdempotencyKey: "unique-string-12345"
};

soap.createClient(url, function(err, client) {
  if (err) return console.error(err);
  
  client.InitiateInstantTransfer(args, function(err, result) {
    if (err) return console.error(err);
    console.log(result);
  });
});
```
